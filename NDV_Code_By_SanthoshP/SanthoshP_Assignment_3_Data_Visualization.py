import streamlit as st
import pandas as pd
import plotly.express as px

# Page configuration
st.set_page_config(page_title="Netflix Data Dashboard", layout="wide")

# Title
st.title("🎬 Netflix Content Dashboard")
st.markdown("Explore Netflix movies and TV shows data")

# =================== FILE UPLOADER (BONUS) ===================
st.markdown("---")
st.subheader("📁 Upload Your Own Dataset")

uploaded_file = st.file_uploader(
    "Choose a CSV file (optional - will use Netflix data by default)",
    type="csv",
    help="Upload your own CSV file to analyze. Should have similar structure to Netflix data."
)

use_uploaded = st.checkbox("Use uploaded file instead of Netflix data") if uploaded_file else False

# Load data function (updated to handle uploaded files)
@st.cache_data
def load_data(uploaded_file=None):
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.success(f"✅ Loaded {len(df)} rows from uploaded file!")
    else:
        df = pd.read_csv("netflix_titles.csv")
        st.info("📺 Using Netflix dataset")
    return df

# Load appropriate dataset
if use_uploaded and uploaded_file:
    df = load_data(uploaded_file)
else:
    df = load_data()

st.markdown("---")

# Load data - simple version without date processing
@st.cache_data
def load_data():
    df = pd.read_csv("netflix_titles.csv")
    return df

df = load_data()

# Display basic info
st.subheader("Dataset Overview")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Titles", len(df))
with col2:
    st.metric("Movies", len(df[df['type'] == 'Movie']))
with col3:
    st.metric("TV Shows", len(df[df['type'] == 'TV Show']))

# Show raw data
if st.checkbox("Show raw data"):
    st.dataframe(df.head(100))  # Show first 100 rows only

st.success("✅ Basic app is working! Ready to add visualizations.")

# =================== SIDEBAR FILTERS ===================
st.sidebar.header("🎛️ Filters")

# Content type filter
content_types = ['All'] + list(df['type'].unique())
selected_type = st.sidebar.selectbox("Select Content Type:", content_types)

# Release year filter
min_year = int(df['release_year'].min())
max_year = int(df['release_year'].max())
year_range = st.sidebar.slider(
    "Select Release Year Range:",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year)
)

# Apply filters
filtered_df = df.copy()
if selected_type != 'All':
    filtered_df = filtered_df[filtered_df['type'] == selected_type]

filtered_df = filtered_df[
    (filtered_df['release_year'] >= year_range[0]) & 
    (filtered_df['release_year'] <= year_range[1])
]

# Update metrics with filtered data
st.subheader("📊 Filtered Data Overview")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Filtered Titles", len(filtered_df))
with col2:
    st.metric("Movies", len(filtered_df[filtered_df['type'] == 'Movie']))
with col3:
    st.metric("TV Shows", len(filtered_df[filtered_df['type'] == 'TV Show']))

# =================== DATA EXPORT (BONUS) ===================
st.markdown("### 💾 Export Filtered Data")

col1, col2, col3 = st.columns(3)

with col1:
    # Export filtered data as CSV
    csv_data = filtered_df.to_csv(index=False)
    st.download_button(
        label="📥 Download Filtered Data (CSV)",
        data=csv_data,
        file_name=f"netflix_filtered_data_{len(filtered_df)}_rows.csv",
        mime="text/csv"
    )

with col2:
    # Export summary statistics
    summary_stats = filtered_df.describe(include='all')
    summary_csv = summary_stats.to_csv()
    st.download_button(
        label="📊 Download Summary Stats",
        data=summary_csv,
        file_name="netflix_summary_statistics.csv",
        mime="text/csv"
    )

with col3:
    # Show current filter info
    st.info(f"**Current Filters:**\n- Content Type: {selected_type}\n- Years: {year_range[0]}-{year_range[1]}\n- Showing: {len(filtered_df)} titles")

# =================== SUMMARY STATISTICS ===================
st.subheader("📈 Summary Statistics")

col1, col2, col3, col4 = st.columns(4)

with col1:
    avg_year = filtered_df['release_year'].mean()
    st.metric("Average Release Year", f"{avg_year:.0f}")

with col2:
    latest_year = filtered_df['release_year'].max()
    st.metric("Latest Release", f"{latest_year}")

with col3:
    oldest_year = filtered_df['release_year'].min()
    st.metric("Oldest Release", f"{oldest_year}")

with col4:
    unique_countries = filtered_df['country'].nunique()
    st.metric("Countries Represented", f"{unique_countries}")

# Show some interesting insights
st.markdown("### 🔍 Quick Insights")
insights_col1, insights_col2 = st.columns(2)

with insights_col1:
    if len(filtered_df) > 0:
        most_common_rating = filtered_df['rating'].mode().iloc[0] if not filtered_df['rating'].mode().empty else "N/A"
        st.info(f"🎭 Most common rating: **{most_common_rating}**")
        
        # Most productive year
        most_productive_year = filtered_df['release_year'].mode().iloc[0] if not filtered_df['release_year'].mode().empty else "N/A"
        year_count = (filtered_df['release_year'] == most_productive_year).sum()
        st.info(f"🎬 Most productive year: **{most_productive_year}** ({year_count} titles)")

