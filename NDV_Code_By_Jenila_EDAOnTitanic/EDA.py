from google.colab import files
uploaded = files.upload()
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r'Titanic.csv')

# 1️⃣ Basic Info
print(df.info())
print(df.describe())
print(df.isnull().sum())

# 2️⃣ Handling missing values
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# 3️⃣ Categorical distribution
print(df['Sex'].value_counts())
print(df['Pclass'].value_counts())

# 4️⃣ Survival Analysis
sns.countplot(x='Survived', data=df)
plt.title('Survival Counts')
plt.show()

# 5️⃣ Survival by Gender
sns.barplot(x='Sex', y='Survived', data=df)
plt.title('Survival Rate by Gender')
plt.show()

# 6️⃣ Age Distribution
sns.histplot(df['Age'], bins=30, kde=True)
plt.title('Age Distribution')
plt.show()

# 7️⃣ Pclass vs Survival
sns.barplot(x='Pclass', y='Survived', data=df)
plt.title('Survival Rate by Class')
plt.show()

# 8️⃣ Correlation Heatmap
plt.figure(figsize=(8,6))
# Select only numerical columns for correlation calculation
numeric_df = df.select_dtypes(include=np.number)
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# 9️⃣ Feature Engineering Example: FamilySize
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
print(df[['SibSp', 'Parch', 'FamilySize']].head())
