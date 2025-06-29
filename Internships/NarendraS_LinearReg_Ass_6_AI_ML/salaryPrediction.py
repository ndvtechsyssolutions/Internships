import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Load the CSV file
df = pd.read_csv("Salary_Data.csv")

# Preview dataset
print("Dataset Preview:")
print(df.head())

# Scatter plot
plt.figure(figsize=(8, 6))
sns.scatterplot(x='YearsExperience', y='Salary', data=df)
plt.title("Years of Experience vs Salary")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.grid(True)
plt.show()

# Split the dataset
X = df[['YearsExperience']]
y = df['Salary']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"\nMean Squared Error: {mse:.2f}")
print(f"R² Score: {r2:.2f}")

# Regression line plot
plt.figure(figsize=(8, 6))
sns.scatterplot(x='YearsExperience', y='Salary', data=df, label="Actual")
plt.plot(X, model.predict(X), color='red', label='Regression Line')
plt.title("Regression Line Fit")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.legend()
plt.grid(True)
plt.show()

# BONUS 1: Error bars for test set
errors = abs(y_test - y_pred)
plt.figure(figsize=(8, 6))
plt.errorbar(X_test['YearsExperience'], y_pred, yerr=errors, fmt='o', label='Predicted ± Error', color='orange')
plt.scatter(X_test, y_test, label='Actual', color='blue')
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Prediction with Error Bars")
plt.legend()
plt.grid(True)
plt.show()

# BONUS 2: Bar chart for comparison
comparison_df = pd.DataFrame({'Actual': y_test.values, 'Predicted': y_pred})
comparison_df = comparison_df.reset_index(drop=True)

comparison_df.plot(kind='bar', figsize=(10, 6))
plt.title("Actual vs Predicted Salaries")
plt.xlabel("Sample Index")
plt.ylabel("Salary")
plt.grid(True)
plt.tight_layout()
plt.show()

# BONUS 3: Custom user input
def predict_custom_salary():
    try:
        exp = float(input("Enter years of experience to predict salary: "))
        prediction = model.predict([[exp]])
        print(f"Predicted Salary for {exp} years of experience: ₹{prediction[0]:,.2f}")
    except Exception as e:
        print("Invalid input:", e)

predict_custom_salary()

