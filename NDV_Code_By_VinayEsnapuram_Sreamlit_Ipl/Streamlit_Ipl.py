
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="IPL Dashboard", layout="wide")


st.title("🏏 IPL Matches Dashboard")


st.sidebar.header("Upload Your CSV")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv("matches.csv")


df['date'] = pd.to_datetime(df['date'], errors='coerce')
df['season'] = df['season'].astype(str)
df['winner'].fillna("No Result", inplace=True)

st.sidebar.header("Filter Options")

season = st.sidebar.selectbox("Select Season", options=df['season'].unique())
team = st.sidebar.selectbox("Select Team", options=sorted(df['team1'].unique()))

filtered_df = df[(df['season'] == season) & ((df['team1'] == team) | (df['team2'] == team))]


st.subheader(f"Summary Statistics for {team} in {season}")
numeric_cols = ['win_by_runs', 'win_by_wickets']


missing_cols = [col for col in numeric_cols if col not in filtered_df.columns]

if missing_cols:
    st.warning(f"Missing columns in dataset: {', '.join(missing_cols)}")
else:
    st.write(filtered_df[numeric_cols].describe())



st.subheader("1️⃣ Total Matches per Season")
season_counts = df['season'].value_counts().sort_index()
st.bar_chart(season_counts)

st.subheader(f"2️⃣ Matches Played by {team} Over Time")
team_df = df[(df['team1'] == team) | (df['team2'] == team)]
team_trend = team_df.groupby(team_df['date'].dt.year).size()
st.line_chart(team_trend)

st.subheader("3️⃣ Toss Decisions")
toss_counts = df['toss_decision'].value_counts()
fig1, ax1 = plt.subplots()
ax1.pie(toss_counts, labels=toss_counts.index, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')
st.pyplot(fig1)


st.sidebar.markdown("### Download Filtered Data")
csv = filtered_df.to_csv(index=False).encode('utf-8')
st.sidebar.download_button("Download CSV", csv, "filtered_data.csv", "text/csv")

