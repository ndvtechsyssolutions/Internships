import streamlit as st
import pandas as pd
import joblib
import numpy as np

st.set_page_config(page_title="Real Estate Price Prediction", page_icon="🏠", layout="centered")

st.title("Real Estate Price Prediction Dashboard")
st.sidebar.title("Instructions")
st.sidebar.info("Enter property details below to predict the estimated price of the property.")

# Input fields
total_sqft = st.number_input('Total Area (in Square Feet)', min_value=300, max_value=10000, value=1000)
bath = st.number_input('Number of Bathrooms (Toilets)', min_value=1, max_value=10, value=2)
bhk = st.number_input('Number of Bedrooms (BHK Units)', min_value=1, max_value=10, value=2)

# Predict button
if st.button("Predict Price"):
    try:
        model = joblib.load('model/model.pkl')
    except FileNotFoundError:
        st.error("Model file not found. Please ensure 'model/model.pkl' exists.")
    else:
        input_data = pd.DataFrame([[total_sqft, bath, bhk]], columns=['total_sqft', 'bath', 'bhk'])
        predicted_price = model.predict(input_data)[0]
        formatted_price = f"₹ {np.round(predicted_price, 2):,.2f} Lakhs"
        st.success(f"Estimated Price: {formatted_price}")

st.markdown("---")
st.caption("Developed by Dolla Chaitra")
