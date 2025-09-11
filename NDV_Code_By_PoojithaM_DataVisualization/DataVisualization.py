import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to calculate statistics
def calculate_statistics(df):
    statistics = df.describe()
    return statistics

# Function to plot bar chart
def plot_bar_chart(df, column):
    fig, ax = plt.subplots()
    sns.countplot(x=column, data=df, ax=ax)
    ax.set_title(f"Bar Chart of {column}")
    ax.set_xlabel(column)
    ax.set_ylabel("Count")
    return fig

# Function to plot pie chart
def plot_pie_chart(df, column):
    fig, ax = plt.subplots()
    df[column].value_counts().plot(kind='pie', ax=ax, autopct='%1.1f%%')
    ax.set_title(f"Pie Chart of {column}")
    return fig

# Function to plot line chart
def plot_line_chart(df, column):
    fig, ax = plt.subplots()
    df[column].value_counts().plot(kind='line', ax=ax)
    ax.set_title(f"Line Chart of {column}")
    ax.set_xlabel(column)
    ax.set_ylabel("Count")
    return fig

# Streamlit app
st.title("IPL Data Visualization Dashboard")

# Upload CSV file
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)

    # Display the dataset
    st.header("Dataset")
    st.write(df)

    # Calculate statistics
    st.header("Statistics")
    statistics = calculate_statistics(df)
    st.write(statistics)

    # Plot charts
    st.header("Visualizations")
    columns = df.columns
    for column in columns:
        if df[column].dtype == 'object':
            st.subheader(f"Visualizations for {column}")
            col1, col2, col3 = st.columns(3)
            with col1:
                fig = plot_bar_chart(df, column)
                st.pyplot(fig)
            with col2:
                fig = plot_pie_chart(df, column)
                st.pyplot(fig)
            with col3:
                fig = plot_line_chart(df, column)
                st.pyplot(fig)

    # Download CSV file
    st.header("Download CSV File")
    st.download_button(label="Download CSV", data=df.to_csv().encode('utf-8'), file_name='ipl_data.csv', mime='text/csv')

else:
    # IPL dataset
    ipl_data = {
        "S.NO": [1, 2, 3, 4, 5],
        "YEAR": [2008, 2009, 2010, 2011, 2012],
        "IPL RUNNERS-UP": ["Chennai Super Kings", "Royal Challengers Bangalore", "Mumbai Indians", "Mumbai Indians", "Chennai Super Kings"],
        "IPL WINNER": ["Rajasthan Royals", "Deccan Chargers", "Chennai Super Kings", "Chennai Super Kings", "Kolkata Knight Riders"],
        "FINAL VENUE": ["Dy Patil Stadium", "M. Chinnaswamy Stadium", "M. A. Chidambaram Stadium", "M. A. Chidambaram Stadium", "M. A. Chidambaram Stadium"]
    }

    # Create a DataFrame
    df = pd.DataFrame(ipl_data)

    # Display the dataset
    st.header("Dataset")
    st.write(df)

    # Calculate statistics
    st.header("Statistics")
    statistics = calculate_statistics(df)
    st.write(statistics)

    # Plot charts
    st.header("Visualizations")
    columns = df.columns
    for column in columns:
        if df[column].dtype == 'object':
            st.subheader(f"Visualizations for {column}")
            col1, col2, col3 = st.columns(3)
            with col1:
                fig = plot_bar_chart(df, column)
                st.pyplot(fig)
            with col2:
                fig = plot_pie_chart(df, column)
                st.pyplot(fig)
            with col3:
                fig = plot_line_chart(df, column)
                st.pyplot(fig)

    # Download CSV file
    st.header("Download CSV File")
    st.download_button(label="Download CSV", data=df.to_csv().encode('utf-8'), file_name='ipl_data.csv', mime='text/csv')
