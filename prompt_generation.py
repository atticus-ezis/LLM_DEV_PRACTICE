import os
from openai import OpenAI

client = OpenAI(api_key = os.getenv("OPEN_AI_KEY1"))

# 1) Generate a chart of pharmeceutical companies 

# specify the user prompt
prompt_generation = """
Generate a table with the 5 most popular pharmaceutical companies and their foundation years. 
The response should include only the table, with no additional text. 
Use the following example format:
---
Company | Foundation Year
Microsoft | 1975
Apple | 1976
Google | 1998
Amazon | 1994
Meta | 2004
---"""

# return response object with intial prompt
initial_response = client.chat.completions.create(
    model="gpt-4o-2024-08-06",
    messages=[
        {"role": "system", "content": "you are a helpful assistant"},
        {"role": "user", "content": prompt_generation},
    ]
)
generated_response = initial_response.choices[0].message.content

# 2) Ensure the generated_response is indeed a chart

prompt_check_table_new = """Your task is to verify if a given table matches the exact format and structure of a provided example table.

Here's an example of the format that the table should have:
---
Company | Foundation Year
Microsoft | 1975
Apple | 1976
Google | 1998
Amazon | 1994
Meta | 2004
---

Table to Check:
{table_to_check}

Instructions:
- The table to check should match the structure, headers, and format of the Example Table exactly.
- The column names must be "Company" and "Foundation Year".
- The values in each row should have the company names and their corresponding foundation years.
- If the given table matches the example table in all these aspects, write "Yes".
- Write "No" if there are any differences in structure, headers, or if any company/year is missing or incorrect.

Only respond with "Yes" or "No".

"""

# checks if the generated table meets prompt_checlk_table_new format
formatted_prompt = prompt_check_table_new.format(table_to_check=generated_response)

final_response = client.chat.completions.create(
    model="gpt-4o-2024-08-06",
    messages=[
        {"role": "system", "content": "You are a strict judge. Evaluate inputs based on the given criteria and provide only the required response"},
        {"role": "user", "content": formatted_prompt},
    ],
    temperature=0
)

print(final_response.choices[0].message.content)