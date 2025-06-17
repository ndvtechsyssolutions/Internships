import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

data = pd.read_csv('Salary_Data.csv')

data.columns = data.columns.str.strip()

print("Column names in dataset:", data.columns.tolist())

data.rename(columns={
    'Years of Experience': 'YearsExperience',
    'Salary (INR)': 'Salary'
}, inplace=True)

data.dropna(inplace=True)

if 'YearsExperience' not in data.columns or 'Salary' not in data.columns:
    raise ValueError("Dataset must contain 'YearsExperience' and 'Salary' columns.")

print("\nData types:\n", data.dtypes)

data['YearsExperience'] = pd.to_numeric(data['YearsExperience'], errors='coerce')
data['Salary'] = pd.to_numeric(data['Salary'], errors='coerce')
data.dropna(inplace=True)

print("\nFirst 5 rows:\n", data.head())

plt.figure(figsize=(8, 6))
sns.scatterplot(x='YearsExperience', y='Salary', data=data)
plt.title("Years of Experience vs. Salary")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.grid(True)
plt.show()

X = data[['YearsExperience']]
y = data['Salary']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"\nMean Squared Error (MSE): {mse:.2f}")
print(f"R² Score: {r2:.2f}")

# Plot regression line
plt.figure(figsize=(8, 6))
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, model.predict(X), color='red', label='Regression Line')
plt.title("Regression Line - Salary vs Experience")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.legend()
plt.grid(True)
plt.show()

# Bonus 1: Error bars
errors = y_test - y_pred
plt.figure(figsize=(8, 6))
plt.errorbar(X_test.values.flatten(), y_pred, yerr=np.abs(errors), fmt='o', label='Prediction with Error Bars')
plt.title("Predictions with Error Bars")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.grid(True)
plt.legend()
plt.show()

# Bonus 2: Actual vs Predicted bar chart
comparison_df = pd.DataFrame({'Actual': y_test.values, 'Predicted': y_pred})
comparison_df.reset_index(drop=True, inplace=True)
comparison_df.plot(kind='bar', figsize=(10, 6))
plt.title("Actual vs Predicted Salaries")
plt.ylabel("Salary")
plt.xticks(rotation=0)
plt.grid(True)
plt.show()

# Bonus 3: User input prediction
try:
    user_exp = float(input("\nEnter years of experience to predict salary: "))
    user_salary = model.predict(np.array([[user_exp]]))[0]
    print(f"Predicted salary for {user_exp} years of experience is: ₹{user_salary:.2f}")
except ValueError:
    print("Invalid input! Please enter a numeric value.")
