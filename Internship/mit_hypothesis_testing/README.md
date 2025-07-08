# Statistical Analysis and Hypothesis Testing on Business Sales Dataset

A hands-on data science project to perform descriptive statistics, hypothesis testing, correlation analysis, and insights extraction using the Superstore sales dataset.

---

## Table of Contents
- [Introduction](#introduction)
- [Objective](#objective)
- [Dataset Description](#dataset-description)
- [Requirements](#requirements)
- [Installation & Setup](#installation--setup)
- [Notebook Sections](#notebook)
- [Conclusion](#conclusion)

---

## Introduction
This project demonstrates how to use Python for statistical analysis and hypothesis testing on a business-related dataset. It includes visualization, statistical inference, and business insights.

---

## Objective
- Perform descriptive statistical analysis.
- Formulate and test null and alternative hypotheses.
- Use t-tests, chi-square test, ANOVA to validate assumptions.
- Extract business insights using pivot tables and correlation.
- Visualize findings with meaningful charts.

---

## Dataset Description
- **Name:** Superstore Sales Dataset  
- **Source:** [Kaggle - Superstore Dataset](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)  
- **Contains:** Sales, profits, discounts, regions, categories, and more across U.S. orders.

---

## Requirements

Install the following Python packages:

```bash
pip install pandas numpy matplotlib seaborn scipy
```

## Installation & Setup

Clone or download this repository.

Open ```superstore_hypothesis.ipynb``` in Jupyter Notebook.

Run the cells in order.

---


### Notebook:

1. Importing Libraries:

    Essential libraries are imported including pandas, numpy, matplotlib, seaborn, and scipy.

2. Data Loading and Exploration:

    Loads the dataset, shows structure, types, missing values, and initial view.

3. Descriptive Statistics:

    Used .describe() and other summary functions to calculate mean, median, std, mode, etc.

4. Data Visualization:

    Created histograms, boxplots to understand distribution and outliers.

5. Hypothesis Formulation:

    Defined null and alternative hypotheses for business-driven questions.

6. t-Tests:

    Performed one-sample and two-sample t-tests to compare means.

7. Chi-Square Test:

    Tested independence between two categorical variables (e.g., Category and Region).

8. ANOVA:

    Tested if the average profit differs across multiple product categories.

9. Correlation Analysis:

    Displayed correlation matrix and heatmap between numeric variables like Sales and Profit.

10. Pivot Tables and Group Summaries:

    Shows average sales / profit by region and category using pivot tables and groupby.


### Conclusion

The overall sales and profit data are highly skewed by a few high-value transactions and significant outliers.

There are distinct performance patterns across product categories and regions.

No significant difference in average profit between East and West regions, nor any dependency between category and region were found.

A significant difference in mean profit exists across categories with **Technology** generally having **higher profits.**

The **Furniture** category in the **central region** shows **negative average profit**

highlighting a specific area requiring **immediate strategic attention** to mitigate losses.
