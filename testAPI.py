import os
from openai import OpenAI

client = OpenAI(
  api_key = os.getenv("OPEN_AI_KEY1")
)
completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "write a haiku about ai"}
  ]
)

print(completion.choices[0].message);