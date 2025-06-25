### COVID-19 Dashboard 

An interactive COVID-19 data visualization dashboard built with Streamlit. This app allows users to explore COVID-19 statistics by country and date range with interactive charts and downloadable filtered data.

## 🔍 Features

Select country and custom date range filters

View total confirmed, deaths, and recovered cases with metrics

Visualize trends over time with line charts

Analyze daily new confirmed cases using bar charts

See current proportions via pie charts

Summary statistics for selected data

Upload your own CSV for exploration

Download filtered data as CSV

## 🛠️ Installation

1. Clone this repository

2. Create and activate a virtual environment (recommended)

python -m venv venv

source venv/bin/activate      # For Linux/macOS

venv\Scripts\activate         # For Windows

3. Install dependencies

pip install -r requirements.txt

⚠️ Place the COVID-19 dataset CSV file (covid_19_clean_complete.csv) in the project directory or update the path in app.py accordingly.
Dataset source: COVID-19 Dataset by Imdevskp on Kaggle

🚀 Usage

streamlit run app.py

After running, open your browser to the address shown (usually http://localhost:8501).

## 📊 Data Source
COVID-19 Dataset by Imdevskp on Kaggle (https://www.kaggle.com/datasets/imdevskp/corona-virus-report/data)

## 📁 Project Structure

├── app.py                         # Main Streamlit application script  
├── covid_19_clean_complete.csv   # COVID-19 dataset (add manually)   
└── README.md                     # This file  
## 🧾 Requirements
Package	 Version

streamlit	1.26.0

pandas	2.0.3

plotly	5.15.0

matplotlib	3.7.1

## To install all dependencies:

pip install streamlit==1.26.0 pandas==2.0.3 plotly==5.15.0 matplotlib==3.7.1