with insights_col2:
    if len(filtered_df) > 0:
        # Movie vs TV Show percentage
        movie_pct = (filtered_df['type'] == 'Movie').mean() * 100
        st.info(f"🎥 Movies make up **{movie_pct:.1f}%** of content")
        
        # Most represented country
        if not filtered_df['country'].isna().all():
            top_country = filtered_df['country'].value_counts().index[0] if len(filtered_df['country'].value_counts()) > 0 else "N/A"
            st.info(f"🌍 Top country: **{top_country}**")

# =================== VISUALIZATIONS ===================
st.subheader("📈 Visualizations")

# 1. Content Type Distribution (Pie Chart)
col1, col2 = st.columns(2)

with col1:
    st.markdown("### Content Type Distribution")
    if len(filtered_df) > 0:
        type_counts = filtered_df['type'].value_counts()
        fig_pie = px.pie(
            values=type_counts.values,
            names=type_counts.index,
            title="Movies vs TV Shows",
            color_discrete_sequence=['#E50914', '#FF6B6B']
        )
        st.plotly_chart(fig_pie, use_container_width=True)
    else:
        st.warning("No data available for selected filters")

with col2:
    st.markdown("### Release Year Trends")
    if len(filtered_df) > 0:
        year_counts = filtered_df.groupby(['release_year', 'type']).size().reset_index(name='count')
        fig_line = px.line(
            year_counts,
            x='release_year',
            y='count',
            color='type',
            title="Content Released Over Time",
            color_discrete_sequence=['#E50914', '#FF6B6B']
        )
        fig_line.update_layout(xaxis_title="Release Year", yaxis_title="Number of Titles")
        st.plotly_chart(fig_line, use_container_width=True)
    else:
        st.warning("No data available for selected filters")

# 2. Top Countries Bar Chart
st.markdown("### 🌍 Top Countries by Content")
if len(filtered_df) > 0:
    # Handle multiple countries (some entries have multiple countries)
    countries_data = []
    for countries in filtered_df['country'].dropna():
        if ',' in str(countries):
            # Split multiple countries
            for country in str(countries).split(','):
                countries_data.append(country.strip())
        else:
            countries_data.append(str(countries).strip())
    
    if countries_data:
        from collections import Counter
        country_counts = Counter(countries_data)
        top_countries = dict(country_counts.most_common(10))
        
        fig_countries = px.bar(
            x=list(top_countries.values()),
            y=list(top_countries.keys()),
            orientation='h',
            title="Top 10 Countries by Number of Titles",
            color=list(top_countries.values()),
            color_continuous_scale='Reds'
        )
        fig_countries.update_layout(
            xaxis_title="Number of Titles",
            yaxis_title="Country",
            showlegend=False
        )
        st.plotly_chart(fig_countries, use_container_width=True)
    else:
        st.info("No country data available for selected filters")

# 3. Content Ratings Distribution
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🎭 Content Ratings")
    if len(filtered_df) > 0:
        rating_counts = filtered_df['rating'].value_counts().head(8)
        fig_rating = px.bar(
            x=rating_counts.index,
            y=rating_counts.values,
            title="Distribution by Rating",
            color=rating_counts.values,
            color_continuous_scale='Blues'
        )
        fig_rating.update_layout(
            xaxis_title="Rating",
            yaxis_title="Number of Titles",
            showlegend=False
        )
        st.plotly_chart(fig_rating, use_container_width=True)

with col2:
    st.markdown("### 📅 Content by Decade")
    if len(filtered_df) > 0:
        # Create decade bins
        filtered_df_copy = filtered_df.copy()
        filtered_df_copy['decade'] = (filtered_df_copy['release_year'] // 10) * 10
        decade_counts = filtered_df_copy['decade'].value_counts().sort_index()
        
        fig_decade = px.bar(
            x=[f"{int(d)}s" for d in decade_counts.index],
            y=decade_counts.values,
            title="Content by Decade",
            color=decade_counts.values,
            color_continuous_scale='Greens'
        )
        fig_decade.update_layout(
            xaxis_title="Decade",
            yaxis_title="Number of Titles",
            showlegend=False
        )
        st.plotly_chart(fig_decade, use_container_width=True)

# 4. Genre Analysis
st.markdown("### 🎬 Popular Genres")
if len(filtered_df) > 0:
    # Process genres (listed_in column)
    genres_data = []
    for genres in filtered_df['listed_in'].dropna():
        if ',' in str(genres):
            for genre in str(genres).split(','):
                genres_data.append(genre.strip())
        else:
            genres_data.append(str(genres).strip())
    
    if genres_data:
        from collections import Counter
        genre_counts = Counter(genres_data)
        top_genres = dict(genre_counts.most_common(15))
        
        fig_genres = px.bar(
            x=list(top_genres.keys()),
            y=list(top_genres.values()),
            title="Top 15 Genres",
            color=list(top_genres.values()),
            color_continuous_scale='Oranges'
        )
        fig_genres.update_layout(
            xaxis_title="Genre",
            yaxis_title="Number of Titles",
            xaxis_tickangle=-45,
            showlegend=False
        )
        st.plotly_chart(fig_genres, use_container_width=True)

# =================== FOOTER ===================
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray; padding: 20px;'>
    <h4>🎬 Netflix Content Dashboard</h4>
    <p>Built with Streamlit & Plotly | Interactive Data Visualization</p>
    <p>Explore Netflix content trends, filter by type and year, and download your analysis!</p>
</div>
""", unsafe_allow_html=True)
