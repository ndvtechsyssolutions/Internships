import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("clean_test.csv")
df['Date'] = pd.to_datetime(df['Date'])  # Ensure Date column is datetime

# Title and description
st.title("COVID-19 Interactive Dashboard")
st.markdown("An interactive dashboard to explore COVID-19 and demographic data")

# Sidebar filters
st.sidebar.header("Filter Options")
countries = df['Country_Region'].unique()
selected_country = st.sidebar.selectbox("Select a Country", sorted(countries))

# Date filter
min_date = df['Date'].min()
max_date = df['Date'].max()
start_date, end_date = st.sidebar.date_input("Select Date Range", [min_date, max_date], min_value=min_date, max_value=max_date)

# Optional plots
show_density = st.sidebar.checkbox("Show Population Density Distribution")
show_temp_humidity = st.sidebar.checkbox("Show Temperature vs Humidity")
show_days_dist = st.sidebar.checkbox("Show Days from First Case Histogram")

# Filter dataset
filtered_df = df[(df['Country_Region'] == selected_country) &
                 (df['Date'] >= pd.to_datetime(start_date)) &
                 (df['Date'] <= pd.to_datetime(end_date))]

# Optional: raw data preview
if st.checkbox("Show raw data"):
    st.write(filtered_df.head())

# Warn if data has missing values
if filtered_df.isnull().values.any():
    st.warning("Some values are missing in the selected data.")

# Summary stats
st.subheader(f"Summary Statistics for {selected_country}")
st.write(filtered_df.describe()[['density', 'avgtemp', 'avghumidity']])

# Line chart
st.subheader("Line Chart: Average Temperature Over Time")
line_data = filtered_df[['Date', 'avgtemp']].sort_values('Date')
st.line_chart(line_data.set_index('Date'))

# Pie chart
st.subheader("Pie Chart: Approximate Gender Distribution")
sex_ratio = filtered_df['sexratio'].mean()
male_ratio = sex_ratio / (1 + sex_ratio)
female_ratio = 1 - male_ratio
fig_pie, ax_pie = plt.subplots()
ax_pie.pie([male_ratio, female_ratio], labels=["Male", "Female"],
           autopct='%1.1f%%', colors=["lightblue", "pink"])
st.pyplot(fig_pie)
plt.close(fig_pie)

# Optional plots
if show_density:
    st.subheader("Bar Chart: Population Density Distribution")
    fig1, ax1 = plt.subplots()
    sns.histplot(filtered_df['density'], bins=20, ax=ax1, color="green")
    st.pyplot(fig1)
    plt.close(fig1)

if show_temp_humidity:
    st.subheader("Scatter Plot: Temperature vs Humidity")
    fig2, ax2 = plt.subplots()
    sns.scatterplot(data=filtered_df, x='avgtemp', y='avghumidity', ax=ax2)
    st.pyplot(fig2)
    plt.close(fig2)

if show_days_dist:
    st.subheader("Histogram: Days from First Case")
    fig3, ax3 = plt.subplots()
    sns.histplot(filtered_df['days_from_firstcase'], bins=30, ax=ax3, color="orange")
    st.pyplot(fig3)
    plt.close(fig3)

# Footer
st.markdown("---")
st.markdown("Dashboard created using *Streamlit* and *Seaborn*")
