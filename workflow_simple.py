import re
from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wlexpr
from embedding_IVF import rag
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
import os

class ModelFunc:
    def __init__(self, model_path, device):
        self.device = device
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"模型路径不存在: {model_path}")
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
            self.model = AutoModelForCausalLM.from_pretrained(model_path, device_map=device, trust_remote_code=True).to(device)
            self.model.eval()
        except Exception as e:
            raise RuntimeError(f"加载模型或分词器时出错: {e}")

    def generate(self, prompt, user_input, max_tokens) -> str:
        try:
            with torch.no_grad():
                message = [{"role":"system","content":prompt},{"role":"user","content":user_input}]
                conversation = self.tokenizer.apply_chat_template(message,add_generation_prompt=True,tokenize=False)
                encoading = self.tokenizer(conversation,return_tensors="pt").to(self.device)
                output_ids = self.model.generate(**encoading,max_new_tokens=max_tokens,repetition_penalty=1.1,pad_token_id=self.tokenizer.eos_token_id)
                response = self.tokenizer.decode(output_ids[0])
                return response
        except Exception as e:
            raise RuntimeError(f"生成回复时出错: {e}")
        
class WorkflowExecutor:
    gpu_num=1
    if gpu_num == -1:
        device = torch.device(f"cpu")
    elif gpu_num == 'auto':
        device = torch.device(f"cuda")
    else:
        device = torch.device(f"cuda:{gpu_num}")
    
    mma = WolframLanguageSession()
    model = ModelFunc(model_path='/data/public/models/DeepSeek-R1-Distill-Qwen-14B',device=device)
    ragger = rag(device)
    def answer_question(problem):
        backgrounds = WorkflowExecutor.ragger.invoke(k=2, query=problem)
        background_text = "\n\n".join([f'document {i+1}:\n"{item}"' for i, item in enumerate(backgrounds)])
        system_prompt = f"""
You are a physics expert. Please solve the following problem. Please use \\boxed{{}} around your final result. Be confident and don't think too much.
For simple problem, you can solve it directly.
If the problem is complex, you can break it down into subproblems and solve them one by one. Some problems can be broken down into four steps: "rigorously analyze the geometric and physical context", "list equations and transform them into mathematical problems", "solve the equations", and "get conclusions from the results".
If the calculation is complex, you can keep the formula and use wolfram language, enclose the calculation expressions within `<wolfram>` and `</wolfram>` tags, for example: `<wolfram>2 + 2</wolfram>`. The wolfram engine will compute the result and replace it in the answer.

Backgrounds:
{background_text}

"""

        user_input = f"""
Problem:
{problem}
"""

        response = WorkflowExecutor.model.generate(system_prompt, user_input, max_tokens=4096)
        
        def replace_mma_match(match):
            expr = match.group(1).strip()
            try:
                result = WorkflowExecutor.mma.evaluate(wlexpr(expr))
                return str(result)
            except:
                return expr
            
        calculate_response = re.sub(r'<wolfram>(.*?)</wolfram>', replace_mma_match, response, flags=re.DOTALL)

        final_response = ""
        match = re.search(r'<｜Assistant｜>(.*)', calculate_response, re.DOTALL)

        if match:
            final_response = match.group(1)
        else:
            final_response = calculate_response
        return final_response

    def solve_problem(problem):
        try:
            answer = WorkflowExecutor.answer_question(problem)
            return answer
        except Exception as e:
            print(f"workflow failed: {str(e)}")

if __name__ == "__main__":
    problem = "Find the potential outside a charged metal sphere (charge $Q$, radius $R$) placed in an otherwise uniform electric field $E_O$."
    answer = WorkflowExecutor.solve_problem(problem)