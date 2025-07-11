# Step 1: Mount your google drive
from google.colab import drive
drive.mount('/content/drive')
# Step 2: Import Required Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
# Step 3: Load the Dataset into a Pandas DataFrame
df = pd.read_csv("/content/drive/MyDrive/data_ndv/netflix_titles.csv")
print("\nFirst 5 records:")
print(df.head())
print("\nLast 5 records: ")
print(df.tail())
# Step 4: Inspect the Dataset
print("\nDataset shape:", df.shape)
print("\nData Types:")
print(df.dtypes)
print("\nMissing Values:")
print(df.isnull().sum())
print("\nDuplicate Records:", df.duplicated().sum())
# Step 5: Drop Duplicate Records
df.drop_duplicates(inplace=True)
print("\nShape after removing duplicates:", df.shape)
# Step 6: Handle Missing Values
# Fill 'rating' with mode
rating_mode = df['rating'].mode()[0]
df['rating'].fillna(rating_mode, inplace=True)
# Fill 'country' and 'director' with 'Unknown'
df['country'].fillna("Unknown", inplace=True)
df['director'].fillna("Unknown", inplace=True)
# Drop rows where 'cast' is missing
df.dropna(subset=['cast'], inplace=True)
# Step 6.1: Clean and Convert 'date_added'
# Strip spaces and convert to datetime, coercing errors to NaT
df['date_added'] = df['date_added'].str.strip()
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
# Check and drop rows with invalid or missing 'date_added'
print("\nMissing or invalid 'date_added' entries:", df['date_added'].isnull().sum())
df = df.dropna(subset=['date_added'])
# Step 6.2: Fill missing 'duration' with mode per 'type'
for content_type in df['type'].unique():
    mode_val = df[df['type'] == content_type]['duration'].mode()[0]
    df.loc[(df['type'] == content_type) & (df['duration'].isnull()), 'duration'] = mode_val
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())
# Step 7: Convert Data Types
# 'date_added' is already datetime
# Create new columns for year and month added
df['year_added'] = df['date_added'].dt.year
df['month_added'] = df['date_added'].dt.month
# Step 8: NumPy Transformations
# Calculate title length using NumPy
df['title_length'] = df['title'].apply(lambda x: np.char.str_len(x))
# Step 9: Filtering, Sorting, Grouping
# Filter only Movies
movies_df = df[df['type'] == 'Movie']
# Sort dataset by year_added descending
df_sorted = df.sort_values(by='year_added', ascending=False)
# Group by content type
type_counts = df['type'].value_counts()
print("\nContent Type Counts:")
print(type_counts)
# Step 10: Summary Statistics
print("\nSummary Statistics:")
print(df.describe(include='all'))
# Step 11: Visualizations
# Visualize missing data using heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title("Missing Value Heatmap")
plt.show()
# Correlation matrix for numerical fields
plt.figure(figsize=(8, 6))
sns.heatmap(df[['title_length', 'month_added', 'year_added']].corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()
# Bar chart of content type distribution
sns.countplot(data=df, x='type', palette='Set2')
plt.title("Content Type Distribution")
plt.show()
# Step 12: Label Encoding for ML-readiness
le = LabelEncoder()
df['type_encoded'] = le.fit_transform(df['type'])
df['rating_encoded'] = le.fit_transform(df['rating'])
# Step 13: Save Cleaned Dataset
df.to_csv("clean_netflix_titles.csv", index=False)
print("\nCleaned dataset saved as 'clean_netflix_titles.csv'")
