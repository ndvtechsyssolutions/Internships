import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import chi2_contingency

df = pd.read_csv("Finance_data assignment.csv")
df.head()

df.info()

df.isna().sum()
df.duplicated()

## Hypothesis 1: Is the average age more than 30?

# Null Hypothesis : μ = 30
# Alternative Hypothesis : μ > 30


stati, p_value = stats.ttest_1samp(df['age'], 30)
print("t-statistic:", round(stati, 2))
print("p-value:", round(p_value / 2, 4))  # One-tailed test

if (p_value / 2 < 0.05) and (stati > 0):
    print("Result : Reject Null hypothesis → Average age is more than 30")
else:
    print("Result : Fail to reject Null hypothesis → Not enough evidence that age is more than 30")
    

stati, p_value = stats.ttest_1samp(df['age'], 25)
print("t-statistic:", round(stati, 2))
print("p-value:", round(p_value / 2, 4))  # One-tailed test

if (p_value / 2 < 0.05) and (stati > 0):
    print("Result : Reject Null hypothesis → Average age is more than 25")
else:
    print("Result : Fail to reject Null hypothesis → Not enough evidence that age is more than 25")

## Hypothesis 2: Do males and females differ in Mutual Fund investment?

# H₀: μ_male = μ_female
# H₁: μ_male ≠ μ_female


male = df[df['gender'] == 'Male']['Mutual_Funds']
female = df[df['gender'] == 'Female']['Mutual_Funds']

stati2, p_value2 = stats.ttest_ind(male, female)
print("t-statistic:", round(stati2, 2))
print("p-value:", round(p_value2, 4))

if p_value2 < 0.05:
    print("Result: Reject Null hypothesis → There is a difference in Mutual Fund investments.")
else:
    print("Result: Fail to reject Null hypothesis → No significant difference found.")


## Chi-square Test: Relationship between Gender and Investment_Avenues


contingency = pd.crosstab(df['gender'], df['Investment_Avenues'])
chi2, p, dof, ex = chi2_contingency(contingency)
print("Chi-square statistic:", round(chi2, 2))
print("p-value:", round(p, 4))

if p < 0.05:
    print("Result: Reject Null hypothesis→ Gender and Investment_Avenues are related.")
else:
    print("Result: Fail to reject Null hypothesis → No relationship found.")


## Visualization

# Histogram of Age
plt.figure(figsize=(6,4))
sns.histplot(df['age'], bins=10, kde=True, color = "purple")
plt.title("Age Distribution")
plt.show()


# Boxplot of Mutual Funds by Gender
plt.figure(figsize=(6,4))
sns.boxplot(data=df, x='gender', y='Mutual_Funds', color ="green")
plt.title("Mutual Fund Investment by Gender")
plt.show()

## CONCLUSIONS

# There is Not enough evidence that proving age is more than 30.
# The average age of respondents is significantly greater than 25.
# There is no strong difference in Mutual Fund investment between males and females.
# Gender and choice of investment avenue are related.
# Visualizations confirm distributions and support statistical insights.


# Correlation Analysis, Heatmap & Pivot Tables

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Correlation Analysis
numeric_cols = df.select_dtypes(include=['int64', 'float64'])
correlation_matrix = numeric_cols.corr()

# Heatmap to visualize correlation
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="YlGnBu", fmt=".2f", linewidths=0.5)
plt.title("Correlation Heatmap of Financial Features")
plt.show()

# Pivot Table 1: Average Mutual Fund investment by Gender
pivot1 = df.pivot_table(values='Mutual_Funds', index='gender', aggfunc='mean')
print("Average Mutual Fund Investment by Gender:\n", pivot1, "\n")

# Pivot Table 2: Average Fixed Deposits and Equity Market investment by Investment_Avenues
pivot2 = df.pivot_table(values=['Fixed_Deposits', 'Equity_Market'], index='Investment_Avenues', aggfunc='mean')
print("Average Fixed Deposits & Equity Market by Investment_Avenues:\n", pivot2, )


## Interpretation
# - High positive correlation indicating related investment preferences (e.g: Equity & Gold).
# - Females prefer safer options (e.g: Fixed Deposits), males prefer higher-risk (Equity).
# - People who invest in different avenues tend to show different averages in financial products.
