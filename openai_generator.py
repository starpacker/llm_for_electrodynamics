import json
import os
from openai import OpenAI
from tqdm import tqdm

topic = "electrodynamics"

# Initialize OpenAI client
client = OpenAI(api_key="sk-abcdef1234567890abcdef1234567890abcdef12", base_url="https://api.deepseek.com")

# Function to generate response for a given input
def generate_response(input_text):
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": """You are an expert in mathematics and physics and their education. Your task is to provide detailed, step-by-step explanations and reasoned answers to questions. Follow the structured format below to ensure clarity and depth:

1. **Understanding the Problem:**
   - Begin by summarizing the problem to ensure clarity.

2. **Step-by-Step Solution and Chain-of-Thought Reasoning:**
   - Break down the problem into smaller parts.
   - Explain each step in detail, including calculations and reasoning.
   - Describe the logical process leading to the solution.
   - Highlight any assumptions or principles used.
   
3. **Highlight your final answer**

Use clear language and examples to enhance understanding. Follow the markdown math format below. Always ensure that your explanations are accessible to learners at different levels. Below is an explicit example you can follow:

--- 

1. **Understanding the Problem and Recall Relevant Background Knowledge:**

   The problem asks us to calculate the group velocity of an electromagnetic wave packet in a dispersive medium. We are given the dispersion relation $\omega = Ak^2$, where $\omega$ is the angular frequency, $k$ is the wave number, and $A$ is a constant.

   Relevant background knowledge:
   - Group velocity is the velocity at which the overall envelope of the wave packet propagates.
   - The formula for group velocity is: $v_g = \frac{d\omega}{dk}$
   - In a dispersive medium, the phase velocity and group velocity are different.
   - The given dispersion relation is non-linear, indicating a dispersive medium.

2. **Step-by-Step Solution and Chain-of-Thought Reasoning:**

   Step 1: Recall the formula for group velocity
   $v_g = \frac{d\omega}{dk}$

   Step 2: Identify the dispersion relation
   $\omega = Ak^2$

   Step 3: Calculate $\frac{d\omega}{dk}$ using the chain rule
   $\frac{d\omega}{dk} = \frac{d}{dk}(Ak^2)$
   $\frac{d\omega}{dk} = A \cdot 2k = 2Ak$

   Step 4: Substitute the result back into the group velocity formula
   $v_g = \frac{d\omega}{dk} = 2Ak$

   Step 5: Interpret the result
   The group velocity depends on both the constant $A$ and the wave number $k$. This means that different frequency components of the wave packet will travel at different speeds, leading to dispersion of the wave packet over time.

   Step 6: Compare with phase velocity
   For comparison, we can calculate the phase velocity:
   $v_p = \frac{\omega}{k} = \frac{Ak^2}{k} = Ak$

   Note that $v_g = 2v_p$ in this case, which is not generally true for all dispersion relations.

3. **Highlight your final answer**

   The group velocity of the electromagnetic wave packet in the given dispersive medium is:
   
   **$v_g = 2Ak$**

   where $A$ is the constant from the dispersion relation and $k$ is the wave number.

---

"""},
            {"role": "user", "content": f"{input_text}"}
        ],
        temperature=0,
        stream=False
    )
    return response.choices[0].message.content


# Read input JSONL file and process each entry
input_file = f'Q_{topic}.jsonl'
output_file = f'A_{topic}.jsonl'
checkpoint_file = f'{topic}_checkpoint.txt'

# Function to get the last processed line number
def get_last_processed_line():
    if os.path.exists(checkpoint_file):
        with open(checkpoint_file, 'r') as f:
            return int(f.read().strip())
    return 0

# Function to update the checkpoint
def update_checkpoint(line_number):
    with open(checkpoint_file, 'w') as f:
        f.write(str(line_number))

# Function to count total lines in the input file
def count_lines(filename):
    with open(filename, 'r') as f:
        return sum(1 for _ in f)

last_processed_line = get_last_processed_line()
total_lines = count_lines(input_file)

try:
    with open(input_file, 'r') as infile, open(output_file, 'a') as outfile:
        # Create a progress bar
        pbar = tqdm(total=total_lines, initial=last_processed_line, desc="Processing", unit="line")
        
        for i, line in enumerate(infile):
            if i < last_processed_line:
                continue  # Skip already processed lines
            
            try:
                entry = json.loads(line)
                input_text = entry['input']
                
                # Generate response
                output = generate_response(input_text)
                
                # print the output
                print(output)
                
                print("----------------------------------------")
                
                # Add output to the entry and write to file
                entry['output'] = output
                json.dump(entry, outfile)
                outfile.write('\n')
                
                # Update the checkpoint after each successful processing
                update_checkpoint(i + 1)
                
                # Update the progress bar
                pbar.update(1)
                
                # Calculate and display percentage completion
                percent_complete = ((i + 1) / total_lines) * 100
                pbar.set_postfix({"Percent Complete": f"{percent_complete:.2f}%"})
            
            except Exception as e:
                print(f"\nAn error occurred while processing line {i + 1}: {str(e)}")
                quit()

        pbar.close()

    print(f"\nProcessing complete. Results saved to {output_file}")

except KeyboardInterrupt:
    print("\nProcessing interrupted. Progress saved. You can resume later.")

finally:
    # Ensure the checkpoint is updated even if an error occurs
    update_checkpoint(i)
    
