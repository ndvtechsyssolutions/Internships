# 1. Import Required Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Set visualization styles
plt.style.use('default')
sns.set_palette("husl")
sns.set_context("notebook", font_scale=1.1)

# Display settings
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', 50)  # Limit column width for better display

# Ignore warnings
import warnings
warnings.filterwarnings('ignore')

print("All libraries imported successfully!")

# 2. Load and Initial Data Exploration
try:
    df = pd.read_csv('D:\\github\\NDVTech_internship\\Assignment 4\\tested.csv')
    print("Dataset loaded successfully!")
except FileNotFoundError:
    print("Error: File not found at the specified path")
    df = pd.DataFrame()

# Display basic information
print(f"\nDataset Shape: {df.shape}")
print(f"Columns: {list(df.columns)}")

# Display first few rows
print("\nFirst 5 rows:")
print(df.head())

# Display last few rows
print("\nLast 5 rows:")
print(df.tail())

# Basic dataset info
print("\nDataset Info:")
print(df.info())

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Check unique values in categorical columns
categorical_cols = df.select_dtypes(include=['object']).columns
print("\nUnique values in categorical columns:")
for col in categorical_cols:
    print(f"\n{col}: {df[col].nunique()} unique values")
    print(f"Sample values: {df[col].unique()[:5]}")  # Show first 5 unique values

# 3. Data Cleaning
# Check for missing values
print("\nMissing Values Analysis:")
missing_data = df.isnull().sum()
missing_percent = (missing_data / len(df)) * 100
missing_df = pd.DataFrame({
    'Missing Count': missing_data,
    'Missing Percentage': missing_percent
})
missing_df = missing_df[missing_df['Missing Count'] > 0].sort_values('Missing Count', ascending=False)
print(missing_df)

# Visualize missing values
plt.figure(figsize=(12, 6))
sns.heatmap(df.isnull(), cbar=True, yticklabels=False, cmap='viridis')
plt.title('Missing Values Heatmap')
plt.savefig('missing_values.png')  # Save instead of showing
print("Saved missing_values.png")
plt.close()

# Handle missing values
# Age: Fill with median based on Pclass and Sex
df['Age'] = df['Age'].fillna(df.groupby(['Pclass', 'Sex'])['Age'].transform('median'))

# Cabin: Create 'Unknown' category
df['Cabin'] = df['Cabin'].fillna('Unknown')

# Embarked: Fill with mode (most frequent value)
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# Fare: Fill with median based on Pclass
df['Fare'] = df['Fare'].fillna(df.groupby('Pclass')['Fare'].transform('median'))

# Verify missing values are handled
print("\nMissing values after cleaning:")
print(df.isnull().sum())

# Fix data types - DO NOT convert Survived to categorical
categorical_columns = ['Sex', 'Embarked', 'Pclass']  # Removed Survived
for col in categorical_columns:
    df[col] = df[col].astype('category')

print("\nData types after conversion:")
print(df.dtypes)

# Remove duplicates
print(f"\nNumber of duplicate rows: {df.duplicated().sum()}")
df = df.drop_duplicates()
print(f"Shape after removing duplicates: {df.shape}")

# 4. Feature Engineering
# Create FamilySize feature
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1

# Create IsAlone feature
df['IsAlone'] = (df['FamilySize'] == 1).astype(int)

# Extract Title from Name - fixed escape sequence
df['Title'] = df['Name'].str.extract(r' ([A-Za-z]+)\.', expand=False)

# Group rare titles
title_counts = df['Title'].value_counts()
rare_titles = title_counts[title_counts < 5].index
df['Title'] = df['Title'].replace(rare_titles, 'Rare')

# Create Age groups
df['AgeGroup'] = pd.cut(
    df['Age'], 
    bins=[0, 12, 18, 35, 60, 100], 
    labels=['Child', 'Teen', 'Adult', 'Middle-aged', 'Senior']
)

# Create Fare groups
try:
    df['FareGroup'] = pd.qcut(
        df['Fare'], 
        q=4, 
        labels=['Low', 'Medium', 'High', 'Very High']
    )
except ValueError:
    # Handle case where fare values are identical
    df['FareGroup'] = 'Medium'

print("\nNew features created:")
print(df[['FamilySize', 'IsAlone', 'Title', 'AgeGroup', 'FareGroup']].head())

# 5. Exploratory Data Analysis
# Updated summary statistics
print("\nSummary Statistics After Cleaning and Feature Engineering:")
print(df.describe(include='all'))

# Value counts for categorical variables
categorical_features = ['Sex', 'Embarked', 'Pclass', 'Title', 'AgeGroup', 'FareGroup']

fig, axes = plt.subplots(3, 2, figsize=(18, 18))
axes = axes.ravel()

for i, feature in enumerate(categorical_features):
    df[feature].value_counts().plot(kind='bar', ax=axes[i])
    axes[i].set_title(f'Distribution of {feature}')
    axes[i].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig('categorical_distributions.png')
print("Saved categorical_distributions.png")
plt.close()

