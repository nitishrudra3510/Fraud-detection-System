import requests

url = "http://127.0.0.1:8000/predict"
headers = {
    "Content-Type": "application/json",
    "X-API-Key": "mysecretkey"
}
data = {
    "V1": 0.1, "V2": 0.2, "V3": 0.3, "V4": 0.4, "V5": 0.5, "V6": 0.6, "V7": 0.7, "V8": 0.8, "V9": 0.9,
    "V10": 1.0, "V11": 1.1, "V12": 1.2, "V13": 1.3, "V14": 1.4, "V15": 1.5, "V16": 1.6, "V17": 1.7,
    "V18": 1.8, "V19": 1.9, "V20": 2.0, "V21": 2.1, "V22": 2.2, "V23": 2.3, "V24": 2.4, "V25": 2.5,
    "V26": 2.6, "V27": 2.7, "V28": 2.8, "Amount": 100.0
}

response = requests.post(url, headers=headers, json=data)
print("Status Code:", response.status_code)
print("Response:", response.json())
