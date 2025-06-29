import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import chi2_contingency
df = sns.load_dataset('tips')
print("Data Preview:")
print(df.head())
print("\nDescriptive Statistics:")
print(df.describe())
print("\nMode of numeric columns:")
print(df.mode())
t_stat, p_value = stats.ttest_1samp(df['tip'], 3)
print("\nOne Sample T-Test Results:")
print("t-statistic:", t_stat)
print("p-value:", p_value)
if p_value < 0.05:
    print(" Significant difference (Reject H0)")
else:
    print(" No significant difference (Fail to reject H0)")
smoker_tips = df[df['smoker']=='Yes']['tip']
nonsmoker_tips = df[df['smoker']=='No']['tip']
t_stat2, p_value2 = stats.ttest_ind(smoker_tips, nonsmoker_tips)
print("\nTwo Sample T-Test (Smoker vs Non-Smoker):")
print("t-statistic:", t_stat2)
print("p-value:", p_value2)
contingency = pd.crosstab(df['smoker'], df['sex'])
chi2, p_chi, dof, expected = chi2_contingency(contingency)
print("\nChi-Square Test (Smoker vs Gender):")
print("Chi2 Statistic:", chi2)
print("p-value:", p_chi)
if p_chi < 0.05:
    print(" Significant association (Reject H0)")
else:
    print(" No significant association (Fail to reject H0)")
anova_result = stats.f_oneway(
    df[df['day']=='Thur']['tip'],
    df[df['day']=='Fri']['tip'],
    df[df['day']=='Sat']['tip'],
    df[df['day']=='Sun']['tip']
)
print("\nANOVA Test (Tips across days):")
print("F-statistic:", anova_result.statistic)
print("p-value:", anova_result.pvalue)
sns.histplot(df['tip'], bins=20, kde=True)
plt.title("Tip Amount Distribution")
plt.show()
sns.boxplot(x='day', y='tip', data=df)
plt.title("Tips across Days")
plt.show()
plt.figure(figsize=(5, 4))
numeric_df = df.select_dtypes(include=np.number)
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()
