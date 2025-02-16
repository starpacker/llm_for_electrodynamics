import json
from typing import List, Dict
import time
import sys
import re
from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wl, wlexpr
from wolframclient.exception import WolframLanguageException
from hyh.embedding import rag
from collections import OrderedDict
from copy import deepcopy
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
import os

class ModelFunc:
    def __init__(self, model_path: str):

        if not os.path.exists(model_path):
            raise FileNotFoundError(f"模型路径不存在: {model_path}")

        # self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.device = torch.device("cuda:2")
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
            self.model = AutoModelForCausalLM.from_pretrained(model_path, trust_remote_code=True).to(self.device)
            self.model.eval()  # 设置为评估模式
        except Exception as e:
            raise RuntimeError(f"加载模型或分词器时出错: {e}")

    def generate(self, prompt: str, max_tokens) -> str:

        try:
            with torch.no_grad():
                message = [{"role":"user","content":prompt}]
                conversation = self.tokenizer.apply_chat_template(message,add_generation_prompt=True,tokenize=False)
                encoading = self.tokenizer(conversation,return_tensors="pt").to(self.device)
                output_ids = self.model.generate(**encoading,max_new_tokens=max_tokens,repetition_penalty=1.1,pad_token_id=self.tokenizer.eos_token_id)
                response = self.tokenizer.decode(output_ids[0])
                return response
        except Exception as e:
            raise RuntimeError(f"生成回复时出错: {e}")
        
