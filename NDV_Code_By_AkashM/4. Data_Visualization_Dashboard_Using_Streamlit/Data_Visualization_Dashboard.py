import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Netflix Data Explorer", layout="wide")

st.title("🍿 Netflix Dataset Interactive Dashboard")

uploaded_file = st.file_uploader("Upload your Netflix CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
    df['year_added'] = df['date_added'].dt.year
    df['duration'] = df['duration'].fillna('Unknown')

    st.sidebar.header("Filter Options")

    type_filter = st.sidebar.multiselect(
        "Select Content Type",
        options=df['type'].unique(),
        default=df['type'].unique()
    )

    country_filter = st.sidebar.multiselect(
        "Select Countries",
        options=df['country'].dropna().unique(),
        default=df['country'].dropna().unique()
    )

    year_min = int(df['year_added'].min()) if df['year_added'].notnull().any() else 2000
    year_max = int(df['year_added'].max()) if df['year_added'].notnull().any() else 2020

    year_range = st.sidebar.slider(
        "Year Added Range",
        min_value=year_min,
        max_value=year_max,
        value=(year_min, year_max)
    )

    show_summary = st.sidebar.checkbox("Show Summary Statistics")

    chart_style = st.sidebar.radio(
        "Chart Style",
        ["Default Colors", "Grayscale"]
    )

    filtered_df = df[
        (df['type'].isin(type_filter)) &
        (df['country'].isin(country_filter)) &
        (df['year_added'].between(year_range[0], year_range[1]))
    ]

    st.subheader("Filtered Data Preview")
    st.dataframe(filtered_df)

    if show_summary:
        st.subheader("Summary Statistics")
        st.write(filtered_df.describe(include='all'))

    st.subheader("Visualizations")

    fig1, ax1 = plt.subplots()
    counts = filtered_df['year_added'].value_counts().sort_index()
    if chart_style == "Grayscale":
        ax1.bar(counts.index, counts.values, color='gray')
    else:
        ax1.bar(counts.index, counts.values, color='skyblue')
    ax1.set_xlabel("Year Added")
    ax1.set_ylabel("Number of Titles")
    ax1.set_title("Titles Added per Year")
    st.pyplot(fig1)

    fig2, ax2 = plt.subplots()
    type_counts = filtered_df['type'].value_counts()
    colors = 'gray' if chart_style == "Grayscale" else None
    ax2.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%', colors=None if not colors else ['lightgray', 'darkgray'])
    ax2.set_title("Content Type Distribution")
    st.pyplot(fig2)

    fig3, ax3 = plt.subplots()
    country_counts = filtered_df['country'].value_counts().head(10)
    ax3.barh(country_counts.index, country_counts.values, color='gray' if chart_style == "Grayscale" else 'coral')
    ax3.set_xlabel("Number of Titles")
    ax3.set_ylabel("Country")
    ax3.set_title("Top 10 Countries by Content")
    st.pyplot(fig3)

    csv = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Filtered Data as CSV",
        data=csv,
        file_name='filtered_netflix_data.csv',
        mime='text/csv'
    )
else:
    st.info("Upload a CSV file to get started.")
