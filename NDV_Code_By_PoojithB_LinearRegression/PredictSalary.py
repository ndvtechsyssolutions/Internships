# Salary Prediction Using Linear Regression

import pandas as pd  
import numpy as np   
import matplotlib.pyplot as plt 
import seaborn as sns  # For enhanced visualizations

# Mount Google Drive (only needed in Google Colab)
from google.colab import drive
drive.mount("/content/drive")

# Import Scikit-learn tools for machine learning
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset
df = pd.read_csv('/content/drive/MyDrive/Data/salary_data.csv')
print("First 5 rows of the dataset:")
print(df.head())  # Display first few records

# Explore the dataset
print("\nDataset Info:")
print(df.info())  # Get column types and missing values

print("\nStatistical Summary:")
print(df.describe())  # Summary statistics (mean, std, etc.)

# Visualize the data: Experience vs Salary
sns.scatterplot(x='YearsExperience', y='Salary', data=df)
plt.title("Experience vs Salary")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.grid(True)
plt.show()

# Prepare features (X) and target (y)
X = df[['YearsExperience']]  # Input variable
y = df['Salary']             # Output/target variable

# Split the data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Print model parameters
print(f"\nIntercept (b): {model.intercept_:.2f}")
print(f"Coefficient (m): {model.coef_[0]:.2f}")

# Make predictions on the test set
y_pred = model.predict(X_test)

# Compare predictions with actual values
results = pd.DataFrame({'Actual': y_test.values, 'Predicted': y_pred})
print("\nActual vs Predicted:\n")
print(results)

# Evaluate the model performance
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"\nMean Squared Error (MSE): {mse:.2f}")
print(f"R² Score: {r2:.2f}")  # Closer to 1 means better fit

# Visualize the regression line
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, model.predict(X), color='red', label='Regression Line')
plt.title("Regression Line - Experience vs Salary")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.legend()
plt.grid(True)
plt.show()

# Error bar plot to show prediction deviation
errors = abs(y_test.values - y_pred)
plt.errorbar(X_test.values.flatten(), y_pred, yerr=errors, fmt='o', color='green', ecolor='red', capsize=4)
plt.title("Prediction Error Bars")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.grid(True)
plt.show()

# Bar chart to compare actual vs predicted
results.reset_index(drop=True).plot(kind='bar', figsize=(10, 5))
plt.title("Actual vs Predicted Salary Comparison")
plt.ylabel("Salary")
plt.xlabel("Test Data Index")
plt.grid(True)
plt.show()

# Function to predict salary for custom input
def predict_salary():
    try:
        exp = float(input("Enter years of experience to predict salary: "))
        predicted = model.predict([[exp]])
        print(f"Predicted Salary for {exp} years of experience is ₹{predicted[0]:,.2f}")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

# Run user input prediction
predict_salary()
