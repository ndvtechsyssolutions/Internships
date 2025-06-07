# 🦠 COVID-19 Data Visualization Dashboard

This Streamlit dashboard provides an interactive interface to explore the **COVID-19 dataset** with filters for country and date range, dynamic metrics, and insightful visualizations.

---

## 📊 Features

- **Sidebar Filters**:
  - Select **country** from a dropdown
  - Choose a **custom date range**

- **Interactive Visuals**:
  - 📈 Line chart: Total cases vs total deaths over time
  - 📊 Bar chart: Metric comparison (total & new cases/deaths)
  - 🥧 Pie chart: Daily case vs death distribution

- **Dynamic Metrics**:
  - Live updates for:
    - Total cases
    - Total deaths
    - New cases (latest)
    - New deaths (latest)

- **Raw Data & Statistics**:
  - Toggle to view first few rows of the original dataset
  - Summary statistics across all numerical fields

---

## 🗂️ Folder Structure

```Suryesh_StreamlitDashboard/
├── app.py # Main Streamlit app
├── data/
│ └── covid_data.csv # Dataset from Our World in Data
├── README.md # Project overview and instructions
└── requirements.txt # Python dependencies
```

---

## 📦 Requirements

Install all dependencies using:

```bash
pip install -r requirements.txt
```
## 🚀 Running the App

Run the Streamlit dashboard locally:
```
streamlit run app.py
```
## 📁 Dataset Source

- **Dataset**: [Our World in Data - COVID-19](https://covid.ourworldindata.org/data/owid-covid-data.csv)  
- Updated regularly and includes global time-series data on COVID-19 cases, deaths, testing, and vaccination.

---

## 📌 Author

- **Suryesh Pandey**  
- B.Sc (Computing), 2nd Year, Bennett University
