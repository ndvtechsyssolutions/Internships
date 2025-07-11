# 📊 Salary Prediction using Simple Linear Regression

This project demonstrates a simple linear regression model using Python to predict an employee's **salary** based on their **years of experience**. The goal is to understand the relationship between these two variables and build a predictive model.

---

## 🎯 Objective

To predict salaries from years of experience using:

- Data visualization
  
- Simple linear regression (Scikit-learn)
  
- Model evaluation
  
- Interactive salary prediction

---

## 🗂️ Dataset

- **Source**: [Kaggle - Salary_Data.csv](https://www.kaggle.com/datasets/ravitejakotharu/salary-datacsv/data)
  
- **Features**:
  
  - `YearsExperience`: Number of years of work experience
    
  - `Salary`: Annual salary in USD

---

## 🛠️ Technologies Used

- Python
  
- Pandas, NumPy
  
- Seaborn, Matplotlib
  
- Scikit-learn

---

## 📌 Key Steps

1. **Data Loading**  

    Load CSV data using Pandas.

2. **Exploratory Data Analysis (EDA)**  

   Understand the dataset using `.info()`, `.describe()`, heatmap, and pairplots.

3. **Data Cleaning**  

    Checked for and removed missing values.

4. **Model Building**  

   - Performed train/test split (80/20)
 
   - Trained linear regression model

5. **Evaluation Metrics**  

   - Mean Squared Error (MSE)

   - R² Score

6. **Visualizations**  
   - Scatter plot with regression line

   - Regression line with error bands

   - Actual vs. predicted salary bar chart

8. **Bonus Feature**  
   
   - User input for live salary prediction via console

---

## 📈 Sample Output

   Intercept: 25792.2
   
   Coefficient: 9450.0
   
   R² Score: 0.97
   
   MSE: 37033068.5

---

## 💡 How to Use

1. Clone the repository

2. Upload the `Salary_Data.csv` to your Google Drive

3. Open the `.ipynb` notebook in **Google Colab**

4. Mount your Google Drive to load the data

5. Run all cells to see EDA, model training, evaluation, and visualization

6. Uncomment the `predict_salary()` function to test user input predictions

---

## ✅ Results

- The model shows a strong linear relationship between experience and salary.

- R² score above 0.95 indicates high accuracy for this dataset.

