import json
import pandas as pd

with open("data/phish-data.json", "r") as f:
    data = json.load(f)

df = pd.json_normalize(data)
print(df.head())
print(df.columns)

# Loads JSON into a dataframe