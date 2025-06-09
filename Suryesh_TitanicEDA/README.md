# 🚢 Titanic Survival Analysis - Exploratory Data Analysis (EDA)

This project performs a full Exploratory Data Analysis (EDA) on the [Titanic dataset](https://www.kaggle.com/c/titanic/data), aiming to uncover key patterns related to passenger survival.

---

## 📁 Project Structure
```
Titanic_EDA_Project/
├── train.csv # Titanic dataset (from Kaggle)
├── Titanic_EDA.py # Main EDA script (VS Code compatible)
└── images/ # Folder with saved plots
```

---

## 📊 Key EDA Steps

- ✅ Data loading and basic inspection
- ✅ Handling missing values (`Age`, `Embarked`, dropped `Cabin`)
- ✅ Summary statistics and data types
- ✅ Visual exploration using Seaborn & Matplotlib
- ✅ Feature engineering: `FamilySize = SibSp + Parch + 1`

---

## 📈 Visualizations Saved in `images/` Folder

- `survival_count.png` — Overall survival distribution
- `age_distribution.png` — Histogram of passenger ages
- `fare_boxplot.png` — Fare distribution using boxplot
- `survival_by_gender.png` — Survival rate by gender
- `survival_by_class.png` — Survival rate by class
- `correlation_heatmap.png` — Heatmap of numeric correlations
- `survival_vs_familysize.png` — Violin plot: FamilySize vs Survival

---

## 🔍 Top Insights
- 🎯 **Females** had a much higher chance of survival than males.
- 🛳️ Passengers in **1st class** were more likely to survive.
- 👶 Younger children had better survival rates than middle-aged adults.
- 💸 Passengers who paid **higher fares** had better survival rates.
- 👨‍👩‍👧 Larger **FamilySize** generally correlated with lower survival.

---

## 📦 Dependencies

Ensure you have the following libraries installed:

```bash
pip install pandas matplotlib seaborn
```
## 📥 Dataset Source

Download the dataset from: [Kaggle Titanic Competition](https://www.kaggle.com/c/titanic/data)

---
## 🏁 How to Run
```
python Titanic_EDA.py

```
## 🧑‍💻 Author

**Suryesh Pandey**  
B.Sc. (Computing), 2nd Year  
Bennett University

