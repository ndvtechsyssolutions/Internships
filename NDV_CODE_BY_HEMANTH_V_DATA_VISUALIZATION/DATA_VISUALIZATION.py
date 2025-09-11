# Install and import required libraries
!pip install --quiet ipywidgets

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import ipywidgets as widgets
from IPython.display import display, clear_output
import zipfile
import warnings
warnings.filterwarnings("ignore")

# Upload ZIP file
from google.colab import files
uploaded = files.upload()

# Extract ZIP
zip_file = list(uploaded.keys())[0]
with zipfile.ZipFile(zip_file, 'r') as zip_ref:
    zip_ref.extractall()
    files = zip_ref.namelist()
    print("Extracted files:", files)

# Load the match records CSV
df = pd.read_csv("each_match_records.csv")
df.columns = df.columns.str.strip().str.lower()  # Normalize column names

print("📋 Columns in dataset:", df.columns.tolist())

# We'll use team1 and team2 as team and opponent
if 'team1' not in df.columns or 'team2' not in df.columns:
    raise ValueError("Required columns 'team1' and 'team2' not found.")

teams = sorted(pd.concat([df['team1'], df['team2']]).dropna().unique())
metrics = ['winner_runs', 'winner_wickets']

team_dropdown = widgets.Dropdown(
    options=teams,
    description='Team:',
    value='India' if 'India' in teams else teams[0]
)

opponent_dropdown = widgets.Dropdown(
    options=teams,
    description='Opponent:',
    value='Australia' if 'Australia' in teams else teams[1]
)

metric_dropdown = widgets.Dropdown(
    options=metrics,
    description='Metric:',
    value='winner_runs'
)

chart_radio = widgets.RadioButtons(
    options=['Bar Chart', 'Pie Chart'],
    description='Chart:'
)

show_stats = widgets.Checkbox(
    value=True,
    description='Show Summary'
)

def update_dashboard(team, opponent, metric, chart_type, show_summary):
    clear_output(wait=True)
    display(team_dropdown, opponent_dropdown, metric_dropdown, chart_radio, show_stats)

    mask = (
        ((df['team1'] == team) & (df['team2'] == opponent)) |
        ((df['team1'] == opponent) & (df['team2'] == team))
    )
    filtered = df[mask]

    if filtered.empty:
        print("⚠️ No data for selected team vs opponent.")
        return

    if show_summary:
        print(f"\n📊 Summary for {team} vs {opponent} - {metric}")
        print(f"Mean: {filtered[metric].mean():.2f}")
        print(f"Median: {filtered[metric].median():.2f}")
        print(f"Total: {filtered[metric].sum():.2f}")

    if chart_type == 'Bar Chart':
        plt.figure(figsize=(10,5))
        sns.barplot(x=filtered['date'], y=filtered[metric], palette='Set2')
        plt.title(f"{metric} by Date: {team} vs {opponent}")
        plt.xticks(rotation=45)
        plt.ylabel(metric)
        plt.show()

    elif chart_type == 'Pie Chart':
        win_counts = filtered['winner'].value_counts()
        plt.figure(figsize=(6,6))
        plt.pie(win_counts, labels=win_counts.index, autopct='%1.1f%%', startangle=90)
        plt.title(f"Win Distribution: {team} vs {opponent}")
        plt.show()

widgets.interact(
    update_dashboard,
    team=team_dropdown,
    opponent=opponent_dropdown,
    metric=metric_dropdown,
    chart_type=chart_radio,
    show_summary=show_stats
)
