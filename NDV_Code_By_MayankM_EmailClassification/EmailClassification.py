# Description:- Classification of Emails into Spam/Ham 

# Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, roc_curve, auc
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling import SMOTE

import warnings
warnings.filterwarnings('ignore')

# Load dataset
try:
    df = pd.read_csv('spam.csv', encoding='latin-1')[['v1', 'v2']]
    df.columns = ['label', 'text']
    print("✅ Data loaded successfully.")
except FileNotFoundError:
    print("❌ 'spam.csv' not found.")
    raise

# Encode 'ham'=0, 'spam'=1
label_encoder = LabelEncoder()
df['label'] = label_encoder.fit_transform(df['label'])  # ham=0, spam=1

# Vectorize using TF-IDF
tfidf = TfidfVectorizer(stop_words='english', max_df=0.95)
X = tfidf.fit_transform(df['text'])
y = df['label']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# Apply SMOTE on training data
smote = SMOTE(random_state=42)
X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

# Scale data
scaler = StandardScaler(with_mean=False)
X_train_scaled = scaler.fit_transform(X_train_resampled)
X_test_scaled = scaler.transform(X_test)

# Train models
logreg = LogisticRegression()
logreg.fit(X_train_scaled, y_train_resampled)

rf = RandomForestClassifier(random_state=42)
rf.fit(X_train_scaled, y_train_resampled)

# Evaluate models
def evaluate_model(model, name):
    y_pred = model.predict(X_test_scaled)
    print(f"\n--- {name} ---")
    print(f"Accuracy:  {accuracy_score(y_test, y_pred):.4f}")
    print(f"Precision: {precision_score(y_test, y_pred):.4f}")
    print(f"Recall:    {recall_score(y_test, y_pred):.4f}")
    print(f"F1 Score:  {f1_score(y_test, y_pred):.4f}")
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

evaluate_model(logreg, "Logistic Regression")
evaluate_model(rf, "Random Forest")

# Plot confusion matrix
def plot_confusion_matrix(y_true, y_pred, title):
    cm = confusion_matrix(y_true, y_pred)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title(f'{title} - Confusion Matrix')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.show()

plot_confusion_matrix(y_test, logreg.predict(X_test_scaled), "Logistic Regression")
plot_confusion_matrix(y_test, rf.predict(X_test_scaled), "Random Forest")
OUPUT:-
✅ Data loaded successfully.

--- Logistic Regression ---
Accuracy:  0.9758
Precision: 0.9841
Recall:    0.8322
F1 Score:  0.9018
Confusion Matrix:
 [[964   2]
 [ 25 124]]

--- Random Forest ---
Accuracy:  0.9749
Precision: 1.0000
Recall:    0.8121
F1 Score:  0.8963
Confusion Matrix:
 [[966   0]
 [ 28 121]]

# ROC Curve
logreg_probs = logreg.predict_proba(X_test_scaled)[:, 1]
rf_probs = rf.predict_proba(X_test_scaled)[:, 1]

fpr1, tpr1, _ = roc_curve(y_test, logreg_probs)
fpr2, tpr2, _ = roc_curve(y_test, rf_probs)

plt.figure(figsize=(10,6))
plt.plot(fpr1, tpr1, label='Logistic Regression')
plt.plot(fpr2, tpr2, label='Random Forest')
plt.plot([0, 1], [0, 1], 'k--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend()
plt.grid()
plt.show()

# GridSearchCV for Random Forest
param_grid = {
    'n_estimators': [100, 200],
    'max_depth': [10, None],
    'min_samples_split': [2, 5]
}

grid_search = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, cv=3, scoring='accuracy', n_jobs=-1)
grid_search.fit(X_train_scaled, y_train_resampled)

print("Best Parameters:", grid_search.best_params_)

# Feature importance from Random Forest
importances = rf.feature_importances_
indices = np.argsort(importances)[-20:]
feature_names = np.array(tfidf.get_feature_names_out())

plt.figure(figsize=(10, 6))
plt.barh(range(20), importances[indices], align='center')
plt.yticks(np.arange(20), feature_names[indices])
plt.xlabel('Importance')
plt.title('Top 20 Important Features (Random Forest)')
plt.show()


