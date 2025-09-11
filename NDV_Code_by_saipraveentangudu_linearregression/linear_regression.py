import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
data = pd.read_csv("Salary_Data.csv")

# Clean the data: Remove any rows with missing values
data = data.dropna()

# Define feature and target variable
age = data[["Age"]]          # Predictor (independent variable)
salary = data["Salary"]      # Target (dependent variable)

# Split the data into training and testing sets
age_train, age_test, salary_train, salary_test = train_test_split(
    age, salary, test_size=0.2, random_state=42
)

# Create and train the Linear Regression model
regressor = LinearRegression()
regressor.fit(age_train, salary_train)

# Predict salaries for the test set
salary_pred = regressor.predict(age_test)

# Evaluation metrics
print("Mean Squared Error (MSE):", mean_squared_error(salary_test, salary_pred))
print("R-squared (R²) Score:", r2_score(salary_test, salary_pred))
print("Model Coefficient (Slope):", regressor.coef_[0])
print("Model Intercept:", regressor.intercept_)

# Plotting the regression line and data points
plt.figure(figsize=(8, 5))
plt.scatter(age, salary, color='blue', label='Actual Salary')
plt.plot(age, regressor.predict(age), color='red', label='Regression Line')
plt.xlabel("Age")
plt.ylabel("Salary")
plt.title("Simple Linear Regression - Age vs Salary")
plt.legend()
plt.grid(True)
plt.show()
