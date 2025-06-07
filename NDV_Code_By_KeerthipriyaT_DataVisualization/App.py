import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Title and description
st.title("IPL Data Visualization Dashboard")
st.markdown("Explore IPL match data using different filters and charts.")

# File uploader
uploaded_file = st.file_uploader("Upload your IPL dataset CSV", type=["csv"])

# Load default or uploaded dataset
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv("https://raw.githubusercontent.com/insaid2018/Data-sets/master/IPL%20Matches/matches.csv")

# Basic cleaning
df.columns = df.columns.str.strip()
df.dropna(inplace=True)

# Sidebar filters
st.sidebar.header("Filter Options")
teams = sorted(df['team1'].unique())
selected_team = st.sidebar.selectbox("Select Team", teams)
chart_type = st.sidebar.radio("Chart Type", ['Bar Chart', 'Pie Chart', 'Line Chart'])
show_stats = st.sidebar.checkbox("Show Summary Statistics", True)

# Filter data
filtered_df = df[df['team1'] == selected_team]

# Display statistics
if show_stats:
    st.subheader("Summary Statistics")
    st.write(filtered_df.describe(include='all'))

# Charts
st.subheader("Visualization")

if chart_type == 'Bar Chart':
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.countplot(data=filtered_df, x='winner', ax=ax)
    ax.set_title(f'Wins when {selected_team} was Team1')
    plt.xticks(rotation=45)
    st.pyplot(fig)

elif chart_type == 'Pie Chart':
    fig, ax = plt.subplots(figsize=(6, 6))
    filtered_df['winner'].value_counts().plot.pie(autopct='%1.1f%%', ax=ax)
    ax.set_ylabel('')
    ax.set_title(f'Win Distribution (Team1 = {selected_team})')
    st.pyplot(fig)

elif chart_type == 'Line Chart':
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
        temp_df = filtered_df.groupby('date').size().reset_index(name='Match Count')
        fig = px.line(temp_df, x='date', y='Match Count', title=f'Matches Over Time - {selected_team}')
        st.plotly_chart(fig)
    else:
        st.error("Date column not found in dataset.")

# Export filtered data
if st.sidebar.button("Export Filtered Data"):
    filtered_df.to_csv(f"{selected_team}_filtered.csv", index=False)
    st.success(f"Data exported as {selected_team}_filtered.csv")

