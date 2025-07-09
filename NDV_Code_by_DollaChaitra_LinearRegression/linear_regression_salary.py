# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset
df = pd.read_csv('Salary_Data.csv')
print("First 5 rows of the dataset:")
print(df.head())

# Dataset information
print("\nDataset Info:")
print(df.info())

# Visualize the data
plt.figure(figsize=(8, 5))
sns.scatterplot(x='YearsExperience', y='Salary', data=df)
plt.title('Years of Experience vs. Salary')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.grid(True)
plt.tight_layout()
plt.show()

# Split the dataset into features and target
X = df[['YearsExperience']]
y = df['Salary']

# Train-test split (80/20)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"\nModel Evaluation:")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"R² Score: {r2:.2f}")

# Plot regression line over actual data
plt.figure(figsize=(8, 5))
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, model.predict(X), color='red', linewidth=2, label='Regression Line')
plt.title('Linear Regression Fit')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Error bars for test predictions
errors = y_test - y_pred
std_dev = np.std(errors)

plt.figure(figsize=(8, 5))
plt.errorbar(X_test.values.flatten(), y_pred, yerr=std_dev, fmt='o', label='Predictions with Error Bars', color='purple')
plt.xlabel('Years of Experience')
plt.ylabel('Predicted Salary')
plt.title('Test Predictions with Error Bars')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Bar chart comparison (actual vs predicted)
comparison_df = pd.DataFrame({'Actual': y_test.values, 'Predicted': y_pred})
comparison_df.reset_index(drop=True, inplace=True)
comparison_df.plot(kind='bar', figsize=(10, 5))
plt.title('Actual vs Predicted Salaries')
plt.xlabel('Index')
plt.ylabel('Salary')
plt.grid(True)
plt.tight_layout()
plt.show()

# User input prediction with error handling and valid feature formatting
while True:
    try:
        user_input = float(input("\nEnter years of experience to predict salary: "))
        user_pred = model.predict(pd.DataFrame({'YearsExperience': [user_input]}))
        print(f"Predicted Salary for {user_input} years of experience: ₹{user_pred[0]:,.2f}")
        break
    except ValueError:
        print("Invalid input. Please enter a numeric value (e.g., 2 or 4.5).")
    except Exception as e:
        print(f"An error occurred: {e}")
        break
