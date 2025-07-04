import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('loan_data.csv')


print(df.info())
print(df.describe())
print(df.isnull().sum())


df['Gender'].fillna(df['Gender'].mode()[0], inplace=True)
df['Married'].fillna(df['Married'].mode()[0], inplace=True)
df['Dependents'].fillna('0', inplace=True)
df['Self_Employed'].fillna(df['Self_Employed'].mode()[0], inplace=True)
df['Credit_History'].fillna(df['Credit_History'].mode()[0], inplace=True)
df['LoanAmount'].fillna(df['LoanAmount'].median(), inplace=True)
df['Loan_Amount_Term'].fillna(df['Loan_Amount_Term'].mode()[0], inplace=True)



sns.countplot(x='Loan_Status', data=df)
plt.title('Loan Approval Status')
plt.xlabel('Loan Status')
plt.ylabel('Frequency')
plt.show()


sns.countplot(x='Property_Area', hue='Loan_Status', data=df)
plt.title('Loan Status by Property Area')
plt.xlabel("Property Area")
plt.ylabel("Count")
plt.show()



sns.histplot(df['ApplicantIncome'], bins=30, kde=True)
plt.title('Applicant Income Distribution')
plt.xlabel("Applicant Income")
plt.ylabel("Count")
plt.grid(True)
plt.show()



sns.boxplot(x='Education', y='LoanAmount', data=df)
plt.title('LoanAmount by Education')
plt.tight_layout()
plt.xlabel("Education")
plt.ylabel("Loan Amount")
plt.show()




sns.barplot(x='Credit_History', y=df['Loan_Status'].apply(lambda x: 1 if x == 'Y' else 0), data=df)
plt.title('Credit History vs Loan Approval Rate')
plt.xlabel("Credit History")
plt.ylabel("Loan Status")
plt.show()



plt.figure(figsize=(8,6))
cols = ['ApplicantIncome','CoapplicantIncome','LoanAmount','Loan_Amount_Term','Credit_History']
data = df[cols]
sns.heatmap(data.corr(), annot=True,cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.xticks(rotation=45)
plt.show()
