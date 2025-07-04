# Description:- Perform data Cleaning and (EDA) on a dataset, Titanic_Dataset from Kaggle. Explore the relationships between variables and identify patterns and trends in the data.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
# LOAD THE DATASET
df = pd.read_csv("Titanic_Dataset.csv") 
df  ## Display the DataFrame
df.describe()
df.head()
print(df.info())
print(df.columns)
# DATA CLEANING
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
# EDA
import warnings

# Suppress FutureWarnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# Survival vs. sex
# This is  Seaborn code 
sns.set(style="whitegrid")
plt.figure(figsize=(8, 4))
sns.countplot(x="Survived", hue="Sex", data=df)
plt.title("Survival by Sex")
plt.show()
# Survival vs. passenger class
plt.figure(figsize=(8, 4))
sns.countplot(x="Survived", hue="Pclass", data=df)
plt.title("Survival by Passenger Class")
plt.show()
# Survival vs. age
plt.figure(figsize=(8, 4))
sns.histplot(data=df, x='Age', kde=True, hue='Survived', common_norm=False)
plt.title("Survival by Age")
plt.show()
# Survival vs. fare
plt.figure(figsize=(8, 4))
sns.histplot(data=df, x='Fare', kde=True, hue='Survived', common_norm=False)
plt.title("Survival by Fare")
plt.show()
# One-hot encode the 'Embarked' column
df = pd.get_dummies(df, columns=['Embarked'], drop_first=True)

# Now, run the correlation matrix
plt.figure(figsize=(10, 6))
correlation_matrix = df[['Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked_Q', 'Embarked_S']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()
# Explore the distribution of passengers' ages
plt.figure(figsize=(8, 4))
sns.histplot(data=df, x='Age', kde=True, bins=20)
plt.title("Age Distribution")
plt.show()
# Explore the distribution of passengers' fares
plt.figure(figsize=(8, 4))
sns.histplot(data=df, x='Fare', kde=True, bins=20)
plt.title("Fare Distribution")
plt.show()
