import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

st.set_page_config(page_title="Real Estate Dashboard", layout="wide")
st.title("\ Real Estate Price Prediction Dashboard")


uploaded_file = st.file_uploader("Upload your Real Estate CSV file", type=['csv'])

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)
        st.success("\ Data loaded successfully!")
        st.write("### Sample Data", df.head())

        required_columns = {'location', 'sqft', 'bedrooms', 'bathrooms', 'price'}
        if not required_columns.issubset(df.columns):
            st.error(f"\ Missing required columns: {required_columns - set(df.columns)}")
        else:

            df['bedrooms'] = pd.to_numeric(df['bedrooms'], errors='coerce').fillna(0).astype(int)
            df['bathrooms'] = pd.to_numeric(df['bathrooms'], errors='coerce').fillna(0).astype(int)
            df['sqft'] = pd.to_numeric(df['sqft'], errors='coerce').fillna(0)
            df = df.dropna(subset=['price'])


            st.sidebar.header("📌 Feature Selection")
            location = st.sidebar.selectbox("Select Location", sorted(df['location'].unique()))
            df_filtered = df[df['location'] == location]


            X = df_filtered[['sqft', 'bedrooms', 'bathrooms']]
            y = df_filtered['price']

            if len(df_filtered) < 5:
                st.warning("⚠️ Not enough data for training in this location. Please upload more data or choose another location.")
            else:
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
                model = LinearRegression()
                model.fit(X_train, y_train)


                st.header("💡 Predict House Price")
                sqft = st.slider("Square Footage", 500, 10000, 1500)
                bedrooms = st.selectbox("Bedrooms", sorted(df['bedrooms'].unique()))
                bathrooms = st.selectbox("Bathrooms", sorted(df['bathrooms'].unique()))

                input_data = pd.DataFrame([[sqft, bedrooms, bathrooms]], columns=['sqft', 'bedrooms', 'bathrooms'])
                predicted_price = model.predict(input_data)[0]
                st.success(f"💰 Estimated Price: ₹{predicted_price:,.0f}")


                st.header("📊 Price Distribution in Selected Location")
                fig, ax = plt.subplots()
                sns.histplot(df_filtered['price'], kde=True, ax=ax)
                ax.set_xlabel("Price (₹)")
                ax.set_ylabel("Frequency")
                st.pyplot(fig)
    except Exception as e:
        st.error(f" Error loading file: {e}")
else:
    st.info("Please upload a CSV file to begin.")
