#import libraries
import pandas as pd
import numpy as np
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt

#Sample business dataset (sales before and after a campaign)
data = {
    'Store_ID': np.arange(1, 11),
    'Sales_Before': [2000, 2200, 2500, 2100, 2700, 2900, 3100, 2300, 2400, 2600],
    'Sales_After': [2500, 2600, 2800, 2600, 3000, 3300, 3500, 2700, 2900, 3100]
}

# creating a data frame
df = pd.DataFrame(data)

#Statistical Summary
print("Statistical Summary:\n")
print(df.describe())

#Hypothesis Test: Paired T-Test
t_stat, p_value = stats.ttest_rel(df['Sales_Before'], df['Sales_After'])

#Result Interpretation
print("\n Paired T-Test Result:")
print(f"T-Statistic: {t_stat:.4f}")
print(f"P-Value: {p_value:.4f}")

if p_value < 0.05:
    print("Result: Statistically significant difference in sales (reject H0)")
else:
    print("Result: No significant difference (fail to reject H0)")

# Visualization (Optional)
plt.figure(figsize=(10, 5))
sns.histplot(df['Sales_Before'], kde=True, color='red', label='Before')
sns.histplot(df['Sales_After'], kde=True, color='green', label='After')
plt.title('Sales Distribution Before vs After')
plt.legend()
plt.show()
