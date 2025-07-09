import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Title
st.set_page_config(page_title="Netflix Dashboard", layout="wide")
st.title("Netflix Data Visualization Dashboard")

# Sidebar - File Uploader
st.sidebar.header("Upload Dataset")
uploaded_file = st.sidebar.file_uploader("Upload CSV file", type=["csv"])

# Load Data
@st.cache_data
def load_data(file):
    df = pd.read_csv(file)
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
    df.drop_duplicates(inplace=True)
    return df

if uploaded_file:
    df = load_data(uploaded_file)
else:
    df = load_data("netflix_titles.csv")

# Sidebar Filters
st.sidebar.header("Filters")
type_filter = st.sidebar.multiselect("Select Type", df["type"].unique(), default=df["type"].unique())
country_filter = st.sidebar.multiselect("Select Country", df["country"].dropna().unique()[:20], default=None)
year_range = st.sidebar.slider("Select Release Year", int(df["release_year"].min()), int(df["release_year"].max()), (2010, 2020))

filtered_df = df[
    (df["type"].isin(type_filter)) &
    (df["release_year"].between(year_range[0], year_range[1])) &
    ((df["country"].isin(country_filter)) if country_filter else True)
]

st.subheader(f"Dataset Overview ({len(filtered_df)} records)")
st.dataframe(filtered_df)

# Metrics
st.markdown("Summary Statistics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Titles", len(filtered_df))
col2.metric("Average Release Year", int(filtered_df["release_year"].mean()))
col3.metric("Median Release Year", int(filtered_df["release_year"].median()))

# Visualizations
st.markdown("Visualizations")

# 1. Bar Chart - Count by Type
st.subheader("Content Type Distribution")
type_count = filtered_df["type"].value_counts()
st.bar_chart(type_count)

# 2. Line Chart - Release Trend
st.subheader("Titles Released Over Years")
release_trend = filtered_df.groupby("release_year").size()
st.line_chart(release_trend)

# 3. Pie Chart - Top Countries
st.subheader("Top 5 Producing Countries")
top_countries = filtered_df["country"].value_counts().nlargest(5)
fig1, ax1 = plt.subplots()
ax1.pie(top_countries, labels=top_countries.index, autopct="%1.1f%%", startangle=90)
ax1.axis("equal")
st.pyplot(fig1)

# Download CSV
st.markdown("Download Filtered Data")
csv = filtered_df.to_csv(index=False)
st.download_button("Download CSV", data=csv, file_name="filtered_netflix_data.csv", mime="text/csv")

st.success("Dashboard Ready")
