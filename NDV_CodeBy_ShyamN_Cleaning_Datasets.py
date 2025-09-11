# Netflix Dataset Preprocessing using Pandas and NumPy

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

# Load the dataset
df = pd.read_csv('netflix_titles.csv')
print("Original dataset shape:", df.shape)

# Check for basic issues
print("\nMissing values:\n", df.isnull().sum())
print("\nDuplicate entries:", df.duplicated().sum())

# --- Data Cleaning ---

# Drop entries without a title
df.dropna(subset=['title'], inplace=True)

# Fill missing values with appropriate defaults
df['director'].fillna('Unknown', inplace=True)
df['cast'].fillna('Not Available', inplace=True)
df['country'].fillna(df['country'].mode()[0], inplace=True)
df['date_added'].fillna(method='ffill', inplace=True)
df['rating'].fillna(df['rating'].mode()[0], inplace=True)

# Remove duplicate records
df.drop_duplicates(inplace=True)

# Convert date column to datetime format
df['date_added'] = pd.to_datetime(df['date_added'])

# Extract numeric duration in minutes
df['duration_minutes'] = df['duration'].str.extract('(\d+)').astype(float).fillna(0)

# --- Summary and Analysis ---

# Basic statistics
print("\nSummary statistics for numerical fields:\n")
print(df.describe())

# Average duration using NumPy
print("\nAverage content duration (in minutes):", np.mean(df['duration_minutes']))

# --- Visualizations ---

# Null values heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title("Missing Values Heatmap")
plt.show()

# Correlation matrix of numerical features
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()

# --- Label Encoding for ML Readiness ---

le = LabelEncoder()
df['type_encoded'] = le.fit_transform(df['type'])
df['rating_encoded'] = le.fit_transform(df['rating'])

print("\nEncoding complete. Sample encoded data:\n")
print(df[['type', 'type_encoded', 'rating', 'rating_encoded']].head())

print("\nFinal cleaned dataset shape:", df.shape)
