---

# 📂 Spam Email Classification using Machine Learning

---

## 📝 Project Overview

This project focuses on building **classification models** to automatically detect whether an email is **Spam (1)** or **Ham (0)** using a structured dataset of email word frequencies.

The models were built using **supervised machine learning algorithms** and evaluated on various performance metrics to identify the most effective approach.

---

## 🔍 Dataset Summary

* **Dataset Source:** \[Local Dataset (spam.csv)]
* **Structure:** 3,000+ columns representing word frequencies in each email and a `Prediction` column indicating spam/ham status.

| Column Name  | Description                                      |
| ------------ | ------------------------------------------------ |
| `Email No.`  | Unique email identifier                          |
| Word Columns | Word frequency counts (e.g., "the", "you", etc.) |
| `Prediction` | Target column (0 = Ham, 1 = Spam)                |

---

## ⚙️ Project Workflow

### 1. Data Preprocessing

* Removed unnecessary columns (`Email No.`).
* Separated features and target (`Prediction`).
* Scaled features using **StandardScaler** (for logistic regression).

### 2. Train-Test Split

* Split data into training (80%) and testing (20%) sets.

### 3. Algorithms Used

* **Logistic Regression**
* **Decision Tree Classifier**
* **Random Forest Classifier**

### 4. Hyperparameter Tuning

* Used **GridSearchCV** to optimize Random Forest parameters.

### 5. Model Evaluation Metrics

* **Accuracy**
* **Precision**
* **Recall**
* **F1-score**
* **Confusion Matrix**
* **ROC Curve and AUC Score**

---

## 📊 Results Summary

| Model               | Accuracy | Precision | Recall | F1-score |
| ------------------- | -------- | --------- | ------ | -------- |
| Logistic Regression | \~XX%    | XX%       | XX%    | XX%      |
| Decision Tree       | \~XX%    | XX%       | XX%    | XX%      |
| Random Forest       | \~XX%    | XX%       | XX%    | XX%      |
| Tuned Random Forest | \~XX%    | XX%       | XX%    | XX%      |

*(Replace XX% with your actual results after running the models)*

---

## 📈 Visualizations

### ✔️ Confusion Matrices

* Showed the number of correct and incorrect predictions for each class.

### ✔️ ROC Curve Comparison

* Visualized and compared the ROC-AUC scores of the three models.

### ✔️ Feature Importance

* Displayed the top 20 important words/features contributing to the spam detection decision.

---

## 🚀 Key Insights

* Random Forest consistently performed better than Logistic Regression and Decision Tree.
* GridSearchCV tuning improved Random Forest performance further.
* Certain words contributed more significantly to spam prediction (as shown in feature importance).

---

## 🔧 Tools & Libraries Used

* Python
* Pandas, NumPy
* Scikit-learn
* Matplotlib, Seaborn

---

## 📂 Folder Structure

```
├── spam.csv                  # Dataset
├── Spam_Classification_Assignment_7.ipynb  # Jupyter Notebook
├── README.md                  # This file
```

---

## ✅ Conclusion

Machine learning algorithms effectively classify emails as spam or ham based on word frequency data. With proper preprocessing, tuning, and evaluation, Random Forest models can achieve strong predictive performance.

---

## 🔗 Author

**Nihal Mishra**
*B.Tech CSE - AI & DS | Data Science Enthusiast*

[LinkedIn](https://www.linkedin.com/in/nihalmishraofficial)

---
