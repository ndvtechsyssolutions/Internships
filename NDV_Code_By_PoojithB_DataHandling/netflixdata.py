# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Netflix data
data = pd.read_csv("netflix_titles.csv")

# Show basic statistics
print(data.describe())

# Fill missing values with defaults
data.fillna({
    'director': 'Unknown',
    'country': 'Unknown',
    'date_added': 'Not Specified',
    'cast': 'Unknown',
    'release_year': 'Unknown',
    'duration': 'Unknown',
    'rating': 'Unknown'
}, inplace=True)

# Convert date to proper format
data['date_added'] = pd.to_datetime(data['date_added'], errors='coerce')

# Add columns for year, month, day name
data['year_added'] = data['date_added'].dt.year
data['month_added'] = data['date_added'].dt.month
data['week_added'] = data['date_added'].dt.day_name()

# Split genre list into multiple items
data['listed_in'] = data['listed_in'].apply(lambda x: [i.strip() for i in x.split(',')])

# Check if content has multiple genres
data['multi_genre'] = data['listed_in'].apply(lambda x: len(x) > 1)

# Standardize country name
data['country'] = data['country'].replace({'United States of America': 'United States'})

# Filter realistic release years
data = data[(data['release_year'] >= 1920) & (data['release_year'] <= 2025)]

# Display first few records
print(data.head(10))

print("\n","-"*30)
print("     VISUALIZATIONS \n")

# Scatter plot for type vs release year
plt.scatter(x='type', y='release_year', data=data)
plt.xlabel('Type')
plt.ylabel('Release Year')
plt.title('Content Release Timeline')
plt.show()

# Count of movies vs TV shows
sns.countplot(data=data, x='type')
plt.xlabel("Type")
plt.ylabel("Count")
plt.title("Movies vs TV Shows")
plt.show()

# Top 10 countries with most content
top_countries = data['country'].value_counts().head(10)
sns.barplot(x=top_countries.values, y=top_countries.index)
plt.title("Top Countries on Netflix")
plt.xlabel("Number of Titles")
plt.ylabel("Country")
plt.show()

# Line plot for titles added over years
yearly_counts = data['year_added'].value_counts().sort_index()
sns.lineplot(x=yearly_counts.index, y=yearly_counts.values)
plt.xlabel("Year")
plt.ylabel("Titles Added")
plt.title("Growth of Netflix Content Over Time")
plt.show()
