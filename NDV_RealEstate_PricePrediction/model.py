import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

def convert_sqft_to_num(x):
    try:
        if '-' in str(x):
            tokens = x.split('-')
            return (float(tokens[0]) + float(tokens[1])) / 2
        return float(x)
    except:
        return None

# Load the dataset
data = pd.read_csv('Bengaluru_House_Data.csv')

# Create bhk column
data['bhk'] = data['size'].str.extract('(\d+)').astype(float)

# Clean total_sqft
data['total_sqft'] = data['total_sqft'].apply(convert_sqft_to_num)

# Drop rows with missing/invalid data
data = data.dropna(subset=['location', 'total_sqft', 'bath', 'bhk', 'price'])

# Select features and target
X = data[['location', 'total_sqft', 'bath', 'bhk']]
y = data['price']

# Preprocess location
preprocessor = ColumnTransformer(
    transformers=[
        ('loc', OneHotEncoder(handle_unknown='ignore'), ['location'])
    ],
    remainder='passthrough'
)

# Build and train the pipeline
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('model', RandomForestRegressor(n_estimators=100, random_state=42))
])

pipeline.fit(X, y)

# Save the trained model
joblib.dump(pipeline, 'real_estate_model.pkl')
print("✅ Model trained and saved as real_estate_model.pkl")
