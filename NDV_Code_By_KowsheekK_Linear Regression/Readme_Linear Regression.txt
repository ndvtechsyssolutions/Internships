# Assignment 6: Linear Regression for Predicting Salary

## Objective

This project aims to predict an employee's salary based on their years of experience using **Simple Linear Regression** in Python.

---

## Dataset

The dataset used is a CSV file with the following columns:

- `YearsExperience`: Number of years an employee has worked
- `Salary`: Corresponding salary in INR

> Filename: `65d8f876-b79f-4313-bd84-b97d519af928.csv`  
> Source: Provided by the instructor

---

## Steps Performed

1. **Loaded** the dataset using Pandas.
2. **Explored** basic statistics and data types.
3. **Visualized** the relationship using a scatter plot.
4. **Split** the data into training and testing sets (80/20 split).
5. **Trained** a linear regression model using `sklearn`.
6. **Predicted** salary for the test set.
7. **Evaluated** the model using:
   - Mean Squared Error (MSE)
   - R² Score
8. **Visualized**:
   - Regression line on data
   - Error bars showing prediction uncertainty
   - Actual vs. Predicted salary comparison bar chart
9. **User Input**: Added functionality to enter custom years of experience and predict salary.

---

## Sample Output
Mean Squared Error: 37717.50
R² Score: 0.95

Predicted Salary for 4.5 years of experience is: ₹73,524.80

