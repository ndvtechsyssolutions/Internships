import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("matches.csv")

df.head()

print("Shape of dataset:", df.shape)
df.info()
df.describe(include='all')
print("\nMissing values per column:")
print(df.isnull().sum())

print("\nNumber of duplicate rows:", df.duplicated().sum())
plt.figure(figsize=(12, 6))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title("Missing Values Heatmap")
plt.show()


df['winner'].fillna('No Result', inplace=True)
df['umpire1'].fillna('Unknown', inplace=True)
df['umpire2'].fillna('Unknown', inplace=True)
df['city'].fillna('Unknown', inplace=True)


df.drop_duplicates(inplace=True)

df['date'] = pd.to_datetime(df['date']) 

categorical_cols = ['season', 'city', 'venue', 'team1', 'team2', 'toss_winner', 'winner', 'toss_decision', 'result']
for col in categorical_cols:
    df[col] = df[col].astype('category')

df['is_close_match'] = np.where(
    ((df['win_by_runs'] > 0) & (df['win_by_runs'] < 10)) |
    ((df['win_by_wickets'] > 0) & (df['win_by_wickets'] < 3)),
    True,
    False
)

mumbai_matches = df[df['city'] == 'Mumbai']


df_sorted = df.sort_values('date')


matches_per_season = df.groupby('season')['id'].count().reset_index(name='Total_Matches')
print(matches_per_season)

plt.figure(figsize=(10,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()

le = LabelEncoder()
label_cols = ['team1', 'team2', 'toss_winner', 'winner', 'venue', 'city']

for col in label_cols:
    df[col + '_encoded'] = le.fit_transform(df[col].astype(str))


df.head()
df.to_csv("cleaned_matches.csv", index=False)
