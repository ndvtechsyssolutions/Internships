import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/content/drive/MyDrive/Data/titanic.csv')
df.head()
df.describe()
df.info()

df.drop_duplicates(inplace=True)
df['Age'].fillna(df['Age'].median())
df['Embarked'].fillna(df['Embarked'].mode()[0])
df['Cabin'].fillna('Unknown')
df['Pclass'] = df['Pclass'].astype('category')
df['Survived'] = df['Survived'].astype('category')

print(df['Sex'].value_counts())
print(df['Embarked'].value_counts())

plt.figure(figsize=(8,5))
sns.histplot(df['Age'], kde=True)
plt.title('Age Distribution')
plt.show()

plt.figure(figsize=(8,5))
sns.boxplot(x='Pclass',y='Age',data=df)
plt.title('Age by Passenger Class')
plt.show()

plt.figure(figsize=(8,5))
sns.countplot(x='Survived',hue='Sex',data=df)
plt.title('Survived by Gender')
plt.show()

sns.pairplot(df[['Age','Fare','Survived']], hue='Survived')
plt.show()

plt.figure(figsize=(8,5))
sns.heatmap(df.corr(numeric_only=True),annot =True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

df['Survived'] = df['Survived'].astype(int)

print("Survival rate by Sex:\n",df.groupby('Sex')['Survived'].mean())
print("Survival rate by Pclass:\n",df.groupby('Pclass',observed=True)['Survived'].mean())

plt.figure(figsize=(8,5))
sns.violinplot(x='Survived',y='Age',data=df)
plt.title('Age Distribution by Survival Status')
plt.show()

df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
print('Avg Survival by FamilySize:\n',df.groupby('FamilySize')['Survived'].mean())
