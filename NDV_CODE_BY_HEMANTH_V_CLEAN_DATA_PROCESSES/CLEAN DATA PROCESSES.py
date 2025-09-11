# STEP 1: Upload the zip file
from google.colab import files
uploaded = files.upload()  # Select the file 'netflix_titles.csv.zip' here

# STEP 2: Extract the CSV file from the ZIP
import zipfile

with zipfile.ZipFile('netflix_titles.csv.zip', 'r') as zip_ref:
    zip_ref.extractall()  # Extracts to current directory

# STEP 3: Import required libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

# STEP 4: Load dataset
df = pd.read_csv("netflix_titles.csv")

# STEP 5: Inspect data
print("Head:\n", df.head())
print("\nInfo:")
print(df.info())
print("\nDescription:")
print(df.describe(include='all'))

# STEP 6: Check for missing values
print("\nMissing values:\n", df.isnull().sum())

# STEP 7: Visualize missing values
plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), cbar=False, cmap="viridis")
plt.title("Heatmap of Missing Values")
plt.show()

# STEP 8: Handle missing values
df['director'].fillna("Unknown Director", inplace=True)
df['cast'].fillna("Cast Not Provided", inplace=True)
df['country'].fillna(df['country'].mode().dropna().values[0], inplace=True)
df['date_added'].fillna("January 1, 2000", inplace=True)
df['rating'].fillna("Not Rated", inplace=True)
df['duration'].fillna("0", inplace=True)  # Safe default for analysis

# STEP 9: Remove duplicates
df.drop_duplicates(inplace=True)

# STEP 10: Convert data types
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['release_year'] = pd.to_numeric(df['release_year'], errors='coerce')
df.dropna(subset=['release_year'], inplace=True)
df['release_year'] = df['release_year'].astype(int)

# STEP 11: NumPy operation – average release year
years = df['release_year'].values
print("\nAverage release year:", np.mean(years))

# STEP 12: Filter and group
movies = df[df['type'] == 'Movie']
shows = df[df['type'] == 'TV Show']
print("Movies count:", len(movies))
print("TV Shows count:", len(shows))

# STEP 13: Group by country and count titles
country_counts = df['country'].value_counts().head(10)
print("\nTop 10 countries by title count:\n", country_counts)

# STEP 14: Correlation matrix
numeric_df = df.select_dtypes(include=[np.number])
if not numeric_df.empty:
    plt.figure(figsize=(8, 6))
    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
    plt.title("Correlation Matrix")
    plt.show()
else:
    print("\nNo numeric data available for correlation.")

# STEP 15: Label encode 'type'
label_encoder = LabelEncoder()
df['type_encoded'] = label_encoder.fit_transform(df['type'])

# STEP 16: Final summary
print("\nFinal Data Info:")
print(df.info())
print("\nFinal Head:\n", df.head())

