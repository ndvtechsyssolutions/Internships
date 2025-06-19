import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('data/Salary_Data.csv')


# Display first 5 rows
print("\n📄 First 5 Records:\n", df.head())

# Basic info
print("\n📋 Dataset Info:")
print(df.info())

# Summary statistics
print("\n📊 Statistical Summary:\n", df.describe())

# Check for missing values
print("\n❓ Missing Values:\n", df.isnull().sum())

# Scatter plot of YearsExperience vs Salary
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='YearsExperience', y='Salary', color='blue')
plt.title("Years of Experience vs. Salary")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.tight_layout()
plt.savefig('visuals/scatter_with_regression.png')

plt.show()

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Step 1: Split data into features and target
X = df[['YearsExperience']]  # Feature must be 2D
y = df['Salary']

# Step 2: Split into training and testing sets (80/20 split)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 4: Predict on test data
y_pred = model.predict(X_test)

# Step 5: Evaluate model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\n📈 Model Evaluation:")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"R² Score: {r2:.4f}")


# Plot regression line on top of scatter plot
plt.figure(figsize=(8, 5))
sns.scatterplot(x=X['YearsExperience'], y=y, color='blue', label='Actual')
plt.plot(X, model.predict(X), color='red', label='Regression Line')
plt.title("Linear Regression Fit")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.legend()
plt.tight_layout()
plt.savefig('visuals/regression_line_plot.png')
plt.show()


import numpy as np

# Bar chart comparing actual vs predicted salaries
plt.figure(figsize=(10, 6))
x_indexes = np.arange(len(y_test))
width = 0.35

plt.bar(x_indexes, y_test, width=width, label='Actual', color='blue')
plt.bar(x_indexes + width, y_pred, width=width, label='Predicted', color='orange')

plt.xlabel("Test Samples")
plt.ylabel("Salary")
plt.title("Actual vs Predicted Salaries")
plt.legend()
plt.tight_layout()
plt.savefig('visuals/predicted_vs_actual_bar.png')
plt.show()


# User input for custom prediction
try:
    exp_input = float(input("\n🔢 Enter years of experience to predict salary: "))
    salary_output = model.predict([[exp_input]])
    print(f"💼 Predicted Salary for {exp_input} years of experience: ₹{salary_output[0]:,.2f}")
except:
    print("⚠️ Invalid input. Please enter a numeric value.")


