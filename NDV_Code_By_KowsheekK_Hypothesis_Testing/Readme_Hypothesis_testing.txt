# Assignment 5: Hypothesis Testing and Statistical Summary

## Objective
This project conducts statistical analysis and hypothesis testing on a real-world **sales dataset**. The goal is to derive insights and validate assumptions related to business performance metrics using Python.

---

## Dataset
**Name:** Sales Data  
**Source:** Public business dataset (e.g., from Kaggle, UCI)  
**Description:** Contains transactional records including sales amount, region, product category, customer type, etc.

---

## Tasks Performed

### 1. Exploratory Data Analysis (EDA)
- Loaded dataset using Pandas
- Cleaned missing values and checked data types

### 2. Descriptive Statistics
- Calculated metrics like mean, median, mode, standard deviation
- Used `df.describe()` for numerical column summaries

### 3. Hypothesis Testing

####  Hypothesis 1: Two-sample t-test
- H₀: Mean sales amount is equal for online and offline customers  
- H₁: Mean sales amount differs between online and offline customers

####  Hypothesis 2: Chi-square test
- H₀: Sales region and product category are independent  
- H₁: Sales region and product category are dependent

### 4. Visualization
- Boxplot: Sales distribution by customer type
- Histogram: Total sales distribution
- Heatmap: Correlation between numerical variables

### 5. Bonus Insights
- Correlation matrix
- Pivot tables grouped by region and customer type

---

##  Tools and Libraries
- Python 3.x
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SciPy

---

## Summary
- Found statistically significant difference in average sales between online and offline customers.
- Regional variation in sales is linked to product category choice.

--
