import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import joblib
import os

# Load dataset
df = pd.read_csv('data/Bengaluru_House_Data.csv')

# Feature Engineering - Extract BHK from 'size'
def extract_bhk(x):
    try:
        return int(str(x).split(' ')[0])
    except:
        return None

df['bhk'] = df['size'].apply(extract_bhk)

# Clean 'total_sqft' column
def convert_sqft(x):
    try:
        if '-' in str(x):
            tokens = str(x).split('-')
            return (float(tokens[0]) + float(tokens[1])) / 2
        elif str(x).replace('.', '', 1).isdigit():
            return float(x)
        else:
            return None  # Skip non-numeric like '15Acres'
    except:
        return None

df['total_sqft'] = df['total_sqft'].apply(convert_sqft)

# Drop missing values
df = df.dropna(subset=['location', 'total_sqft', 'bath', 'bhk', 'price'])

# Select Features and Target
X = df[['total_sqft', 'bath', 'bhk']]
y = df['price']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build Pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', RandomForestRegressor(n_estimators=100, random_state=42))
])

# Train Model
pipeline.fit(X_train, y_train)

# Save Model
os.makedirs('model', exist_ok=True)
joblib.dump(pipeline, 'model/model.pkl')

print("Model trained and saved as 'model/model.pkl'")
