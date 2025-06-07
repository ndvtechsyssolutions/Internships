#Titanic EDA
from google.colab import drive
drive.mount("/content/drive")

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('/content/drive/MyDrive/Data/Titanic.csv')

#Basic Info
print(df.info())
print(df.describe())
print(df.isnull().sum())

#Handling missing values
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

#Categorical distribution
print(df['Sex'].value_counts())
print(df['Pclass'].value_counts())
#Survival Analysis
sns.countplot(x='Survived', data=df)
plt.title('Survival Counts')
plt.show()

#Survival by Gender
sns.barplot(x='Sex', y='Survived', data=df)
plt.title('Survival Rate by Gender')
plt.show()

#Age Distribution
sns.histplot(df['Age'], bins=30, kde=True)
plt.title('Age Distribution')
plt.show()

#Pclass vs Survival
sns.barplot(x='Pclass', y='Survived', data=df)
plt.title('Survival Rate by Class')
plt.show()

#Correlation Heatmap
plt.figure(figsize=(8,6))
# Select only numerical columns for correlation calculation
numeric_df = df.select_dtypes(include=np.number)
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()
#Feature Engineering Example: FamilySize
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
print(df[['SibSp', 'Parch', 'FamilySize']].head())
