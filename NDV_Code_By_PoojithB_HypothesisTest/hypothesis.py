import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import ttest_ind, chi2_contingency

# Load dataset
df = pd.read_csv("sales_data.csv")

# Descriptive Statistics
print("Descriptive Statistics:\n")
print(df.describe())

print("\nMissing values:\n", df.isnull().sum())

# Distribution of Gender
sns.countplot(x='Gender', data=df)
plt.title("Gender Distribution")
plt.show()

# Spending Score distribution
sns.histplot(df['Spending_Score'], bins=20, kde=True)
plt.title("Spending Score Distribution")
plt.xlabel("Spending Score")
plt.ylabel("Frequency")
plt.show()

# Boxplot of Spending Score by Gender
sns.boxplot(x='Gender', y='Spending_Score', data=df)
plt.title("Spending Score by Gender")
plt.show()

# Hypothesis Testing

# T-test: Are male and female spending scores significantly different?
male_score = df[df['Gender'] == 'Male']['Spending_Score']
female_score = df[df['Gender'] == 'Female']['Spending_Score']

t_stat, p_value = ttest_ind(male_score, female_score)
print("\nT-test for Spending Score by Gender:")
print(f"t-statistic = {t_stat:.4f}, p-value = {p_value:.4f}")

if p_value < 0.05:
    print(" Statistically significant difference in spending scores between genders.")
else:
    print(" No significant difference in spending scores between genders.")

# Chi-Square Test: Is Product Category associated with Gender?
contingency_table = pd.crosstab(df['Gender'], df['Product_Category'])
chi2, p, dof, expected = chi2_contingency(contingency_table)

print("\nChi-Square Test for Gender vs Product Category:")
print(f"Chi2 = {chi2:.4f}, p-value = {p:.4f}")

if p < 0.05:
    print("Significant association between gender and product category.")
else:
    print("No significant association between gender and product category.")
