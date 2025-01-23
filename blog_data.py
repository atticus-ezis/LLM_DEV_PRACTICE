import pandas as pd

url ="https://raw.githubusercontent.com/AlaFalaki/tutorial_notebooks/main/data/mini-llama-articles.csv"
mini_dataset = pd.read_csv(url)

mini_dataset.head()
print(mini_dataset.head())
