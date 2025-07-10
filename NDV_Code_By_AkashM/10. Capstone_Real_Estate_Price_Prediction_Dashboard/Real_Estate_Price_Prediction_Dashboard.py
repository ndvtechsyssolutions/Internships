import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model
model = joblib.load('bengaluru_model.pkl')

st.title("🏠 Real Estate Price Prediction Dashboard")

st.subheader("📥 Enter Feature Values (encoded/numeric)")

# Input fields for all 8 features
area_type = st.number_input("Area Type (encoded integer)", min_value=0)
availability = st.number_input("Availability (encoded integer)", min_value=0)
location = st.number_input("Location (encoded integer)", min_value=0)
size = st.number_input("Size (encoded integer)", min_value=0)
society = st.number_input("Society (encoded integer)", min_value=0)

total_sqft = st.number_input("Square Footage", min_value=0.0)
bath = st.number_input("Number of Bathrooms", min_value=0.0)
balcony = st.number_input("Number of Balconies", min_value=0.0)

# Predict button
if st.button("Predict Price"):
    input_data = np.array([[area_type, availability, location, size, society, total_sqft, bath, balcony]])
    prediction = model.predict(input_data)
    st.success(f"💰 Predicted Price: ₹{prediction[0]:,.2f}")
