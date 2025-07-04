### 📊 Sales Data Analysis – Hypothesis Testing & Statistical Summary

## 📝 Overview

This project involves statistical analysis and hypothesis testing using a business-related sales dataset. The goal is to extract meaningful insights and validate assumptions using descriptive statistics, hypothesis tests, and visualizations.

---

## 📁 Dataset

- **Name:** Sample Sales Data
  
- **Source:** [Kaggle - Sample Sales Data](https://www.kaggle.com/datasets/kyanyoga/sample-sales-data)
  
- **Description:** The dataset contains sales records including order details, customer information, product line, deal size, and financial metrics like sales, profit, and quantity ordered.

---

## 🎯 Objectives

- Load and explore the dataset using Pandas.
  
- Generate summary statistics for key numeric columns.
  
- Formulate and test the following hypotheses:
  
  - **One-sample t-test**: Is the average sales different from $3,000?
    
  - **Chi-square test**: Is there a relationship between Product Line and Deal Size?
    
- Visualize data distributions and relationships.
  
- Perform correlation analysis and pivot table summaries.
  
- Interpret results with statistical significance (p-values).

---

## 📌 Key Steps

### 🔹 Summary Statistics

Calculated `mean`, `median`, `std`, `min`, `max`, and `sum` for:

- Quantity Ordered
  
- Price Each
  
- Sales
  
- Profit

### 🔹 Hypothesis Testing

**1️⃣ One-Sample t-Test**  

- **H₀ (Null):** Mean Sales = 3000
  
- **H₁ (Alt):** Mean Sales ≠ 3000
  
- **Result:** Reject H₀ (p < 0.05)

**2️⃣ Chi-Square Test**  

- **H₀ (Null):** Product Line and Deal Size are independent
   
- **H₁ (Alt):** Product Line and Deal Size are related
  
- **Result:** Reject H₀ (p < 0.05)

### 🔹 Visualizations

- Histogram of Sales with sample and hypothesized mean
  
- Boxplots for distribution analysis
  
- Heatmap of ProductLine vs DealSize counts
  
- Correlation heatmap
  
- Pivot tables for summary insights

---

## 📈 Visual Samples

| Visualization | Description |
|---------------|-------------|
| Histogram     | Distribution of sales with mean comparison |
| Heatmap       | Product Line vs Deal Size relationship |
| Boxplots      | Distribution of profit, sales by category |

---

## 🛠️ Technologies Used

- Python
  
- Pandas
  
- NumPy
  
- Matplotlib
  
- Seaborn
  
- SciPy

---

## 📂 How to Run

1. Clone this repository.

2. Open the Jupyter Notebook in Google Colab or Jupyter Lab.

3. Ensure the dataset is uploaded or linked to your notebook path.

4. Run each cell sequentially to perform the analysis.

---

## 📌 Conclusion

This project demonstrates how basic hypothesis testing and descriptive analysis can help validate business assumptions and extract actionable insights from real-world data.

