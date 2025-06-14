import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from warnings import filterwarnings
filterwarnings('ignore')

#Read dataset
df=pd.read_csv("netflix_titles.csv")

df.info()

df.describe().T

df.head()

df.tail()

df.shape

df.dtypes

#Check duplicate values
df.duplicated().sum()

#Check null values
df.isnull().sum().sort_values(ascending=False)

#Handling missing values
df['director'].fillna('Unknown',inplace=True)
df['country'].fillna('Unknown',inplace=True)
df['cast'].fillna('Not Specified',inplace=True)
df['duration'].fillna('Not Specified',inplace=True)
df['rating'].fillna(df['rating'].mode()[0],inplace=True)
df['date_added']=pd.to_datetime(df['date_added'], errors='coerce')

#Handle inconsistent data
df['country']=df['country'].replace({'United States if America':'United States'})

#EDA to find outliers
for i in df:
  sns.boxplot(df[[i]])

#Handle outliers
Q1 = df['release_year'].quantile(0.25)
Q3 = df['release_year'].quantile(0.75)
IQR = Q3 - Q1
outliers = (df['release_year'] < (Q1 - 1.5 * IQR)) | (df['release_year'] > (Q3 + 1.5 * IQR))
df=df.loc[~(outliers)]
sns.boxplot(df['release_year'])

from sklearn.preprocessing import LabelEncoder,StandardScaler

print("Type: ",df['type'].nunique())
#Label encoding
le = LabelEncoder()
df['type'] = le.fit_transform(df['type'])
df['type'].unique()

#Scaling
df_numeric=df.select_dtypes(include=['float64','int64'])
scaler=StandardScaler()
data=scaler.fit_transform(df_numeric)
data
