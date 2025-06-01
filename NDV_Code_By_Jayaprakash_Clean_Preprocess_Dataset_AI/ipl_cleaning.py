import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('sample_ipl.csv')
print("Initial Data:")
print(df.head())

# Inspect the dataset
print("\nData Info:")
print(df.info())
print("\nSummary Statistics:")
print(df.describe(include='all'))

# Check for duplicates and missing values
print("\nDuplicate Rows:", df.duplicated().sum())
print("\nMissing Values:\n", df.isnull().sum())

# Drop duplicate records
df.drop_duplicates(inplace=True)

# Handle missing values
df['Player'].fillna("Unknown", inplace=True)
df['Runs'].fillna(df['Runs'].mean(), inplace=True)
df['Average'].fillna(df['Average'].mean(), inplace=True)

# Ensure correct data types
df = df.astype({ "Matches": int, "Runs": float, "Average": float })
print("\nData Types After Cleaning:")
print(df.info())

# Visualize missing values
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title('Missing Values Heatmap')
plt.show()

# Correlation Matrix
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()
