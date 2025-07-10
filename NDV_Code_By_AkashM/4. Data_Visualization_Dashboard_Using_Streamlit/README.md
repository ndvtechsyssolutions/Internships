🍿 Netflix Data Explorer Dashboard

📂 Project Overview
    This project builds an interactive data visualization dashboard using Streamlit to explore the Netflix dataset. Users can upload a Netflix CSV file and dynamically filter data by content type, country, and year added. The dashboard provides useful charts and summary statistics to gain insights into Netflix’s content library.

📑 Files in This Folder
    app.py
    Main Streamlit app for uploading data, applying filters, displaying charts, and downloading filtered data.

    netflix_titles.csv
    Sample Netflix dataset containing metadata about TV shows and movies on Netflix.

🔧 Features & Functionality
    File Upload

    Upload a Netflix CSV file through the Streamlit file uploader.

    Data Processing

    Convert date_added to datetime, extract year_added.

    Fill missing duration values with "Unknown".

    Filters

    Multi-select filters for content type and country.

    Slider to select year added range.

    Summary Statistics

    Option to view descriptive statistics of the filtered dataset.

    Visualizations

    Bar chart of titles added per year.

    Pie chart showing content type distribution.

    Horizontal bar chart for top 10 countries by content count.

    Choice of chart color style: default colors or grayscale.

    Data Export

    Download the filtered data as a CSV file.

📊 How to Run
    Install required packages if not installed:
    pip install streamlit pandas matplotlib

Run the app:
    streamlit run app.py
    Upload your Netflix CSV dataset and explore using the filters and charts.

✅ Outcomes
    Interactive dashboard to explore Netflix data visually.

    Customizable filtering for tailored analysis.

    Easy export of filtered datasets for offline use.

💡 Future Enhancements
    Add more interactive charts (e.g., genre analysis).

    Include time-series analysis of content trends.

    Implement user authentication for saving preferences.

✍️ Author
    Created as a project to demonstrate Streamlit-powered interactive dashboards for data visualization.

