### 📊 Titanic Dataset - Exploratory Data Analysis (EDA)

## 🔍 Objective
This project performs Exploratory Data Analysis (EDA) on the Titanic dataset from Kaggle:

🔗 Titanic Dataset (https://www.kaggle.com/datasets/yasserh/titanic-dataset)

The aim is to analyze survival patterns based on demographic and travel features, identify insights, and visualize key relationships.

## 🗂️ Dataset Features

The dataset includes the following columns:

1. PassengerId: Unique ID

2. Survived: Survival (0 = No, 1 = Yes)

3. Pclass: Ticket class (1 = 1st, 2 = 2nd, 3 = 3rd)

4. Name, Sex, Age

5. SibSp, Parch: # of siblings/spouses and parents/children aboard

6. Ticket, Fare, Cabin, Embarked

## ✅ Key Tasks Completed

1. Loaded the dataset using Pandas

2. Handled missing values, removed duplicates, and fixed data types

3. Generated summary statistics using .describe(), .info(), .value_counts()

4. Visualized data using Seaborn and Matplotlib

5. Histograms, Box plots, Count plots

6. Violin plot and Pair plot

7. Correlation Heatmap

8. Performed groupby analysis by Sex, Pclass

9. Created a new feature: FamilySize = SibSp + Parch + 1

10. Documented top 5 insights using markdown cells

## 📌 Top 5 Insights

1. Females had a significantly higher survival rate than males.

2. 1st class passengers had better survival rates than 2nd or 3rd class.

3. Children (lower age group) were more likely to survive.

4. Passengers with smaller family sizes had better survival chances.

5. Higher Fare paid correlated with a greater chance of survival.

## 📁 Files Included
ASSIGNMENT4.ipynb – Main Jupyter Notebook with code, visualizations, and markdown

Titanic-Dataset.csv – Titanic dataset from Kaggle

README.md – Project overview and instructions

## 🚀 How to Run
Open the .ipynb notebook in Google Colab or Jupyter Notebook

Upload the dataset (Titanic-Dataset.csv)

Run the cells sequentially to view analysis and visualizations

## 📚 Libraries Used
- pandas

- numpy

- seaborn

- matplotlib
