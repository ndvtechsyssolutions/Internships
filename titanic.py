import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas import read_csv
from google.colab import drive
drive.mount('/content/drive')

data = pd.read_csv("/content/drive/MyDrive/code/Titanic-Dataset.csv")
print("Dataset Info:")
data.info()

print("\nSummary Statistics:")
print(data.describe())

print("\nSurvival Counts:")
print(data['Survived'].value_counts())
print("\nPassenger Class Counts:")
print(data['Pclass'].value_counts())
print("\nSex Counts:")
print(data['Sex'].value_counts())
print("\nEmbarked Counts:")
print(data['Embarked'].value_counts())
plt.style.use('seaborn-v0_8')
plt.figure(figsize=(12, 10))

plt.subplot(2, 2, 1)
data['Age'].hist(bins=20, color='skyblue')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Count')

plt.subplot(2, 2, 2)
sns.boxplot(x='Pclass', y='Fare', data=data, color='lightgreen')
plt.title('Fare by Passenger Class')
plt.ylim(0, 100)

plt.subplot(2, 2, 3)
sns.countplot(x='Survived', data=data, color='salmon')
plt.title('Survival Count')
plt.xlabel('Survived (0 = No, 1 = Yes)')
plt.ylabel('Count')

plt.subplot(2, 2, 4)
sns.countplot(x='Sex', data=data, color='lightblue')
plt.title('Sex Distribution')
plt.xlabel('Sex')
plt.ylabel('Count')

plt.tight_layout()

plt.savefig('titanic_eda_plots.png')
plt.show()
