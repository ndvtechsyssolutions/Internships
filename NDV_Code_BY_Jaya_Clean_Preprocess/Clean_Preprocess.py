import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

# Load Dataset
file_path = "C:/Users/jayal/OneDrive/Desktop/AI_ML Internship/netflix_titles.csv"  # path
df = pd.read_csv(file_path)

# Step 1: Display the first few records
print("Initial Data Preview:")
print(df.head())

# Step 2: Dataset structure and basic info
print("\nDataset Info:")
print(df.info())

# Step 3: Check for missing values
print("\nMissing Values Count:")
print(df.isnull().sum())

# Step 4: Check for duplicate rows
print("\nNumber of Duplicates:", df.duplicated().sum())

# Step 5: Drop rows with too many missing values
df = df.dropna(thresh=4)

# Step 6: Fill or drop missing values
if 'Rating' in df.columns:
    df['Rating'] = df['Rating'].fillna(df['Rating'].mode()[0])

df = df.dropna()

# Step 7: Remove duplicate records
df = df.drop_duplicates()

# Step 8: Convert data types
if 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Step 9: Add new column using NumPy
if 'Rating' in df.columns:
    df['Is_High_Rated'] = np.where(df['Rating'] > 7.0, 1, 0)

# Step 10: Filter, sort, and group
if 'Type' in df.columns:
    print("\nFiltered Movies Only:")
    movies = df[df['Type'] == 'Movie']
    print(movies.head())

if 'Rating' in df.columns:
    print("\nTop 5 Rated Records:")
    print(df.sort_values(by='Rating', ascending=False).head())

if 'Genre' in df.columns and 'Rating' in df.columns:
    print("\nAverage Rating per Genre:")
    genre_rating = df.groupby('Genre')['Rating'].mean()
    print(genre_rating)

# Step 11: Summary Statistics
print("\nSummary Statistics:")
print(df.describe(include='all'))

# Step 12: Heatmap of Null Values (Bonus)
print("\nVisualizing Null Values...")
plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title("Missing Values Heatmap")
plt.show()

# Step 13: Correlation Matrix (Bonus)
print("\nCorrelation Matrix:")
corr = df.corr(numeric_only=True)
plt.figure(figsize=(10, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()

# Step 14: Label Encoding (Bonus)
le = LabelEncoder()
for col in df.select_dtypes(include='object').columns:
    df[col] = le.fit_transform(df[col])

print("\nData after Label Encoding:")
print(df.head())

# Save the cleaned data (optional)
df.to_csv("cleaned_data.csv", index=False)
print("\nCleaned data saved to 'cleaned_data.csv'")
