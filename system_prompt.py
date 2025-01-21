# pip install openai
from openai import OpenAI
import os 

client = OpenAI(api_key = os.getenv("OPEN_AI_KEY1"))

system_prompt = """You are a helpful assistant who only answer question related to Artificial Intelligence.
                If the question is not related, respond with the following: The question is not related to AI."""


response = client.chat.completions.create(
    model='gpt-4o-mini',
    temperature=0.0,
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": "what is the tallest mountain in the world?"},
    ]
)

print(response.choices[0].message.content)