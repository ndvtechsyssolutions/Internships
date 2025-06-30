# Titanic_EDA.py

import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create images folder if it doesn't exist
os.makedirs("images", exist_ok=True)

# Set style for seaborn
sns.set(style="darkgrid", font_scale=1.1)

# Load dataset
df = pd.read_csv('train.csv')

# Basic info
print("Shape of dataset:", df.shape)
print("\nData Types & Nulls:\n")
print(df.info())

# Summary statistics
print("\nSummary Statistics:\n", df.describe())

# Check missing values
print("\nMissing Values:\n", df.isnull().sum())

# Drop 'Cabin' column (too many nulls)
df.drop('Cabin', axis=1, inplace=True)

# Fill missing values
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# Drop duplicates if any
df.drop_duplicates(inplace=True)

# Confirm cleaning
print("\nMissing Values After Cleaning:\n", df.isnull().sum())

# --------------------
# 📊 Visualizations
# --------------------

# 1. Survival Count
sns.countplot(data=df, x='Survived')
plt.title('Survival Count')
plt.savefig("images/survival_count.png")
plt.clf()

# 2. Age Histogram
df['Age'].hist(bins=30)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.savefig("images/age_distribution.png")
plt.clf()

# 3. Boxplot of Fare
sns.boxplot(x='Fare', data=df)
plt.title('Fare Boxplot')
plt.savefig("images/fare_boxplot.png")
plt.clf()

# 4. Survival by Gender
sns.countplot(data=df, x='Sex', hue='Survived')
plt.title('Survival by Gender')
plt.savefig("images/survival_by_gender.png")
plt.clf()

# 5. Survival by Class
sns.countplot(data=df, x='Pclass', hue='Survived')
plt.title('Survival by Class')
plt.savefig("images/survival_by_class.png")
plt.clf()

# 6. Correlation Heatmap (only numeric columns)
numeric_df = df.select_dtypes(include=['number'])
plt.figure(figsize=(10, 6))
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.savefig("images/correlation_heatmap.png")
plt.clf()

# 7. Feature Engineering - Family Size
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
sns.violinplot(x='Survived', y='FamilySize', data=df)
plt.title('Survival vs Family Size')
plt.savefig("images/survival_vs_familysize.png")
plt.clf()

print("\n🎯 EDA Complete! All plots are saved in the 'images/' folder.\n")
