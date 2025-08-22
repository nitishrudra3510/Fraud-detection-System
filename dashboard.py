import streamlit as st
import requests

st.title("Fraud Detection Dashboard")

st.sidebar.header("Transaction Input")
def user_input_features():
    features = {}
    for i in range(1, 29):
        features[f"V{i}"] = st.sidebar.number_input(f"V{i}", value=0.0)
    features["Amount"] = st.sidebar.number_input("Amount", value=0.0)
    return features

input_data = user_input_features()

if st.button("Predict Fraud"):
    url = "http://127.0.0.1:8000/predict"
    headers = {"Content-Type": "application/json", "X-API-Key": "mysecretkey"}
    response = requests.post(url, headers=headers, json=input_data)
    if response.status_code == 200:
        result = response.json()
        st.success(f"Fraud: {result['is_fraud']} (Probability: {result['probability']:.4f})")
    else:
        st.error(f"API Error: {response.status_code}")

st.sidebar.markdown("---")
st.sidebar.write("Model Info:")
if st.sidebar.button("Show Model Info"):
    url = "http://127.0.0.1:8000/model_info"
    headers = {"X-API-Key": "mysecretkey"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        st.sidebar.json(response.json())
    else:
        st.sidebar.error(f"API Error: {response.status_code}")
