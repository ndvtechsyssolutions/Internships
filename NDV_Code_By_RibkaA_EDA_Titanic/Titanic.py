# Importing necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Set display style
sns.set(style='whitegrid')
plt.rcParams['figure.figsize'] = (10, 6)

# Load Titanic dataset (from seaborn or local CSV)
df = sns.load_dataset('titanic')

# Preview the dataset
print("First 5 rows of the dataset:")
print(df.head())

# Checking for missing values
print("\nMissing values before cleaning:")
print(df.isnull().sum())

# Handling missing values
df['age'].fillna(df['age'].median(), inplace=True)
df['embarked'].fillna(df['embarked'].mode()[0], inplace=True)
df['embark_town'].fillna(df['embark_town'].mode()[0], inplace=True)
df['deck'].fillna('Unknown', inplace=True)

# Dropping irrelevant columns
df.drop(['alive', 'class', 'who', 'adult_male'], axis=1, inplace=True)

# Removing duplicates
df.drop_duplicates(inplace=True)

# Displaying dataset info
print("\nDataset Info after cleaning:")
print(df.info())

# Summary statistics
print("\nSummary statistics:")
print(df.describe())

# Value counts
print("\nValue Counts:")
print("Sex:\n", df['sex'].value_counts())
print("Survived:\n", df['survived'].value_counts())

# Histogram for Age
sns.histplot(df['age'], kde=True, bins=30)
plt.title("Age Distribution")
plt.show()

# Countplot for Survival
sns.countplot(x='survived', data=df)
plt.title("Survival Count")
plt.show()

# Boxplot of Fare vs Survival
sns.boxplot(x='survived', y='fare', data=df)
plt.title("Fare vs Survival")
plt.show()

# Pairplot
sns.pairplot(df[['age', 'fare', 'survived']], hue='survived')
plt.show()

# Correlation Heatmap
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

# Violin Plot
sns.violinplot(x='sex', y='age', hue='survived', data=df, split=True)
plt.title("Age Distribution by Gender and Survival")
plt.show()

# Grouped Survival Rate
df.groupby(['sex', 'pclass'])['survived'].mean().unstack().plot(kind='bar')
plt.title("Survival Rate by Sex and Passenger Class")
plt.ylabel("Survival Rate")
plt.show()

# Feature Engineering - Family Size
df['FamilySize'] = df['sibsp'] + df['parch'] + 1

# Visualizing Family Size
sns.barplot(x='FamilySize', y='survived', data=df)
plt.title("Survival Rate by Family Size")
plt.show()
