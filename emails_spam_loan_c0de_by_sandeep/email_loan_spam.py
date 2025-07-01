from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report


emails = [
    "Claim your free prize now!",
    "Meeting at 10am tomorrow",
    "Win money by clicking this link",
    "Lunch at the cafe?",
    "Earn from home without work",
    "Project deadline extended"
]
labels = ['spam', 'ham', 'spam', 'ham', 'spam', 'ham']


X_train, X_test, y_train, y_test = train_test_split(emails, labels, test_size=0.3, random_state=42)
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)


model = MultinomialNB()
model.fit(X_train_vec, y_train)


y_pred = model.predict(X_test_vec)
print(classification_report(y_test, y_pred))
