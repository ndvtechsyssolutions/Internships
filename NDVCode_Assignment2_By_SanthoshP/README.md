# Clean and Preprocess Netflix Dataset

---

## Project Overview

This project focuses on cleaning and preprocessing the Netflix dataset to prepare it for analysis and machine learning tasks. The dataset includes Netflix titles with various attributes such as director, cast, country, date added, duration, release year, and ratings.
The goal is to handle missing values, remove duplicates, engineer new features, convert data types appropriately, and apply basic exploratory data analysis (EDA) including visualizations and label encoding for ML readiness.

---

## Environment Setup

### Required Libraries
- Python 3.x
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn

### Installation

Use the following pip commands to install the necessary libraries if not already installed:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```
### Dataset

* **Filename:** netflix_titles.csv
* **Source:** Netflix Titles Dataset from Kaggle (downloaded locally)

* *Dataset contains columns such as:*
`show_id`, `type`, `title`, `director`, `cast`, `country`, `date_added`, `release_year`, `rating`, `duration`, `listed_in`, `description`

### Data Cleaning and Preprocessing Steps

1. Load Dataset
* Read the CSV file into a pandas DataFrame.
* Verify dataset shape and initial structure.

2. Initial Inspection
* Check data types for all columns.
* Identify missing values per column.
* Detect duplicate rows.

3. Handle Missing Values
* Fill missing values in director, cast, country, rating, and date_added with placeholders like "Unknown" or "Not Rated".
* Drop rows missing critical fields such as duration and release_year.

4. Remove Duplicates
  Identify and remove duplicate rows to ensure data integrity.

5. Convert Data Types
* Convert date_added to datetime format, handling errors gracefully.
* Ensure release_year is stored as an integer type.

6. Feature Engineering
* Extract year, month, and day from date_added into separate columns.
* Calculate content_age as the difference between the current year and the release_year.
* Split duration into numeric duration (duration_num) and unit (duration_unit) for more granular analysis.

7. Summary Statistics
  Generate descriptive statistics for numerical and categorical columns to understand data distributions and characteristics.

8. Numerical Transformation
  Normalize content_age using Min-Max scaling via NumPy for machine learning readiness.

9. Filtering, Sorting, and Grouping
* Identify top 5 countries by the number of Netflix titles.
* Group data by type (Movie or TV Show) and count entries per category.

### Exploratory Data Analysis (EDA) and Visualization
* Missing Values Heatmap: Visualize missing data patterns with Seaborn heatmap to assess data quality.
* Correlation Matrix: Explore correlations among numerical features (release_year, duration_num, content_age, content_age_norm) using a heatmap.

## Label Encoding for Machine Learning

* Apply label encoding to categorical features:
    * `type`
    * `rating`
    * `duration_unit`
    * `country`

This step converts categorical text data into numeric format, making it compatible with machine learning algorithms.

## Results and Insights

* Successfully cleaned dataset by addressing missing values and duplicates.
* Extracted and engineered useful features for analysis.
* Normalized key numeric columns for consistent scale.
* Identified the top countries producing Netflix titles and distribution of movies versus TV shows.
* Visualizations provided insights into missing data and feature correlations.
* Prepared dataset for downstream ML tasks via label encoding.

Contact me [here](mailto:santhoshpakkiri550@gmail.com)
