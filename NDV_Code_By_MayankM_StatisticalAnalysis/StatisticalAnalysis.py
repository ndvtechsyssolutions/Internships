# Description:- Perform descriptive statistics and hypothesis testing on a real-world business dataset to extract insights and validate assumptions.

# Import necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import ttest_ind, chi2_contingency, f_oneway

# Set styles for plots
sns.set(style="whitegrid")
%matplotlib inline

# Load dataset
df = pd.read_csv('WA_Fn-UseC_-HR-Employee-Attrition.csv')

# Display basic information
df.info()

# Preview the first few rows
df.head()

# Select only numerical columns
numerical_df = df.select_dtypes(include='number')

# Basic descriptive statistics: mean, std, min, 25%, 50%, 75%, max
summary_stats = numerical_df.describe()

# Add mode and median to the summary
summary_stats.loc['median'] = numerical_df.median()
summary_stats.loc['mode'] = numerical_df.mode().iloc[0]  # First mode if multiple

# Reorder rows for clarity
summary_stats = summary_stats.loc[['mean', 'median', 'mode', 'std', 'min', '25%', '50%', '75%', 'max']]

# Display the result
print("📈 Summary Statistics for Numerical Columns:\n")
summary_stats


# Summary statistics for numerical columns
df.describe()

# Mode for categorical data
df.mode().iloc[0]

# Checking null values
df.isnull().sum()

# Hypothesis 1
- Null Hypothesis (H0): There is no significant difference in monthly income between employees who left and stayed.
- Alternative Hypothesis (H1): There is a significant difference.
# Separate groups
income_left = df[df['Attrition'] == 'Yes']['MonthlyIncome']
income_stayed = df[df['Attrition'] == 'No']['MonthlyIncome']

# Two-sample t-test
t_stat, p_value = ttest_ind(income_left, income_stayed, equal_var=False)

print(f"T-Statistic: {t_stat:.4f}, P-Value: {p_value:.4f}")
if p_value < 0.05:
    print("Reject the null hypothesis: Income differs based on attrition.")
else:
    print("Fail to reject the null hypothesis: No significant income difference.")
  
  # Hypothesis 2
- H0: Attrition and Job Role are independent.
- H1: There is an association between Attrition and Job Role.
# Create a contingency table
contingency = pd.crosstab(df['Attrition'], df['JobRole'])

# Perform Chi-Square Test
chi2, p_val, dof, expected = chi2_contingency(contingency)

print(f"Chi2 Statistic: {chi2:.4f}, P-Value: {p_val:.4f}")
if p_val < 0.05:
    print("Reject the null hypothesis: There is a relationship between attrition and job role.")
else:
    print("Fail to reject the null: No significant relationship.")
  # Data Visualization
plt.figure(figsize=(10, 6))
sns.histplot(df['MonthlyIncome'], kde=True, bins=30)
plt.title('Distribution of Monthly Income')
plt.xlabel('Monthly Income')
plt.ylabel('Frequency')
plt.show()
# Monthly Income By Attrition
plt.figure(figsize=(10, 6))
sns.boxplot(x='Attrition', y='MonthlyIncome', data=df)
plt.title('Monthly Income by Attrition')
plt.show()
# Correlation Matrix
# Select a subset of numerical features that are likely relevant
subset_features = ['MonthlyIncome', 'YearsAtCompany', 'JobSatisfaction', 'TotalWorkingYears', 'Age', 'DistanceFromHome']

# Create a new DataFrame with only the selected features
df_subset = df[subset_features]

# Calculate the correlation matrix for the subset
corr_subset = df_subset.corr(numeric_only=True) # Use numeric_only=True to be explicit

# Plot heatmap for the subset with a reasonable figure size
plt.figure(figsize=(8, 6))
sns.heatmap(corr_subset, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap - Subset of Features')
plt.show()
# Group-wise summary: Avg income and satisfaction by department
pivot = df.pivot_table(values=['MonthlyIncome', 'JobSatisfaction'],
                       index='Department',
                       aggfunc=np.mean)
pivot
# ANOVA - Does Job Satisfaction differ by Job Role?
# Prepare data
job_roles = df['JobRole'].unique()
groups = [df[df['JobRole'] == role]['JobSatisfaction'] for role in job_roles]

# ANOVA Test
f_stat, p_value = f_oneway(*groups)

print(f"F-Statistic: {f_stat:.4f}, P-Value: {p_value:.4f}")
if p_value < 0.05:
    print("Reject the null hypothesis: Job Satisfaction differs across Job Roles.")
else:
    print("Fail to reject the null hypothesis.")






