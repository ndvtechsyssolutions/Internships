import pandas as pd
import numpy as np

df = pd.read_csv("netflix_titles.csv")
df
df.head()
df.tail(5)

df.columns.str.strip().str.lower().str.replace(' ','_')

df.isna().sum()

# finding and handling misiing values
df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('not specified')
df['country'] = df['country'].fillna('Unknown')
df['rating'] = df['rating'].fillna(df['rating'].mode() [0])
df['date_added'] = pd.to_datetime(df['date_added'], errors ='coerce')

df.isna().sum()

df['year_added'] = df['date_added'].dt.year
df['month_added'] = df['date_added'].dt.month
df['weekday_added'] = df['date_added'].dt.day_name()

# split listed_in (genres) into list

import pandas as pd
import numpy as np

df['listed_in_list'] = df['listed_in'].apply(lambda x: [i.strip() for i in x.split(',')] if pd.notna(x) else np.nan)

# flag for multiple genres
df['multi_genre'] = df['listed_in_list'].apply(lambda x: len(x) > 1)

## Handle inconsistent country names (example)
df['country'] = df['country'].replace({'United States of America': 'United States'})

## Outlier check for release years
df = df[(df ['release_year'] >= 1920) & (df['release_year'] <= 2025)]

#Aggregation example: Number of titles by country 

country_counts = df ['country'].value_counts().head(10)
print("\nTop 10 Countries by Content:\n", country_counts)

#Final dataset preview
print("\nCleaned Netflix Dataset:")
print(df.head())

df.isna().sum()
