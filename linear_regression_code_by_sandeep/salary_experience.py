import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


data = {
    'YearsExperience': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Salary': [35000, 40000, 50000, 55000, 60000, 65000, 70000, 75000, 80000, 85000]
}

df = pd.DataFrame(data)


X = df[['YearsExperience']]  # feature matrix
y = df['Salary']             # target variable


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = LinearRegression()
model.fit(X_train, y_train)


y_pred = model.predict(X_test)


plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, model.predict(X), color='red', label='Regression Line')
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Linear Regression: Salary vs Experience")
plt.legend()
plt.show()


print(f"Intercept: {model.intercept_}")
print(f"Coefficient: {model.coef_[0]}")


experience = np.array([[5.5]])
predicted_salary = model.predict(experience)
print(f"Predicted Salary for 5.5 years of experience: ${predicted_salary[0]:,.2f}")
