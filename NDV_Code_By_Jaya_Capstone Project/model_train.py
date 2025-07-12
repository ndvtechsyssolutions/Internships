# Real Estate Price Prediction with Boston Housing Dataset

## 1. Import Libraries
 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
import joblib


## 2. Load and Preprocess Dataset
 
# Load the dataset
df = pd.read_csv("real_estate.csv")

# Handle missing values
imputer = SimpleImputer(strategy='mean')
df[['RM']] = imputer.fit_transform(df[['RM']])

# Feature Scaling
scaler = StandardScaler()
scaled_features = scaler.fit_transform(df.drop("MEDV", axis=1))
X = pd.DataFrame(scaled_features, columns=df.columns[:-1])
y = df["MEDV"]


## 3. Split Data and Train Model
 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

## 4. Evaluate Model
 
from math import sqrt

rmse = sqrt(mean_squared_error(y_test, y_pred))
print("RMSE:", rmse)
print("MAE:", mean_absolute_error(y_test, y_pred))
print("R² Score:", r2_score(y_test, y_pred))


## 5. Save Model and Scaler
 
joblib.dump(model, "boston_rf_model.pkl")
joblib.dump(scaler, "boston_scaler.pkl")