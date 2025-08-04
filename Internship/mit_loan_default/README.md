# Loan Default Prediction

This project focuses on building and evaluating machine learning models to predict loan defaults. 

The analysis is performed using Python, pandas, scikit-learn, and matplotlib/seaborn for data manipulation, modeling, and visualization.

### Summary:

The primary objective of this project is to develop a robust predictive model that can identify potential loan defaults based on various borrower and loan characteristics. 

We employ a supervised learning approach, utilizing Logistic Regression, Decision Tree Classifier, and Random Forest Classifier to classify loan applications as either 'Default' or 'No Default'. 

The process involves thorough data preprocessing, including handling categorical features and scaling numerical ones, followed by comprehensive model evaluation.

### Approach:

**Data Loading and Initial Inspection:**

The ```Loan_default.csv``` dataset is loaded into a pandas DataFrame.

The ```LoanID``` column is dropped as it is an identifier and not relevant for model training.

Initial checks are performed to understand the data structure, identify missing values (none found in this dataset), and check for duplicate entries (none found).

**Feature and Target Variable Definition:**

The target variable y is defined as the Default column (0 for No Default, 1 for Default).

All other columns are designated as features X.

**Column Categorization:**

**Numerical Columns:**

Identified automatically using X.select_dtypes(include=np.number). 

These include Age, Income, LoanAmount, CreditScore, MonthsEmployed, NumCreditLines, InterestRate, LoanTerm, and DTIRatio.

**One-Hot Encoded Columns:**

Categorical features with no inherent order are selected for one-hot encoding: Education, EmploymentType, MaritalStatus, and LoanPurpose.

**Label Encoded Columns:**

Binary or ordinal categorical features are selected for ordinal encoding: HasMortgage, HasDependents, and HasCoSigner.

**Preprocessing Pipeline:**

A ColumnTransformer is used to apply different preprocessing steps to different types of columns:

StandardScaler is applied to numerical columns to normalize their range.

OneHotEncoder is used for one-hot encoded columns to convert categorical values into a binary matrix. handle_unknown='ignore' is set to prevent errors during prediction if unseen categories appear.

OrdinalEncoder is used for label encoded columns to convert categories to numerical labels.

remainder='passthrough' ensures that any columns not explicitly listed in the transformers are kept in the dataset.

**Data Splitting:**

The dataset is split into training and testing sets using train_test_split with an 80/20 ratio (test_size=0.2).

random_state=42 is used for reproducibility.

stratify=y is crucial to ensure that the proportion of default and non-default cases is maintained in both the training and testing sets, which is important for imbalanced datasets.

**Model Training and Evaluation:**

Three classification models are implemented within a Pipeline (preprocessing + classifier):

**Logistic Regression:**

A linear model for binary classification. class_weight='balanced' is used to handle potential class imbalance.

**Decision Tree Classifier:**

A non-linear model that makes decisions based on feature values. class_weight='balanced' is also applied here.

**Random Forest Classifier:**

An ensemble method that builds multiple decision trees and merges their predictions to improve accuracy and control overfitting. class_weight='balanced' is used.

For each model, the following metrics are calculated and printed:

**Accuracy:** 

Overall correctness of predictions.

**Precision:** 

Proportion of positive identifications that were actually correct.

**Recall (Sensitivity):** 

Proportion of actual positives that were correctly identified.

**F1-Score:**

Harmonic mean of precision and recall.

**Confusion Matrix:**

A table showing true positives, true negatives, false positives, and false negatives. A heatmap visualization of the confusion matrix is displayed.

**ROC Curve and AUC (Area Under the Curve):**

Visualizes the trade-off between true positive rate and false positive rate. AUC provides a single metric to summarize the curve's performance.

---

# Results:

The results highlight significant differences in how each model performs, especially concerning the highly imbalanced nature of loan default prediction (where defaults are rare). 

The class_weight='balanced' parameter attempts to mitigate this, but its effectiveness varies.

**Logistic Regression:**

Achieves a relatively high **Recall** (```0.6992```), meaning it correctly identifies about 70% of actual defaults. 

This is a crucial metric for loan default prediction, as missing a default can be costly.

However, its **Precision** (```0.2196```) is **very low**, indicating a high number of false positives (predicting default when there isn't one). 

This means many non-defaulting loans would be flagged incorrectly.

The **F1-Score** (```0.3342```) is moderate, reflecting the trade-off between its good recall and poor precision. 

The **ROC AUC** of 0.75 suggests it has decent discriminative power overall.

**Decision Tree Classifier:**

Shows a much higher **Accuracy** (```0.8171```) than Logistic Regression, likely due to its ability to correctly classify the majority class (non-defaults).

However, its **Precision** (```0.2052```) and **Recall** (```0.2000```) are very low, leading to a poor **F1-Score** (```0.2025```). 

This indicates that while it's accurate overall, it's **poor at identifying actual defaults** and also produces many false positives. 

The **ROC AUC** of 0.55 is barely better than random chance (```0.5```), confirming its weak performance in distinguishing between the two classes.

**Random Forest Classifier:**

Achieves the highest **Accuracy** (```0.8847```) and **Precision** (```0.6414```), indicating it's very good at correctly classifying non-defaults and, when it predicts a default, it's often correct.

Crucially, its **Recall** (```0.0157```) **is extremely low**, resulting in a very low **F1-Score** (```0.0306```). 

This means the model **misses almost all actual loan defaults**, which is a significant drawback for this problem. 

Despite a decent **ROC AUC** of 0.74, its practical utility for identifying defaults is severely limited due to the low recall. The confusion matrix for Random Forest clearly shows a very high number of false negatives (5838) and a very low number of true positives (```93```).

**Overall Conclusion:**

Based on these results, **none of the models perfectly balance the need for high recall (identifying defaults) and high precision (minimizing false alarms).**

**Logistic Regression** offers the best recall for identifying defaults among the three, but at the cost of many false positives.

**Decision Tree Classifier** performs poorly across all key metrics for default prediction.

**Random Forest Classifier**, while having high overall accuracy and precision for its positive predictions, **fails to identify the vast majority of actual defaults**, making it unsuitable for a task where identifying defaults is paramount.
