import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set style for plots
sns.set(style="whitegrid")

#Generate Synthetic Data

# Set random seed for consistency
np.random.seed(1)

# Create date range from Jan 1 to Mar 1, 2025
date_range = pd.date_range(start='2025-01-01', end='2025-03-01')

# List of fruit products
fruits = ['Apples', 'Bananas', 'Oranges', 'Grapes', 'Mangoes']

# Generate 200 rows of random data
data = {
    'Date': np.random.choice(date_range, size=200),
    'Fruit': np.random.choice(fruits, size=200),
    'Sales_Amount': np.random.randint(50, 500, size=200),   # In Rupees
    'Units_Sold': np.random.randint(1, 10, size=200)         # Quantity sold
}

# Create DataFrame
df = pd.DataFrame(data)

# Ensure 'Date' is datetime
df['Date'] = pd.to_datetime(df['Date'])

# Preview the data
print("First 5 Rows:")
print(df.head())


# Simple EDA

# Basic info
print("\n Data Info:")
print(df.info())

# Summary statistics
print("\n Summary Statistics:")
print(df.describe())

# Check for missing values
print("\n Missing Values:")
print(df.isnull().sum())
#visualization

#Daily Sales Trend
daily_sales = df.groupby('Date')['Sales_Amount'].sum()

plt.figure(figsize=(10, 5))
daily_sales.plot()
plt.title("Daily Fruit Sales (₹)")
plt.xlabel("Date")
plt.ylabel("Total Sales (₹)")
plt.grid(True)
plt.tight_layout()
plt.show()

#Average Sales per Fruit
plt.figure(figsize=(8, 5))
sns.barplot(x='Fruit', y='Sales_Amount', data=df, estimator=np.mean)
plt.title("Average Sales by Fruit")
plt.ylabel("Avg Sales (₹)")
plt.tight_layout()
plt.show()

#Units Sold Distribution by Fruit
plt.figure(figsize=(8, 5))
sns.boxplot(x='Fruit', y='Units_Sold', data=df)
plt.title("Units Sold per Fruit")
plt.tight_layout()
plt.show()

#printing output
print("\n Retail Fruit Sales Analysis Complete!")
Footer
© 2
