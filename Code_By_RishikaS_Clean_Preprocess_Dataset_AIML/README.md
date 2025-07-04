**Netflix Titles Dataset Cleaning and Preprocessing**

This project involves cleaning, preprocessing, and exploring the Netflix Titles dataset using Python libraries such as Pandas and NumPy. The dataset provides information about movies and TV shows available on Netflix as of 2021.

🔍 Dataset Source

Kaggle: https://www.kaggle.com/datasets/padmapriyatr/netflix-titles

🧰 Libraries Used

•	pandas

•	numpy

•	seaborn

•	matplotlib

•	scikit-learn (LabelEncoder)

📌 Objectives

•	Load and inspect the dataset

•	Handle missing values and duplicates

•	Convert and format data types appropriately

•	Perform basic numerical transformations

•	Filter, sort, and group data

•	Visualize patterns and relationships

•	Prepare the dataset for machine learning use

📂 Steps Performed

1.	Data Loading

o	Loaded the dataset using Pandas

o	Inspected the first few rows and column data types

3.	Data Cleaning

o	Removed duplicate records

o	Handled missing values:

	Filled missing rating values with the mode

	Filled missing director and country with 'Unknown'

	Dropped rows where cast was missing

	Converted and cleaned date_added values

	Filled missing duration values based on mode per type (Movie or TV Show)

4.	Data Type Conversion

o	Converted date_added to datetime

o	Extracted year_added and month_added

5.	Feature Engineering
	
o	Computed title length using NumPy

o	Encoded categorical features (type and rating) using LabelEncoder

6.	Data Analysis
	
o	Generated summary statistics

o	Grouped and counted content types

o	Visualized:

	Missing value heatmap

	Content type distribution

	Correlation matrix of numerical fields

📊 Visualizations

•	Heatmap showing missing values before and after cleaning

•	Correlation matrix for numerical features (title_length, year_added, month_added)

•	Bar chart showing content type distribution

🧼 Output

A fully cleaned dataset with:

•	No missing values

•	Consistent and appropriate data types

•	Machine-learning-ready features

Cleaned CSV file: clean_netflix_titles.csv

📁 Files Included

•	Clean_Preprocess_Dataset_AIML.ipynb

•	netflix_titles.csv

•	clean_netflix_titles.csv

•	README.md

✅ How to Run

1.	Open the notebook or Python script in Google Colab or your local IDE
   
2.	Upload the raw netflix_titles.csv file
	
3.	Execute all cells to clean and explore the dataset
   
4.	View outputs and visualizations inline
	
📌 Note

All missing values have been resolved using appropriate techniques. The dataset is now prepared for deeper analysis or modeling
