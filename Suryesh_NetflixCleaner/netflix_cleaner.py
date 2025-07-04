# netflix_cleaner.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
import warnings
warnings.filterwarnings("ignore")

# Phase 1: Load and Inspect the Dataset

# Load the Netflix dataset
df = pd.read_csv('Suryesh_NetflixCleaner/data/netflix_titles.csv')

# Display first 5 records
print("First 5 entries:")
print(df.head(), end="\n\n")

# Dataset info
print("Dataset Info:")
print(df.info(), end="\n\n")

# Shape of dataset (rows x columns)
print(f"Dataset shape: {df.shape}\n")

# Check for missing values per column
print("Missing values per column:")
print(df.isnull().sum(), end="\n\n")

# Check for duplicate entries
print(f"Number of duplicate rows: {df.duplicated().sum()}\n")

# Check data types of each column
print("Column data types:")
print(df.dtypes, end="\n\n")


# Phase 2: Data Cleaning and Preprocessing

# Convert 'date_added' to datetime, handle leading spaces and errors
df['date_added'] = pd.to_datetime(df['date_added'].str.strip(), errors='coerce')

# Identify most common values to use for filling missing values
most_common_country = df['country'].mode()[0]
most_common_rating = df['rating'].mode()[0]

# Fill missing 'director' and 'cast' with 'Unknown'
df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Unknown')

# Fill missing 'country' and 'rating' with their most frequent values
df['country'] = df['country'].fillna(most_common_country)
df['rating'] = df['rating'].fillna(most_common_rating)

# Drop rows where 'duration' is missing (only a few rows)
df = df.dropna(subset=['duration'])

# Confirm that all missing values are handled
print("After Cleaning - Remaining Missing Values:")
print(df.isnull().sum())
print(f"\nNew shape after cleaning: {df.shape}")


# Phase 3: Summary Statistics and Grouping

# Display summary statistics for all columns
print("\nSummary Statistics:")
print(df.describe(include='all'), end="\n\n")

# Distribution of content type (Movies vs TV Shows)
print("Content Type Distribution:")
print(df['type'].value_counts(), end="\n\n")

# Top genres (categories listed in 'listed_in')
print("Top Genres:")
print(df['listed_in'].value_counts().head(10), end="\n\n")

# Top 10 countries producing content
print("Top 10 Producing Countries:")
print(df['country'].value_counts().head(10), end="\n\n")

# Titles released per year (top 10 most common years)
print("Titles per Release Year (Top 10):")
print(df['release_year'].value_counts().head(10), end="\n\n")

# Grouping content by type and release year
type_year_group = df.groupby(['type', 'release_year']).size().unstack(fill_value=0)
print("Grouped Data by Type and Release Year (sample):")
print(type_year_group.tail(5), end="\n\n")

# Count of titles by rating
print("Rating Distribution:")
print(df['rating'].value_counts(), end="\n\n")


# Phase 4: Data Visualizations

# Bar chart: Movies vs TV Shows
plt.figure(figsize=(6,4))
sns.countplot(data=df, x='type', palette='Set2')
plt.title("Distribution of Content Type")
plt.xlabel("Type")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# Bar chart: Top 10 countries producing Netflix content
top_countries = df['country'].value_counts().head(10)
plt.figure(figsize=(10,5))
sns.barplot(x=top_countries.index, y=top_countries.values, palette='viridis')
plt.title("Top 10 Producing Countries")
plt.xlabel("Country")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Line plot: Number of titles released over the years
titles_per_year = df['release_year'].value_counts().sort_index()
plt.figure(figsize=(12,6))
plt.plot(titles_per_year.index, titles_per_year.values, marker='o')
plt.title("Titles Released Over the Years")
plt.xlabel("Release Year")
plt.ylabel("Count")
plt.grid(True)
plt.tight_layout()
plt.show()

# Bar chart: Top 10 ratings
plt.figure(figsize=(10,5))
sns.countplot(data=df, x='rating', order=df['rating'].value_counts().index[:10], palette='Set1')
plt.title("Top 10 Ratings Distribution")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Phase 5: Label Encoding for ML Readiness

# Create a copy of the dataframe for ML use
df_ml = df.copy()

# Initialize LabelEncoder
le = LabelEncoder()

# Encode 'type' and 'rating'
df_ml['type_encoded'] = le.fit_transform(df_ml['type'])
df_ml['rating_encoded'] = le.fit_transform(df_ml['rating'])

# Limit country encoding to top 10 countries, group others as 'Other'
top_10_countries = df_ml['country'].value_counts().index[:10]
df_ml['country_cleaned'] = df_ml['country'].apply(lambda x: x if x in top_10_countries else 'Other')
df_ml['country_encoded'] = le.fit_transform(df_ml['country_cleaned'])

# Show sample of encoded values
print("Encoded Columns Sample:")
print(df_ml[['type', 'type_encoded', 'rating', 'rating_encoded', 'country_cleaned', 'country_encoded']].head())
