import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("📊 Interactive Data Visualization Dashboard")

# Upload CSV File
uploaded_file = st.sidebar.file_uploader("Upload your CSV file", type=["csv"])


if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("✅ File uploaded successfully.")
else:
    st.warning("⚠️ Please upload a CSV file to proceed.")
    st.stop()

# Show raw data (optional)
with st.expander("🔍 View Raw Data"):
    st.dataframe(df)

# Show available columns for reference
st.sidebar.markdown("### Available Columns")
st.sidebar.write(df.columns.tolist())

# Try to auto-detect useful columns
season_col = None
runs_col = None

for col in df.columns:
    if 'season' in col.lower():
        season_col = col
    if 'run' in col.lower() and df[col].dtype in ['int64', 'float64']:
        runs_col = col

# Filter: season dropdown (if found)
if season_col:
    seasons = df[season_col].dropna().unique()
    selected_seasons = st.sidebar.multiselect("Filter by Season", sorted(seasons))
    if selected_seasons:
        df = df[df[season_col].isin(selected_seasons)]

# 📈 Summary Statistics
st.header("📌 Summary Statistics")
st.write(df.describe(include='all'))

# 📊 Bar Chart - Count by Season
if season_col:
    st.header("📊 Bar Chart")
    st.subheader("Match Count by Season")
    st.bar_chart(df[season_col].value_counts().sort_index())

# 📈 Line Chart - Total Runs Over Time
if season_col and runs_col:
    st.header("📈 Line Chart")
    st.subheader(" Total Runs Over Seasons")
    df[season_col] = df[season_col].astype(str)
    df[runs_col] = pd.to_numeric(df[runs_col], errors='coerce')
    line_data = df.groupby(season_col)[runs_col].sum()
    st.line_chart(line_data)
else:
    st.info("ℹ️ Line chart could not be shown due to missing 'season' or 'runs' column.")

# 🥧 Pie Chart - Top Winners or any categorical column
categorical_cols = df.select_dtypes(include='object').columns.tolist()
if categorical_cols:
    pie_col = st.sidebar.selectbox("Select Column for Pie Chart", categorical_cols)
    st.subheader(f"🥧 Pie Chart - Distribution of {pie_col}")
    pie_data = df[pie_col].value_counts().head(5)
    fig, ax = plt.subplots()
    ax.pie(pie_data, labels=pie_data.index, autopct="%1.1f%%", startangle=90)
    ax.axis("equal")
    st.pyplot(fig)

# 💾 Download filtered data
st.download_button("💾 Download Filtered Data as CSV", df.to_csv(index=False), "filtered_data.csv")
