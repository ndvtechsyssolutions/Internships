# House price prediction system - Linear and ensemble models
#step-1: Importing libraries and dataset
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dataset=pd.read_excel("HousePricePrediction.xlsx")
print(dataset.head(5))
dataset.shape

#step-2: Data Processing
obj=(dataset.dtypes=="object")
object_cols=list(obj[obj].index)
print("Categorical Variables:",len(object_cols))

int_ =(dataset.dtypes=="int")
int_cols=list(int_[int_].index)
print("Integer Variables:",len(int_cols))

flo=(dataset.dtypes=="float")
float_cols=list(flo[flo].index)
print("Float Variables:",len(float_cols))

#step-3: Exploratory Data Analysis
numerical_dataset=dataset.select_dtypes(include=['number'])
plt.figure(figsize=(12,6))
sns.heatmap(numerical_dataset.corr(),
            cmap='BrBG',
            fmt='.2f',
            linewidths = 2, 
            annot= True)


unique_values=[]
for col in object_cols:
  unique_values.append(dataset[col].unique().size)
plt.figure(figsize=(10,6))
plt.title('Number of unique values of categorical variables')
plt.xticks(rotation=90)
sns.barplot(x=object_cols,y=unique_values)

plt.figure(figsize=(15,10))
plt.title('Categorical Features: Distribution')
plt.xticks(rotation=90)
index=1
for col in object_cols:
  y=dataset[col].value_counts()
  plt.subplot(5,3, index)
  plt.xticks(rotation=90)
  sns.barplot(x=list(y.index),y=y)
  index +=1

#step-4: Data Cleaning
dataset.drop(['Id'],         
             axis=1,
             inplace=True)   #As Id Column will not be participating in any prediction. So we can Drop it.

#Replacing SalePrice empty values with their mean values to make the data distribution symmetric.
dataset['SalePrice']=dataset['SalePrice'].fillna(dataset['SalePrice'].mean())

#Drop records with null values (as the empty records are very less).
new_dataset=dataset.dropna()

#Checking features which have null values in the new dataframe (if there are still any).
new_dataset.isnull().sum()

#step-5: OneHotEncoder- for label Categorical features
from sklearn.preprocessing import OneHotEncoder

s=(dataset.dtypes=='object')
object_cols=list(s[s].index)
print("Categorical variables:")
print(object_cols)
print("No.of categorical features:",len(object_cols))

OH_encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
OH_cols = pd.DataFrame(OH_encoder.fit_transform(new_dataset[object_cols]))
OH_cols.index = new_dataset.index
OH_cols.columns = OH_encoder.get_feature_names_out()
df_final = new_dataset.drop(object_cols, axis=1)
df_final = pd.concat([df_final, OH_cols], axis=1)

#step-6: splitting the dataset into Training and Testing
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

x=df_final.drop(['SalePrice'],axis=1)
y=df_final['SalePrice']
x_train, x_valid, y_train, y_valid = train_test_split(x,y,train_size=0.8,test_size=0.2,random_state=0)

#Step-7: Model training and Accuracy
#Support Vector Machine

from sklearn import svm
from sklearn.svm import SVC
from sklearn.metrics import mean_absolute_percentage_error

model_SVR=svm.SVR()
model_SVR.fit(x_train,y_train)
Y_pred=model_SVR.predict(x_valid)
print(mean_absolute_percentage_error(y_valid,Y_pred))

#Random Forest Regression
from sklearn.ensemble import RandomForestRegressor

model_RFR=RandomForestRegressor(n_estimators=10)
model_RFR.fit(x_train,y_train)
Y_pred=model_RFR.predict(x_valid)
mean_absolute_percentage_error(y_valid,Y_pred)

#Linear Regression
from sklearn.linear_model import LinearRegression

model_LR=LinearRegression()
model_LR.fit(x_train,y_train)
Y_pred=model_LR.predict(x_valid)
print(mean_absolute_percentage_error(y_valid,Y_pred))
