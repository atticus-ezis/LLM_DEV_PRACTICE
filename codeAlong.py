import requests
import os 

api_key = os.getenv("OPEN_AI_KEY1")
print(f"key is {api_key}")

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
        "content": "You are a helpful assistant that translate from English to French"
        },
        {
            "role":"user",
            "content":"Hello, how are you?"
        }
    ],
    "max_tokens": 60,
    "temperature": 0.7,
}

# response = requests.post(url, json=data, headers=headers)
# if response.status_code == 200:
#     print(response.json())
# else:
#     print(f"Failed {response.status_code}: {response.text}")

