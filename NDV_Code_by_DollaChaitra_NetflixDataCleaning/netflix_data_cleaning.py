

# 1. Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("netflix_titles.csv")

# 3. Initial Data Inspection
print(" Initial Data Info:")
print(df.info())
print("\nMissing Values:\n", df.isnull().sum())
print("\nDuplicate Records:", df.duplicated().sum())

# 4. Handling Missing Values
df['director'].fillna('Unknown', inplace=True)
df['cast'].fillna('Not Provided', inplace=True)
df['country'].fillna(df['country'].mode()[0], inplace=True)
df['date_added'].fillna(method='ffill', inplace=True)
df['rating'].fillna(df['rating'].mode()[0], inplace=True)
df['duration'].fillna('Unknown', inplace=True)

# 5. Remove Duplicate Records
df.drop_duplicates(inplace=True)

# 6. Correct Data Types
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# 7. Use NumPy for Transformation
df['release_year_log'] = np.log1p(df['release_year'])

# 8. Filter, Sort, Group Examples
movies = df[df['type'] == 'Movie']
tv_shows = df[df['type'] == 'TV Show']

print("\nTop 5 Movies:")
print(movies[['title', 'release_year']].head())

# 9. Summary Statistics
print("\n Summary Statistics:")
print(df.describe())

# 10. Optional: Null Heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), cbar=False, cmap='Reds')
plt.title("Missing Value Heatmap")
plt.show()

# 11. Optional: Correlation Matrix
plt.figure(figsize=(8, 6))
corr = df.select_dtypes(include=[np.number]).corr()
sns.heatmap(corr, annot=True, cmap='Blues', linewidths=0.5)
plt.title("Correlation Matrix")
plt.show()

# 12. Label Encoding (Optional)
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df['type_encoded'] = le.fit_transform(df['type'])

print("\n Data cleaning and preprocessing complete.")
