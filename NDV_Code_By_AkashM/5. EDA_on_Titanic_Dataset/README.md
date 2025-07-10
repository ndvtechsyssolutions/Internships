Titanic Dataset Exploratory Data Analysis (EDA)

📂 Project Overview
    This project performs an exploratory data analysis on the Titanic dataset from Kaggle. The goal is to understand the dataset’s structure, clean missing values, analyze passenger demographics, and explore factors affecting survival rates.

📑 Files in This Folder

    -Titanic_EDA.ipynb
     Jupyter Notebook containing all code for data loading, cleaning, visualization, and analysis.

    -titanic.csv
     Original Titanic dataset with passenger information.

🔧 Steps Performed
    Data Loading

    Imported libraries: pandas, numpy, seaborn, matplotlib.

    Uploaded and loaded the Titanic CSV file into a DataFrame.

    Initial Data Inspection

    Displayed first few rows (head()).

    Checked for missing values using isnull().sum().

    Examined data types and overall info.

    Data Cleaning

    Filled missing Age values with median age.

    Filled missing Embarked values with the most frequent port.

    Removed duplicate records.

    Descriptive Statistics

    Generated summary statistics (describe()).

    Counted survival distribution.

    Visualization and Analysis

    Boxplot of Age distribution across Passenger Classes (Pclass).

    Countplot showing survival by gender.

    Pairplot of numerical features colored by survival status.

    Heatmap of correlations between numerical variables.

    Grouped survival rates by Passenger Class and Gender.

    Violin plot showing Age distribution split by survival and Passenger Class.

    Created new feature FamilySize (sum of siblings/spouses and parents/children plus one).

    Barplot of survival rate by family size.

📊 Key Insights
    Age varies significantly across passenger classes.

    Females had a higher survival rate than males.

    Higher class passengers had better chances of survival.

    Family size appears to influence survival probability.

🚀 How to Run
    Open Titanic_EDA.ipynb in Jupyter or Google Colab.

    Upload titanic.csv when prompted.

    Run all cells sequentially to reproduce the analysis and visualizations.

✅ Outcomes
    Dataset cleaned of missing values and duplicates.

    Visual understanding of passenger demographics and survival factors.

    Created new feature for deeper insight into family influence.

💡 Future Improvements
    Analyze impact of ticket fare and cabin location on survival.

    Use machine learning models to predict survival.

    Explore text data like passenger names and titles for additional features.

✍️ Author
    This EDA was conducted to understand the Titanic dataset and prepare it for predictive modeling.