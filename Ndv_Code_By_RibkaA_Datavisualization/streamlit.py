import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Set page config
st.set_page_config(page_title="Data Visualization Dashboard", layout="wide")

# Title
st.title("📊 Data Visualization Dashboard")
st.markdown("Explore your dataset with filters and visualizations.")

# File uploader
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

# Use sample dataset if no file uploaded
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    df = sns.load_dataset("iris")

# Show data
st.subheader("Dataset Preview")
st.dataframe(df)

# Filter columns
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
cat_cols = df.select_dtypes(include=['object']).columns

# Sidebar Filters
st.sidebar.header("🔎 Filter Options")
selected_col = st.sidebar.selectbox("Choose column to visualize", df.columns)

# Summary Statistics
st.subheader("📈 Summary Statistics")
st.write(df.describe())

# Visualizations
st.subheader("📊 Visualizations")

chart_type = st.selectbox("Select Chart Type", ["Bar Chart", "Line Chart", "Pie Chart", "Histogram", "Box Plot"])

if chart_type == "Bar Chart":
    fig = px.bar(df, x=selected_col)
    st.plotly_chart(fig, use_container_width=True)

elif chart_type == "Line Chart":
    fig = px.line(df, x=df.index, y=selected_col)
    st.plotly_chart(fig, use_container_width=True)

elif chart_type == "Pie Chart":
    if df[selected_col].nunique() < 10:
        pie_data = df[selected_col].value_counts().reset_index()
        pie_data.columns = [selected_col, 'count']
        fig = px.pie(pie_data, values='count', names=selected_col)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Too many unique values for pie chart.")

elif chart_type == "Histogram":
    fig = px.histogram(df, x=selected_col)
    st.plotly_chart(fig, use_container_width=True)

elif chart_type == "Box Plot":
    fig = px.box(df, y=selected_col)
    st.plotly_chart(fig, use_container_width=True)

# Download filtered data
st.sidebar.download_button("Download CSV", df.to_csv(index=False), file_name="filtered_data.csv")

# Footer
st.markdown("---")
st.markdown("✅ Created using **Streamlit**")

