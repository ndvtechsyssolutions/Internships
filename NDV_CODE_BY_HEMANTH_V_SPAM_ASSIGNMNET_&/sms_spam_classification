# 📌 Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import zipfile
import os
import warnings
warnings.filterwarnings("ignore")

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (accuracy_score, precision_score, recall_score,
                             f1_score, confusion_matrix, classification_report,
                             roc_curve, auc)

# 📁 Upload ZIP and Extract
from google.colab import files
uploaded = files.upload()

with zipfile.ZipFile("sms_spam_datase_csv.zip", 'r') as zip_ref:
    zip_ref.extractall()

print("\nExtracted files:", os.listdir())

# 📄 Load CSV with proper encoding
csv_files = [f for f in os.listdir() if f.endswith('.csv')]
print("\nUsing file:", csv_files[0])

data = pd.read_csv(csv_files[0], encoding='latin1')

# 🧹 Preprocess
print("\nOriginal columns:", data.columns.tolist())

if 'v1' in data.columns and 'v2' in data.columns:
    data = data[['v1', 'v2']]
    data.columns = ['label', 'text']
else:
    data = data[['label', 'text']]

data['label'] = data['label'].map({'ham': 0, 'spam': 1})

print("\nData sample:")
print(data.sample(5))

# 🔤 Text Vectorization
vectorizer = TfidfVectorizer(stop_words='english', max_df=0.8)
features = vectorizer.fit_transform(data['text'])
labels = data['label']

# 📊 Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    features, labels, test_size=0.25, random_state=1, stratify=labels
)

# 🤖 Train Models
model_lr = LogisticRegression()
model_rf = RandomForestClassifier(random_state=1)
model_sgd = SGDClassifier(loss='log_loss', random_state=1)

model_lr.fit(X_train, y_train)
model_rf.fit(X_train, y_train)
model_sgd.fit(X_train, y_train)

# 🔍 Predictions
pred_lr = model_lr.predict(X_test)
pred_rf = model_rf.predict(X_test)
pred_sgd = model_sgd.predict(X_test)

# 📈 Evaluation Function
def show_metrics(y_true, y_pred, title):
    print(f"\n🧪 {title}")
    print("Accuracy:", accuracy_score(y_true, y_pred))
    print("Precision:", precision_score(y_true, y_pred))
    print("Recall:", recall_score(y_true, y_pred))
    print("F1 Score:", f1_score(y_true, y_pred))
    print("Confusion Matrix:\n", confusion_matrix(y_true, y_pred))

show_metrics(y_test, pred_lr, "Logistic Regression")
show_metrics(y_test, pred_rf, "Random Forest")
show_metrics(y_test, pred_sgd, "SGD Classifier")

# 🧱 Confusion Matrix Plot
def draw_cm(y_actual, y_predicted, title):
    cmatrix = confusion_matrix(y_actual, y_predicted)
    sns.heatmap(cmatrix, annot=True, fmt="d", cmap="magma")
    plt.title(title)
    plt.ylabel("Actual")
    plt.xlabel("Predicted")
    plt.show()

draw_cm(y_test, pred_lr, "Confusion Matrix - Logistic Regression")
draw_cm(y_test, pred_rf, "Confusion Matrix - Random Forest")
draw_cm(y_test, pred_sgd, "Confusion Matrix - SGD Classifier")

# 🧬 ROC Curve Plot
def plot_auc(model, name):
    probs = model.predict_proba(X_test)[:, 1]
    fpr, tpr, _ = roc_curve(y_test, probs)
    roc_auc = auc(fpr, tpr)
    plt.plot(fpr, tpr, label=f'{name} AUC = {roc_auc:.2f}')

plt.figure(figsize=(8, 5))
plot_auc(model_lr, "LogReg")
plot_auc(model_rf, "RandomForest")
plot_auc(model_sgd, "SGD")
plt.plot([0, 1], [0, 1], 'k--')
plt.title("ROC Curve Comparison")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.legend()
plt.grid()
plt.show()

# 🛠️ Hyperparameter Tuning for Random Forest
params = {
    'n_estimators': [100, 150],
    'max_depth': [None, 15]
}
grid_rf = GridSearchCV(RandomForestClassifier(random_state=1), params, cv=3, scoring='f1')
grid_rf.fit(X_train, y_train)

print("\n📌 Best Parameters:", grid_rf.best_params_)
best_rf_model = grid_rf.best_estimator_
best_preds = best_rf_model.predict(X_test)

show_metrics(y_test, best_preds, "Optimized Random Forest")

# ⭐ Feature Importance
importance_vals = best_rf_model.feature_importances_
top10_idx = np.argsort(importance_vals)[-10:]
top_features = np.array(vectorizer.get_feature_names_out())[top10_idx]

plt.figure(figsize=(7, 4))
plt.barh(top_features, importance_vals[top10_idx], color='teal')
plt.title("Top 10 Important Features - Random Forest")
plt.xlabel("Importance")
plt.tight_layout()
plt.show()
