import pandas as pd
import numpy as np

# 1. Load the dataset
df = pd.read_csv('IPL DATA.csv')

print("▶️ First 5 rows:\n", df.head(), "\n")
print("▶️ Data types:\n", df.dtypes, "\n")
print("▶️ Missing values per column:\n", df.isna().sum(), "\n")
print("▶️ Duplicate rows:", df.duplicated().sum(), "\n")

# 3. Cleaning
df = (
    df
    .drop_duplicates()                
    .fillna({                          
        'IPL RUNNERS-UP':'Unknown',
        'IPL WINNER':'Unknown',
        'FINAL VENUE':'Unknown'
    })
)

# 4. Correct data types
df['S.NO'] = df['S.NO'].astype(int)
df['YEAR'] = df['YEAR'].astype(int)

for col in df.select_dtypes(include='object'):
    df[col] = df[col].str.strip()

df['YEARS_SINCE_START'] = df['YEAR'] - df['YEAR'].min()

mumbai_finals = df[df['FINAL VENUE'] == 'Mumbai'].sort_values('YEAR')
print("▶️ Mumbai finals:\n", mumbai_finals, "\n")

wins = df.groupby('IPL WINNER')['YEAR'].count().rename('WINS')
print("▶️ Championship tally:\n", wins.reset_index(), "\n")

print("▶️ Numeric summary:\n", df.describe(), "\n")
print("▶️ Year counts:\n", df['YEAR'].value_counts().sort_index(), "\n")

corr = df.select_dtypes(include=[np.number]).corr()
print("▶️ Correlation matrix:\n", corr, "\n")
