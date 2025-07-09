import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer

def load_data(path):
    df = pd.read_csv(path, encoding='latin-1')[['v1', 'v2']]
    df.columns = ['label', 'text']
    return df

def encode_labels(df):
    le = LabelEncoder()
    df['label_num'] = le.fit_transform(df['label'])
    return df

def vectorize_text(df):
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(df['text'])
    return X, df['label_num'], vectorizer