# 🏏IPL Match Dataset – Data Cleaning & Preprocessing

### 📁 Project Title:
**IPL Dataset Cleaning & EDA**  
*Internship Project – AI/ML with Data Analytics*  
**Organization:** NDVS Techys  
**Mentor:** Srinu Sir  
**Director:** Durga Inturi Ma'am

---

### 📌 Project Overview

This project focuses on cleaning, preprocessing, and conducting exploratory data analysis (EDA) on the **Indian Premier League (IPL) Match Dataset** containing records from **2008 to 2024**.

The goal was to prepare clean, structured data for further analysis and potential modeling. This was done as part of my Data Analytics Internship at **NDVS Techys**.

---

### 📊 Dataset Highlights

- **Total Records:** 1,095 matches  
- **Columns Before Cleaning:** 20  
- **Columns After Cleaning:** 18  
- **Time Span:** IPL Seasons from 2008 to 2024  
- **Data Source:** Kaggle (matches.csv)

---

### ✅ Cleaning Tasks Performed

- Removed irrelevant columns: `method`, `super_over`
- Handled missing values in:
  - `city` (51 missing)
  - `player_of_match` (5 missing)
  - `winner` (5 missing)
  - `result_margin`, `target_runs`, `target_overs`
- Converted `date` column to datetime format
- Extracted a new `year` column from the match date
- Checked for and confirmed: No duplicate values

---

### 📈 Exploratory Visualizations

- Count of matches by **match type** (League, Qualifier, Final)
- Wins by **team**
- Match frequency across **cities**
- Year-wise IPL match count

Visuals created using:
- **Seaborn**
- **Matplotlib**

---

### 🛠️ Tools & Libraries

- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- Jupyter Notebook

---

### 🔁 Output

- Cleaned dataset saved as: `cleaned_matches.csv`  
- Dataset ready for predictive modeling or deep EDA

---

### 🙌 Acknowledgment

This project was completed as a hands-on exercise under the mentorship of **Srinu Sir** and leadership of **Durga Inturi Ma’am** during my internship at **NDVS Techys**. Their guidance helped me deeply understand the importance of data preprocessing in the ML pipeline.

---------------
