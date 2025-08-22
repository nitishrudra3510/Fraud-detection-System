import pandas as pd
import requests

# Load a real sample from the cleaned dataset
csv_path = "data/creditcard.csv"
df = pd.read_csv(csv_path)

# Drop the label if present
if 'Class' in df.columns:
    sample = df.drop('Class', axis=1).iloc[0].to_dict()
else:
    sample = df.iloc[0].to_dict()

url = "http://127.0.0.1:8000/predict"
headers = {
    "Content-Type": "application/json",
    "X-API-Key": "mysecretkey"
}

response = requests.post(url, headers=headers, json=sample)
print("Status Code:", response.status_code)
print("Response:", response.json())
