from google.colab import drive
drive.mount('/content/drive')
import os

# List everything in your Google Drive
drive_path = '/content/drive/MyDrive'
for item in os.listdir(drive_path):
    print(item)
# Check inside the kaggle dataset folder
dataset_path = '/content/drive/MyDrive/kaggle dataset'
for item in os.listdir(dataset_path):
    print(item)
# Step 2: Set ZIP path (make sure the filename is correct)
zip_path = '/content/drive/MyDrive/kaggle dataset/archive (1).zip'

# Step 3: Extract ZIP file
import zipfile
import os

# Create destination folder
os.makedirs('/content/data', exist_ok=True)

# Extract
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall('/content/data')

print("✅ Extraction completed.")
#load the dataset
import pandas as pd

# Use full path to the file inside extracted folder
df = pd.read_csv('/content/data/Titanic-Dataset.csv')
df.head()
# Check missing values
print("Missing values in each column:")
print(df.isnull().sum())

# Drop duplicate rows
df = df.drop_duplicates()

# Handle missing values
if 'Age' in df.columns:
    df['Age'].fillna(df['Age'].median(), inplace=True)  # Fill missing Age with median

if 'Embarked' in df.columns:
    df.dropna(subset=['Embarked'], inplace=True)        # Drop rows with missing 'Embarked'

# Confirm changes
print("\nAfter cleaning:")
print(df.isnull().sum())
#summarization
df.describe()
df.info()
df['Survived'].value_counts() 
#visualization using barplot,histogram
import seaborn as sns
import matplotlib.pyplot as plt

# Histograms
df['Age'].hist()
plt.title("Age Distribution")
plt.show()

# Box plot
sns.boxplot(x='Survived', y='Age', data=df)

# Count plot
sns.countplot(x='Survived', data=df)
import seaborn as sns
import matplotlib.pyplot as plt

# Correlation heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

# Pair plot (only if columns exist)
if all(col in df.columns for col in ['Age', 'Fare', 'Survived']):
    sns.pairplot(df[['Age', 'Fare', 'Survived']])
    plt.suptitle("Pair Plot", y=1.02)
    plt.show()
else:
    print("One or more columns ['Age', 'Fare', 'Survived'] are missing from the DataFrame.")
  #group by operation
  # Group by Survival
df.groupby('Pclass')['Survived'].mean()

# Cross-tabulation
pd.crosstab(df['Sex'], df['Survived'], normalize='index')

