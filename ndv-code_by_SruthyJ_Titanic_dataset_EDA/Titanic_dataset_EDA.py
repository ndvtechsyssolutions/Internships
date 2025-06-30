# Titanic EDA Assignment
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('titanic')

# Data Cleaning
df.drop_duplicates(inplace=True)

df['age'] = df['age'].fillna(df['age'].median())
df['embarked'] = df['embarked'].fillna(df['embarked'].mode()[0])
df['fare'] = df['fare'].fillna(df['fare'].median())
df['sex'] = df['sex'].astype('category')
df['embarked'] = df['embarked'].astype('category')

print("Info:\n", df.info())
print("\nDescription:\n", df.describe())
print("\nSurvived value counts:\n", df['survived'].value_counts())

# Creating a new column
df['familySize'] = df['sibsp'] + df['parch'] + 1

# Visualization
sns.histplot(df['age'], bins=20, kde=True)
plt.title("Age Distribution")
plt.show()

sns.boxplot(x='survived', y='age', data=df)
plt.title("Survival vs Age")
plt.show()

sns.countplot(x='pclass', hue='survived', data=df)
plt.title("Survival by Class")
plt.show()

sns.pairplot(df[['survived', 'age', 'fare', 'familySize']], hue='survived')
plt.suptitle("Pairplot of Key Features", y=1.02)
plt.show()

plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

print("\nSurvival Rate by Sex:\n", df.groupby('sex')['survived'].mean())
print("\nSurvival Rate by Pclass:\n", df.groupby('pclass')['survived'].mean())

sns.violinplot(x='pclass', y='age', hue='survived', data=df, split=True)
plt.title("Age Distribution by Class and Survival")
plt.show()
