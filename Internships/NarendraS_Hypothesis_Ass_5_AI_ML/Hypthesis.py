
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

# -----------------------------
# 1. Load and Clean the Dataset
# -----------------------------
df = pd.read_csv("Superstore.csv", encoding='latin1')
print("Data Loaded")

# Basic Info
print("\nDataset Info:")
print(df.info())
print("\nSummary Stats:")
print(df.describe())

# Handle missing values
print("\n Missing Values:\n", df.isnull().sum())
if 'Postal Code' in df.columns:
    df['Postal Code'].fillna(df['Postal Code'].median(), inplace=True)

# -----------------------------
# 2. Summary Statistics
# -----------------------------
numerical_cols = df.select_dtypes(include=np.number)

# Handle mean, median, std
summary_stats = numerical_cols.agg(['mean', 'median', 'std'])
print("\nSummary Statistics (Mean, Median, Std):")
print(summary_stats)

# Handle mode separately
print("\nMode:")
for col in numerical_cols.columns:
    print(f"{col} Mode: {numerical_cols[col].mode().values}")

# -----------------------------
# 3. Hypothesis Tests
# -----------------------------

# H1: Region and Ship Mode are independent
print("\nChi-square Test (Region vs Ship Mode):")
contingency = pd.crosstab(df['Region'], df['Ship Mode'])
chi2_stat, chi2_p, _, _ = stats.chi2_contingency(contingency)
print(f"Chi2 = {chi2_stat:.2f}, p = {chi2_p:.4f}")
if chi2_p < 0.05:
    print("==Reject H₀: Region and Ship Mode are dependent.")
else:
    print("==Fail to reject H₀: No significant relationship.")

# H2: Sales means differ across regions (ANOVA)
print("\nANOVA Test (Sales by Region):")
anova_groups = [group['Sales'] for name, group in df.groupby('Region')]
f_stat, p_val = stats.f_oneway(*anova_groups)
print(f"F = {f_stat:.2f}, p = {p_val:.4f}")
if p_val < 0.05:
    print("==Reject H₀: Sales means differ across regions.")
else:
    print("==Fail to reject H₀: No significant difference in sales.")

# -----------------------------
# 4. Visualizations
# -----------------------------

# Histogram: Sales
plt.figure(figsize=(6,4))
sns.histplot(df['Sales'], kde=True)
plt.title("Sales Distribution")
plt.tight_layout()
plt.savefig("sales_distribution.png")

# Boxplot: Sales by Region
plt.figure(figsize=(6,4))
sns.boxplot(x='Region', y='Sales', data=df)
plt.title("Sales by Region")
plt.tight_layout()
plt.savefig("sales_by_region_boxplot.png")

# Heatmap: Correlation
plt.figure(figsize=(6,4))
sns.heatmap(numerical_cols.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("correlation_heatmap.png")

print("Plots saved as PNG files.")

# -----------------------------
# 5. Bonus: Pivot Table
# -----------------------------
print("\nPivot Table (Category Summary):")
pivot = df.pivot_table(index='Category', values='Sales', aggfunc=['sum', 'mean', 'count'])
print(pivot.round(2))

# -----------------------------
# 6. Export Cleaned Data
# -----------------------------
df.to_csv("superstore_cleaned.csv", index=False)
print("\nCleaned data exported to 'superstore_cleaned.csv'")

