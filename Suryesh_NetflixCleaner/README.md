# Netflix Dataset Cleaning and Preprocessing

## 📌 Project Overview

This project demonstrates the complete data cleaning and preprocessing pipeline on the **Netflix Movies and TV Shows** dataset. The dataset contains metadata about Netflix content such as title, cast, director, country, rating, and release year.

The goal was to prepare the dataset for analysis and potential machine learning applications by:
- Cleaning missing or inconsistent data
- Exploring summary statistics
- Visualizing key insights
- Encoding categorical variables

---

## 📁 Dataset Source

Dataset used: [Netflix Movies and TV Shows - Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows)

---

## 🧹 Tasks Performed

### ✅ Data Inspection
- Loaded CSV using `pandas`
- Checked for missing values, incorrect data types, and duplicate rows

### ✅ Data Cleaning
- Converted `date_added` column to datetime format
- Filled missing values in `director`, `cast`, `country`, and `rating` columns
- Dropped rows with missing `duration` field
- Removed any unnecessary whitespace

### ✅ Summary Statistics and Grouping
- Counted content types (Movie vs TV Show)
- Analyzed most common genres and countries
- Reviewed content production trends across release years
- Grouped data by type and year

### ✅ Visualizations
- Bar charts for content types and top countries
- Line plot of titles released over the years
- Rating distribution plot

### ✅ Label Encoding (ML Readiness)
- Encoded `type`, `rating`, and simplified `country` columns using `LabelEncoder`

---

## 📊 Key Insights

- **Movies** dominate the platform with over 6000 entries.
- **United States** and **India** produce the most content.
- Majority of Netflix content was released between **2017–2020**.
- Most common content rating is **TV-MA**.

---

## 🛠️ Tools Used

- Python 3.x
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

---

## 📂 Folder Structure
```
Suryesh_NetflixCleaner/
├── data/
│ └── netflix_titles.csv
├── netflix_cleaner.py
└── README.md
```
---
## 🚀 How to Run

1. Clone or download this repository
2. Install required libraries if not already installed:
```
pip install pandas numpy matplotlib seaborn scikit-learn
```
3. Run the script:
```
python netflix_cleaner.py
```
---

## 👤 Author

**Suryesh Pandey**  
B.Sc. (Computing), 2nd Year  
Bennett University
