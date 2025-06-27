

import pandas as pd

df = pd.read_csv('Salary_Data.csv')
print(df.head())
print(df.info())
print(df.describe())

import seaborn as sns
import matplotlib.pyplot as plt

sns.scatterplot(x='YearsExperience', y='Salary', data=df)
plt.title('Salary vs. Years of Experience')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

from sklearn.model_selection import train_test_split

X = df[['YearsExperience']]
y = df['Salary']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import pandas as pd


y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error: {mse:.2f}')
print(f'R² Score: {r2:.2f}')


plt.scatter(X, y, color='blue', label='Actual')
plt.plot(X, model.predict(X), color='red', label='Regression Line')
plt.xlabel('Total Working Years')
plt.ylabel('Monthly Income')
plt.title('Linear Regression: Monthly Income vs. Total Working Years')
plt.legend()
plt.show()


errors = y - model.predict(X)
plt.errorbar(X['TotalWorkingYears'], y, yerr=abs(errors), fmt='o', label='Actual with Error Bars')
plt.plot(X, model.predict(X), color='red', label='Regression Line')
plt.xlabel('Total Working Years')
plt.ylabel('Monthly Income')
plt.title('Regression with Error Bars')
plt.legend()
plt.show()


compare = pd.DataFrame({'Actual': y_test.values, 'Predicted': y_pred})
compare.reset_index(drop=True, inplace=True)
compare.plot(kind='bar', figsize=(10, 5))
plt.title('Actual vs. Predicted Monthly Incomes')
plt.xlabel('Test Sample')
plt.ylabel('Monthly Income')
plt.tight_layout()
plt.show()
