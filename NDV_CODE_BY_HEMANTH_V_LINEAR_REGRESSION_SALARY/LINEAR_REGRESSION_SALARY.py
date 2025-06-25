# Upload and extract salary dataset
from google.colab import files
import zipfile
import os

# Upload the zip file
uploaded = files.upload()

# Extract the zip
zip_path = list(uploaded.keys())[0]
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall()
    extracted_files = zip_ref.namelist()

# Load the CSV file
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

csv_file = [f for f in extracted_files if f.endswith('.csv')][0]
df = pd.read_csv(csv_file)
print("✅ First 5 rows:")
print(df.head())

# Data exploration
print("\n📊 Dataset Info:")
print(df.info())

print("\n📈 Statistical Summary:")
print(df.describe())

# Scatter plot
sns.scatterplot(x='YearsExperience', y='Salary', data=df)
plt.title("Experience vs Salary")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.grid(True)
plt.show()

# Split data
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

X = df[['YearsExperience']]
y = df['Salary']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

print(f"\n🔧 Intercept: {model.intercept_:.2f}")
print(f"🧮 Coefficient: {model.coef_[0]:.2f}")

# Predict and compare
y_pred = model.predict(X_test)
results = pd.DataFrame({'Actual': y_test.values, 'Predicted': y_pred})
print("\n🎯 Actual vs Predicted:\n")
print(results)

# Evaluate
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"\n📉 Mean Squared Error (MSE): {mse:.2f}")
print(f"📊 R² Score: {r2:.2f}")

# Regression line plot
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, model.predict(X), color='red', label='Regression Line')
plt.title("Regression Line - Experience vs Salary")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.legend()
plt.grid(True)
plt.show()

# Error bar plot
errors = abs(y_test.values - y_pred)
plt.errorbar(X_test.values.flatten(), y_pred, yerr=errors, fmt='o', color='green', ecolor='red', capsize=4)
plt.title("Prediction Error Bars")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.grid(True)
plt.show()

# Bar chart comparison
results.reset_index(drop=True).plot(kind='bar', figsize=(10, 5))
plt.title("Actual vs Predicted Salary Comparison")
plt.ylabel("Salary")
plt.xlabel("Test Data Index")
plt.grid(True)
plt.show()

# User input salary prediction
def predict_salary():
    try:
        exp = float(input("Enter years of experience to predict salary: "))
        predicted = model.predict([[exp]])
        print(f"💼 Predicted Salary for {exp} years of experience is ₹{predicted[0]:,.2f}")
    except ValueError:
        print("⚠️ Invalid input. Please enter a numeric value.")

predict_salary()
