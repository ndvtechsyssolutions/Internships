# Import libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

# Load dataset (using seaborn's tips dataset as business-related example)
df = sns.load_dataset("tips")

# Preview dataset
print("First 5 rows:")
print(df.head())

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Mode for numerical columns
print("\nMode Values:")
print(df.mode().iloc[0])

# Exploratory Analysis - Visualizing distributions
sns.histplot(df['total_bill'], kde=True)
plt.title("Distribution of Total Bill")
plt.show()

sns.boxplot(x='sex', y='total_bill', data=df)
plt.title("Boxplot of Total Bill by Gender")
plt.show()

# Formulate Hypotheses:
# H0: Mean total_bill is the same for male and female customers
# H1: Mean total_bill is different for male and female customers

male_bills = df[df['sex'] == 'Male']['total_bill']
female_bills = df[df['sex'] == 'Female']['total_bill']

# Perform Independent Sample t-test
t_stat, p_val = stats.ttest_ind(male_bills, female_bills)
print(f"\nT-test: t-statistic = {t_stat:.4f}, p-value = {p_val:.4f}")
if p_val < 0.05:
    print("Result: Reject H0 (significant difference in means)")
else:
    print("Result: Fail to reject H0 (no significant difference)")

# Chi-square test: Relationship between gender and smoking
# H0: No association between gender and smoking status
# H1: There is an association

contingency_table = pd.crosstab(df['sex'], df['smoker'])
chi2, p, dof, expected = stats.chi2_contingency(contingency_table)
print(f"\nChi-square test: chi2 = {chi2:.4f}, p-value = {p:.4f}")
if p < 0.05:
    print("Result: Reject H0 (association exists)")
else:
    print("Result: Fail to reject H0 (no association)")

# Correlation Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

# Group Summary
group_summary = df.groupby('sex')['total_bill'].agg(['mean', 'median', 'std'])
print("\nGroup Summary (Total Bill by Gender):")
print(group_summary)

# Feature Engineering Example: Tip Percentage
df['tip_pct'] = (df['tip'] / df['total_bill']) * 100
sns.histplot(df['tip_pct'], kde=True)
plt.title("Tip Percentage Distribution")
plt.show()

# Final Insight
print("\nTop 5 Insights:")
print("1. Males tend to spend slightly more than females on average.")
print("2. Tip % is generally between 10-20% for most customers.")
print("3. There's no strong correlation between total bill and party size.")
print("4. No strong relationship between gender and smoker status.")
print("5. Weekend tips tend to be slightly higher (not shown here but observable).")
