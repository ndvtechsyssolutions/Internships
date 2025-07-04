import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

st.set_page_config(page_title="COVID-19 Dashboard", layout="wide")

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv(r'C:\RISHIKA_S_ASSIGNMENT\Code_By_RishikaS_DataVisualization_Streamlit\covid_19_clean_complete.csv', parse_dates=['Date'])
    df['Country/Region'] = df['Country/Region'].astype(str)
    return df

df = load_data()

# Sidebar Filters with background color and padding
st.sidebar.markdown(
    """
    <style>
    /* Sidebar background and padding */
    .css-1d391kg {
        background-color: #f7f9fc !important;
        padding: 1rem 1rem 2rem 1rem;
        border-radius: 8px;
    }
    /* Sidebar title color */
    .css-1d391kg h2, .css-1d391kg h3 {
        color: #333333;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.sidebar.title("Filters")
country = st.sidebar.selectbox("Select Country", sorted(df['Country/Region'].unique()))
start_date = st.sidebar.date_input("Start Date", df['Date'].min())
end_date = st.sidebar.date_input("End Date", df['Date'].max())

# Filtered Data
filtered_df = df[(df['Country/Region'] == country) & 
                 (df['Date'] >= pd.to_datetime(start_date)) &
                 (df['Date'] <= pd.to_datetime(end_date))]

# Main Layout
st.title(f"COVID-19 Dashboard - {country}")
st.markdown("### Overview")
col1, col2, col3 = st.columns(3)

# Colored Metrics
with col1:
    st.metric("Total Confirmed", int(filtered_df['Confirmed'].max()))
    st.markdown("<div style='color:orange; font-weight:bold;'>Confirmed cases in orange</div>", unsafe_allow_html=True)
with col2:
    st.metric("Total Deaths", int(filtered_df['Deaths'].max()))
    st.markdown("<div style='color:red; font-weight:bold;'>Deaths in red</div>", unsafe_allow_html=True)
with col3:
    st.metric("Total Recovered", int(filtered_df['Recovered'].max()))
    st.markdown("<div style='color:green; font-weight:bold;'>Recovered in green</div>", unsafe_allow_html=True)

# Line Chart with colors
st.markdown("### Trend Over Time")
fig = px.line(
    filtered_df, 
    x='Date', 
    y=['Confirmed', 'Deaths', 'Recovered'], 
    labels={"value": "Count", "variable": "Metric"},
    color_discrete_map={
        'Confirmed': 'orange',
        'Deaths': 'red',
        'Recovered': 'green'
    }
)
st.plotly_chart(fig, use_container_width=True)

# Bar Chart with color
st.markdown("### Daily Change (Bar Chart)")
daily_df = filtered_df.copy()
daily_df['New Confirmed'] = daily_df['Confirmed'].diff().fillna(0)
fig2 = px.bar(
    daily_df, 
    x='Date', 
    y='New Confirmed', 
    labels={"New Confirmed": "New Cases"},
    color_discrete_sequence=['orange']
)
st.plotly_chart(fig2, use_container_width=True)

# Pie Chart with matching colors
st.markdown("### Current Proportion (Pie Chart)")
latest = filtered_df.iloc[-1]
pie_data = pd.Series({
    'Confirmed': latest['Confirmed'],
    'Deaths': latest['Deaths'],
    'Recovered': latest['Recovered']
})
colors = ['orange', 'red', 'green']
fig3, ax = plt.subplots()
ax.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%', startangle=90, colors=colors, textprops={'color':"w"})
ax.axis('equal')
st.pyplot(fig3)

# Summary Stats
st.markdown("### Summary Statistics")
st.write(filtered_df[['Confirmed', 'Deaths', 'Recovered']].describe())

# Upload Your Own CSV
st.sidebar.markdown("### Upload Your Own CSV")
uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    user_df = pd.read_csv(uploaded_file)
    st.write("Preview of uploaded file:")
    st.dataframe(user_df.head())

# Bonus: Download Filtered Data
@st.cache_data
def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')

csv = convert_df(filtered_df)
st.download_button("Download Filtered Data as CSV", csv, "filtered_data.csv", "text/csv")
