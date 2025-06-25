# 📊 Project Summary – Exploratory Data Analysis on Titanic Dataset

This project involves a thorough Exploratory Data Analysis (EDA) of the Titanic dataset to uncover key insights about the survival of passengers aboard the ship. The dataset contains demographic, class, fare, and survival-related information for each passenger.

---

## ✅ Key Steps Performed

### 📥 Data Loading
- Loaded the dataset (`tested.csv`) using Pandas.

### 🧹 Data Cleaning
- Filled missing values in the `Age` and `Embarked` columns.
- Dropped the `Cabin` column due to too many null values.
- Removed duplicate entries to ensure data integrity.

### 📈 Summary Statistics
- Used `info()`, `describe()`, and `value_counts()` to explore dataset structure.

### 📊 Visualizations
- Created histograms for Age distribution.
- Box plots for Age vs Pclass.
- Count plots to show survival breakdown by gender.
- Violin plots to illustrate survival trends by class and age.
- Correlation heatmap and pair plot to examine feature relationships.

### 👥 Group Analysis
- Used `groupby()` to explore survival rates across gender and class.

### 🏗️ Feature Engineering
- Introduced a `FamilySize` column (`SibSp + Parch + 1`) to measure family impact on survival.

### 🧠 Top 5 Insights Documented
- Key takeaways captured in Markdown format for clarity.

---

## 🌟 Top 5 Insights

1. **Females had a significantly higher survival rate** than males.
2. **First-class passengers had the highest likelihood** of survival.
3. **Children under 10 years old** showed notably better survival chances.
4. **Small family groups (2–4 members)** had higher survival rates than those traveling alone or in large groups.
5. **Paying a higher fare** was generally linked to increased survival probability.

---

## 🧩 Tools Used

- **Python (Jupyter Notebook)**
- **Libraries**: Pandas, NumPy, Matplotlib, Seaborn