class WorkflowExecutor:
    def __init__(self,model_path):
        self.sub_problems = []
        self.intermediate_answers = []
        self.final_conclusion = ""
        self.mma = WolframLanguageSession()
        self.problem = ""
        self.model = ModelFunc(model_path=model_path)
    
    def eval_split_result(self,response):
        eval_prompt = """
Your task is to evaluate the quality of the following response.
If the response is perfect and does not require any changes, reply with the word "perfect".
If the response has issues that can be fixed, reply with the word "fixable".
Here is the response: {problem}"""

        response = self.model.generate(
            eval_prompt.format(problem=response),
            max_tokens= 1000
        )
        if "perfect" in response:
            return "perfect", response  
        else:
            return "fixable", response

    def eval_final_result(self,response):
        eval_prompt = ""
        response = self.generate(
        eval_prompt.format(problem=response),
        max_tokens= 1000
        )
        return response  

    # 阶段1: 问题拆分
    def split_into_subproblems(self) -> List[str]:
        max_attempts = 5  # 防止无限循环
        error_history = []  # 记录错误历史
        error_feedback = ""
        system_prompt = """
You are a physics expert. Please solve the following problem. 
You can solve the problem or break it down into series subproblems when the problem is complex.
If you can solve it directly, please use \\box{{}} around your final result.
If you decide to break it down, pay attention to:
- Some problems can be broken down into four steps: "rigorously analyze the geometric and physical context", "list equations and transform them into mathematical problems", "solve the equations", and "get conclusions from the results".
- Ignore details that are not relevant to solving the problem, such as unnecessary object properties or unrelated parts of the system.
- If applicable, check the limiting behaviors or simplified cases to see if the problem can be reduced further. This can be the last subproblem.
- Use strict JSON array format: ["Sub-problem 1", "Sub-problem 2", "Sub-problem 3"].
- Avoiding unnecessary subdivisions.

{error_feedback}
Problem: {problem}
<think>"""
        
        for attempt in range(max_attempts):
            # 生成带错误反馈的提示
            error_feedback = "\n".join(error_history[-2:])  # 只显示最近两次错误
            prompt = system_prompt.format(
                problem=self.problem,
                error_feedback=f"Previous issues to be solved:\n{error_feedback}" if error_feedback else ""
            )
            
            # 调用模型生成
            response = self.model.generate(prompt, max_tokens=10000)
            
            print("-----------------------",response,"-----------------------")
            
            
            # 评估并获取详细反馈
            evaluation, feedback = self.eval_split_result(response)
            
            if evaluation == "perfect":
                break
                # return parse_json(response)  # 假设有解析JSON的函数
            else:
                error_history.append(f"Attempt {attempt+1} failed, response:{response}, feedback:{feedback}")
                    
        # analyze the result
        try:
            self.sub_problems = json.loads(response)
            print(f"🔄 Split into {len(self.sub_problems)} sub-problems")
            return self.sub_problems
        except json.JSONDecodeError:
            raise ValueError("Failed to parse sub-problems")
        
        
    def get_raw_answer(self, augmented_context, sub_problem, max_iterations=3):
        """
        迭代式RAG检索增强函数
        参数：
            sub_problem: 原始问题/查询
            max_iterations: 最大迭代次数
        返回：
            最终检索到的增强文本
        """
        raw_answer = ""
        final_raw_answer = None
        
        prompt_first = f"""You are a physics expert. Please solve a subproblem divided from the initial problem. 
        Please comprehend the following subproblem and context about the whole problem, and try to solve the subproblem step by step.
        
        If you need to perform mathematical calculations, use wolfram language and enclose the calculation expressions within `<wolfram>` and `</wolfram>` tags, for example: `<wolfram>2 + 2</wolfram>`.
        The wolfram engine will automatically compute the result and replace it in the answer.

        If information isn't enough, you should ask for more background information instead of answering the subproblem.
        You should use `<rag>``</rag>` tags around your ask. For example: `<rag>How to solve a first-order linear differential equation?</rag>`.

        Context Information:
        {augmented_context}

        Question: {sub_problem}

        Please think step-by-step and use the `<wolfram>``</wolfram>` tags when calculations are needed.
        Your response:"""

        raw_answer = self.model.generate(prompt_first, max_tokens=1000)

        pattern = r'<rag>(.*?)</rag>'
    
        # 使用 re.search 查找第一个匹配
        match = re.search(pattern, raw_answer)
        
        if match:
            background = rag(k=2, query=match.group(1))
        else:
            final_raw_answer = raw_answer
        
        for idx in range(max_iterations-1):
            if final_raw_answer:
                break
            
            prompt = f"""You are a physics expert. Please use the provided context and background information to answer the following questions step-by-step. 
            If you need to perform mathematical calculations, use wolfram language and enclose the calculation expressions within `<wolfram>` and `</wolfram>` tags, for example: `<wolfram>2 + 2</wolfram>`.
            The wolfram engine will automatically compute the result and replace it in the answer.

            Context Information:
            {augmented_context}

            Relevant Background Knowledge:
            {background}

            Question: {sub_problem}

            Please think step-by-step and use the `<wolfram>``</wolfram>` tags when calculations are needed.
            Your response:"""

            raw_answer = self.model.generate(prompt, max_tokens=1000)

            match = re.search(pattern, raw_answer)
        
            if match:
                background += rag(k=2, query=match.group(1))
            else:
                final_raw_answer = raw_answer
            
        return final_raw_answer
    
    # 阶段2: 顺序解决子问题
    def solve_subproblems(self) -> List[Dict]:
        """使用RAG和MMA按顺序解决子问题(支持动态数学计算)"""
        
        context = OrderedDict()    # 维护上下文信息
        
        for idx, sub_problem in enumerate(self.sub_problems, 1):
            print(f"🔍 Processing sub-problem {idx}/{len(self.sub_problems)}")
            
            # 组合上下文与当前问题
            augmented_context = "\n".join([f"{k}: {v}" for k, v in context.items()])
            
            raw_answer = self.get_raw_answer(augmented_context=augmented_context,sub_problem=sub_problem,max_iterations=3)

            # 处理答案中的MMA计算
            processed_answer = self.process_mma_calculations(raw_answer)
            
            # 存储中间结果
            self.intermediate_answers.append({
                "step": idx,
                "context": context.copy(),
                "sub_problem": sub_problem,
                "answer": processed_answer,
            })
            
            # 更新上下文（保留最近3步）
            context[f"Step_{idx}"] = f"problem: {sub_problem}\nanswer: {processed_answer}"
            context = self.clean_context(context, keep_last=3)
            # 整理新字典
            updated_context = OrderedDict()
            updated_context["initial problem"] = self.problem

            for k, v in context.items(): # 再添加 context 中的其他内容
                if k != "initial problem": # 避免重复添加
                    updated_context[k] = v

            context = deepcopy(updated_context)  # 更新原始的 context 字典
        
        print("✅ All sub-problems solved")
        return self.intermediate_answers

    def process_mma_calculations(self, answer: str) -> str:
        """处理答案中的wolfram计算标签"""
        def replace_mma_match(match):
            expr = match.group(1).strip()
            try:
                result = self.mma.evaluate(wlexpr(expr))
                return str(result)
            except WolframLanguageException as e:
                return f"[wolfram error: {str(e)}]"
            except Exception as e:
                return f"[system error: {str(e)}]"
        
        # 使用正则表达式替换所有<wolfram>标签
        return re.sub(r'<wolfram>(.*?)</wolfram>', replace_mma_match, answer, flags=re.DOTALL)


    def clean_context(self, context: dict, keep_last: int = 3) -> dict:
        """保持上下文简洁,保留最近N个字典"""
        return dict(list(context.items())[-keep_last:])

    #阶段3，综合step生成final answer
    def generate_conclusion(self, max_retries: int = 3) -> str:
        """Generate a structured final conclusion with a self-checking mechanism"""

        formatted_steps = "\n".join([
            f"Step {ans['step']}: {ans['sub_problem']}\n"
            f"Answer: {ans['answer']}\n"
            for ans in self.intermediate_answers
        ])
        
        final_answer = ""
        
        final_prompt = f"""You are a physics expert. Generate a final conclusion for the given problem.
        Please use '<box>' and '</box>' tags around your final answer.
        Example:
        Problem: Find the square root of 144.
        
        Step-by-step Solutions:
        ......
        
        Your final conclusion and answer:
        The square root of 144 is <box>12</box>.
        
        Problem:
        {self.problem}
        
        Step-by-step Solutions:
        {formatted_steps}
        
        Your final conclusion and answer:
        """                
        
        retry_count = 0
        while retry_count < max_retries:
            try:
                final_answer = self.model.generate(final_prompt, max_tokens=1000)
                
                synthesis_prompt = f"""There is a physics problem and its solution.
                Problem:
                {self.problem}

                Step-by-Step Solutions:
                {formatted_steps}
                
                Final Conclusion:
                {final_answer}

                Please first verify the following conditions:
                - All mathematical calculation results are correctly referenced
                - Key data points are complete
                - Main conclusions are self-consistent
                - Final answer is in tag format <box>...</box>
                
                Please respond in JSON format: {{"valid": bool, "issues": [str]}}, 
                If all conditions are satisfied, please set "valid" to true and leave "issues" empty. Otherwise, set "vaild" to false and provide a list of issues to be solved.
                Your response:"""
                
                eval_prompt = self.model.generate(synthesis_prompt, max_tokens=1000)
                
                evaluation = json.loads(self.model.generate(eval_prompt, max_tokens=300))
                
                if evaluation.get("valid", True):
                    self.final_conclusion = final_answer
                    return self.final_conclusion

                # Regenerate with feedback
                final_prompt = f"""You are a physics expert. Generate a final conclusion for the given problem.
                Please use '<box>' and '</box>' tags around your final answer.
                Example:
                Problem: Find the square root of 144.
                
                Step-by-step Solutions:
                ......
                
                Your final conclusion and answer:
                The square root of 144 is <box>12</box>.
                
                Problem:
                {self.problem}
                
                Step-by-step Solutions:
                {formatted_steps}
                
                Issues to be solved:
                {evaluation.get("issues", "No issues found")}
                
                Your final conclusion and answer:
                """                

                retry_count += 1
                
            except (json.JSONDecodeError, KeyError) as e:
                print(f"Conclusion validation error: {str(e)}")
                retry_count += 1
                continue
                
        # Fallback return mechanism
        print("⚠️ Conclusion generation reached maximum retries, returning the last result")
        self.final_conclusion = final_answer
        return self.final_conclusion

# 主执行流程
def main(model_path):
    executor = WorkflowExecutor(model_path)
    
    # Step 1: 输入问题
    problem = input("please load your problem")
    if not problem.strip():
        raise ValueError("Problem input cannot be empty")
    
    executor.problem = problem
    
    # Step 2: 拆分问题
    sub_problems = executor.split_into_subproblems()
    print("\nsplit sub-problems:")
    print("\n".join(f"{i+1}. {p}" for i, p in enumerate(sub_problems)))
    
    # Step 3: 解决子问题
    answers = executor.solve_subproblems()
    print("\nintermediate answers:")
    print(json.dumps(answers, indent=4, ensure_ascii=False))
    
    # Step 4: 生成结论
    conclusion = executor.generate_conclusion(max_retries = 4)
    print("\nfinal conclusions:")
    print(conclusion)
            

if __name__ == "__main__":
    main('/data/public/models/DeepSeek-R1-Distill-Qwen-14B')