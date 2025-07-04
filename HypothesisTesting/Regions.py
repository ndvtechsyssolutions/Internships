import numpy as np
import pandas as pd
from scipy.stats import ttest_ind
import seaborn as sns
import matplotlib.pyplot as plt

from google.colab import drive # Make sure google.colab is imported if using Colab
drive.mount("/content/drive") # Mount Google Drive if using Colab

# Load dataset (replace with your actual file path)
# Specify the encoding to handle potential non-UTF-8 characters
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

# Statistical Summary
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
    print("No significant difference (Fail to reject H0)")

# Mean profit by region
print(df.groupby('Region')['Profit'].mean())

# Pivot table (if applicable)
pivot = pd.pivot_table(df, values='Profit', index='Region', aggfunc=['mean', 'std'])
print(pivot)

plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title(" Correlation Heatmap")
plt.show()

#Optional: Visualize with Boxplot
sns.boxplot(x='Region', y='Profit', data=df[df['Region'].isin([region1, region2])])
plt.title('Profit Distribution by Region')
plt.show()
