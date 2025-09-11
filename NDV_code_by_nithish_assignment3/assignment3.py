# app.py

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="IPL Deliveries Dashboard", layout="wide")

st.title(" IPL Deliveries Dashboard")
uploaded_file = st.file_uploader("Upload an IPL deliveries CSV file", type="csv")

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        st.success(" File uploaded successfully!")
    except Exception as e:
        st.error(f" Error reading uploaded file: {e}")
        st.stop()
else:
    try:
        df = pd.read_csv("deliveries.csv")  
        st.info("Using default file: deliveries.csv")
    except FileNotFoundError:
        st.error(" 'deliveries.csv' not found! Please upload a file to continue.")
        st.stop()
required_columns = ['batting_team', 'inning', 'total_runs', 'batsman_runs']
missing_columns = [col for col in required_columns if col not in df.columns]

if missing_columns:
    st.error(f" Missing required columns: {missing_columns}")
    st.stop()

st.sidebar.header(" Filters")

teams = sorted(df['batting_team'].dropna().unique())
selected_teams = st.sidebar.multiselect("Select Batting Team(s):", teams, default=teams[:2])
df = df[df['batting_team'].isin(selected_teams)]

innings = sorted(df['inning'].dropna().unique())
selected_innings = st.sidebar.multiselect("Select Inning(s):", innings, default=innings)
df = df[df['inning'].isin(selected_innings)]

st.subheader("Summary Statistics")
st.dataframe(df[['total_runs', 'batsman_runs', 'extra_runs']].describe(), use_container_width=True)

st.subheader("Visualizations")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🏏 Total Runs by Batting Team")
    team_runs = df.groupby('batting_team')['total_runs'].sum().sort_values(ascending=False)
    fig1 = px.bar(team_runs, x=team_runs.index, y=team_runs.values,
                  labels={'x': 'Team', 'y': 'Runs'}, text=team_runs.values)
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.markdown("###  Top 10 Batsmen (by Runs)")
    if 'batsman' in df.columns:
        top_batsmen = df.groupby('batsman')['batsman_runs'].sum().nlargest(10)
        fig2 = px.bar(top_batsmen, x=top_batsmen.index, y=top_batsmen.values,
                      labels={'x': 'Batsman', 'y': 'Runs'}, text=top_batsmen.values)
        st.plotly_chart(fig2, use_container_width=True)
    else:
        st.warning("⚠ 'batsman' column not found in data. Cannot show top batsmen.")

with col3:
    st.markdown("### ❌ Dismissal Types")
    if 'dismissal_kind' in df.columns and df['dismissal_kind'].notna().any():
        dismissal_counts = df['dismissal_kind'].value_counts()
        fig3 = px.pie(names=dismissal_counts.index, values=dismissal_counts.values,
                      title='Dismissal Types')
        st.plotly_chart(fig3, use_container_width=True)
    else:
        st.info("No dismissal data available.")

st.sidebar.markdown("---")
st.sidebar.download_button(
    label="⬇ Download Filtered Data",
    data=df.to_csv(index=False),
    file_name="filtered_ipl_data.csv",
    mime='text/csv'
)

st.markdown("---")
st.caption("🚀 Built with ❤ using Streamlit, Plotly & IPL Dataset")
