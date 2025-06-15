import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score
import matplotlib.pyplot as plt


df = pd.read_csv("Salary_Data.csv")
df.dropna(inplace = True)
df.head()

X = df[["Age"]]
y = df["Salary"]
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2,random_state = 42)
model = LinearRegression()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)

print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R-squared Score:", r2_score(y_test, y_pred))
print("Slope:", model.coef_)
print("Intercept:", model.intercept_)


plt.scatter(X, y, color='blue', label='Actual')
plt.plot(X, model.predict(X), color='red', label='Predicted')
plt.xlabel("Age")
plt.ylabel("Salary")
plt.title("Linear Regression")
plt.legend()
plt.grid(True)
plt.show()
