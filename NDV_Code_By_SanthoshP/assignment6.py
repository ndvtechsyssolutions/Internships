# 1. Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# 2. Load Dataset
df = pd.read_csv('Salary_Data.csv')  # Make sure the file is in the same directory
print(df.head())

# 3. Visualize with Scatter Plot
plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x='YearsExperience', y='Salary', color='blue', s=100)
plt.title("Salary vs Years of Experience")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.grid(True)
plt.show()

# 4. Split the Dataset
X = df[['YearsExperience']]
y = df['Salary']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Train the Model
model = LinearRegression()
model.fit(X_train, y_train)

# 6. Predict on Test Data
y_pred = model.predict(X_test)

# 7. Evaluate the Model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Mean Squared Error: {mse:.2f}")
print(f"R² Score: {r2:.2f}")

# 8. Plot Regression Line
plt.figure(figsize=(8,6))
sns.scatterplot(x=X['YearsExperience'], y=y, label='Actual')
plt.plot(X, model.predict(X), color='red', label='Regression Line')
plt.title("Linear Regression Fit")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.legend()
plt.grid(True)
plt.show()

# BONUS: Prediction Error Bars
plt.figure(figsize=(8,6))
plt.errorbar(X_test['YearsExperience'], y_pred, yerr=np.sqrt(mse), fmt='o', label='Predicted with Error Bars', color='green')
plt.scatter(X_test['YearsExperience'], y_test, label='Actual', color='blue')
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.legend()
plt.title("Prediction vs Actual with Error Bars")
plt.grid(True)
plt.show()

# BONUS: Compare Predictions with Actual (Bar Chart)
comparison_df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
comparison_df.plot(kind='bar', figsize=(10,6))
plt.title("Actual vs Predicted Salary")
plt.xlabel("Index")
plt.ylabel("Salary")
plt.grid(True)
plt.tight_layout()
plt.show()

# BONUS: Predict salary from user input
def predict_salary():
    years = float(input("Enter years of experience: "))
    predicted_salary = model.predict([[years]])[0]
    print(f"Predicted Salary: ₹{predicted_salary:.2f}")

predict_salary()
