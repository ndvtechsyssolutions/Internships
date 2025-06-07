import numpy as np
import pandas as pd
from scipy.stats import ttest_ind
import seaborn as sns
import matplotlib.pyplot as plt
from google.colab import drive 
drive.mount("/content/drive") 
try:
    df = pd.read_csv('/content/drive/MyDrive/code/s.csv', encoding='utf-8')
except UnicodeDecodeError:
    print("UTF-8 decoding failed, trying 'latin-1'")
    df = pd.read_csv('/content/drive/MyDrive/code/s.csv', encoding='latin-1')
df = df[['Region', 'Profit']].dropna()
region1 = 'East'
region2 = 'West'

profit_region1 = df[df['Region'] == region1]['Profit']
profit_region2 = df[df['Region'] == region2]['Profit']

print("📌 Statistical Summary:")
print(df.groupby('Region')['Profit'].describe())

t_stat, p_value = ttest_ind(profit_region1, profit_region2, equal_var=False)

print("\n📌 Hypothesis Test: Profit Difference between East and West")
print(f"T-Statistic: {t_stat:.4f}")
print(f"P-Value: {p_value:.4f}")

if p_value < 0.05:
    print("✅ Significant difference in average profits (Reject H0)")
else:
    print("❌ No significant difference (Fail to reject H0)")
sns.boxplot(x='Region', y='Profit', data=df[df['Region'].isin([region1, region2])])
plt.title('Profit Distribution by Region')
plt.show()
