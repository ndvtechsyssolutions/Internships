# Step 1: Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Step 2: Create sample dataset
data = {
    'location': ['Indira Nagar', 'Whitefield', 'Electronic City', 'HSR Layout', 'Marathahalli'],
    'sqft': [1000, 1500, 850, 1250, 1000],
    'bhk': [2, 3, 2, 3, 2],
    'bath': [2, 3, 1, 2, 2],
    'price': [80, 120, 60, 110, 85]  # Price in Lakhs
}
df = pd.DataFrame(data)

# Step 3: Save to CSV
df.to_csv('housing.csv', index=False)

# Step 4: Load the dataset
df = pd.read_csv('housing.csv')

# Step 5: Encode categorical column
le = LabelEncoder()
df['location'] = le.fit_transform(df['location'])

# Step 6: Define features and label
X = df[['location', 'sqft', 'bhk', 'bath']]
y = df['price']

# Step 7: Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 8: Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 9: Predict and evaluate
y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("Model Evaluation:")
print(f"RMSE: {rmse:.2f}")
print(f"R² Score: {r2:.2f}")

# Step 10: Test prediction
sample = pd.DataFrame({
    'location': le.transform(['Whitefield']),  # Encode using same encoder
    'sqft': [1400],
    'bhk': [3],
    'bath': [2]
})

predicted_price = model.predict(sample)[0]
print(f"\nPredicted price for sample input: ₹{predicted_price:.2f} Lakhs")
