import pandas as pd

# Load Kaggle heart dataset
df = pd.read_csv("heart.csv")
print(df.head())


# Initial Exploration and Cleaning
print(df.info())
print(df.describe())
print(df.isnull().sum())


# Visualize Relationships
import seaborn as sns
import matplotlib.pyplot as plt

# Correlation heatmap
plt.figure(figsize=(12,8))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Feature Correlation Heatmap")
plt.show()



# Distribution of target classes
sns.countplot(data=df, x='target')
plt.title("Target Class Distribution")
plt.show()




# Age vs. Heart Disease
sns.boxplot(x='target', y='age', data=df)
plt.title("Age vs. Heart Disease")
plt.show()

# Preprocessing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X = df.drop("target", axis=1)
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# Model Training + Tuning

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

param_grid = {
    'n_estimators': [100, 150],
    'max_depth': [4, 6, 8],
    'min_samples_split': [2, 4]}

rf = RandomForestClassifier(random_state=42)
grid = GridSearchCV(rf, param_grid, cv=5)
grid.fit(X_train, y_train)

print("Best Parameters:", grid.best_params_)


# Evaluate the Model
from sklearn.metrics import classification_report, confusion_matrix
y_pred = grid.predict(X_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
