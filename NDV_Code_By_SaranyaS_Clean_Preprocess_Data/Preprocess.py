import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

#loading the daatset
d=pd.read_excel("netflix_titles.xlsx")

# 1.Having missing values,duplicated and incorrect data types or not
print(d.isnull().sum())  
print('\n')

#filling up all the null values 
d.fillna({'director':'Unknown'},inplace=True)
d.fillna({'cast':'Unknown'},inplace=True)
d.fillna({'country':'Unknown'},inplace=True)
date_added_mode=d['date_added'].mode()
rating_mode=d['rating'].mode()
duration_mode=d['duration'].mode()
d.fillna({'date_added':date_added_mode[0]},inplace=True)
d.fillna({'rating':rating_mode[0]},inplace=True)
d.fillna({'duration':duration_mode[0]},inplace=True)

#finding the duplicates
print("The number of records that have duplicates:",d.duplicated().sum()) #no duplicates found
print('\n')

#checking the data types before changing it
print("The data types before changing them:")
print(d.dtypes)
print('\n')


#2.changing the data types of the data 
d['duration_int']=d['duration'].str.extract('(\d+)').astype('float')
d['duration_type']=d['duration'].str.extract('([a-z[A-Z]+)')
d.drop('duration',axis=1,inplace=True)
#after changing the data types of the data 
print("The data types after changing them:")
print(d.dtypes)
print('\n')
print(d.isnull().sum())

#filtering the rows
print(d[(d['type']=='Movie' )&(d['rating']=='TV-PG')][['title','description']])


# Grouping: Count of movies each day
print("\nCoutn of Movies per day")
print(df['date_added'].value_counts())
print('\n\n')

#sorting the year wise mvies list
print(d.sort_values(by='release_year',ascending=False).head(5))
print('\n\n')


#3.summary statistics
print(d.describe())
print('\n\n')


#4.null value distribution
sns.heatmap(d.isnull(),cbar=False,cmap='viridis')
plt.title("Missing value heatmap")
plt.show()

#correlation matrix
correlation_matrix = d[['duration_int', 'release_year']].corr()
print(correlation_matrix)

plt.figure(figsize=(6, 4))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", square=True)
plt.title('Correlation Matrix')
plt.show()
print('\n\n')


#label encoder
le = LabelEncoder()
df['type_encoded'] = le.fit_transform(df['type'])

print("\nSample of Encoded Data:")
print(df[['type', 'type_encoded']].head())
