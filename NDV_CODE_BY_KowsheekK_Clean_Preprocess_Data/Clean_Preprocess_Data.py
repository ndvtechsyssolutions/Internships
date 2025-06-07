import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("netflix_titles.csv")

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Handle missing values
df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Not Available')
df['country'] = df['country'].fillna('Unknown')
df['rating'] = df['rating'].fillna(df['rating'].mode()[0])
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['duration'] = df['duration'].fillna('Unknown')

# Remove duplicates
df.drop_duplicates(inplace=True)

# Basic analysis
print("Total Movies:", len(df[df['type'] == 'Movie']))
print("Total TV Shows:", len(df[df['type'] == 'TV Show']))

# Group by country
top_countries = df['country'].value_counts().head(10)
print("Top 10 Countries:\n", top_countries)

# Optional: heatmap of missing values
sns.heatmap(df.isnull(), cbar=False, cmap='magma')
plt.title("Missing Values Heatmap")
plt.show()

# Print cleaned data sample
print("\nCleaned Data Preview:")
print(df.head())

# Save cleaned dataset
df.to_csv("netflix_cleaned.csv", index=False)
print("Cleaned data saved as netflix_cleaned.csv")
