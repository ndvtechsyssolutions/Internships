# IPL Dataset Preprocessing using Pandas and NumPy
# Author: Praveen Yadav
# Date: 27/05/2025
# Description: Clean and preprocess IPL datasets (matches & deliveries)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
matches = pd.read_csv("ipl/matches.csv")
deliveries = pd.read_csv("ipl/deliveries.csv")

# ----------------- Data Inspection ------------------
print("Matches Dataset Info:")
print(matches.info())
print("\nDeliveries Dataset Info:")
print(deliveries.info())

# ----------------- Handling Missing Values ------------------

# Visualize missing values in matches dataset
plt.figure(figsize=(12, 6))
sns.heatmap(matches.isnull(), cbar=False, cmap='magma')
plt.title("Missing Values Heatmap - Matches")
plt.show()

# Visualize missing values in deliveries dataset
plt.figure(figsize=(12, 6))
sns.heatmap(deliveries.isnull(), cbar=False, cmap='magma')
plt.title("Missing Values Heatmap - Deliveries")
plt.show()

# Fill or drop missing values (matches)
matches['city'].fillna("Unknown", inplace=True)
matches['player_of_match'].fillna("Unknown", inplace=True)
matches['winner'].fillna("No Result", inplace=True)
matches['result_margin'].fillna(0, inplace=True)
matches['target_runs'].fillna(0, inplace=True)
matches['target_overs'].fillna(0, inplace=True)
matches.drop(columns=['method'], inplace=True)  # Too many missing

# Fill or drop missing values (deliveries)
deliveries['extras_type'].fillna("None", inplace=True)
deliveries['player_dismissed'].fillna("None", inplace=True)
deliveries['dismissal_kind'].fillna("None", inplace=True)
deliveries['fielder'].fillna("None", inplace=True)

# ----------------- Remove Duplicates ------------------
matches.drop_duplicates(inplace=True)
deliveries.drop_duplicates(inplace=True)

# ----------------- Convert Data Types ------------------
matches['date'] = pd.to_datetime(matches['date'])

# ----------------- NumPy Transformations ------------------
# Normalize result_margin for numerical insights
matches['result_margin_zscore'] = (
    matches['result_margin'] - np.mean(matches['result_margin'])
) / np.std(matches['result_margin'])

# ----------------- Filter, Sort, Group ------------------
# Example: Top 5 players of the match
top_players = matches['player_of_match'].value_counts().head()
print("\nTop 5 Player of the Match Winners:\n", top_players)

# Example: Total runs scored by each team
team_runs = deliveries.groupby('batting_team')['total_runs'].sum().sort_values(ascending=False)
print("\nTotal Runs by Team:\n", team_runs)

# ----------------- Summary Statistics ------------------
print("\nMatches Summary:\n", matches.describe(include='all'))
print("\nDeliveries Summary:\n", deliveries.describe())

# ----------------- Correlation Matrix ------------------
plt.figure(figsize=(10, 8))
sns.heatmap(matches.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix - Matches")
plt.show()

# ----------------- Label Encoding (Optional ML Prep) ------------------
from sklearn.preprocessing import LabelEncoder
label_enc_cols = ['city', 'venue', 'team1', 'team2', 'toss_winner', 'winner']
encoder = LabelEncoder()
for col in label_enc_cols:
    matches[col] = encoder.fit_transform(matches[col])

# ----------------- Save Cleaned Data ------------------
matches.to_csv("cleaned_matches.csv", index=False)
deliveries.to_csv("cleaned_deliveries.csv", index=False)
