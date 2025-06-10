import pandas as pd
import numpy as np
df = pd.read_csv("data.csv")
print(" Available Columns:")
print(df.columns)
if 'director' in df.columns:
    df['director'].fillna('Unknown', inplace=True)
if 'country' in df.columns:
    df['country'].fillna('Unknown', inplace=True)
if 'date_added' in df.columns:
    df['date_added'].fillna(method='ffill', inplace=True)
if 'rating' in df.columns:
    df['rating'].fillna(df['rating'].mode()[0], inplace=True)
if 'duration' in df.columns:
    df['duration'].fillna('0', inplace=True
df.drop_duplicates(inplace=True)
if 'date_added' in df.columns:
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
if 'release_year' in df.columns:
    df['release_year'] = pd.to_numeric(df['release_year'], errors='coerce')
print("\n🔹 Summary Statistics:")
print(df.describe(include='all'))
if 'release_year' in df.columns:
    df['year_plus_5'] = df['release_year'] + 5
if 'country' in df.columns:
    print("\n🔹 Top 5 countries by number of shows:")
    print(df.groupby('country').size().sort_values(ascending=False).head(5))
import seaborn as sns
import matplotlib.pyplot as plt
sns.heatmap(df.isnull(), cbar=False, cmap='Reds')
plt.title("Missing Values Heatmap")
plt.show()
