import pandas as pd
import plotly.express as px
from collections import Counter

# loading ipl dataset
df = pd.read_csv("/content/drive/MyDrive/Data/ipl_matches.csv")

# preprocessing: drop nulls for clarity
df['season'] = df['season'].astype(str)
df['winner'] = df['winner'].fillna('No Result')
df['player_of_match'] = df['player_of_match'].fillna('Unknown')
df['city'] = df['city'].fillna('Unknown')

# plot 1: matches per season
season_count = df['season'].value_counts().sort_index()
fig1 = px.bar(x=season_count.index, y=season_count.values,
              labels={'x': 'Season', 'y': 'Number of Matches'},
              title='Total Matches Played per Season',
              color=season_count.values, color_continuous_scale='teal')
fig1.show()

# plot 2: most matches won by teams
wins = df['winner'].value_counts().head(10)
fig2 = px.bar(x=wins.values, y=wins.index,
              orientation='h',
              labels={'x': 'Wins', 'y': 'Team'},
              title='Top 10 Most Successful Teams',
              color=wins.values, color_continuous_scale='aggrnyl')
fig2.show()

# plot 3: toss winner vs match winner (same team)
df['toss_match_win'] = df['toss_winner'] == df['winner']
match_winner_same = df['toss_match_win'].value_counts()
labels = ['Different Teams', 'Same Team']
fig3 = px.pie(values=match_winner_same.values, names=labels,
              title='Did Toss Winner Also Win the Match?',
              color_discrete_sequence=px.colors.sequential.RdBu)
fig3.show()

# plot 4: top 10 players of the match
top_players = df['player_of_match'].value_counts().head(10)
fig4 = px.bar(x=top_players.values, y=top_players.index,
              orientation='h',
              labels={'x': 'Awards', 'y': 'Player'},
              title='Top 10 Players of the Match',
              color=top_players.values, color_continuous_scale='inferno')
fig4.show()

# plot 5: most common venues
top_venues = df['venue'].value_counts().head(10)
fig5 = px.bar(x=top_venues.values, y=top_venues.index,
              orientation='h',
              title='Top 10 IPL Venues',
              labels={'x': 'Matches Hosted', 'y': 'Venue'},
              color=top_venues.values, color_continuous_scale='purples')
fig5.show()
