# Loan Dataset Analysis
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

# Load dataset
loan_path = 'loan_data.csv'
loan_df = pd.read_csv(loan_path)

# Handle missing values
loan_df['Gender'].fillna(loan_df['Gender'].mode()[0], inplace=True)
loan_df['Married'].fillna(loan_df['Married'].mode()[0], inplace=True)
loan_df['Dependents'].fillna('0', inplace=True)
loan_df['Self_Employed'].fillna(loan_df['Self_Employed'].mode()[0], inplace=True)
loan_df['Credit_History'].fillna(loan_df['Credit_History'].mode()[0], inplace=True)
loan_df['LoanAmount'].fillna(loan_df['LoanAmount'].median(), inplace=True)
loan_df['Loan_Amount_Term'].fillna(loan_df['Loan_Amount_Term'].mode()[0], inplace=True)

# Display dataset summary
print("Loan Data Summary:\n")
print(loan_df.describe())

# Visualizations

# Loan status count
plt.figure(figsize=(6, 4))
sns.countplot(data=loan_df, x='Loan_Status', palette='pastel')
plt.title("Loan Approval Status")
plt.xlabel("Loan Status")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# Loan status by property area
plt.figure(figsize=(7, 5))
sns.countplot(data=loan_df, x='Property_Area', hue='Loan_Status', palette='Set2')
plt.title("Loan Status by Property Area")
plt.xlabel("Property Area")
plt.ylabel("Count")
plt.legend(title='Loan Approved')
plt.grid(axis='y', linestyle='--', alpha=0.3)
plt.tight_layout()
plt.show()

# Applicant Income Distribution
plt.figure(figsize=(7, 5))
sns.histplot(loan_df['ApplicantIncome'], bins=25, kde=True, color='teal')
plt.title("Distribution of Applicant Income")
plt.xlabel("Applicant Income")
plt.ylabel("Frequency")
plt.grid(axis='y', linestyle='--', linewidth=0.5, alpha=0.7)
plt.tight_layout()
plt.show()

# Credit history vs loan approval
loan_df['Loan_Approved'] = loan_df['Loan_Status'].map({'Y': 1, 'N': 0})
plt.figure(figsize=(6, 4))
sns.barplot(data=loan_df, x='Credit_History', y='Loan_Approved', palette='muted')
plt.title("Credit History vs Loan Approval")
plt.xlabel("Credit History")
plt.ylabel("Approval Probability")
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# Correlation heatmap
plt.figure(figsize=(8, 6))
cols = ['ApplicantIncome','CoapplicantIncome','LoanAmount','Loan_Amount_Term','Credit_History']
corr_matrix = loan_df[cols].corr()
sns.heatmap(corr_matrix, annot=True, cmap='YlGnBu', fmt=".2f", linewidths=0.5)
plt.title("Correlation Matrix")
plt.tight_layout()
plt.show()
