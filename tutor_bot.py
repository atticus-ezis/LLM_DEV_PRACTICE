import os 
from openai import OpenAI

api_key = os.getenv("OPEN_AI_KEY1")

client = OpenAI(api_key=api_key)

def ask_ai_tutor(question):
    try:
        system_prompt = (
            "You are an AI tutor specialized in answering artificial intelligence-related questions. "
            "Only answer AI-related question, else say that you cannot answer this question."
        )

        prompt = f"Please provide an informative and accurate answer to the following question.\nQuestion: {question}\nAnswer:"

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            temperature=0,
            messages= [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt},
            ]
        )

        return response.choices[0].message.content.strip()
    
    except Exception as e:
        return f"an error occured: {e}"
    
QUESTION_AI =  "list a number of famous artificial frameworks"
RES_AI = ask_ai_tutor(QUESTION_AI)

QUESTION_NOT_AI = "What is the name of the highest mountain in the world and its height?"
RES_NOT_AI = ask_ai_tutor(QUESTION_NOT_AI)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    temperature=0,
    messages=[
        {
            "role": "system",
            "content": "You are an AI tutor specialized in answering artificial intelligence-related questions. Only answer AI-related question, else say that you cannot answer this question.",
        },
        {
            "role": "user",
            "content": "Please provide an informative and accurate answer to the following question.\nQuestion: List a number of famous artificial intelligence frameworks?\nAnswer:",
        },
        {"role": "assistant", "content": RES_AI},
        {
            "role": "user",
            "content": "Please provide an informative and accurate answer to the following question.\nQuestion: What is the name of the highest mountain in the world and its height?\nAnswer:",
        },
        {"role": "assistant", "content": RES_NOT_AI},
        {
            "role": "user",
            "content": "Please provide an informative and accurate answer to the following question.\nQuestion: Can you write a summary of the first suggested AI framework in the first question?\nAnswer:",
        },
    ],
)

print(response.choices[0].message.content.strip())


