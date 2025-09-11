import pandas as pd
import numpy as np
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Download NLTK stopwords
nltk.download('stopwords')

# Sample dataset
data = {
    'text': [
        'Win a free prize now! Click here!',
        'Meeting scheduled for tomorrow at 3pm',
        'You have won $1000! Claim your reward',
        'Hi John, just checking in about the project',
        'Limited time offer! 50% off all products',
        'Reminder: Team lunch on Friday',
        'Congratulations! You are selected for a free gift',
        'Please find attached the report you requested',
        'Urgent! Your account has been compromised',
        'Weekly status update meeting'
    ],
    'label': ['spam', 'ham', 'spam', 'ham', 'spam', 'ham', 'spam', 'ham', 'spam', 'ham']
}

# Create DataFrame
df = pd.DataFrame(data)

# Preprocessing function
def preprocess_text(text):
    text = text.lower()  # lowercase
    text = ''.join([char for char in text if char not in string.punctuation])  # remove punctuation
    words = text.split()  # tokenize
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]  # remove stopwords
    stemmer = PorterStemmer()
    words = [stemmer.stem(word) for word in words]  # stemming
    return ' '.join(words)

# Apply preprocessing
df['processed_text'] = df['text'].apply(preprocess_text)

# Features and labels
X = df['processed_text']
y = df['label']

# TF-IDF vectorization
vectorizer = TfidfVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.3, random_state=42)

# Train Naive Bayes model
model = MultinomialNB()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
print("Model Evaluation:")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Predict a new email
new_email = ["Congratulations! You've won a free vacation. Click now to claim!"]
processed_email = preprocess_text(new_email[0])
email_vectorized = vectorizer.transform([processed_email])
prediction = model.predict(email_vectorized)

print("\nExample Prediction:")
print("Email:", new_email[0])
print("Prediction:", prediction[0])
