# Description:- Salary Prediction using Simple Linear Regression

# import the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# import the dataset
dataset = pd.read_csv("Salary_Data.csv")
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

print(dataset)

OUTPUT:-
    YearsExperience    Salary
0               1.1   39343.0
1               1.3   46205.0
2               1.5   37731.0
3               2.0   43525.0
4               2.2   39891.0
5               2.9   56642.0
6               3.0   60150.0
7               3.2   54445.0
8               3.2   64445.0
9               3.7   57189.0
10              3.9   63218.0
11              4.0   55794.0
12              4.0   56957.0
13              4.1   57081.0
14              4.5   61111.0
15              4.9   67938.0
16              5.1   66029.0
17              5.3   83088.0
18              5.9   81363.0
19              6.0   93940.0
20              6.8   91738.0
21              7.1   98273.0
22              7.9  101302.0
23              8.2  113812.0
24              8.7  109431.0
25              9.0  105582.0
26              9.5  116969.0
27              9.6  112635.0
28             10.3  122391.0
29             10.5  121872.0

# split the dataset into training and test set
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# train the simple linear regression model on the training set
from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(X_train, y_train)

# predict the test set results
y_pred = regressor.predict(X_test)

# visualize the training set results
plt.scatter(X_train, y_train, color="red")
plt.plot(X_train, regressor.predict(X_train), color="green")
plt.title("Salary vs Experience (Training Set)")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()

# predict the salary of an employee with 5 years of experience
mid_level = round(regressor.predict([[5]])[0], 2)
print("Salary prediction for a mid level role:", mid_level)

# predict the salary of an employee with 12 years of experience
senior_level = round(regressor.predict([[12]])[0], 2)
print("Salary prediction for a senior level role:", senior_level)

# get the coefficients and intercept
print(round(regressor.coef_[0], 2))
print(round(regressor.intercept_, 2))

OUPUT:-
Salary prediction for a mid level role: 73342.97
Salary prediction for a senior level role: 138531.0
9312.58
26780.1
