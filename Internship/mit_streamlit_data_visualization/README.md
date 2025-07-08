# Sales Dashboard – USA Sales Dataset

## Introduction

This is an interactive **Sales Dashboard** built with **Streamlit** and **Plotly**. The dashboard allows users to upload a CSV file containing sales data, explore business metrics, and visualize insights related to sales performance across various categories, regions, and time periods.

---

## Table of Contents

- [Introduction](#introduction)
- [Objective](#objective)
- [Features](#features)
- [Usage](#usage)
- [Setup Instructions](#setup-instructions)
  - [1. Clone the Repository](#1-clone-the-repository)
  - [2. Install Python](#2-install-python)
  - [3. Install Dependencies](#3-install-dependencies)
  - [4. Add Dataset](#4-add-dataset)
  - [5. Run the App](#5-run-the-app)
- [Required CSV Columns](#required-csv-columns)
- [File Structure](#file-structure)

---

## Objective

The objective of this dashboard is to:
- Provide a user-friendly, no-code tool for business users and analysts to analyze sales data.
- Summarize key metrics such as total sales, profit, and order volume.
- Visualize trends and distributions across regions and product categories.
- Enable CSV file uploads and real-time filtering via sidebar widgets.

---

## Features

- **File Upload**: Upload your own CSV file containing sales data.
- **Data Preprocessing**: Handles missing values, normalizes columns, and parses dates and numbers.
- **Sidebar Filters**: Filter data by:
  - Date range
  - Region
  - Product category
- **KPIs**: View Total Orders, Total Sales, Total Profit, and Average Profit per Order.
- **Visualizations**:
  - Bar chart: Sales by Category
  - Line chart: Monthly Profit Trend
  - Pie chart: Orders by Region
  - Map: Sales locations (if latitude and longitude are present)
- **Download Option**: Export the filtered dataset as a CSV file.
- **Data Preview**: Scrollable and filterable table of the processed dataset.

---

## Usage

1. Launch the Streamlit app.
2. Upload your sales dataset in CSV format or use the default `sales data.csv` file.
3. Use the sidebar to:
   - Adjust the date range.
   - Select one or more regions and product categories.
4. Review metrics, explore visualizations, preview the data, or download the filtered CSV.

---

## Setup Instructions

### 1. Clone the Repository

```
git clone <repository-url>
cd <project-folder>
```

### 2. Install Python

Make sure Python 3.7+ is installed. You can download it from python.org


### 3. Install Dependencies
```
pip install streamlit pandas plotly
```

### 4. Add Dataset
Ensure a file named ```sales data.csv``` is present in the same directory if you want to use the default dataset. Alternatively, you can upload your own CSV file from the sidebar in the app.

### 5. Run the App
```
streamlit run app.py
```

### Required CSV Columns

Make sure your dataset contains the following columns:

```order_id```

```sales```

```profit```

```quantity```

```category```

```region```

```order_date```

Optional columns for geolocation:

```latitude```

```longitude```

Column names can be in any case but will be normalized automatically.

---

# File Structure

```
├── app.py
├── sales data.csv
└── README.md
```





