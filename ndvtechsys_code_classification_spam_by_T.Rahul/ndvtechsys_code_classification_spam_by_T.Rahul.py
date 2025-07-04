## assignment-7
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_auc_score, roc_curve
df = pd.read_csv('spam_ham_dataset.csv')
df.head()

# Load data
df = pd.read_csv('spam_ham_dataset.csv')

# Drop unnecessary columns
df.drop(columns=['Unnamed: 0', 'label_num'], inplace=True)

# Rename columns
df.rename(columns={'label': 'target', 'text': 'message'}, inplace=True)

# Check for missing values
print(df.isnull().sum())

# Encode target: ham = 0, spam = 1
df['target'] = df['target'].map({'ham': 0, 'spam': 1})

# Vectorize message using TF-IDF
tfidf = TfidfVectorizer(stop_words='english', max_df=0.7)
X = tfidf.fit_transform(df['message'])
y = df['target']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
##Logistic Regression
lr_model = LogisticRegression()
lr_model.fit(X_train, y_train)
y_pred_lr = lr_model.predict(X_test)

##Random Forest
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train, y_train)
y_pred_rf = rf_model.predict(X_test)

##Evaluate the model using accuracy, precision, recall, F1-score, and confusion matrix.
def evaluate_model(y_true, y_pred, model_name):
    print(f"\n--- {model_name} ---")
    print("Accuracy:", accuracy_score(y_true, y_pred))
    print("Classification Report:\n", classification_report(y_true, y_pred))
    cm = confusion_matrix(y_true, y_pred)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Purples')
    plt.title(f'{model_name} - Confusion Matrix')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.show()
evaluate_model(y_test, y_pred_lr, "Logistic Regression")
evaluate_model(y_test, y_pred_rf, "Random Forest")

##Visualize model performance using confusion matrix and ROC curve.
def plot_roc_curve(model, X_test, y_test, label):
    probs = model.predict_proba(X_test)[:, 1]
    fpr, tpr, _ = roc_curve(y_test, probs)
    auc_score = roc_auc_score(y_test, probs)
    plt.plot(fpr, tpr, label=f'{label} (AUC = {auc_score:.2f})')

plt.figure(figsize=(8, 6))
plot_roc_curve(lr_model, X_test, y_test, "Logistic Regression")
plot_roc_curve(rf_model, X_test, y_test, "Random Forest")
plt.plot([0,1],[0,1],'k--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curves')
plt.legend()
plt.grid(True)
plt.show()

## GridSearchCV (Random Forest)
param_grid = {
    'n_estimators': [50, 100],
    'max_depth': [10, None],
    'min_samples_split': [2, 5]
}
grid_rf = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, cv=3, scoring='accuracy')
grid_rf.fit(X_train, y_train)
print("Best Parameters:", grid_rf.best_params_)
best_rf = grid_rf.best_estimator_
y_pred_best_rf = best_rf.predict(X_test)
evaluate_model(y_test, y_pred_best_rf, "Random Forest (Tuned)")

##Feature Importance
importances = best_rf.feature_importances_
indices = np.argsort(importances)[-20:]
features = np.array(tfidf.get_feature_names_out())[indices]
plt.figure(figsize=(10, 6))
plt.barh(features, importances[indices])
plt.xlabel("Importance")
plt.title("Top 20 TF-IDF Words in Random Forest")
plt.show()
