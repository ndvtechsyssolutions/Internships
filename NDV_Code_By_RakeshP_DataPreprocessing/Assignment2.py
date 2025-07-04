import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("netflix_titles.csv")
print(data.describe())
# print("First five records of the data before preprocessing : \n")
# print(data.head())
# print("Data After Preprocessing : \n")
# data.columns = data.columns.str.strip().str.lower().str.replace(' ','_')
# # data['director'].fillna("Unknown",inplace=True)
# # data['country'].fillna("Unknown",inplace=True)
# # data['date_added'].fillna("Not Specified",inplace=True)
# # data['cast'].fillna("Unknown",inplace=True)
# # data['release_year'].fillna("Unknown",inplace=True)
# # data['duration'].fillna("Unknown",inplace=True)
# # data['rating'].fillna("Unknown",inplace=True)
data.fillna({
    'director': 'Unknown',
    'country': 'Unknown',
    'date_added': 'Not Specified',
    'cast': 'Unknown',
    'release_year': 'Unknown',
    'duration': 'Unknown',
    'rating': 'Unknown'
}, inplace=True)


data['date_added'] = pd.to_datetime(data['date_added'], errors='coerce')
data['year_added'] = data['date_added'].dt.year
data['month_added'] = data['date_added'].dt.month
data['week_added'] = data['date_added'].dt.day_name()

data['listed_in'] = data['listed_in'].apply(lambda x: [i.strip() for i in x.split(',')])

data['multi_genre'] = data['listed_in'].apply(lambda x: len(x) > 1)

data['country'] = data['country'].replace({'United States of America' : 'United States'})

data = data[(data['release_year'] >= 1920) & (data['release_year'] <= 2025)]

print(data.head(10))

print("\n","-"*30)
print("     VISUALIZATIONS \n")

plt.scatter(x = 'type',y = 'release_year',data = data)
plt.xlabel('Type of the Content')
plt.ylabel("Years")
plt.title("The Movies and TVSHOWS Released Years")
plt.show()


sns.countplot(data = data, x = 'type')
plt.xlabel("Type of the content")
plt.ylabel("Frequency")
plt.title("FREQUENCY OF MOVIES AND TV SHOWS")
plt.show()


top_countries = data['country'].value_counts().head(10)
sns.barplot(x = top_countries.values, y = top_countries.index)
plt.title("TOP 10 COUNTRIES PROVIDING NETFLIX CONTENT")
plt.xlabel("Values")
plt.ylabel("Countries")
plt.show()


data['year_added'] = pd.to_datetime(data['date_added']).dt.year
yearly_counts = data['year_added'].value_counts().sort_index()                                      
sns.lineplot(x = yearly_counts.values, y = yearly_counts.index)
plt.xlabel("Number of titles")
plt.ylabel("Year")
plt.title("Number of titles added over time")
plt.show()
