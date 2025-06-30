# 🚢 Titanic EDA (Final Version with Subplots and Enhancements)

# 0️⃣ Mount Google Drive
from google.colab import drive
drive.mount("/content/drive")

# 📦 Import Required Libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 📂 Load the Titanic Dataset
df = pd.read_csv('/content/drive/MyDrive/Data/Titanic.csv')

# 1️⃣ Basic Data Overview
print("🔎 Dataset Information:")
print(df.info())
print("\n📊 Summary Statistics:")
print(df.describe())
print("\n❗ Missing Values Count:")
print(df.isnull().sum())

# 2️⃣ Data Cleaning - Handle Missing Values
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# 3️⃣ Categorical Distribution Counts
print("\n📌 Gender Count:\n", df['Sex'].value_counts())
print("\n📌 Passenger Class Count:\n", df['Pclass'].value_counts())

# 4️⃣ Survival Count Plot
plt.figure(figsize=(5, 4))
sns.countplot(x='Survived', data=df)
plt.title('Survival Counts')
plt.xlabel('Survived (0 = No, 1 = Yes)')
plt.ylabel('Number of Passengers')
plt.tight_layout()
plt.show()

# 5️⃣ Survival by Gender
plt.figure(figsize=(5, 4))
sns.barplot(x='Sex', y='Survived', data=df)
plt.title('Survival Rate by Gender')
plt.xlabel('Gender')
plt.ylabel('Survival Rate')
plt.tight_layout()
plt.show()

# 6️⃣ Distribution Subplots
plt.figure(figsize=(16, 4))

# Subplot 1: Age Histogram
plt.subplot(1, 3, 1)
sns.histplot(df['Age'], bins=30, kde=True)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')

# Subplot 2: Age by Sex
plt.subplot(1, 3, 2)
sns.boxplot(x='Sex', y='Age', data=df)
plt.title('Age by Sex')
plt.xlabel('Sex')
plt.ylabel('Age')

# Subplot 3: Survival Count
plt.subplot(1, 3, 3)
sns.countplot(x='Survived', data=df)
plt.title('Survival Count')
plt.xlabel('Survived')
plt.ylabel('Count')

plt.tight_layout()
plt.show()

# 7️⃣ Pclass vs Survival
plt.figure(figsize=(5, 4))
sns.barplot(x='Pclass', y='Survived', data=df)
plt.title('Survival Rate by Passenger Class')
plt.xlabel('Pclass')
plt.ylabel('Survival Rate')
plt.tight_layout()
plt.show()

# 8️⃣ Correlation Heatmap (Numeric Columns Only)
plt.figure(figsize=(8, 6))
numeric_df = df.select_dtypes(include=np.number)
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.tight_layout()
plt.show()

# 9️⃣ Feature Engineering - Family Size
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
print("\n👪 Family Size Feature (first 5 rows):")
print(df[['SibSp', 'Parch', 'FamilySize']].head())

# 🔟 Bonus: Survival vs Family Size Plot
plt.figure(figsize=(6, 4))
sns.barplot(x='FamilySize', y='Survived', data=df)
plt.title('Survival Rate vs Family Size')
plt.xlabel('Family Size')
plt.ylabel('Survival Rate')
plt.tight_layout()
plt.show()
