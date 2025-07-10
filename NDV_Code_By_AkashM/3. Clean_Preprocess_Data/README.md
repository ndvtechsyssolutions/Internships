# Clean and Preprocess Netflix Titles Data

## 📂 Project Overview

This project focuses on **cleaning and preprocessing the Netflix Titles dataset** to prepare it for further analysis or modeling tasks. The dataset was sourced from **Kaggle**, containing detailed metadata about TV shows and movies available on Netflix.

The process involved:
- Handling missing values.
- Removing duplicates.
- Feature engineering (e.g., extracting year, title length).
- Generating useful summaries and visualizations.

---

## 📑 Files in This Folder

- **Clean_Preprocess_Data.ipynb**  
  Contains all code for data loading, cleaning, and exploratory data analysis.

- **netflix_titles.csv**  
  The original dataset with information on Netflix content.

---

## 🔧 Steps Performed

### 1. Data Loading
- Imported required libraries (`pandas`, `numpy`, `matplotlib`, `seaborn`).
- Loaded the dataset using `pandas.read_csv`.
- Inspected the dataset shape, column names, and initial rows.

### 2. Exploratory Checks
- Displayed dataset information (`info()`).
- Counted missing values in each column.
- Visualized missing data using a heatmap.

### 3. Handling Missing Data
- Filled missing **rating** values with the most common rating in the dataset.
- Replaced missing **country** entries with `"Not Specified"`.
- Removed rows where **date_added** was missing.

### 4. Duplicate Removal
- Identified duplicate records.
- Removed duplicates to maintain data integrity.

### 5. Feature Engineering
- Converted **date_added** to datetime format.
- Extracted **year_added** from **date_added**.
- Encoded **type** as numerical codes (`Movie=1`, `TV Show=0`).
- Calculated **title_length** to measure the length of each title string.

### 6. Filtering and Sorting
- Created a subset of **recent movies** added after 2016.
- Sorted titles by their length to find the longest names.

### 7. Summarization and Statistics
- Aggregated the number of titles by country.
- Generated descriptive statistics for all fields.
- Visualized correlations among numeric variables.

---

## 📊 Key Outputs

- **Missing Value Heatmap**  
  Helps to quickly identify columns needing attention.

- **Correlation Matrix**  
  Shows relationships between numeric fields like `title_length` and `year_added`.

- **Summary Statistics**  
  Provides a clear overview of the dataset distribution.

---

## 🚀 How to Run

1. Open the `Clean_Preprocess_Data.ipynb` notebook.
2. Upload `netflix_titles.csv` when prompted.
3. Run each cell sequentially to reproduce the results.

---

## ✅ Outcomes

By completing this cleaning and preprocessing workflow:
- The dataset is **free of duplicates**.
- Missing data has been properly handled.
- New features have been created for more insightful analysis.
- The data is ready for visualization, modeling, or dashboarding.

---

## 💡 Future Improvements

- Further feature engineering (e.g., parsing genres, duration).
- Detailed analysis by country and year.
- Integrate with recommendation systems or clustering.

---

## ✍️ Author

This project was prepared as part of a data cleaning and preprocessing exercise.