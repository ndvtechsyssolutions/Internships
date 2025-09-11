import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
 
file_path = "/content/drive/MyDrive/Data/ipl_matches.csv"
data = pd.read_csv(file_path)

print("First 5 rows:")
print(data.head())

print("\nShape of Dataset:")
print(data.shape)

print("\nInfo")
print(data.info())

print("\nMissing Values:")
print(data.isnull().sum())

sns.heatmap(data.isnull(), cbar = True, cmap = "viridis")
plt.title("Missing values Heatmap")
plt.show()

data = data.dropna(thresh=data.shape[1]//2)

if 'winner' in data.columns:
    data['winner'] = data['winner'].fillna("No Result")

if 'city' in data.columns:
    data['city'] = data["city"].fillna(method='ffill')

if 'player_of_match' in data.columns:
    data['player_of_match'] = data["player_of_match"].fillna("Unknown")

data = data.drop_duplicates()

if 'date' in data.columns:
    data['date'] = pd.to_datetime(data["date"], errors='coerce')

if 'date' in data.columns:
    data['Match_year'] = data['date'].dt.year

if 'winner' in data.columns:
    top_teams = data['winner'].value_counts().head(5)

print("Top 5 Winning Teams:")
print(top_teams)

top_teams.plot(kind='bar', color='skyblue')
plt.title("Top 5 IPL Teams by Wins")
plt.xlabel("Team")
plt.ylabel("Wins")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

numeric_data = data.select_dtypes(include=[np.number])
if not numeric_data.empty:
    corr = numeric_data.corr()

sns.heatmap(data= corr, annot=True, cmap="coolwarm")
plt.title('Correlation Matrix (Numeric Columns)')
plt.show()

if 'team1' in data.columns:
    le = LabelEncoder()
    data['team1_encoded'] = le.fit_transform(data['team1'])
    data['team2_encoded'] = le.fit_transform(data['team2'])

print("Summary Statistics:")
print(data.describe(include='all'))

data.to_csv("Cleaned_ipl_dataset.csv", index=False)
print("\nCleaned IPL Dataset saved to 'Cleaned_ipl_dataset.csv'")
