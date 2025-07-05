
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Settings
sns.set(style='whitegrid')
plt.rcParams['figure.figsize'] = (10, 6)

# 1. Load the dataset
df = pd.read_csv("titanic.csv")  # adjust path if needed

# 2. Clean column names (if necessary)
df.columns = df.columns.str.strip().str.lower()

# 3. Drop duplicates
df.drop_duplicates(inplace=True)

# 4. Fill missing values
df['age'] = df['age'].fillna(df['age'].median())

# 5. Feature Engineering
df['familysize'] = df['sibsp'] + df['parch'] + 1

# 6. Summary statistics
print("=== Dataset Info ===")
print(df.info())
print("\n=== Describe ===")
print(df.describe(include='all'))
print("\n=== Value Counts ===")
for col in ['survived', 'pclass', 'sex']:
    print(f"\n{col.upper()}:\n", df[col].value_counts())

# 7. Distribution Plots
fig, axs = plt.subplots(2, 2, figsize=(14, 10))
sns.histplot(df['age'], kde=True, ax=axs[0, 0]).set_title("Age Distribution")
sns.boxplot(x='survived', y='age', data=df, ax=axs[0, 1]).set_title("Age vs Survived")
sns.histplot(df['fare'], kde=True, ax=axs[1, 0]).set_title("Fare Distribution")
sns.boxplot(x='survived', y='fare', data=df, ax=axs[1, 1]).set_title("Fare vs Survived")
plt.tight_layout()
plt.show()

# 8. Count Plots for categorical features
for col in ['pclass', 'sex']:
    plt.figure(figsize=(6, 4))
    sns.countplot(x=col, hue='survived', data=df)
    plt.title(f"Survival by {col.capitalize()}")
    plt.show()

# 9. Correlation Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(df[['survived', 'age', 'fare', 'sibsp', 'parch', 'familysize']].corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

# 10. Pair Plot
sns.pairplot(df[['survived', 'age', 'fare', 'sibsp', 'parch']], hue='survived', diag_kind='hist')
plt.show()

# 11. Group-by Survival Rates
print("\n=== Survival Rates ===")
print("By Class:\n", df.groupby('pclass')['survived'].mean())
print("\nBy Sex:\n", df.groupby('sex')['survived'].mean())

# 12. Violin and Swarm Plots: FamilySize vs Survival
plt.figure(figsize=(6, 4))
sns.violinplot(x='survived', y='familysize', data=df)
plt.title("FamilySize vs Survival (Violin)")
plt.show()

plt.figure(figsize=(6, 4))
sns.swarmplot(x='survived', y='familysize', data=df)
plt.title("FamilySize vs Survival (Swarm)")
plt.show()

# 13. Top Insights
print("\n=== Top 5 Insights ===")
insights = [
    "1. Women had a much higher survival rate than men.",
    "2. Passengers in 1st class had the highest survival rate.",
    "3. Mid-sized families (2–4 members) had higher chances of survival.",
    "4. Higher fare values are generally associated with survivors.",
    "5. Younger passengers (age < 15) were more likely to survive."
]
for line in insights:
    print(line)

