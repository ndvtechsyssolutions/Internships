# Description:- Use Pandas and NumPy libraries in Python to clean and preprocess a real-world dataset such as Netflix .

# Import Required Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("Libraries imported.")

# Load the Dataset
try:
    df = pd.read_csv('netflix_titles.csv')
    print("CSV file loaded successfully.")
    print(f"Type of df after loading: {type(df)}") # Check the type
except FileNotFoundError:
    print("Error: 'netflix_titles.csv' not found. Please check the file path.")
    df = None # Explicitly set df to None if file not found
except Exception as e:
    print(f"An error occurred while loading the CSV: {e}")
    df = None # Explicitly set df to None if any other error occurs

# Now, proceed with inspecting the dataset ONLY if df is not None
if df is not None:
    # Inspect the Dataset
    print("\nInspecting the dataset:")
    # Display the first few rows
    print("\nFirst 5 rows:")
    display(df.head()) # Using display from IPython.display for better output

    # Get dataset shape
    print("\nDataset shape:")
    print(df.shape)

    # Get data types and non-null counts
    print("\nDataset info:")
    df.info()

    # Check for missing values
    print("\nMissing values count:")
    print(df.isnull().sum())

    # Check for duplicate rows
    print("\nDuplicate rows count:")
    print(df.duplicated().sum())
else:
    print("\nCannot inspect dataset because df was not loaded successfully.")
  # Handle Missing Values
# Drop rows where 'director' or 'cast' is missing
df.dropna(subset=['director', 'cast'], inplace=True)

# Fill missing 'rating' with 'TV-MA'
df['rating'].fillna('TV-MA', inplace=True)

# Fill missing 'date_added' with 'Unknown'
df['date_added'].fillna('Unknown', inplace=True)
# Remove Duplicate Records
df.drop_duplicates(inplace=True)
# Convert Data Types
# Convert 'release_year' to integer
df['release_year'] = df['release_year'].astype(int)

# Convert 'date_added' to datetime
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
#  Feature Engineering
# Extract year and month from 'date_added'
df['added_year'] = df['date_added'].dt.year
df['added_month'] = df['date_added'].dt.month

# Extract duration in minutes
df['duration_minutes'] = df['duration'].apply(lambda x: int(x.split()[0]) if isinstance(x, str) and x.split()[0].isdigit() else np.nan)

# Create a 'Category' column based on 'type'
df['Category'] = df['type'].map({'Movie': 'Movie', 'TV Show': 'TV Show'})
# Data Filtering and Grouping
# Filter movies released after 2015
recent_movies = df[(df['Category'] == 'Movie') & (df['release_year'] > 2015)]

# Group by 'release_year' and count occurrences
release_counts = df.groupby('release_year').size()

# Group by 'rating' and count occurrences
rating_counts = df.groupby('rating').size()
# Data Visualization
plt.figure(figsize=(6, 4))
sns.countplot(x='type', data=df, palette='Set2')
plt.title('Distribution of Content Types on Netflix')
plt.xlabel('Type')
plt.ylabel('Count')
plt.show()
top_countries = df['country'].value_counts().head(10)

plt.figure(figsize=(10, 5))
sns.barplot(x=top_countries.index, y=top_countries.values, palette='viridis')
plt.title('Top 10 Countries with Most Netflix Content')
plt.ylabel('Number of Titles')
plt.xticks(rotation=45)
plt.show()
# Ensure 'year_added' column exists and is numeric (you created 'added_year' in your notebook)
# Let's use 'added_year' which you created.
plt.figure(figsize=(10, 5))
df['added_year'].value_counts().sort_index().plot(kind='line', marker='o')
plt.title('Number of Titles Added by Year')
plt.xlabel('Year Added')
plt.ylabel('Number of Titles')
plt.grid(True)
plt.show()
plt.figure(figsize=(10, 5))
sns.countplot(y='rating', data=df, order=df['rating'].value_counts().index, palette='coolwarm')
plt.title('Distribution of Ratings')
plt.xlabel('Count')
plt.ylabel('Rating')
plt.show()
# Ensure you handle potential 'Not Specified' or missing values in 'director'
top_directors = df[df['director'].fillna('Not Specified') != 'Not Specified']['director'].value_counts().head(10)

plt.figure(figsize=(10, 5))
sns.barplot(x=top_directors.values, y=top_directors.index, palette='magma')
plt.title('Top 10 Directors with Most Titles on Netflix')
plt.xlabel('Number of Titles')
plt.ylabel('Director')
plt.show()
# Correlation Matrix (For Numerical Features)
# Check the unique values in the original 'duration' column
print(df['duration'].unique())

# Refine the duration_minutes extraction to handle potential errors
def extract_duration_minutes(duration_str):
    try:
        # Check if it's a string and contains digits
        if isinstance(duration_str, str) and duration_str.split()[0].isdigit():
            return int(duration_str.split()[0])
        else:
            return np.nan # Set to NaN if extraction fails
    except:
        return np.nan # Set to NaN for any other errors

df['duration_minutes'] = df['duration'].apply(extract_duration_minutes)

# Handle NaN values in duration_minutes (choose one approach)
# Option 1: Fill NaN with 0
df['duration_minutes'].fillna(0, inplace=True)

# Option 2: Drop rows with NaN in duration_minutes
# df.dropna(subset=['duration_minutes'], inplace=True)

# Now compute the correlation matrix
corr_matrix = df.corr(numeric_only=True) # Use numeric_only=True to be explicit

# Plot correlation matrix
plt.figure(figsize=(10, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# Label Encoding (For Machine Learning)
from sklearn.preprocessing import LabelEncoder

# Initialize LabelEncoder
le = LabelEncoder()

# Apply label encoding to 'rating' and 'Category'
df['rating_encoded'] = le.fit_transform(df['rating'])
df['Category_encoded'] = le.fit_transform(df['Category'])

# Save the Cleaned Dataset
df.to_csv('cleaned_netflix_titles.csv', index=False)


