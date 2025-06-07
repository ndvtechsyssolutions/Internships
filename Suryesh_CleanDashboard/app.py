# app.py

import streamlit as st
import pandas as pd

# -----------------------------------
# Page Configuration and Title
# -----------------------------------
st.set_page_config(page_title="COVID-19 Dashboard", layout="wide")
st.title("COVID-19 Data Visualization Dashboard")
st.markdown("Explore global COVID-19 statistics with interactive filters and visualizations.")

# -----------------------------------
# Load Dataset
# -----------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("data/covid_data.csv")
    df['date'] = pd.to_datetime(df['date'])  # Ensure date column is parsed
    return df

df = load_data()

# -----------------------------------
# Sidebar Filters
# -----------------------------------
st.sidebar.header("Filter the Data")

# Unique country list
country_list = df['location'].dropna().unique().tolist()
country_list.sort()

# Country selection
selected_country = st.sidebar.selectbox("Select a Country", country_list, index=country_list.index("India") if "India" in country_list else 0)

# Filter for selected country
country_df = df[df['location'] == selected_country]

# Date range slider based on selected country's data
min_date = country_df['date'].min()
max_date = country_df['date'].max()

selected_dates = st.sidebar.date_input("Select Date Range", [min_date, max_date], min_value=min_date, max_value=max_date)

if len(selected_dates) == 2:
    start_date, end_date = selected_dates
    country_df = country_df[
        (country_df['date'] >= pd.to_datetime(start_date)) &
        (country_df['date'] <= pd.to_datetime(end_date))
    ]

# -----------------------------------
# Show Filtered Data and Metrics
# -----------------------------------
st.subheader(f"Filtered Data for {selected_country}")
st.dataframe(country_df[['date', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths']].tail(10))

st.subheader("Key Metrics")
st.metric("Total Cases", f"{country_df['total_cases'].max():,.0f}")
st.metric("Total Deaths", f"{country_df['total_deaths'].max():,.0f}")
st.metric("New Cases (Latest)", f"{country_df['new_cases'].iloc[-1]:,.0f}")
st.metric("New Deaths (Latest)", f"{country_df['new_deaths'].iloc[-1]:,.0f}")

# -----------------------------------
# Raw Dataset (Optional)
# -----------------------------------
if st.checkbox("Show Raw Dataset"):
    st.write(df.head())

# -----------------------------------
# Full Dataset Summary Stats
# -----------------------------------
st.subheader("Summary Statistics")
st.write(df.describe(include='all'))


import matplotlib.pyplot as plt

# -----------------------------------
# Line Chart: Cases and Deaths Over Time
# -----------------------------------
st.subheader(f"Trend Over Time for {selected_country}")

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(country_df['date'], country_df['total_cases'], label='Total Cases', color='blue')
ax.plot(country_df['date'], country_df['total_deaths'], label='Total Deaths', color='red')
ax.set_xlabel("Date")
ax.set_ylabel("Count")
ax.set_title("Total Cases vs Total Deaths Over Time")
ax.legend()
st.pyplot(fig)

# -----------------------------------
# Bar Chart: Total Metrics Comparison
# -----------------------------------
st.subheader(f"Total Comparison for {selected_country}")

bar_data = {
    "Metric": ["Total Cases", "Total Deaths", "New Cases", "New Deaths"],
    "Value": [
        country_df['total_cases'].max(),
        country_df['total_deaths'].max(),
        country_df['new_cases'].iloc[-1],
        country_df['new_deaths'].iloc[-1]
    ]
}
bar_df = pd.DataFrame(bar_data)

st.bar_chart(bar_df.set_index("Metric"))

# -----------------------------------
# Pie Chart: Latest Case Distribution
# -----------------------------------
st.subheader(f"Latest Daily Distribution for {selected_country}")

# Get last valid row (not NaN) from country_df
latest_valid_row = country_df[['new_cases', 'new_deaths']].dropna().tail(1)

# If valid row exists, plot pie
if not latest_valid_row.empty:
    latest_values = {
        "New Cases": latest_valid_row['new_cases'].values[0],
        "New Deaths": latest_valid_row['new_deaths'].values[0]
    }
    fig2, ax2 = plt.subplots()
    ax2.pie(latest_values.values(), labels=latest_values.keys(), autopct='%1.1f%%', startangle=90, colors=["skyblue", "lightcoral"])
    ax2.axis("equal")
    st.pyplot(fig2)
else:
    st.warning("Not enough data to show pie chart for latest values.")
