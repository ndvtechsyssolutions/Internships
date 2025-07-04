import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,confusion_matrix
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('spam_mail.csv')
df.head()

le = LabelEncoder()
df['text_enc'] = le.fit_transform(df['text'])
df['label_enc'] = le.fit_transform(df['label'])

X = df[['text_enc','label_enc']]
y = df['label_num']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.3,random_state = 42)
model = DecisionTreeClassifier(criterion = 'gini',random_state = 42,max_depth = 3)

model.fit(X_train,y_train)

y_pred = model.predict(X_test)

print("Accuracy : ",accuracy_score(y_test,y_pred))
print("Precision : ",precision_score(y_test,y_pred))
print("Recall : ",recall_score(y_test,y_pred))
print("F1 Score : ",f1_score(y_test,y_pred))
print("Confusion Matrix : \n",confusion_matrix(y_test,y_pred))


plot_tree(model,filled = True)
plt.show()

X = df[['text_enc']]
y = df['label_num']
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.3,random_state = 42)

lr = LogisticRegression()
lr.fit(X_train,y_train)

y_pre = lr.predict(X_test)

print("Accuracy : ",accuracy_score(y_test,y_pre))
print("Precision : ",precision_score(y_test,y_pre))
print("Recall : ",recall_score(y_test,y_pre))
print("F1 Score : ",f1_score(y_test,y_pre))
print("Confusion Matrix : \n",confusion_matrix(y_test,y_pre))

plt.scatter(X,y, color='blue', label='Actual')
plt.plot(X, model.predict(X), color='red', label='Predicted')
plt.title("Logistic Regression")
plt.legend()
plt.grid(True)
plt.show()
