import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pydeck as pdk

st.set_page_config(layout="wide")
st.title("📈 Smart Data Explorer")
st.markdown("Upload any dataset to visualize key patterns, trends, and stats.")

# Upload file
file = st.sidebar.file_uploader("📁 Upload CSV File", type=["csv"])
if file:
    df = pd.read_csv(file)
    st.success("File uploaded successfully.")
else:
    st.warning("Please upload a CSV file to continue.")
    st.stop()

# Show raw data
with st.expander("🔍 Preview Data"):
    st.dataframe(df.head())

# Auto-detect columns
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
categorical_cols = df.select_dtypes(include='object').columns.tolist()

date_col = next((col for col in df.columns if 'date' in col.lower()), None)
lat_col = next((col for col in df.columns if 'lat' in col.lower()), None)
lon_col = next((col for col in df.columns if 'lon' in col.lower()), None)

# Filters (for categorical columns)
if categorical_cols:
    filter_col = st.sidebar.selectbox("🔘 Filter by Categorical Column", categorical_cols)
    filter_vals = df[filter_col].dropna().unique()
    selected_vals = st.sidebar.multiselect(f"Select values from {filter_col}", filter_vals)
    if selected_vals:
        df = df[df[filter_col].isin(selected_vals)]

# Summary
st.header("📊 Summary Statistics")
st.write(df.describe(include='all'))

# Bar Chart
if categorical_cols:
    st.subheader("🟦 Bar Chart")
    bar_col = st.selectbox("Select Categorical Column", categorical_cols)
    st.bar_chart(df[bar_col].value_counts().head(10))

# Line Chart
if date_col and numeric_cols:
    st.subheader("📈 Line Chart")
    line_y = st.selectbox("Select Numeric Column", numeric_cols, key="line")
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
    time_data = df.groupby(df[date_col].dt.date)[line_y].sum()
    st.line_chart(time_data)

# Pie Chart
if categorical_cols:
    st.subheader("🥧 Pie Chart")
    pie_col = st.selectbox("Select Categorical Column for Pie", categorical_cols, key="pie")
    pie_data = df[pie_col].value_counts().head(5)
    fig, ax = plt.subplots()
    ax.pie(pie_data, labels=pie_data.index, autopct="%1.1f%%", startangle=90)
    ax.axis("equal")
    st.pyplot(fig)

# Map (if lat/lon available)
if lat_col and lon_col:
    st.subheader("🗺️ Map Visualization")
    st.map(df[[lat_col, lon_col]].dropna())

# Download option
st.download_button("💾 Download Data", df.to_csv(index=False), "filtered_data.csv")
