import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO

# Streamlit page settings
st.set_page_config(page_title="Data Visualization Dashboard", layout="wide")

# Title
st.title("📊 Data Visualization Dashboard")
st.markdown("Explore datasets using filters, visualizations, and summary statistics.")

# Sidebar
st.sidebar.header("Upload & Filter Data")

# File uploader
uploaded_file = st.sidebar.file_uploader("Upload your CSV file", type=["csv"])

# Load dataset: either uploaded or default
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("✅ CSV file successfully loaded.")
else:
    try:
        df = pd.read_csv("sample_data.csv")
        st.info("Using default dataset: sample_data.csv")
    except FileNotFoundError:
        st.error("⚠ No CSV file uploaded and default sample_data.csv not found. Please upload a CSV file.")
        st.stop()

# Show data preview
if st.checkbox("Show raw data"):
    st.write(df.head())

# Select numeric column for analysis
numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
if numeric_cols:
    selected_column = st.sidebar.selectbox("Select numeric column for analysis", numeric_cols)
else:
    st.warning("No numeric columns found in dataset.")
    st.stop()

# Sidebar filter slider
min_val = int(df[selected_column].min())
max_val = int(df[selected_column].max())
value_range = st.sidebar.slider(f"Filter {selected_column} range", min_val, max_val, (min_val, max_val))
df_filtered = df[(df[selected_column] >= value_range[0]) & (df[selected_column] <= value_range[1])]

# Summary statistics
st.subheader(f"Summary statistics for '{selected_column}' (Filtered Data)")
st.write(df_filtered[selected_column].describe())

# --- VISUALIZATIONS ---
st.subheader("Visualizations")

# 1. Histogram
st.write("### Histogram")
fig1, ax1 = plt.subplots()
sns.histplot(df_filtered[selected_column], bins=20, kde=True, ax=ax1)
st.pyplot(fig1)

# 2. Boxplot
st.write("### Boxplot")
fig2, ax2 = plt.subplots()
sns.boxplot(x=df_filtered[selected_column], ax=ax2)
st.pyplot(fig2)

# 3. Line chart
st.write("### Line Chart")
st.line_chart(df_filtered[selected_column])

# --- OPTIONAL PIE CHART if categorical columns exist ---
categorical_cols = df.select_dtypes(include='object').columns.tolist()
if categorical_cols:
    selected_cat_col = st.sidebar.selectbox("Select categorical column for Pie Chart", categorical_cols)
    st.write("### Pie Chart")
    pie_data = df[selected_cat_col].value_counts()
    fig3, ax3 = plt.subplots()
    ax3.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%', startangle=90)
    ax3.axis('equal')
    st.pyplot(fig3)

# --- DOWNLOAD FILTERED DATA ---
csv = df_filtered.to_csv(index=False).encode('utf-8')
st.download_button(
    label="📥 Download filtered data as CSV",
    data=csv,
    file_name="filtered_data.csv",
    mime='text/csv'
)

# Footer
st.write("---")
st.caption("Built with ❤ using Streamlit - Interactive Dashboard Assignment")