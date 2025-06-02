import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="darkgrid")
%matplotlib inline

# 📁 Load Dataset
df = pd.read_csv('/content/loan.csv')  # Ensure the file is in your working directory

# 🧾 Basic Info and Stats
print(df.info())
print(df.describe())
print(df.isnull().sum())

# 🧹 Data Cleaning
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
df.drop(columns='Cabin', inplace=True)  # too many missing values
df['Pclass'] = df['Pclass'].astype('category')
df['Survived'] = df['Survived'].astype('category')
df.drop_duplicates(inplace=True)

# 📊 Visualizations

# Age Distribution
sns.histplot(df['Age'], kde=True)
plt.title('Age Distribution')
plt.show()

# Survival Count
sns.countplot(x='Survived', data=df)
plt.title('Survival Count')
plt.show()

# Boxplot: Age by Class
sns.boxplot(x='Pclass', y='Age', data=df)
plt.title('Age by Passenger Class')
plt.show()

# Pairplot
sns.pairplot(df[['Survived', 'Pclass', 'Age', 'Fare']], hue='Survived')
plt.show()

# Heatmap
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# 📚 Groupby Analysis
print("Survival Rate by Gender:\n", df.groupby('Sex')['Survived'].mean())
print("\nSurvival Rate by Pclass:\n", df.groupby('Pclass')['Survived'].mean())

# 🌟 Bonus

# Violin Plot
sns.violinplot(x='Pclass', y='Age', hue='Survived', data=df, split=True)
plt.title('Age and Class Distribution by Survival')
plt.show()

# Feature Engineering: Family Size
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
sns.countplot(x='FamilySize', hue='Survived', data=df)
plt.title('Survival by Family Size')
plt.show()
