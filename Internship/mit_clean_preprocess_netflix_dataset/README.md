# Clean and Preprocess Netflix Dataset

## Introduction
This jupyter notebook focuses on cleaning and preprocessing the Netflix dataset to prepare it for further analysis or machine learning tasks.

## Approach

### 1. Data Loading and Initial Exploration
The necessary libraries are imported.

The column width of the ouput is increased for better viewing.

The `netflix_titles.csv` dataset is loaded into a pandas DataFrame. 

Initial exploration includes displaying the head and tail of the DataFrame,

checking data types and non-null counts using `df.info()`, 

and identifying the sum of null values for each column using `df.isnull().sum()`. 

A heatmap visualization is also used to show the distribution of null values before handling them.

Count of Duplicates is checked furthermore to handle them.

### 2. Handling Missing Values
* **'director'**: Missing values are filled with 'Unknown'.
* **'cast'**: Missing values are filled with 'Unknown'.
* **'country'**: Missing values are filled 'Unknown'.
* **'date_added'**: Missing values are filled with 1st day and month of the release year.
* **'rating'**: Missing values are filled with the mode of the 'rating' column.
* **'duration'**: Missing values are filled with the mode of the 'duration' column.

### 3. Data Type Conversion and Feature Extraction
* The `date_added` column is converted to datetime objects.
* New features `month_added` and `year_added` are extracted from the `date_added` column.
* Duration time and the type of duration are extracted from 'duration' column.

### 4. Feature Engineering
* No. of years since the release of the movie is added.

### 5. Label Encoding
Categorical columns such as `type`, `rating`, `duration_type` are label encoded to convert them into numerical representations suitable for machine learning models.

### 6. Saving Cleaned Data
The cleaned and preprocessed DataFrame is saved to a new CSV file named `netflix_clean.csv`, without including the index.

## Findings

Key findings from the preprocessing include:

* Identification and treatment of significant missing values in `director`, `cast`, and `country` columns.
* Successful conversion of date strings to datetime objects and extraction of granular date features.
* Transformation of categorical data into a numerical format using Label Encoding, making it ready for model training.

### Visualization Insights:

* **Heatmap of Null Values**: The heatmap clearly revealed the columns with the most significant missing data, particularly `director`, `cast`, and `country`, visually confirming the need for missing value imputation in these areas.

* **Countplot of Content Types**: A countplot visualizing the 'type' column highlighted that the Netflix dataset contains a substantially higher number of "Movies" compared to "TV Shows".

* **Top Countries Plot**: A bar plot showing the distribution of content by 'country' indicated that the United States has the highest number of titles on Netflix, followed by India and other countries.

## Summary
This Jupyter notebook provides a comprehensive example of data cleaning and preprocessing for the Netflix dataset. 

By following the outlined steps, the raw data is transformed into a clean, structured, and machine learning-ready format, addressing missing values, converting data types, and engineering relevant features. 