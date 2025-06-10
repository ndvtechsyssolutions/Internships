# Clean and Preprocess Netflix Dataset

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from sklearn.preprocessing import LabelEncoder
import warnings
warnings.filterwarnings('ignore')

pd.set_option('display.max_columns', None)

# Loading the dataset
file_path = r"C:/Users/santh/Downloads/archive/netflix_titles.csv"
df = pd.read_csv(file_path)
print("Dataset loaded successfully. Shape:", df.shape)

# Checking for null values and duplicates
print("\nData Types and Missing Values:")
print(df.info())

print("\nMissing Values Count:")
print(df.isnull().sum())

print("\nDuplicates Count:")
print(df.duplicated().sum())

# For simplicity, fill missing 'director', 'cast', 'country', 'rating', 'date_added' with placeholders
df['director'].fillna("Unknown", inplace=True)
df['cast'].fillna("Unknown", inplace=True)
df['country'].fillna("Unknown", inplace=True)
df['rating'].fillna("Not Rated", inplace=True)
df['date_added'].fillna("Unknown", inplace=True)

# dropping rows with missing 'duration' and 'release_year'
df.dropna(subset=['duration', 'release_year'], inplace=True)

# removing the duplicates
duplicates_removed = df.duplicated().sum()
df.drop_duplicates(inplace=True)
print(f"Removed {duplicates_removed} duplicate rows.")

# converting the data types for better memory efficiency

# Convert 'date_added' to datetime (coerce errors to NaT)
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# Ensure 'release_year' is integer
df['release_year'] = df['release_year'].astype(int)

# feature engineering: Extracting useful features

# Extract year, month, day from date_added
df['year_added'] = df['date_added'].dt.year
df['month_added'] = df['date_added'].dt.month
df['day_added'] = df['date_added'].dt.day

# Calculate 'content_age' as difference between current year and release_year
current_year = datetime.now().year
df['content_age'] = current_year - df['release_year']

# Clean 'duration' column: separate number and unit (min or seasons)
df['duration_num'] = df['duration'].str.extract(r'(\d+)').astype(int)
df['duration_unit'] = df['duration'].str.extract('([a-zA-Z]+)')

# summary statistics and data exploration

print("\nSummary statistics for numerical columns:")
print(df.describe())

print("\nSummary of categorical columns:")
print(df.describe(include=['object']))

# -using numpy for normalization and scaling

# Example: normalize content_age using Min-Max scaling with NumPy
min_age = df['content_age'].min()
max_age = df['content_age'].max()
df['content_age_norm'] = (df['content_age'] - min_age) / (max_age - min_age)

# using pandas for data exploration

# Example: Top 5 countries with most titles
top_countries = df['country'].value_counts().head(5)
print("\nTop 5 countries by number of titles:")
print(top_countries)

# Group by type and count
type_counts = df.groupby('type').size()
print("\nCount by type (Movie/TV Show):")
print(type_counts)

# using seaborn and matplotlib for visualization

# Visualize missing values heatmap
plt.figure(figsize=(10,6))
sns.heatmap(df.isnull(), cbar=False, yticklabels=False, cmap='viridis')
plt.title("Missing Values Heatmap")
plt.show()

# Correlation matrix for numerical fields
numeric_cols = ['release_year', 'duration_num', 'content_age', 'content_age_norm']
plt.figure(figsize=(8,5))
sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()

# Label Encoding for ML readiness

label_encoders = {}
for col in ['type', 'rating', 'duration_unit', 'country']:
    le = LabelEncoder()
    df[col+'_encoded'] = le.fit_transform(df[col].astype(str))
    label_encoders[col] = le

print("\nLabel encoding applied for columns: type, rating, duration_unit, country")

# --- Final DataFrame Overview ---
print("\nFinal DataFrame preview:")
print(df.head())

# Optionally save cleaned data to CSV
df.to_csv("cleaned_netflix_titles.csv", index=False)
