# Step 1: Import essential librariesAdd commentMore actions
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Models
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

# Metrics
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, roc_curve, auc, classification_report

# Ignore warnings for cleaner output
import warnings
warnings.filterwarnings('ignore')

# step 2: Upload file manually in Colab
from google.colab import files
uploaded = files.upload()

# Load from local upload or path
df = pd.read_csv('spam_ham_dataset.csv')  # Replace with your file
df.head()

df.tail()

# Step 3: Data Preprocessing
# Basic info
df.info()

# Check for missing values
print(df.isnull().sum())

# We'll focus on 'label' and 'text' columns
df = df[['label', 'text']]

# Encode labels (ham = 0, spam = 1)
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# Check balance of classes
df['label'].value_counts()

# Step 4: Vectorize the text data using TF-IDF
# Initialize vectorizer
tfidf = TfidfVectorizer(stop_words='english', max_df=0.7)

# Transform the text data
X = tfidf.fit_transform(df['text'])
y = df['label']

# Step 5: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Step 6:  Train Models
lr = LogisticRegression()
lr.fit(X_train, y_train)
y_pred_lr = lr.predict(X_test)

rf = RandomForestClassifier(random_state=42)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)

# Step 7 : Evaluate the models
def evaluate_model(y_test, y_pred, model_name):
    print(f"--- {model_name} ---")
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Precision:", precision_score(y_test, y_pred))
    print("Recall:", recall_score(y_test, y_pred))
    print("F1 Score:", f1_score(y_test, y_pred))
    print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
    print("\nClassification Report:\n", classification_report(y_test, y_pred))

evaluate_model(y_test, y_pred_lr, "Logistic Regression")
evaluate_model(y_test, y_pred_rf, "Random Forest")

# Step 8: Confusion matrix visualization
def plot_confusion(y_test, y_pred, title):
    cm = confusion_matrix(y_test, y_pred)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title(title)
    plt.ylabel('Actual')
    plt.xlabel('Predicted')
    plt.show()

plot_confusion(y_test, y_pred_lr, "Logistic Regression Confusion Matrix")
plot_confusion(y_test, y_pred_rf, "Random Forest Confusion Matrix")

# Step 9: ROC Curve
def plot_roc(y_test, y_proba, title):
    fpr, tpr, _ = roc_curve(y_test, y_proba)
    roc_auc = auc(fpr, tpr)
    plt.plot(fpr, tpr, label=f'{title} (AUC = {roc_auc:.2f})')
    plt.plot([0,1], [0,1], 'k--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve')
    plt.legend()
    plt.show()

# Predict proba
plot_roc(y_test, lr.predict_proba(X_test)[:,1], 'Logistic Regression')
plot_roc(y_test, rf.predict_proba(X_test)[:,1], 'Random Forest')

# Step 10 :  Hyperparameter Tuning
param_grid = {
    'max_depth': [None, 10, 20],
    'n_estimators': [50, 100, 200]
}

grid = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, cv=3, scoring='f1')
grid.fit(X_train, y_train)

print("Best parameters:", grid.best_params_)
best_rf = grid.best_estimator_
y_pred_best_rf = best_rf.predict(X_test)

evaluate_model(y_test, y_pred_best_rf, "Tuned Random Forest")

# Step 11:  Feature Importance
# Get feature importances
importances = best_rf.feature_importances_
indices = np.argsort(importances)[-10:]  # Top 10

# Map back to feature names
features = np.array(tfidf.get_feature_names_out())[indices]

#step 12: Plot
plt.barh(features, importances[indices])
plt.title("Top 10 Important Features (Random Forest)")
plt.show()
