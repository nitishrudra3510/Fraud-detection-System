# Fraud Detection Project

## Overview
A modular, production-grade pipeline for detecting fraudulent transactions using machine learning. Includes data processing, feature engineering, model training, real-time serving, monitoring, and infrastructure setup.

## Architecture
- Data ingestion, processing, and feature engineering
- Model training, evaluation, and threshold tuning
- Real-time API and streaming pipeline
- Monitoring and drift detection
- Infrastructure: Docker, Airflow, MLflow

## Setup
1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. See `infra/docker/` and `infra/airflow/` for infra setup

## Demo
- Run notebooks in `notebooks/`
- Start API: `cd src/serving && uvicorn app:app --reload`

---

See each module's README or docstrings for details.
# Fraud-detection-System
