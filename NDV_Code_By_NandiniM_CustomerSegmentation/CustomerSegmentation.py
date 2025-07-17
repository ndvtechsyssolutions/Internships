#Customer Segmentation
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from koko import files
import io
import zipfile
import warnings
warnings.filterwarnings('ignore')

uploaded = files.upload()

for filename in uploaded.keys():
    if filename.endswith('.zip'):
        with zipfile.ZipFile(io.BytesIO(uploaded[filename]), 'r') as zip_ref:
            zip_ref.extractall()
            for name in zip_ref.namelist():
                if name.endswith('.csv'):
                    df = pd.read_csv(name)
    elif filename.endswith('.csv'):
        df = pd.read_csv(io.BytesIO(uploaded[filename]))

df.columns = df.columns.str.strip()
print(df.columns.tolist())

if 'CustomerID' in df.columns:
    df.drop(columns=["CustomerID"], inplace=True)

gender_col = 'Gender' if 'Gender' in df.columns else ('Genre' if 'Genre' in df.columns else None)

if gender_col:
    plt.figure(figsize=(8,7))
    sns.countplot(data=df, x=gender_col)
    plt.show()

    plt.figure(figsize=(20,7))
    sns.countplot(data=df, x="Age", hue=gender_col)
    plt.show()

plt.figure(figsize=(10,8))
sns.histplot(df["Age"], color="green", bins=20)
plt.show()

plt.figure(figsize=(18,7))
sns.countplot(x="Age", data=df)
plt.show()

plt.figure(figsize=(30,7))
for i, column in enumerate(df.columns[1:], 1):
    plt.subplot(1, 4, i)
    sns.histplot(df[column], kde=True, color="green")
    plt.xlabel(column)
plt.tight_layout()
plt.show()

X = df.iloc[:, [2, 3]].values

plt.figure(figsize=(12,8))
plt.scatter(X[:, 0], X[:, 1])
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.show()

kmeans = KMeans(n_clusters=2, random_state=42)
kmeans.fit(X)
plt.figure(figsize=(12,8))
plt.scatter(X[:,0], X[:,1], c=kmeans.labels_, cmap='rainbow')
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], color='black')
plt.show()

kmeans_10 = KMeans(n_clusters=10, random_state=42)
kmeans_10.fit(X)
plt.figure(figsize=(12,8))
plt.scatter(X[:,0], X[:,1], c=kmeans_10.labels_, cmap='rainbow')
plt.scatter(kmeans_10.cluster_centers_[:,0], kmeans_10.cluster_centers_[:,1], color='black')
plt.show()

wcss = []
for i in range(1, 11):
    km = KMeans(n_clusters=i, random_state=42)
    km.fit(X)
    wcss.append(km.inertia_)

plt.figure(figsize=(12, 8))
plt.plot(range(1, 11), wcss, marker='8', color='blue')
plt.xticks(range(1, 11))
plt.grid(True)
plt.show()
