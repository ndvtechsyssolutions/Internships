import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


sales_before = np.array([210, 220, 215, 208, 225, 230, 218])
sales_after = np.array([235, 240, 245, 250, 238, 255, 260])


df = pd.DataFrame({
    'Sales': np.concatenate([sales_before, sales_after]),
    'Period': ['Before'] * len(sales_before) + ['After'] * len(sales_after)
})


sns.boxplot(x='Period', y='Sales', data=df)
plt.title("Sales Before vs After Strategy")
plt.show()



shapiro_before = stats.shapiro(sales_before)
shapiro_after = stats.shapiro(sales_after)
print(f"Shapiro Test (Before): p = {shapiro_before.pvalue}")
print(f"Shapiro Test (After): p = {shapiro_after.pvalue}")


levene_test = stats.levene(sales_before, sales_after)
print(f"Levene’s Test for Equal Variances: p = {levene_test.pvalue}")


t_stat, p_value = stats.ttest_ind(sales_after, sales_before, equal_var=(levene_test.pvalue > 0.05))
print(f"\nT-statistic: {t_stat}")
print(f"P-value: {p_value}")


alpha = 0.05
if p_value < alpha:
    print(" Reject the null hypothesis: Sales have significantly increased.")
else:
    print(" Fail to reject the null hypothesis: No significant change detected.")
