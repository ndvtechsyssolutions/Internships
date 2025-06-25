# Salary Prediction Using Linear Regression

# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from google.colab import drive
drive.mount("/content/drive")

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset
df = pd.read_csv('/content/drive/MyDrive/Data/salary_data.csv')
print("First 5 rows of the dataset:")
print(df.head())

# Explore the dataset
print("\nDataset Info:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

# Scatter plot to visualize the relationship
sns.scatterplot(x='YearsExperience', y='Salary', data=df)
plt.title("Experience vs Salary")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.grid(True)
plt.show()

# Split the data
X = df[['YearsExperience']]
y = df['Salary']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Train the model
model = LinearRegression()
model.fit(X_train, y_train)

print(f"\nIntercept: {model.intercept_:.2f}")
print(f"Coefficient: {model.coef_[0]:.2f}")

# Predict on test set
y_pred = model.predict(X_test)

# Compare predictions with actual values
results = pd.DataFrame({'Actual': y_test.values, 'Predicted': y_pred})
print("\nActual vs Predicted:\n")
print(results)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"\nMean Squared Error (MSE): {mse:.2f}")
print(f"R² Score: {r2:.2f}")

# Plot regression line with all data
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, model.predict(X), color='red', label='Regression Line')
plt.title("Regression Line - Experience vs Salary")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.legend()
plt.grid(True)
plt.show()

# Error bars on test predictions
errors = abs(y_test.values - y_pred)
plt.errorbar(X_test.values.flatten(), y_pred, yerr=errors, fmt='o', color='green', ecolor='red', capsize=4)
plt.title("Prediction Error Bars")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.grid(True)
plt.show()

# Bar chart comparison
results.reset_index(drop=True).plot(kind='bar', figsize=(10,5))
plt.title("Actual vs Predicted Salary Comparison")
plt.ylabel("Salary")
plt.xlabel("Test Data Index")
plt.grid(True)
plt.show()

# User input prediction
def predict_salary():
    try:
        exp = float(input("Enter years of experience to predict salary: "))
        predicted = model.predict([[exp]])
        print(f"Predicted Salary for {exp} years of experience is ₹{predicted[0]:,.2f}")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

# Run the prediction
predict_salary()
