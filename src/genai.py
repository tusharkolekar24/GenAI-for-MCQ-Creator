
import json
import os
import openai

with open('src\openai_key.json','r') as jsonfile:
     openai_key_info = json.load(jsonfile)

openai.api_key = openai_key_info["api_key"]

def generate_mcq(content: str, question: str) -> str:
    prompt = f"""
            You are an expert quiz assistant. Based on the content provided below, determine whether the question can be answered **only using this content**.

            If the content contains enough information to answer the question, follow these steps:
            1. Generate one multiple-choice question using the provided question.
            2. Create four options: A, B, C, and D.
            3. Clearly identify the correct answer from the content.

            However, if the content does **not contain** the answer to the question, simply respond with:
            "Invalid question asked by user"

            Content:
            \"\"\" 
            {content} 
            \"\"\"

            Question:
            {question}

            Your Output Format (if valid):
            Q: {question}

            A. Option A  
            B. Option B  
            C. Option C  
            D. Option D  


            Answer: [Correct Option Letter]
            """

    # Simulate sending prompt to LLM (e.g., OpenAI API or local model)
    # For example:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return {"content":content,'response':response['choices'][0]['message']['content']} 

# os.environ["OPENAI_API_KEY"] = openai_key_info["api_key"]
# def get_mcq_info(content,question):

#     from langchain.prompts import PromptTemplate
#     from langchain.llms import OpenAI  # Or another LLM, like ChatOpenAI
#     from langchain.chains import LLMChain
    
#     template = """
#     You are an expert quiz assistant. Based on the content provided below, generate a multiple-choice question and its answer.

#     Content:
#     \"\"\"{content}\"\"\"

#     Question:
#     {question}

#     Your task:
#     - Ensure the question is answerable from the content.
#     - Generate 4 answer options (A, B, C, D), only one of which is correct.
#     - Clearly identify the correct answer.

#     Rules:
#     - If the answer is not present in the content, or the question is irrelevant, respond only with:
#     "Invalid question asked by user."

#     Output Format (when valid):
#     Q: {question}
#     A. Option A
#     B. Option B
#     C. Option C
#     D. Option D
#     Answer: [Correct Option Letter]
#     """


#     prompt = PromptTemplate(
#         input_variables=["content", "question"],
#         template=template,
#     )

#     # 2. Initialize your LLM (e.g., OpenAI)
#     llm = OpenAI(temperature=0.0)  # adjust temperature as needed

#     # 3. Create the LLMChain
#     chain = LLMChain(llm=llm, prompt=prompt)

#     # 5. Generate the quiz
#     result = chain.run({"content": content, "question": question})
#     print("Process Completed Successfully.")
    
#     return {"content":content,'response':result}