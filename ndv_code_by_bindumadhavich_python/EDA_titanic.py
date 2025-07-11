# Step 1: Install and Import Libraries
!pip install seaborn --quiet
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style='whitegrid')
%matplotlib inline
# Step 2: Load Dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)
# Preview
df.head()
# Step 3: Data Cleaning
# --- Missing values ---
print("\nMissing values:\n", df.isnull().sum())
# Fill Age with median, Embarked with mode, drop Cabin
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
df.drop(columns='Cabin', inplace=True)
# Remove duplicates
df.drop_duplicates(inplace=True)

# Check data types
df.info()
# Step 4: Summary Statistics
df.describe(include='all')
# Step 5: Univariate Visualizations
plt.figure(figsize=(12, 6))
# Age distribution
plt.subplot(1, 2, 1)
sns.histplot(df['Age'], kde=True, bins=30, color='skyblue')
plt.title('Age Distribution')
# Count of survivors
plt.subplot(1, 2, 2)
sns.countplot(x='Survived', data=df, palette='Set2')
plt.title('Survival Count')
plt.xticks([0, 1], ['No', 'Yes'])
plt.tight_layout()
plt.show()
# Step 6: Boxplot & Violin Plot
plt.figure(figsize=(14, 6))
# Boxplot of Fare by Pclass
plt.subplot(1, 2, 1)
sns.boxplot(x='Pclass', y='Fare', data=df, palette='Pastel1')
plt.title('Fare Distribution by Class')
# Violin plot (Bonus)
plt.subplot(1, 2, 2)
sns.violinplot(x='Survived', y='Age', data=df, palette='Set3')
plt.title('Age vs Survival (Violin Plot)')
plt.xticks([0, 1], ['No', 'Yes'])
plt.tight_layout()
plt.show()
# Step 7: Pair Plot & Correlation Heatmap
# Pair Plot (only selected features to avoid overplotting)
sns.pairplot(df[['Survived', 'Pclass', 'Age', 'Fare']], hue='Survived')
plt.suptitle('Pair Plot', y=1.02)
plt.show()
# Correlation Heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation Heatmap')
plt.xticks(rotation=45)
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()
# Step 9: Feature Engineering (Bonus)
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
# Compare survival by family size
plt.figure(figsize=(10, 5))
sns.barplot(x='FamilySize', y='Survived', data=df, palette='Blues_d')
plt.title('Survival Rate by Family Size')
plt.show()
