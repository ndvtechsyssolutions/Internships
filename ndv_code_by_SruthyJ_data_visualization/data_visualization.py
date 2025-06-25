import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("clean_test.csv")


st.title("COVID-19 Interactive Dashboard")
st.markdown("An interactive dashboard to explore COVID-19 and demographic data")


st.sidebar.header("Filter Options")
countries = df['Country_Region'].unique()
selected_country = st.sidebar.selectbox("Select a Country", sorted(countries))

show_density = st.sidebar.checkbox("Show Population Density Distribution")
show_temp_humidity = st.sidebar.checkbox("Show Temperature vs Humidity")
show_days_dist = st.sidebar.checkbox("Show Days from First Case Histogram")


filtered_df = df[df['Country_Region'] == selected_country]


st.subheader(f"Summary Statistics for {selected_country}")
st.write(filtered_df.describe()[['density', 'avgtemp', 'avghumidity']])


st.subheader("Line Chart: Average Temperature Over Time")
line_data = filtered_df[['Date', 'avgtemp']].copy()
line_data['Date'] = pd.to_datetime(line_data['Date'])
line_data = line_data.sort_values('Date')
st.line_chart(line_data.set_index('Date'))

st.subheader("Pie Chart: Approximate Gender Distribution")
male_ratio = filtered_df['sexratio'].mean() / (1 + filtered_df['sexratio'].mean())
female_ratio = 1 - male_ratio
fig_pie, ax_pie = plt.subplots()
ax_pie.pie([male_ratio, female_ratio], labels=["Male", "Female"],
           autopct='%1.1f%%', colors=["lightblue", "pink"])
st.pyplot(fig_pie)
plt.clf()

if show_density:
    st.subheader("Bar Chart: Population Density Distribution")
    fig1, ax1 = plt.subplots()
    sns.histplot(filtered_df['density'], bins=20, ax=ax1, color="green")
    st.pyplot(fig1)
    plt.clf()

if show_temp_humidity:
    st.subheader("Scatter Plot: Temperature vs Humidity")
    fig2, ax2 = plt.subplots()
    sns.scatterplot(data=filtered_df, x='avgtemp', y='avghumidity', ax=ax2)
    st.pyplot(fig2)
    plt.clf()

if show_days_dist:
    st.subheader("Histogram: Days from First Case")
    fig3, ax3 = plt.subplots()
    sns.histplot(filtered_df['days_from_firstcase'], bins=30, ax=ax3, color="orange")
    st.pyplot(fig3)
    plt.clf()

st.markdown("---")
st.markdown("Dashboard created using *Streamlit* and *Seaborn*")
