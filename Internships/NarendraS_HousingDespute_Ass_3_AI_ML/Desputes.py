import streamlit as st
import pandas as pd
import plotly.express as px
from io import StringIO

# Title
st.set_page_config(page_title="Landlord-Tenant Disputes Dashboard", layout="wide")
st.title("Landlord-Tenant Disputes Interactive Dashboard")
st.markdown("Explore housing dispute cases with filters, dynamic charts, and export options.")

# File uploader
uploaded_file = st.sidebar.file_uploader("Upload your own CSV file", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv("Housing_Landlord-Tenant_Disputes_20240525.csv")

# Data cleaning
df['Date Filed'] = pd.to_datetime(df['Date Filed'], errors='coerce')
df['Date Closed'] = pd.to_datetime(df['Date Closed'], errors='coerce')
df.dropna(subset=['City', 'Zip', 'Date Filed'], inplace=True)

# Sidebar filters
st.sidebar.header("Filters")
cities = st.sidebar.multiselect("Select Cities", df['City'].unique(), default=['ROCKVILLE', 'SILVER SPRING'])
case_types = st.sidebar.multiselect("Select Case Types", df['Case Type'].unique(), default=df['Case Type'].unique())
complaints = st.sidebar.multiselect("Complaint Type", df['Type of Complaint'].dropna().unique(), default=df['Type of Complaint'].dropna().unique())
date_range = st.sidebar.date_input("Date Filed Range", [df['Date Filed'].min(), df['Date Filed'].max()])

# Apply filters
filtered_df = df[
    (df['City'].isin(cities)) &
    (df['Case Type'].isin(case_types)) &
    (df['Type of Complaint'].isin(complaints)) &
    ((df['Date Filed'].between(pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1]))))
]

st.markdown(f"### Showing {len(filtered_df)} filtered cases")

# Summary statistics
st.subheader("Summary Statistics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Cases", len(filtered_df))
col2.metric("Mean Duration (days)", round((filtered_df['Date Closed'] - filtered_df['Date Filed']).dt.days.mean(), 2))
col3.metric("Unique Cities", filtered_df['City'].nunique())

# Charts
st.subheader("Visualizations")

tab1, tab2, tab3 = st.tabs(["Line Chart", "Bar Chart", "Pie Chart"])

with tab1:
    time_group = filtered_df.groupby('Date Filed').size().reset_index(name='Case Count')
    fig1 = px.line(time_group, x='Date Filed', y='Case Count', title='Cases Over Time')
    st.plotly_chart(fig1, use_container_width=True)

with tab2:
    bar_data = filtered_df.groupby('City').size().reset_index(name='Cases')
    fig2 = px.bar(bar_data, x='City', y='Cases', title='Cases by City')
    st.plotly_chart(fig2, use_container_width=True)

with tab3:
    pie_data = filtered_df['Type of Complaint'].value_counts().reset_index()
    pie_data.columns = ['Complaint Type', 'Count']
    fig3 = px.pie(pie_data, names='Complaint Type', values='Count', title='Distribution of Complaint Types')
    st.plotly_chart(fig3, use_container_width=True)

# Map (if coordinates exist)
if filtered_df['Location'].str.contains(r'\(([^)]+)\)').any():
    import re
    def extract_coords(loc):
        match = re.search(r'\(([^,]+), ([^)]+)\)', loc)
        return float(match.group(1)), float(match.group(2)) if match else (None, None)

    lat_lng = filtered_df['Location'].apply(extract_coords).dropna()
    latitudes = lat_lng.map(lambda x: x[0])
    longitudes = lat_lng.map(lambda x: x[1])
    map_df = pd.DataFrame({'lat': latitudes, 'lon': longitudes})
    st.map(map_df)

# Export data
csv = filtered_df.to_csv(index=False).encode('utf-8')
st.download_button("Download Filtered Data as CSV", csv, "filtered_cases.csv", "text/csv")

# Footer
st.markdown("---")
st.caption("Created with ❤️ using Streamlit. Dataset: Landlord-Tenant Disputes - 2024")