# Distribution of numerical variables
numerical_features = ['Age', 'Fare', 'SibSp', 'Parch', 'FamilySize']

fig, axes = plt.subplots(2, 3, figsize=(18, 12))
axes = axes.ravel()

for i, feature in enumerate(numerical_features):
    df[feature].hist(bins=30, ax=axes[i], alpha=0.7)
    axes[i].set_title(f'Distribution of {feature}')
    axes[i].set_xlabel(feature)
    axes[i].set_ylabel('Frequency')

# Remove empty subplot if needed
if len(numerical_features) < len(axes):
    for j in range(len(numerical_features), len(axes)):
        fig.delaxes(axes[j])

plt.tight_layout()
plt.savefig('numerical_distributions.png')
print("Saved numerical_distributions.png")
plt.close()

# Survival analysis - FIXED: Survived is numeric now
survival_rate = df['Survived'].mean()
print(f"\nOverall Survival Rate: {survival_rate:.2%}")

plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='Survived')
plt.title('Survival Count')
plt.xlabel('Survived (0: No, 1: Yes)')
plt.savefig('survival_count.png')
print("Saved survival_count.png")
plt.close()

# Survival by different features
features_to_analyze = ['Sex', 'Pclass', 'Embarked', 'AgeGroup', 'Title']

fig, axes = plt.subplots(3, 2, figsize=(20, 20))
axes = axes.ravel()

for i, feature in enumerate(features_to_analyze):
    sns.countplot(data=df, x=feature, hue='Survived', ax=axes[i])
    axes[i].set_title(f'Survival by {feature}')
    axes[i].tick_params(axis='x', rotation=45)

# Remove empty subplot if needed
if len(features_to_analyze) < len(axes):
    for j in range(len(features_to_analyze), len(axes)):
        fig.delaxes(axes[j])

plt.tight_layout()
plt.savefig('survival_by_features.png')
print("Saved survival_by_features.png")
plt.close()

# Correlation analysis
numerical_df = df.select_dtypes(include=[np.number])
correlation_matrix = numerical_df.corr()

plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, square=True)
plt.title('Correlation Heatmap')
plt.savefig('correlation_heatmap.png')
print("Saved correlation_heatmap.png")
plt.close()

# Advanced visualizations
plt.figure(figsize=(12, 8))
sns.violinplot(data=df, x='Pclass', y='Age', hue='Survived', split=True)
plt.title('Age Distribution by Class and Survival')
plt.savefig('age_class_survival.png')
print("Saved age_class_survival.png")
plt.close()

# GroupBy analysis
print("\n=== SURVIVAL ANALYSIS BY GROUPS ===")

# By Sex
sex_survival = df.groupby('Sex')['Survived'].agg(['count', 'sum', 'mean']).round(3)
sex_survival.columns = ['Total', 'Survived', 'Survival_Rate']
print("\nSurvival by Sex:")
print(sex_survival)

# By Class
class_survival = df.groupby('Pclass')['Survived'].agg(['count', 'sum', 'mean']).round(3)
class_survival.columns = ['Total', 'Survived', 'Survival_Rate']
print("\nSurvival by Class:")
print(class_survival)

# By Age Group
age_survival = df.groupby('AgeGroup')['Survived'].agg(['count', 'sum', 'mean']).round(3)
age_survival.columns = ['Total', 'Survived', 'Survival_Rate']
print("\nSurvival by Age Group:")
print(age_survival)

# Statistical tests
print("\n=== STATISTICAL SIGNIFICANCE TESTS ===")

# Chi-square test for Sex vs Survival
sex_survival_crosstab = pd.crosstab(df['Sex'], df['Survived'])
chi2, p_value, dof, expected = stats.chi2_contingency(sex_survival_crosstab)
print(f"\nSex vs Survival - Chi-square: {chi2:.4f}, p-value: {p_value:.6f}")

# T-test for Age difference between survivors and non-survivors
survivors_age = df[df['Survived'] == 1]['Age'].dropna()
non_survivors_age = df[df['Survived'] == 0]['Age'].dropna()
t_stat, p_value = stats.ttest_ind(survivors_age, non_survivors_age)
print(f"\nAge difference - t-statistic: {t_stat:.4f}, p-value: {p_value:.4f}")

# Final data quality report
print("\n=== FINAL DATA QUALITY REPORT ===")
print(f"Dataset shape: {df.shape}")
print(f"Missing values: {df.isnull().sum().sum()}")
print(f"Duplicate rows: {df.duplicated().sum()}")
print(f"Data types:\n{df.dtypes.value_counts()}")

# Key insights
print("\n=== KEY INSIGHTS ===")
print("1. Survival rate by gender:")
print(sex_survival)
print("\n2. Survival rate by passenger class:")
print(class_survival)
print("\n3. Survival rate by age group:")
print(age_survival)
print("\n4. Family size distribution:")
print(df['FamilySize'].value_counts())
print("\n5. Most common titles:")
print(df['Title'].value_counts().head(10))

print("\nAnalysis completed successfully! All visualizations saved as PNG files.")
