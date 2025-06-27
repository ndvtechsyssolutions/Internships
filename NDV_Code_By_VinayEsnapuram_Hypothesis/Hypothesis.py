import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("HR_Analytics.csv")

df.info()

df.head()

df.describe()

df.median(numeric_only=True)
df.mode(numeric_only=True).iloc[0]


df.isnull().sum()


from scipy.stats import ttest_ind

df.columns = df.columns.str.strip()

income_male = df[df['Gender'] == 'Male']['MonthlyIncome']
income_female = df[df['Gender'] == 'Female']['MonthlyIncome']

t_stat, p_val = ttest_ind(income_male, income_female, nan_policy='omit')
print(f"t-statistic = {t_stat:.4f}, p-value = {p_val:.4f}")


from scipy.stats import chi2_contingency

contingency = pd.crosstab(df['Attrition'], df['MaritalStatus'])

chi2, p, dof, expected = chi2_contingency(contingency)
print(f"Chi-square = {chi2:.2f}, p-value = {p:.4f}")


import seaborn as sns
sns.boxplot(x='Gender', y='MonthlyIncome', data=df)


df.pivot_table(values='MonthlyIncome', index='JobRole', columns='Gender', aggfunc='mean')
