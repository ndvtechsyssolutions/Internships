##assignment-6
# 1. Import Required Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# 2. Load Dataset
df = pd.read_csv('salary_data.csv')  # make sure this file is in the same folder
print(" First 5 Rows of the Dataset:")
print(df.head())

# 3. Dataset Information
print("\n Dataset Info:")
print(df.info())

# 4. Scatter Plot - Data Visualization
plt.figure(figsize=(8,6))
sns.scatterplot(x='YearsExperience', y='Salary', data=df, color='teal')
plt.title('Years of Experience vs Salary')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.grid(True)
plt.show()

# 5. Feature and Target
X = df[['YearsExperience']]  # Feature
y = df['Salary']             # Target

# 6. Train-Test Split (80/20)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# 7. Linear Regression Model Training
model = LinearRegression()
model.fit(X_train, y_train)

# 8. Predictions on Test Data
y_pred = model.predict(X_test)

# 9. Model Evaluation
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"\n Model Performance:")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"R² Score: {r2:.2f}")

# 10. Plot Regression Line
plt.figure(figsize=(8,6))
sns.scatterplot(x='YearsExperience', y='Salary', data=df, color='blue', label='Actual')
plt.plot(df['YearsExperience'], model.predict(X), color='red', label='Regression Line')
plt.title('Linear Regression Fit')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.legend()
plt.grid(True)
plt.show()

# 11. Bonus: Confidence Interval
from scipy.stats import t
n = len(X_test)
se = np.sqrt(mse)
t_score = t.ppf(0.975, df=n-1)
conf_interval = t_score * se

plt.figure(figsize=(8,6))
plt.scatter(X_test, y_test, color='green', label='Actual')
plt.plot(X_test, y_pred, color='orange', label='Predicted')
plt.fill_between(X_test['YearsExperience'], y_pred - conf_interval, y_pred + conf_interval,
                 color='gray', alpha=0.3, label='95% Confidence Interval')
plt.title('Prediction with Confidence Interval')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.legend()
plt.grid(True)
plt.show()

# 12. Bonus: Bar Chart - Actual vs Predicted
comparison_df = pd.DataFrame({'Actual': y_test.values, 'Predicted': y_pred})
comparison_df.plot(kind='bar', figsize=(10,6), colormap='Set3')
plt.title('Comparison: Actual vs Predicted Salaries')
plt.xlabel('Index')
plt.ylabel('Salary')
plt.tight_layout()
plt.grid(True)
plt.show()

# 13. Bonus: Predict Based on User Input
def predict_custom_salary():
    try:
        exp = float(input("Enter Years of Experience: "))
        pred_salary = model.predict([[exp]])[0]
        print(f" Predicted Salary for {exp:.1f} years of experience: ₹{pred_salary:.2f}")
    except:
        print(" Please enter a valid number.")

predict_custom_salary()
