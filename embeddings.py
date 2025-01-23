import os 
import csv 




google_ai_key = os.environ["GOOGLE_AI_KEY"]
open_ai_key = os.environ["OPEN_AI_KEY1"] 



def split_into_chunks(text, chunk_size=1024):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])
    return chunks 

chunks = []

with open("./mini-llama-articles.csv", mode="r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for idx, row in enumerate(reader):
        if idx == 0: continue
        chunks.extend(split_into_chunks(row[1]))
print("number of articles:", idx)
print("number of chunks:", len(chunks))

import pandas as pd

df = pd.DataFrame(chunks, columns=["chunk"])
print(df.keys())

from openai import OpenAI
client = OpenAI(api_key = os.getenv("OPEN_AI_KEY1"))

def get_embedding(text):
    try:
        text = text.replace("\n", " ")
        res = client.embeddings.create(input=[text], model="text-embedding-3-small")
        return res.data[0].embedding
    except:
       return None
    
from tqdm import tqdm
import numpy as np

print("generating embeddings")
embeddings = []
for index, row in tqdm(df.iterrows()):
    embeddings.append(get_embedding(row["chunk"]))

embeddings_values = pd.Series(embeddings)
df.insert(loc=1, column='embedding', value=embeddings_values)