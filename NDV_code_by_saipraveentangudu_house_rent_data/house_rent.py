# House Rent Dataset Analysis
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind, f_oneway, pearsonr

# Load dataset
house_path = 'House_Rent_Dataset.csv'
house_df = pd.read_csv(house_path)

# Clean and prepare data
filtered_house_df = house_df[['City', 'Rent', 'Size', 'BHK']].dropna()

# Display basic summary
print("House Rent Data Summary:\n")
print(filtered_house_df.describe())

# Grouped summary by city
print("\nCity-wise Statistical Summary:\n")
print(filtered_house_df.groupby('City')['Rent'].describe())

# T-test between Bangalore and Hyderabad
city_a = 'Bangalore'
city_b = 'Hyderabad'
rent_a = filtered_house_df[filtered_house_df['City'] == city_a]['Rent']
rent_b = filtered_house_df[filtered_house_df['City'] == city_b]['Rent']

t_value, p_val = ttest_ind(rent_a, rent_b, equal_var=False)
print("\n📊 T-Test Result: Bangalore vs Hyderabad")
print(f"T-Statistic: {t_value:.4f}")
print(f"P-Value: {p_val:.4f}")
if p_val < 0.05:
    print("✅ Significant difference (Reject Null Hypothesis)")
else:
    print("❌ No significant difference (Fail to reject Null Hypothesis)")

# Box plot for city rent comparison
plt.figure(figsize=(7, 5))
sns.boxplot(data=filtered_house_df[filtered_house_df['City'].isin([city_a, city_b])],
            x='City', y='Rent', palette='Set2')
plt.title("Rent Distribution: Bangalore vs Hyderabad")
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# One-way ANOVA for Bangalore, Mumbai, Hyderabad
size_bangalore = filtered_house_df[filtered_house_df['City'] == 'Bangalore']['Size']
size_mumbai = filtered_house_df[filtered_house_df['City'] == 'Mumbai']['Size']
size_hyderabad = filtered_house_df[filtered_house_df['City'] == 'Hyderabad']['Size']

anova_stat, anova_p_val = f_oneway(size_bangalore, size_mumbai, size_hyderabad)
print("\n📊 One-Way ANOVA Test:")
print(f"F-Statistic: {anova_stat:.4f}")
print(f"P-Value: {anova_p_val:.4f}")
if anova_p_val < 0.05:
    print("✅ Significant difference between groups (Reject Null Hypothesis)")
else:
    print("❌ No significant difference (Fail to reject Null Hypothesis)")

# Pearson correlation between BHK and Rent
corr_coeff, p_corr = pearsonr(filtered_house_df['BHK'], filtered_house_df['Rent'])
print("\n📊 Pearson Correlation: BHK vs Rent")
print(f"Correlation Coefficient: {corr_coeff:.4f}")
print(f"P-Value: {p_corr:.4f}")
if p_corr < 0.05:
    print("✅ Significant correlation (Reject Null Hypothesis)")
else:
    print("❌ No significant correlation (Fail to reject Null Hypothesis)")

# Scatter plot: BHK vs Rent
plt.figure(figsize=(7, 5))
sns.scatterplot(data=filtered_house_df, x='BHK', y='Rent', color='darkorange', marker='o')
plt.title("BHK vs Rent")
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
