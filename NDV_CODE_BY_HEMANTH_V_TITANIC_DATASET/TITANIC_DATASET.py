# Upload and extract zip file
from google.colab import files
import zipfile
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Upload zip file
uploaded = files.upload()

# Extract the zip file
with zipfile.ZipFile("titanic_dataset.zip", 'r') as zip_ref:
    zip_ref.extractall()

# Check extracted file name(s)
extracted_files = os.listdir()
print("Extracted files:", extracted_files)

# Automatically find the CSV file
csv_file = [file for file in extracted_files if file.endswith(".csv")][0]

# Load dataset
df = pd.read_csv(csv_file)

# Basic Info
print(df.info())
print(df.describe(include='all'))
print("\nMissing Values:\n", df.isnull().sum())

# Handling missing values
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# Categorical distributions
print("\nSex value counts:\n", df['Sex'].value_counts())
print("\nPclass value counts:\n", df['Pclass'].value_counts())

# Survival Analysis
sns.countplot(x='Survived', data=df)
plt.title('Survival Counts')
plt.show()

# Survival by Gender
sns.barplot(x='Sex', y='Survived', data=df)
plt.title('Survival Rate by Gender')
plt.show()

# Age Distribution
sns.histplot(df['Age'], bins=30, kde=True)
plt.title('Age Distribution')
plt.show()

# Pclass vs Survival
sns.barplot(x='Pclass', y='Survived', data=df)
plt.title('Survival Rate by Class')
plt.show()

# Correlation Heatmap
plt.figure(figsize=(8, 6))
numeric_df = df.select_dtypes(include=np.number)
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# Feature Engineering - Family Size
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
print("\nFamily Size Preview:\n", df[['SibSp', 'Parch', 'FamilySize']].head())
