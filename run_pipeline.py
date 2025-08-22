import pandas as pd
from src.features.build_features import build_features
from src.models.train import train_model
from src.models.evaluate import evaluate_model
from src.models.thresholding import tune_threshold
import joblib
import os

# 1. Load data
RAW_DATA = 'data/raw/creditcard.csv'
df = pd.read_csv(RAW_DATA)

# 2. Feature engineering
features = build_features(df)

# 3. Prepare train/test split
from sklearn.model_selection import train_test_split
X = features.drop('Class', axis=1)
y = features['Class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# 4. Train model
model = train_model(X_train, y_train)

# 5. Evaluate model
print('Evaluation:')
y_pred, y_prob = evaluate_model(model, X_test, y_test)

# 6. Threshold tuning
print('Threshold tuning:')
best_thresh, best_f1 = tune_threshold(y_test, y_prob)

# 7. Save model for serving
joblib.dump(model, 'model.joblib')
print('Model saved to model.joblib')
