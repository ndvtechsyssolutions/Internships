from google.colab import files
uploaded = files.upload()
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv(r'netflix_titles.csv.zip')
print(df.head())
df.head()
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)
# Convert 'date_added' to datetime if it exists
if 'date_added' in df.columns:
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
# Example: Create a new column indicating movie length category
if 'duration' in df.columns:
    df['duration_minutes'] = df['duration'].str.extract('(\d+)').astype(float)
    df['duration_category'] = np.where(df['duration_minutes'] >= 60, 'Long', 'Short')
# Filter for only movies
movies_df = df[df['type'] == 'Movie']
# Sort by release year
df_sorted = df.sort_values(by='release_year', ascending=False)
# Group by country and count
country_counts = df['country'].value_counts()
# Plot count of content types
sns.countplot(data=df, x='type')
plt.title("Distribution of Content Types")
plt.show()
# Top 10 countries by content count
df['country'].value_counts().head(10).plot(kind='bar', title="Top 10 Countries with Most Content")
plt.show()
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title("Missing Values Heatmap")
plt.show()
numerical_df = df.select_dtypes(include=np.number)
sns.heatmap(numerical_df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
for col in df.select_dtypes(include='object').columns:
    df[col] = le.fit_transform(df[col].astype(str))
