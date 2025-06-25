import numpy as np
import pandas as pd
from scipy.stats import ttest_ind
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('House_Rent_Dataset.csv')
df.describe


# Clean data: Remove missing profits or regions
df = df[['City', 'Rent']].dropna()


# Filter two regions for comparison
region1 = 'Bangalore'
region2 = 'Hyderabad'

rent_region1 = df[df['City'] == region1]['Rent']
rent_region2 = df[df['City'] == region2]['Rent']

print(df.describe)


print(" Statistical Summary:")
print(df.groupby('City')['Rent'].describe())



t_stat, p_value = ttest_ind(rent_region1, rent_region2, equal_var=False)
print("\n📌 Hypothesis Test: Rent Difference between Banglore and Hyderabad")
print(f"T-Statistic: {t_stat:.4f}")
print(f"P-Value: {p_value:.4f}")
if p_value < 0.05:
    print("✅ Significant difference in average profits (Reject H0)")
else:
    print("❌ No significant difference (Fail to reject H0)")



sns.boxplot(x='City', y='Rent', data=df[df['City'].isin([region1, region2])])
plt.title('Rent Distribution by City')
plt.show()


from scipy.stats import f_oneway

bng_rents = df[df['City'] == 'Bangalore']['Size']
mum_rents = df[df['City'] == 'Mumbai']['Size']
hyd_rents = df[df['City'] == 'Hyderabad']['Size']

f_stat, p_value = f_oneway(bng_rents,mum_rents,hyd_rents)


print(" One-Way ANOVA Test Results")
print(f"F-Statistic: {f_stat:.4f}")
print(f"P-Value: {p_value:.4f}")

if p_value < 0.05:
    print("✅ At least one group mean is significantly different (Reject H0)")
else:
    print("❌ No significant difference between group means (Fail to reject H0)")


sns.boxplot(x='City', y='Size', data=df)
plt.title('Size Distribution by City')
plt.show()


from scipy.stats import chi2_contingency

print("Contingency Table:")
cols = ['Rent','BHK']
data = df[cols]
print(data)

chi2, p, dof, expected = chi2_contingency(data)

print("\nChi-Square Test Results:")
print(f"Chi-Square Statistic: {chi2:.4f}")
print(f"P-Value: {p:.4f}")
print(f"Degrees of Freedom: {dof}")
print("\nExpected Frequencies:")
print(expected)
if p < 0.05:
    print("✅ There is a significant relationship (Reject H0: Independent)")
else:
    print("❌ No significant relationship (Fail to reject H0)")

from scipy.stats import pearsonr
corr_coef, p_value = pearsonr(df['BHK'], df['Rent'])

# 📌 Output results
print("📌 Pearson Correlation Test Results")
print(f"Correlation Coefficient (r): {corr_coef:.4f}")
print(f"P-Value: {p_value:.4f}")

if p_value < 0.05:
    print("✅ Significant linear relationship (Reject H0)")
else:
    print("❌ No significant linear relationship (Fail to reject H0)")


sns.scatterplot(x='BHK', y='Rent', data=df)
plt.title('BHK vs Rent')
plt.show()
