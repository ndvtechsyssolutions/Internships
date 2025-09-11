# 📧 Spam Email Classification

## 📝 Project Overview

This project focuses on classifying emails as **Spam** or **Ham (Not Spam)** using machine learning techniques. The task is part of an assignment to build a supervised learning model, evaluate its performance, and explain its behavior using feature importance and visualizations.

## 📂 Dataset

- **Source:** [Spam Mails Dataset on Kaggle](https://www.kaggle.com/datasets/venky73/spam-mails-dataset)
  
- **Description:** The dataset contains labeled email messages, with each entry categorized as either `spam` or `ham` (not spam).
- 
- **Features Used:** The email text was converted into numerical features using TF-IDF vectorization.

## ⚙️ Project Workflow

1. **Data Preprocessing**

   - Checked for missing values (none found).
     
   - Used only `label` and `text` columns.

   - Encoded labels (`ham` = 0, `spam` = 1).

   - Applied TF-IDF vectorization on email text.

3. **Modeling**

   - Split data into 80% training and 20% testing.
     
   - Built and evaluated:
     
     - Logistic Regression
       
     - Random Forest

     - Tuned Random Forest (using GridSearchCV)

5. **Evaluation Metrics**

   - Accuracy

   - Precision

   - Recall

   - F1-Score

   - Confusion Matrix

   - ROC Curve

6. **Explainability**

   - Displayed top important features from the Random Forest model.

---

## 💻 Technologies Used

| Tool / Library | Purpose |
|----------------|---------|
| **Python 3.x** | Programming language |
| **Pandas** | Data manipulation and analysis |
| **NumPy** | Numerical operations |
| **Scikit-learn** | Machine learning models, evaluation metrics, hyperparameter tuning |
| **Matplotlib / Seaborn** | Data visualization and plotting |
| **Google Colab** | Cloud-based Jupyter Notebook environment |
| **TF-IDF Vectorizer** | Text feature extraction |
| **GridSearchCV** | Hyperparameter tuning |

---

## 📈 Visualizations

- ✅ Confusion matrices for each model

- ✅ ROC curves showing AUC for Logistic Regression and Random Forest

- ✅ Top 10 important features from the Random Forest classifier

---

## 🚀 How to Run

1. Open the Jupyter Notebook (`Spam_Email_Classification.ipynb`) in **Google Colab**.

2. Upload the dataset CSV file when prompted.

3. Run the notebook cells sequentially.

4. Review the output metrics and plots.

---

## 💡 Conclusions

- The models performed well on the dataset, with [best model] achieving the highest accuracy and balanced precision-recall.

- Feature importance from Random Forest highlighted key words contributing to spam classification.

- Hyperparameter tuning further improved the Random Forest model’s performance.
