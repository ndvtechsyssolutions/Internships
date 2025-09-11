## assignment-5
import pandas as pd
import numpy as np
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind, chi2_contingency
df = pd.read_csv('Superstore.csv', encoding='latin1')
df
print(" Statistical Summary:\n")
print(df.describe())
# Load dataset (adjust encoding if needed)
df = pd.read_csv('Superstore.csv', encoding='latin1')

# ========================================
#  Hypothesis Set 1: t-test (East vs West Profit)
# ========================================
east_profit = df[df['Region'] == 'East']['Profit']
west_profit = df[df['Region'] == 'West']['Profit']

t_stat, p_val = ttest_ind(east_profit, west_profit)

print(" Hypothesis Test 1: t-test on Profit (East vs West)")
print(f"t-statistic = {t_stat:.4f}")
print(f"p-value     = {p_val:.4f}")
if p_val < 0.05:
    print(" Result: Reject Null Hypothesis → Profits are significantly different.\n")
else:
    print(" Result: Fail to Reject Null Hypothesis → No significant difference in profits.\n")

# ========================================
#  Hypothesis Set 2: Chi-square (Region vs Ship Mode)
# ========================================
contingency_table = pd.crosstab(df['Region'], df['Ship Mode'])

chi2, chi_p, dof, expected = chi2_contingency(contingency_table)

print(" Hypothesis Test 2: Chi-square Test (Region vs Ship Mode)")
print(f"Chi2 statistic = {chi2:.4f}")
print(f"p-value         = {chi_p:.4f}")
if chi_p < 0.05:
    print(" Result: Reject Null Hypothesis → Region and Ship Mode are dependent.")
else:
    print(" Result: Fail to Reject Null Hypothesis → Region and Ship Mode are independent.")

print('\n')
# ===============================
#  1. One-sample t-test
# ===============================
# H0: Mean Sales = 250
# H1: Mean Sales ≠ 250

sales = df['Sales']
t_stat1, p_val1 = ttest_1samp(sales, 250)

print(" One-sample t-test: Is mean Sales = 250?")
print(f"t-statistic = {t_stat1:.4f}, p-value = {p_val1:.4f}")
if p_val1 < 0.05:
    print(" Reject H₀ → Mean Sales is significantly different from 250.\n")
else:
    print(" Fail to reject H₀ → No significant difference from 250.\n")
print('\n')
# ===============================
#  3. Chi-square test: Region vs Ship Mode
# ===============================
contingency_table = pd.crosstab(df['Region'], df['Ship Mode'])
chi2, chi_p, dof, expected = chi2_contingency(contingency_table)

print(" Chi-square Test: Region vs Ship Mode")
print(f"Chi2 = {chi2:.4f}, p-value = {chi_p:.4f}")
if chi_p < 0.05:
    print(" Reject H₀ → Region and Ship Mode are dependent.\n")
else:
    print(" Fail to reject H₀ → They are independent.\n")
print('\n')
# ===============================
#  4. ANOVA: Profit across Regions
# ===============================
central_profit = df[df['Region'] == 'Central']['Profit']
south_profit = df[df['Region'] == 'South']['Profit']

f_stat, anova_p = f_oneway(east_profit, west_profit, central_profit, south_profit)

print(" ANOVA: Profit across 4 Regions")
print(f"F-statistic = {f_stat:.4f}, p-value = {anova_p:.4f}")
if anova_p < 0.05:
    print(" Reject H₀ → At least one region has different mean profit.\n")
else:
    print(" Fail to reject H₀ → No significant difference in profit among regions.\n")
print('\n')
# ===============================
#  1. Histograms of numerical features
# ===============================
plt.figure(figsize=(16, 4))

# Histogram: Sales
plt.subplot(1, 3, 1)
sns.histplot(df['Sales'], bins=30, kde=True, color='skyblue')
plt.title("Sales Distribution")

# Histogram: Profit
plt.subplot(1, 3, 2)
sns.histplot(df['Profit'], bins=30, kde=True, color='salmon')
plt.title("Profit Distribution")

# Histogram: Discount
plt.subplot(1, 3, 3)
sns.histplot(df['Discount'], bins=20, kde=True, color='lightgreen')
plt.title("Discount Distribution")

plt.tight_layout()
plt.show()
print('\n')
# ===============================
#  2. Boxplots by Region
# ===============================
plt.figure(figsize=(14, 4))

plt.subplot(1, 3, 1)
sns.boxplot(x='Region', y='Sales', data=df, palette='pastel')
plt.title("Sales by Region")


plt.subplot(1, 3, 2)
sns.boxplot(x='Region', y='Profit', data=df, palette='muted')
plt.title("Profit by Region")


plt.subplot(1, 3, 3)
sns.boxplot(x='Region', y='Discount', data=df, palette='Set3')
plt.title("Discount by Region")

plt.tight_layout()
plt.show()
print('\n')
### Perform correlation analysis and visualize with heatmaps.
numerical_cols = df[['Sales', 'Quantity', 'Discount', 'Profit']]
corr_matrix = numerical_cols.corr()

plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Correlation Heatmap of Numerical Features")
plt.tight_layout()
plt.show()
print('\n')
## Create pivot tables or group-wise summaries to support insights.
region_summary = df.groupby('Region')[['Sales', 'Profit']].sum().reset_index()
print(" Total Sales and Profit by Region:\n")
print(region_summary)
