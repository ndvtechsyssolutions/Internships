import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('Titanic-Dataset.csv')

# Show dataset info
print("Dataset Information:")
print(df.info())

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Check for missing values
print("\nMissing Values Count:")
print(df.isnull().sum())

# Fill missing values
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# Display counts
print("\nGender Count:\n", df['Sex'].value_counts())
print("\nPassenger Class Count:\n", df['Pclass'].value_counts())

# Plot 1: Survival Counts
plt.figure(figsize=(5, 4))
sns.countplot(x='Survived', data=df)
plt.title('Survival Counts')
plt.xlabel('Survived (0 = No, 1 = Yes)')
plt.ylabel('Number of Passengers')
plt.tight_layout()
plt.show()

# Plot 2: Survival Rate by Gender
plt.figure(figsize=(5, 4))
sns.barplot(x='Sex', y='Survived', data=df)
plt.title('Survival Rate by Gender')
plt.xlabel('Gender')
plt.ylabel('Survival Rate')
plt.tight_layout()
plt.show()

# Plot 3: Subplots for Age, Age vs Sex, Survival Count
plt.figure(figsize=(16, 4))

plt.subplot(1, 3, 1)
sns.histplot(df['Age'], bins=30, kde=True)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')

plt.subplot(1, 3, 2)
sns.boxplot(x='Sex', y='Age', data=df)
plt.title('Age by Sex')
plt.xlabel('Sex')
plt.ylabel('Age')

plt.subplot(1, 3, 3)
sns.countplot(x='Survived', data=df)
plt.title('Survival Count')
plt.xlabel('Survived')
plt.ylabel('Count')

plt.tight_layout()
plt.show()

# Plot 4: Survival Rate by Passenger Class
plt.figure(figsize=(5, 4))
sns.barplot(x='Pclass', y='Survived', data=df)
plt.title('Survival Rate by Passenger Class')
plt.xlabel('Pclass')
plt.ylabel('Survival Rate')
plt.tight_layout()
plt.show()

# Plot 5: Correlation Heatmap
plt.figure(figsize=(8, 6))
numeric_df = df.select_dtypes(include=np.number)
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.tight_layout()
plt.show()

# Feature Engineering: Family Size
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
print("\nFamily Size Feature (first 5 rows):")
print(df[['SibSp', 'Parch', 'FamilySize']].head())

# Plot 6: Survival Rate vs Family Size
plt.figure(figsize=(6, 4))
sns.barplot(x='FamilySize', y='Survived', data=df)
plt.title('Survival Rate vs Family Size')
plt.xlabel('Family Size')
plt.ylabel('Survival Rate')
plt.tight_layout()
plt.show()
