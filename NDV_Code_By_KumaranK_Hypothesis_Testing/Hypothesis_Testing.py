import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats

#https://drive.google.com/file/d/1D_9cUoWFjTtU-k7XbbreSTUisTrjV7ev/view?usp=drive_link
df = pd.read_csv("/content/drive/MyDrive/Data/HRDataset.csv")

print(df.describe())
print(df.mode(numeric_only=True))
print(df.median(numeric_only=True))

plt.figure(figsize=(12,7))
sns.histplot(df['Salary'],kde=True)
plt.title('Salary Distribution')
plt.show()

plt.figure(figsize=(12,7))
sns.boxplot(x=df['Department'],y=df['Salary'],data=df)
plt.title('Salary by Department')
plt.show()

t_stat,p_val = stats.ttest_1samp(df['Salary'].dropna(),50000)
print("T-test Result: t =",round(t_stat,2),"p =",round(p_val,4))

contingency = pd.crosstab(df['Sex'],df['EmploymentStatus'])
chi2,p,dof,expected = stats.chi2_contingency(contingency)
print("Chi-square Test Result: chi2 =",round(chi2,2),"p =",round(p,4))

anova = stats.f_oneway(*[group['Salary'].dropna() for name, group in df.groupby('Department')])
print("ANOVA result: F=", round(anova.statistic, 2), "p =", round(anova.pvalue,4))

plt.figure(figsize=(12,7))
sns.heatmap(df.corr(numeric_only=True),annot=True, cmap = 'coolwarm')
plt.title('Correlation Heatmap')
plt.show()

print(df.groupby('Department')['Salary'].mean())
