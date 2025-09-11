# Retail Sales Dashboard - EDA & Visualization Using Python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv('customer_shopping_data.csv')
data.head()
data.info()
data.describe()
data.drop_duplicates(inplace=True) #removes duplicates
data.isnull().sum()  #check for nulls

# Basic KPIs
print("Total sales:",data['price'].sum())
print("Total Transactions:", data['invoice_no'].nunique())
print("Unique Customers:", data['invoice_no'].nunique)

#changing the datatype of invoice_date
data['invoice_date']=pd.to_datetime(data['invoice_date'],dayfirst=True)   #converts string dates to datetime format
data['Day']=data['invoice_date'].dt.day_name()
data['Month']=data['invoice_date'].dt.month_name()
data['MonthNo']=data['invoice_date'].dt.month
data['year']=data['invoice_date'].dt.year
data.head()

# UNIVARIATE ANALYSIS

#Order distribution based on
#'gender', 'category', 'payment_method', 'shoping_mall', 'month', 'year'

cols=['gender','category','payment_method','shopping_mall','Month','year']
fig, axes=plt.subplots(len(cols),1,figsize=(6,len(cols)*4))
for i, col in enumerate(cols):
  counts=data[col].value_counts()
  axes[i].pie(counts.values.tolist(),labels=counts.keys(),autopct='%0.1f%%', radius=2)
  axes[i].pie([1],colors=['w'],radius=1.5, wedgeprops={'edgecolor':'white'})
  axes[i].set_title(col)
plt.tight_layout()
plt.show()

fig, ax=plt.subplots(figsize=(15,5))
sns.histplot(data['age'],kde=True,ax=ax)

fig,ax=plt.subplots(figsize=(15,5))
sns.histplot(data['price'],kde=True,ax=ax)

#Bivariate analysis
#category vs gender

product_category_count=data.groupby('gender')['category'].value_counts()
product_category_count.unstack().plot(kind='bar', stacked=False, figsize=(10, 6))
plt.xlabel('Gender')
plt.ylabel('Count')
plt.title('Product Category Distribution by Gender')
plt.legend(title='Product Category')
plt.xticks(rotation=30)
plt.show()

# Payment type with respect to gender
payment_type_count=data.groupby('gender')['payment_method'].value_counts()
payment_type_count.unstack().plot(kind='bar', stacked=False, figsize=(10, 6))

#price by category
category_sales=data.groupby('category')['price'].sum().sort_values()
category_sales.plot(kind='barh', color='skyblue')
plt.title("Total Price by Category")
plt.tight_layout()
plt.show()
