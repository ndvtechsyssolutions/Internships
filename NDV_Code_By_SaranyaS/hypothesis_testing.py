
import pandas as pd
import numpy as np
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency
from scipy.stats import f_oneway
from scipy.stats import ttest_ind
from scipy.stats import pearsonr

# Sample business dataset (sales before and after a campaign)
data = {
    'Store_ID': np.arange(1, 11),
    'Sales_Before': [2000, 2200, 2500, 2100, 2700, 2900, 3100, 2300, 2400, 2600],
    'Sales_After': [2500, 2600, 2800, 2600, 3000, 3300, 3500, 2700, 2900, 3100]
}

# creating a data frame
df = pd.DataFrame(data)

# Statistical Summary
print(" Statistical Summary:\n")
print(df.describe())

# Hypothesis Test: Paired T-Test
t_stat, p_value = stats.ttest_rel(df['Sales_Before'], df['Sales_After'])

#  Result Interpretation
print("\n Paired T-Test Result:")
print(f"T-Statistic: {t_stat:.4f}")
print(f"P-Value: {p_value:.4f}")

if p_value < 0.05:
    print(" Result: Statistically significant difference in sales (reject H0)")
else:
    print(" Result: No significant difference (fail to reject H0)")

try:
    df = pd.read_csv('/content/drive/MyDrive/Data/Superstore.csv', encoding='utf-8')
except UnicodeDecodeError:
    print("UTF-8 decoding failed, trying 'latin-1'")
    df = pd.read_csv('/content/drive/MyDrive/Data/Superstore.csv', encoding='latin-1')


# Clean data: Remove missing profits or regions
df = df[['Region', 'Profit']].dropna()

# Filter two regions for comparison
region1 = 'East'
region2 = 'West'

profit_region1 = df[df['Region'] == region1]['Profit']
profit_region2 = df[df['Region'] == region2]['Profit']

#  Statistical Summary
print(" Statistical Summary:")
print(df.groupby('Region')['Profit'].describe())

#  Hypothesis Test: Are average profits different between Region 1 and Region 2?
t_stat, p_value = ttest_ind(profit_region1, profit_region2, equal_var=False)

print("\n Hypothesis Test: Profit Difference between East and West")
print(f"T-Statistic: {t_stat:.4f}")
print(f"P-Value: {p_value:.4f}")

if p_value < 0.05:
    print(" Significant difference in average profits (Reject H0)")
else:
    print(" No significant difference (Fail to reject H0)")

#ANOVA

# Sample data simulating total sales in 3 different regions
data = {
    'Region': ['East'] * 5 + ['West'] * 5 + ['South'] * 5,
    'Sales': [210, 220, 230, 225, 215, 250, 270, 260, 255, 265, 180, 190, 175, 185, 195]
}
df = pd.DataFrame(data)

#  Visualize the distributions
sns.boxplot(x='Region', y='Sales', data=df)
plt.title('Sales Distribution by Region')
plt.show()

#  Perform One-Way ANOVA
east_sales = df[df['Region'] == 'East']['Sales']
west_sales = df[df['Region'] == 'West']['Sales']
south_sales = df[df['Region'] == 'South']['Sales']

f_stat, p_value = f_oneway(east_sales, west_sales, south_sales)

#  Output results
print(" One-Way ANOVA Test Results")
print(f"F-Statistic: {f_stat:.4f}")
print(f"P-Value: {p_value:.4f}")

if p_value < 0.05:
    print(" At least one group mean is significantly different (Reject H0)")
else:
    print(" No significant difference between group means (Fail to reject H0)")

#chi-sqaure testing

# Sample data: Contingency table of Gender vs Purchase Decision
data = {
    'Purchased': [50, 30],
    'Not Purchased': [20, 40]
}
df = pd.DataFrame(data, index=['Male', 'Female'])

#  View the contingency table
print("Contingency Table:")
print(df)

#  Perform Chi-Square Test
chi2, p, dof, expected = chi2_contingency(df)

#  Output results
print("\nChi-Square Test Results:")
print(f"Chi-Square Statistic: {chi2:.4f}")
print(f"P-Value: {p:.4f}")
print(f"Degrees of Freedom: {dof}")
print("\nExpected Frequencies:")
print(expected)

# Decision
if p < 0.05:
    print(" There is a significant relationship (Reject H0: Independent)")
else:
    print(" No significant relationship (Fail to reject H0)")

#  Sample data: Advertising budget vs Sales
data = {
    'TV_Ads': [250, 300, 320, 400, 150, 180, 270, 220, 330, 360],
    'Sales': [22, 25, 27, 31, 14, 16, 24, 19, 28, 30]
}
df = pd.DataFrame(data)

#  Pearson Correlation Test
corr_coef, p_value = pearsonr(df['TV_Ads'], df['Sales'])

#  Output results
print(" Pearson Correlation Test Results")
print(f"Correlation Coefficient (r): {corr_coef:.4f}")
print(f"P-Value: {p_value:.4f}")

if p_value < 0.05:
    print(" Significant linear relationship (Reject H0)")
else:
    print(" No significant linear relationship (Fail to reject H0)")
