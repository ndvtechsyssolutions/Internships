# Netflix Data Cleaning and Preprocessing

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from google.colab import drive
drive.mount("/content/drive")

#Load Data
df=pd.read_csv('/content/drive/MyDrive/Data/netflix_titles.csv')

print("Initial Data Info:")
df.info()

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Drop rows with missing title
df.dropna(subset=['title'], inplace=True)

# Fill missing values
df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Unknown')
df['country'] = df['country'].fillna('Unknown')
df['rating'] = df['rating'].fillna('Not Rated')
df['duration'] = df['duration'].fillna('Unknown')

# Remove duplicates
df.drop_duplicates(inplace=True)

# Convert data types if needed
df['release_year'] = df['release_year'].astype(int)

# NumPy transformations: Title length
df['title_length'] = np.where(df['title'].notnull(), df['title'].str.len(), 0)

# Filtering: Only Movies
df_movies = df[df['type'] == 'Movie']

# Sorting by year
df_movies_sorted = df_movies.sort_values(by='release_year', ascending=False)

# Group by country
country_group = df.groupby('country')['show_id'].count().sort_values(ascending=False)
print("\nTop Countries by Number of Shows:")
print(country_group.head(10))

# Summary statistics
print("\nSummary Statistics:")
print(df.describe(include='all'))

# Visualization: Null value heatmap
plt.figure(figsize=(10,6))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title("Missing Values Heatmap")
plt.show()

# Correlation matrix (only numerical fields)
numeric_df = df.select_dtypes(include=['int64', 'float64'])
plt.figure(figsize=(6,4))
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()

# Label Encoding for 'type' column
le = LabelEncoder()
df['type_encoded'] = le.fit_transform(df['type'])

# Save the cleaned dataset
df.to_csv('netflix_cleaned.csv', index=False)
print("\nCleaned dataset saved as 'netflix_cleaned.csv'")
