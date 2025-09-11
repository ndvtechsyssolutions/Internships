import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('/content/drive/MyDrive/Data/Titanic.csv')

# Basic Info
print(df.info())
print(df.describe())
print(df.isnull().sum())

# Handling missing values
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

#  Categorical distribution
print(df['Sex'].value_counts())
print(df['Pclass'].value_counts())

#  Survival Analysis
sns.countplot(x='Survived', data=df)
plt.title('Survival Counts')
plt.show()

#  Survival by Gender
sns.barplot(x='Sex', y='Survived', data=df)
plt.title('Survival Rate by Gender')
plt.show()

#  Age Distribution
sns.histplot(df['Age'], bins=30, kde=True)
plt.title('Age Distribution')
plt.show()

#  Pclass vs Survival
sns.barplot(x='Pclass', y='Survived', data=df)
plt.title('Survival Rate by Class')
plt.show()

#  Correlation Heatmap
plt.figure(figsize=(8,6))
# Select only numerical columns for correlation calculation
numeric_df = df.select_dtypes(include=np.number)
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

#  Feature Engineering Example: FamilySize
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
print(df[['SibSp', 'Parch', 'FamilySize']].head())

# loan prediction
# Load dataset
df = pd.read_csv('loan_data.csv')

#  Basic Info
print(df.info())
print(df.describe())
print(df.isnull().sum())

#  Fill Missing Values
df['Gender'].fillna(df['Gender'].mode()[0], inplace=True)
df['Married'].fillna(df['Married'].mode()[0], inplace=True)
df['Dependents'].fillna('0', inplace=True)
df['Self_Employed'].fillna(df['Self_Employed'].mode()[0], inplace=True)
df['Credit_History'].fillna(df['Credit_History'].mode()[0], inplace=True)
df['LoanAmount'].fillna(df['LoanAmount'].median(), inplace=True)
df['Loan_Amount_Term'].fillna(df['Loan_Amount_Term'].mode()[0], inplace=True)

#  Loan Status Count
sns.countplot(x='Loan_Status', data=df)
plt.title('Loan Approval Status')
plt.show()

#  Loan Status by Property Area
sns.countplot(x='Property_Area', hue='Loan_Status', data=df)
plt.title('Loan Status by Property Area')
plt.show()

#  Income Distribution
sns.histplot(df['ApplicantIncome'], bins=30, kde=True)
plt.title('Applicant Income Distribution')
plt.show()

#  Boxplot: Education vs LoanAmount
sns.boxplot(x='Education', y='LoanAmount', data=df)
plt.title('LoanAmount by Education')
plt.show()

#  Credit History Impact
sns.barplot(x='Credit_History', y=df['Loan_Status'].apply(lambda x: 1 if x == 'Y' else 0), data=df)
plt.title('Credit History vs Loan Approval Rate')
plt.show()

#  Correlation Heatmap
plt.figure(figsize=(8,6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

