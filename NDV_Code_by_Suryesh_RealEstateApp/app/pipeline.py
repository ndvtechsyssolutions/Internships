# app/pipeline.py

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler

def clean_data(df):
    df = df.drop(['area_type', 'society', 'balcony', 'availability'], axis=1)
    df.dropna(inplace=True)

    # Extract BHK from 'size'
    df['BHK'] = df['size'].apply(lambda x: int(x.split(' ')[0]) if isinstance(x, str) else None)
    df = df.drop('size', axis=1)

    # Convert total_sqft to number
    def convert_sqft(x):
        try:
            if '-' in x:
                tokens = x.split('-')
                return (float(tokens[0]) + float(tokens[1])) / 2
            return float(x)
        except:
            return None

    df['total_sqft'] = df['total_sqft'].apply(convert_sqft)
    df.dropna(inplace=True)

    # Reduce locations
    df['location'] = df['location'].apply(lambda x: x.strip())
    loc_stats = df['location'].value_counts()
    locations_less_than_10 = loc_stats[loc_stats <= 10].index
    df['location'] = df['location'].apply(lambda x: 'other' if x in locations_less_than_10 else x)

    # Feature + label split
    X = df[['location', 'total_sqft', 'bath', 'BHK']]
    y = df['price']

    # Encode categorical
    X = pd.get_dummies(X, drop_first=True)

    # Scale
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled, y, scaler, X.columns.tolist()

