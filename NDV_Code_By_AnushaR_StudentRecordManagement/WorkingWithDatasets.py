# ipl_assignment2.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

# Step 1: Load the dataset
df = pd.read_csv("IPL_Matches.csv")
print("✅ Dataset loaded!")

# Step 2: Basic inspection
print("\n🔍 First 5 rows:")
print(df.head())

print("\n📊 Dataset info:")
print(df.info())

print("\n🧼 Missing values:")
print(df.isnull().sum())

# Step 3: Visualize missing values
plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), cbar=False, cmap="YlOrBr")
plt.title("Missing Values Heatmap")
plt.savefig("missing_values_heatmap.png")
plt.close()

# Step 4: Handle missing values
df['City'].fillna('Unknown', inplace=True)
df['WinningTeam'].fillna('Match Abandoned', inplace=True)
df['Umpire1'].fillna('Not Available', inplace=True)
df['Umpire2'].fillna('Not Available', inplace=True)

# Step 5: Remove duplicates
before = df.shape[0]
df.drop_duplicates(inplace=True)
after = df.shape[0]
print(f"\n🧹 Removed {before - after} duplicate rows.")

# Step 6: Data type conversions
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Step 7: Create win margin column
# Note: IPL dataset uses 'WonBy' and 'Margin' instead of win_by_runs/wickets
df['total_win_margin'] = df['Margin'].fillna(0)

# Step 8: Grouping and Filtering
matches_per_season = df['Season'].value_counts().sort_index()
top_teams = df['WinningTeam'].value_counts().head(10)

print("\n📅 Matches per season:\n", matches_per_season)
print("\n🏆 Top 10 winning teams:\n", top_teams)

# Step 9: Summary statistics
print("\n📈 Summary Statistics:")
print(df.describe(include='all'))

# Step 10: Visualizations
plt.figure(figsize=(10, 6))
matches_per_season.plot(kind='bar', color='skyblue')
plt.title("Matches per Season")
plt.xlabel("Season")
plt.ylabel("No. of Matches")
plt.tight_layout()
plt.savefig("matches_per_season.png")
plt.close()

plt.figure(figsize=(10, 6))
top_teams.plot(kind='barh', color='orange')
plt.title("Top 10 Teams with Most Wins")
plt.xlabel("Wins")
plt.tight_layout()
plt.savefig("top_teams.png")
plt.close()

# Step 11: Correlation matrix
# 'dl_applied' and win_by_runs/wickets not in your dataset — skip that
corr = df[['Margin', 'total_win_margin']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.tight_layout()
plt.savefig("correlation_matrix.png")
plt.close()

# Step 12: Label Encoding
le = LabelEncoder()
df['Team1_encoded'] = le.fit_transform(df['Team1'])
df['Team2_encoded'] = le.fit_transform(df['Team2'])
df['WinningTeam_encoded'] = le.fit_transform(df['WinningTeam'])

# Step 13: Save cleaned data
df.to_csv("IPL_Cleaned.csv", index=False)
print("\n✅ Cleaned data saved as 'IPL_Cleaned.csv'")
print("🎉 Assignment Completed Successfully!")
