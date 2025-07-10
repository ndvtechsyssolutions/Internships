Hypothesis Testing and Statistical Summary on Business Datasets

📂 Project Overview
    This project applies hypothesis testing and generates statistical summaries on the Titanic dataset (used as a business dataset example). It focuses on understanding differences in fare between male and female passengers and explores the dependency between survival and sex.

📑 Files in This Folder

    -Hypothesis_Testing_Stat_Summary.ipynb
     Jupyter Notebook containing all code for data loading, cleaning, hypothesis tests, and visualizations.

    -titanic.csv
     Titanic dataset from Kaggle with passenger information.

🔧 Steps Performed

    Data Loading and Inspection

    Imported pandas, numpy, seaborn, matplotlib, and scipy.stats libraries.

    Uploaded and read the dataset into a DataFrame.

    Displayed first few rows, dataset info, and descriptive statistics.

    Calculated mode values for Age and Fare.

    Data Cleaning

    Removed rows with missing values in key columns: Age, Fare, Sex, and Survived.

    Hypothesis Testing: Fare by Sex

    Extracted fare values separately for male and female passengers.

    Conducted an independent two-sample t-test to check if average fares differ by sex.

    Evaluated the p-value to accept or reject the null hypothesis (H0).

    Hypothesis Testing: Survival vs Sex

    Created a contingency table for Sex and Survived.

    Performed a Chi-square test of independence to check if survival depends on sex.

    Evaluated the p-value to accept or reject the null hypothesis (H0).

    Visualization

    Plotted histogram with KDE for age distribution.

    Boxplot showing fare distribution by sex.

    Heatmap displaying correlations between numerical variables.

📊 Key Outputs
    T-test results:
        Determines if the difference in average fare between male and female passengers is statistically significant.

    Chi-square test results:
        Tests if survival is dependent on sex.

    Visualizations:
        Age distribution, fare by sex, and correlation heatmap provide graphical insights into data patterns.

🚀 How to Run
    Open the Hypothesis_Testing_Stat_Summary.ipynb notebook.

    Upload the titanic.csv file when prompted.

    Run all cells sequentially to perform hypothesis tests and generate visualizations.

✅ Outcomes
    Successfully cleaned the dataset to remove missing values.

    Found statistical evidence on fare differences between male and female passengers.

    Established the relationship between survival and sex.

    Visualized key distributions and correlations to support analysis.

💡 Future Improvements
    Extend hypothesis testing to other variables like passenger class or embarked port.

    Use non-parametric tests if normality assumptions fail.

    Explore more complex statistical models for prediction.

✍️ Author
    This project was prepared to demonstrate the application of statistical hypothesis testing and summary in a business dataset context using Titanic data.