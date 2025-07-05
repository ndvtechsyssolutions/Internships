from google.colab import drive
drive.mount('/content/drive')
import os

# List everything in your Google Drive
drive_path = '/content/drive/MyDrive'
for item in os.listdir(drive_path):
    print(item)
# Check inside the kaggle dataset folder
dataset_path = '/content/drive/MyDrive/kaggle dataset'
for item in os.listdir(dataset_path):
    print(item)
# Step 2: Set ZIP path (make sure the filename is correct)
zip_path = '/content/drive/MyDrive/kaggle dataset/archive (2).zip'

# Step 3: Extract ZIP file
import zipfile
import os

# Create destination folder
os.makedirs('/content/data', exist_ok=True)

# Extract
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall('/content/data')

print("✅ Extraction completed.")
#load the dataset
import pandas as pd

# Use full path to the file inside extracted folder
df = pd.read_csv('/content/data/sales_data_sample.csv', encoding='latin-1')
df.head()
# Summary of numeric columns
df.describe()

# Check data types and missing values
df.info()
df.isnull().sum()
#ANOVA 
from scipy.stats import f_oneway

region_groups = [group['SALES'].dropna() for name, group in df.groupby('TERRITORY')]
f_stat, p_val = f_oneway(*region_groups)
print(f"F-statistic: {f_stat:.2f}, P-value: {p_val:.4f}")
#T-Test
from scipy.stats import ttest_ind

# Define groups from DEALSIZE
small_deals = df[df['DEALSIZE'] == 'Small']['SALES'].dropna()
large_deals = df[df['DEALSIZE'] == 'Large']['SALES'].dropna()

# Perform two-sample t-test
t_stat, p_val = ttest_ind(small_deals, large_deals)

# Display results
print(f"T-statistic: {t_stat:.2f}")
print(f"P-value: {p_val:.4f}")
#CHI-SQUARETEST
from scipy.stats import chi2_contingency
import pandas as pd

# Create contingency table
contingency = pd.crosstab(df['PRODUCTLINE'], df['TERRITORY'])

# Perform chi-square test
chi2, p, dof, expected = chi2_contingency(contingency)

# Print results
print(f"Chi2: {chi2:.2f}")
print(f"P-value: {p:.4f}")
#Visualizations
import seaborn as sns
import matplotlib.pyplot as plt

# Boxplot for SALES across TERRITORY
sns.boxplot(x='TERRITORY', y='SALES', data=df)
plt.title("Sales by Territory")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Histogram of SALES distribution
sns.histplot(df['SALES'], kde=True, bins=30, color='skyblue')
plt.title("Distribution of Sales")
plt.xlabel("Sales Amount")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()
