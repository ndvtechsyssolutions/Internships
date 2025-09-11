from google.colab import files
uploaded = files.upload()  # Upload 'superstore_dataset_csv.zip'

import zipfile
import pandas as pd
import os

# Extract zip file
for filename in uploaded.keys():
    with zipfile.ZipFile(filename, 'r') as zip_ref:
        zip_ref.extractall()
        extracted_files = zip_ref.namelist()

csv_file = [f for f in extracted_files if f.endswith('.csv')][0]
df = pd.read_csv(csv_file)

# Clean columns
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Show actual columns
print("📄 Columns in dataset:")
print(df.columns.tolist())

# We'll now use 'sales', 'region', 'category', 'sub-category'
df = df[['region', 'sales', 'category', 'sub-category']].dropna()

# 📌 T-Test: Sales difference between East and West
from scipy.stats import ttest_ind

east_sales = df[df['region'] == 'East']['sales']
west_sales = df[df['region'] == 'West']['sales']

t_stat, p_value = ttest_ind(east_sales, west_sales, equal_var=False)

print(f"\n📌 T-Test: Sales Difference (East vs West)")
print(f"T-Statistic: {t_stat:.4f}, P-Value: {p_value:.4f}")
if p_value < 0.05:
    print("✅ Significant difference (Reject H0)")
else:
    print("❌ No significant difference (Fail to reject H0)")

# 📊 Boxplot
import seaborn as sns
import matplotlib.pyplot as plt

sns.boxplot(x='region', y='sales', data=df[df['region'].isin(['East', 'West'])])
plt.title('Sales Distribution: East vs West')
plt.show()

# 📌 ANOVA: Sales by Region
from scipy.stats import f_oneway
regions = df['region'].unique()
region_groups = [df[df['region'] == r]['sales'] for r in regions]

f_stat, p_val = f_oneway(*region_groups)

print(f"\n📌 ANOVA (Sales by Region)")
print(f"F-Statistic: {f_stat:.4f}, P-Value: {p_val:.4f}")
if p_val < 0.05:
    print("✅ At least one region is significantly different")
else:
    print("❌ No significant difference")

sns.boxplot(x='region', y='sales', data=df)
plt.title('Sales Distribution by Region')
plt.show()

# 📌 Chi-square test: Category vs Sub-category
from scipy.stats import chi2_contingency

contingency = pd.crosstab(df['category'], df['sub-category'])
chi2, p, dof, expected = chi2_contingency(contingency)

print(f"\n📌 Chi-Square Test (Category vs Sub-Category)")
print(f"Chi2: {chi2:.4f}, P-Value: {p:.4f}, DoF: {dof}")
if p < 0.05:
    print("✅ Relationship exists (Reject H0)")
else:
    print("❌ No relationship (Fail to reject H0)")

# 📊 Heatmap for expected frequencies
sns.heatmap(expected, annot=True, fmt=".1f", cmap="YlGnBu")
plt.title("Expected Frequencies (Chi-Square)")
plt.show()
