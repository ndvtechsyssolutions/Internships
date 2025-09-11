import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import ast

#Load the data
# ============================================
df = pd.read_csv('flipkart_50_raw.csv')

# Inspect the data
print("Dataset Info:")
print(df.info())
print("\nMissing Values:\n", df.isnull().sum())
print("\nDuplicate Rows:", df.duplicated().sum())

# missing values
df['retail_price'] = df['retail_price'].fillna(df['retail_price'].median())
df['discounted_price'] = df['discounted_price'].fillna(df['discounted_price'].median())

#==============================================================
df['overall_rating'] = pd.to_numeric(df['overall_rating'].replace('No rating available', np.nan), errors='coerce')
df['product_rating'] = pd.to_numeric(df['product_rating'].replace('No rating available', np.nan), errors='coerce')
overall_median = df['overall_rating'].median()
product_median = df['product_rating'].median()
df['overall_rating'] = df['overall_rating'].fillna(overall_median if not pd.isna(overall_median) else 0)
df['product_rating'] = df['product_rating'].fillna(product_median if not pd.isna(product_median) else 0)

df['brand'] = df['brand'].fillna('Unknown')
df = df.dropna(subset=['product_specifications', 'description'])

# Remove duplicates
df = df.drop_duplicates()
# =========================================================

# Converting data types
df['retail_price'] = df['retail_price'].astype(float)
df['discounted_price'] = df['discounted_price'].astype(float)
df['is_FK_Advantage_product'] = df['is_FK_Advantage_product'].astype(bool)

# Calculate discount percentage
df['discount_percentage'] = np.where(
    df['retail_price'] > 0,
    ((df['retail_price'] - df['discounted_price']) / df['retail_price']) * 100,0)

# Extract primary category safely
df['primary_category'] = df['product_category_tree'].apply(lambda x: ast.literal_eval(x)[0].split(' >> ')[0] if isinstance(x, str) and x else 'Unknown')

# Filtering and Sorting
df = df[df['retail_price'] > 0].sort_values(by='discounted_price', ascending=False)

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# =================================================================
# Visualizing discount percentage in histoplot
plt.figure(figsize=(8, 5))
sns.histplot(df['discount_percentage'], bins=20, kde=True)
plt.title('Discount Percentage Distribution')
plt.xlabel('Discount Percentage')
plt.ylabel('Frequency')
plt.savefig('discount_distribution.png')
plt.close()

# Save cleaned dataset
df.to_csv('flipkart_cleaned.csv', index=False)
print("\nCleaned dataset saved as 'flipkart_cleaned.csv'")
