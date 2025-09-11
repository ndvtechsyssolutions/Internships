# Import necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_auc_score, roc_curve

# Load dataset (Spam/Ham - can be downloaded from Kaggle or use below if available)
url = "https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv"
df = pd.read_csv(url, sep='\t', header=None, names=['label', 'message'])

# Encode target labels
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# Vectorize the text data
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['message'])
y = df['label']

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

lr_model = LogisticRegression()
lr_model.fit(X_train, y_train)
lr_pred = lr_model.predict(X_test)

# Evaluate Logistic Regression
print(" Logistic Regression Performance:")
print("Accuracy:", accuracy_score(y_test, lr_pred))
print("Classification Report:\n", classification_report(y_test, lr_pred))

# Confusion Matrix
sns.heatmap(confusion_matrix(y_test, lr_pred), annot=True, fmt='d', cmap='Blues')
plt.title("Confusion Matrix - Logistic Regression")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# ROC Curve
y_prob = lr_model.predict_proba(X_test)[:, 1]
fpr, tpr, thresholds = roc_curve(y_test, y_prob)
plt.plot(fpr, tpr, label='Logistic Regression')
plt.plot([0, 1], [0, 1], 'k--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend()
plt.grid(True)
plt.show()


nb_model = MultinomialNB()
nb_model.fit(X_train, y_train)
nb_pred = nb_model.predict(X_test)

# Evaluation for Naive Bayes
print(" Naive Bayes Performance:")
print("Accuracy:", accuracy_score(y_test, nb_pred))
print("Classification Report:\n", classification_report(y_test, nb_pred))

# Feature Importance for Logistic Regression (top features)
feature_names = vectorizer.get_feature_names_out()
coeffs = lr_model.coef_[0]
top_features = pd.DataFrame({'feature': feature_names, 'coefficient': coeffs})
top_positive = top_features.sort_values('coefficient', ascending=False).head(10)
top_negative = top_features.sort_values('coefficient').head(10)

# Plot top positive & negative features
plt.figure(figsize=(10, 5))
sns.barplot(x='coefficient', y='feature', data=top_positive, color='green')
plt.title("Top Words Predicting Spam (Positive Coefficients)")
plt.show()

plt.figure(figsize=(10, 5))
sns.barplot(x='coefficient', y='feature', data=top_negative, color='red')
plt.title("Top Words Predicting Ham (Negative Coefficients)")
plt.show()
