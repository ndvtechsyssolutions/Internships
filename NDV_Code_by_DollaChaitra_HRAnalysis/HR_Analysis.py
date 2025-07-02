# Import Libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

# Load Dataset
df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")

# Basic Info & Summary Stats
print("Dataset Overview")
print(df.info())
print("\nMissing Values:\n", df.isnull().sum())
print("\nDescriptive Statistics:\n", df.describe())

# Central Tendency
print("\nMean Monthly Income:", df["MonthlyIncome"].mean())
print("\nMedian Age:", df["Age"].median())
print("\nMode Job Role:", df["JobRole"].mode()[0])

# Distribution Plot – Monthly Income
plt.figure(figsize=(8, 5))
sns.histplot(df["MonthlyIncome"], kde=True, bins=30, color="skyblue")
plt.title("Distribution of Monthly Income")
plt.xlabel("Monthly Income")
plt.ylabel("Frequency")
plt.show()

# Boxplot – Age vs Attrition
plt.figure(figsize=(8, 5))
sns.boxplot(x="Attrition", y="Age", data=df, palette="Set2")
plt.title("Age Distribution by Attrition")
plt.show()

# Hypothesis Test 1: Attrition vs Monthly Income
# H0: No significant difference | H1: Significant difference
left = df[df["Attrition"] == "Yes"]["MonthlyIncome"]
stayed = df[df["Attrition"] == "No"]["MonthlyIncome"]
t_stat, p_value = stats.ttest_ind(left, stayed)
print("\nT-Test (Monthly Income by Attrition):")
print("T-statistic:", round(t_stat, 3), "| P-value:", round(p_value, 4))
if p_value < 0.05:
    print("Reject Null Hypothesis: Monthly Income varies by Attrition")
else:
    print("Fail to Reject Null Hypothesis")

# Hypothesis Test 2: Job Role vs Attrition (Chi-Square)
contingency = pd.crosstab(df["JobRole"], df["Attrition"])
chi2_stat, p_chi, dof, expected = stats.chi2_contingency(contingency)
print("\nChi-Square Test (Job Role vs Attrition):")
print("Chi2 Statistic:", round(chi2_stat, 3), "| P-value:", round(p_chi, 4))
if p_chi < 0.05:
    print("Reject Null Hypothesis: Job Role affects Attrition")
else:
    print("Fail to Reject Null Hypothesis")

# Correlation Heatmap (Better Visual)
plt.figure(figsize=(20, 16))  # Increase figure size
corr = df.select_dtypes(include=np.number).corr()

sns.heatmap(
    corr,
    annot=True,
    fmt=".2f",  # show 2 decimal places
    cmap="coolwarm",
    linewidths=0.5,  # lines between cells
    cbar_kws={"shrink": 0.6},  # shrink color bar
    annot_kws={"size": 10}  # increase font size
)
plt.title("Correlation Heatmap", fontsize=18)
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()
plt.show()


# 10. Pivot Table – Average Monthly Income by Department & Attrition
pivot = df.pivot_table(values='MonthlyIncome', index='Department', columns='Attrition', aggfunc='mean')
print("\nAverage Monthly Income by Department & Attrition:\n", pivot)
