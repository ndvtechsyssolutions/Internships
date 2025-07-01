
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


titanic = pd.read_csv("titanic.csv")  # Replace with actual path


loan = pd.read_csv("loan.csv")        # Replace with actual path


print("=== TITANIC DATASET INFO ===")
print(titanic.info())
print("\n=== TITANIC DATA DESCRIPTION ===")
print(titanic.describe(include='all'))


print("\nMissing values in Titanic Dataset:")
print(titanic.isnull().sum())

sns.countplot(data=titanic, x='Survived')
plt.title("Survival Count on Titanic")
plt.show()


sns.countplot(data=titanic, x='Survived', hue='Sex')
plt.title("Survival by Gender")
plt.show()


sns.histplot(titanic['Age'].dropna(), kde=True, bins=30)
plt.title("Age Distribution")
plt.show()


print("\n=== LOAN DATASET INFO ===")
print(loan.info())
print("\n=== LOAN DATA DESCRIPTION ===")
print(loan.describe(include='all'))


print("\nMissing values in Loan Dataset:")
print(loan.isnull().sum())


sns.countplot(data=loan, x='Loan_Status')
plt.title("Loan Status Count")
plt.show()


sns.countplot(data=loan, x='Loan_Status', hue='Gender')
plt.title("Loan Status by Gender")
plt.show()

# ApplicantIncome distribution
sns.histplot(loan['ApplicantIncome'], kde=True, bins=30)
plt.title("Applicant Income Distribution")
plt.show()
