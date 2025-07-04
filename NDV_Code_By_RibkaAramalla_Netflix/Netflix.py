import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("/content/netflix.csv")
print(df.head())
print(df.info())
print(df.describe())
print("Missing values:\n", df.isnull().sum())

sns.heatmap(df.isnull(), cbar=False, cmap="viridis")
plt.title("Heatmap of Missing Values")
plt.show()

df['director'].fillna("Unknown", inplace=True)
df['cast'].fillna("Not Available", inplace=True)
df['country'].fillna(df['country'].mode()[0], inplace=True)
df['date_added'].fillna("Unknown", inplace=True)
df['rating'].fillna("Not Rated", inplace=True)
df['duration'].fillna("Unknown", inplace=True)

df.drop_duplicates(inplace=True)
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['release_year'] = df['release_year'].astype(int)

years = df['release_year'].values
print("Average release year:", np.mean(years))

movies = df[df['type'] == 'Movie']
shows = df[df['type'] == 'TV Show']
print("Movies count:", len(movies))
print("TV Shows count:", len(shows))

country_counts = df.groupby('country').size().sort_values(ascending=False).head(10)
print("Top 10 countries by title count:\n", country_counts)

numeric_df = df.select_dtypes(include=[np.number])
correlation_matrix = numeric_df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()

label_encoder = LabelEncoder()
df['type_encoded'] = label_encoder.fit_transform(df['type'])

print(df.info())
print(df.head())
