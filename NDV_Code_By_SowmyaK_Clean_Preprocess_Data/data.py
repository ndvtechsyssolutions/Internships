from google.colab import drive
drive.mount('/content/drive')
drive.mount("/content/drive", force_remount=True)
import zipfile
import os

# Set the correct path to the ZIP file in your Google Drive
zip_path = '/content/drive/MyDrive/kaggle dataset/archive.zip'

# Extract the contents of the ZIP file to a folder in Colab
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall('/content/data')

# List files inside the extracted folder
os.listdir('/content/data')
#Loaad the dataset
import pandas as pd
import numpy as np

# Load Netflix data
df = pd.read_csv('/content/data/netflix_titles.csv')
df.head()
#Inspect the data
# Shape and structure
print("Shape:", df.shape)
print("Columns:\n", df.columns)
print("\nInfo:")
df.info()

# Check for missing values
print("\nMissing values:\n", df.isnull().sum())

# Check for duplicates
print("\nDuplicates:", df.duplicated().sum())
#Data cleaning
#  Remove duplicate rows
before = df.shape[0]
df.drop_duplicates(inplace=True)
after = df.shape[0]
print(f" Removed {before - after} duplicate rows.")

#  Fill missing values (forward fill)
df.ffill(inplace=True)
print(" Applied forward fill to missing values.")

#  Fill remaining missing values (backward fill)
df.bfill(inplace=True)
print("Applied backward fill to remaining missing values.")

#  Check if any missing values remain
print("\n Final missing values per column:\n")
print(df.isnull().sum())
# Check if 'date_added' column exists before converting
if 'date_added' in df.columns:
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
    print(" Converted 'date_added' to datetime format.")
else:
    print(" Column 'date_added' not found.")
  #Numpy transformations
# Create a NumPy array to classify duration length (short/long show)
import numpy as np

if 'duration_num' in df.columns:
    # Fill any missing values in duration_num just in case
    df['duration_num'].fillna(0, inplace=True)

    # Use NumPy to classify long/short
    df['is_long'] = np.where(df['duration_num'] >= 60, 'Yes', 'No')
    print("'is_long' column created using NumPy.")
else:
    print(" 'duration_num' column not found")
# Describe numerical columns
print(df.describe())

# Value counts
print(df['type'].value_counts())
#Heatmap
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
sns.heatmap(df.isnull(), cbar=False, cmap="YlOrRd")
plt.title('Missing Values Heatmap')
plt.show()
#label encoding
from sklearn.preprocessing import LabelEncoder


le = LabelEncoder()


df['type_encoded'] = le.fit_transform(df['type'])


print(df[['type', 'type_encoded']].drop_duplicates())
#corelation matrix
plt.figure(figsize=(6,4))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()


