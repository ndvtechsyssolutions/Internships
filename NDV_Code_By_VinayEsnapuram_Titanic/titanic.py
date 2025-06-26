import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')


df = pd.read_csv("titanic_cleaned.csv")
df.head()

df.info()
df.describe()
df.isnull().sum()
df.duplicated().sum()

for col in ['Sex', 'Embarked']:
    print(f"\nValue counts for {col}:\n")
    print(df[col].value_counts())


sns.histplot(df['Age'], kde=True)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.show()

sns.boxplot(data=df, x='Fare')
plt.title('Fare Boxplot')
plt.show()

sns.countplot(data=df, x='Survived')
plt.title('Survival Count')
plt.show()

sns.countplot(data=df, x='Sex', hue='Survived')
plt.title('Survival by Sex')
plt.show()

sns.countplot(data=df, x='Pclass', hue='Survived')
plt.title('Survival by Passenger Class')
plt.show()



plt.figure(figsize=(10,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

sns.pairplot(df[['Survived', 'Age', 'Fare']], hue='Survived')


print(df.groupby('Pclass')['Survived'].mean())

print(df.groupby('Embarked')['Survived'].mean())



sns.violinplot(data=df, x='Survived', y='Age', hue='Sex', split=True)
plt.title('Violin Plot: Age vs Survival by Sex')
plt.show()

sns.swarmplot(data=df.sample(200), x='Pclass', y='Fare', hue='Survived')


df['FamilySize'] = df['SibSp'] + df['Parch'] + 1

sns.barplot(data=df, x='FamilySize', y='Survived')
plt.title('Survival by Family Size')
plt.show()
