import requests
import os 

api_key = os.getenv("OPEN_AI_KEY1")

url = "https://api.openai.com/v1/chat/completions"

headers = {
    "Authorization":f"Bearer {api_key}",
    "Content-Type":"application/json"
}

data = {
    "model":"gpt-4o-mini",
    "messages": [
        {
            "role": "system",
        "content": "You are a helpful assistant"
        },
        {
            "role":"user",
            "content":"{prompt}"
        }
    ],
    "max_tokens": 256,
    "temperature": 0.0,
}

def generate(prompt):
    data['messages'][1]['content'] = prompt

    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        content = response.json()["choices"][0]["message"]["content"]
        print(content)
    else:
        print(f"Failed {response.status_code}: {response.text}")

generate( "What is the name of the Towards AI developed largest open-source model and what is its size?" )