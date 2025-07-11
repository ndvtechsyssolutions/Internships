# app/streamlit_app.py

import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model, scaler, and feature names
model = joblib.load('models/price_predictor.pkl')
scaler = joblib.load('models/scaler.pkl')
feature_names = joblib.load('models/features.pkl')

# Location list from training
location_options = [col.replace('location_', '') for col in feature_names if col.startswith('location_')]
location_options.append('other')  # For fallback

def predict_price(location, sqft, bath, bhk):
    # Create a single-row dataframe with all required features
    input_dict = {
        'total_sqft': sqft,
        'bath': bath,
        'BHK': bhk
    }

    for loc in [f'location_{l}' for l in location_options if f'location_{l}' in feature_names]:
        input_dict[loc] = 1 if location == loc.replace('location_', '') else 0

    # Fill in missing location columns
    for col in feature_names:
        if col not in input_dict:
            input_dict[col] = 0

    df_input = pd.DataFrame([input_dict])[feature_names]
    scaled_input = scaler.transform(df_input)

    prediction = model.predict(scaled_input)[0]
    return round(prediction, 2)

# UI Layout
st.set_page_config(page_title="🏡 Real Estate Price Predictor", layout="centered")
st.title("🏡 Real Estate Price Prediction Dashboard")
st.write("Enter property details to get estimated market price.")

# Form
with st.form("predict_form"):
    location = st.selectbox("Select Location", sorted(location_options))
    sqft = st.number_input("Total Square Feet", min_value=300.0, step=50.0)
    bath = st.number_input("Number of Bathrooms", min_value=1, step=1)
    bhk = st.number_input("Number of Bedrooms (BHK)", min_value=1, step=1)

    submitted = st.form_submit_button("Predict Price")

    if submitted:
        price = predict_price(location, sqft, bath, bhk)
        st.success(f"🏷 Estimated Price: ₹ {price} Lakhs")

# Optional: CSV Upload for Batch Prediction
st.markdown("---")
st.subheader("📦 Batch Prediction from CSV (Optional)")
uploaded_file = st.file_uploader("Upload CSV file with columns: location, total_sqft, bath, BHK", type=["csv"])

if uploaded_file:
    try:
        batch_df = pd.read_csv(uploaded_file)

        def batch_predict(df):
            df['location'] = df['location'].apply(lambda x: x.strip())
            input_list = []
            for _, row in df.iterrows():
                input_dict = {
                    'total_sqft': row['total_sqft'],
                    'bath': row['bath'],
                    'BHK': row['BHK']
                }
                for loc in [f'location_{l}' for l in location_options if f'location_{l}' in feature_names]:
                    input_dict[loc] = 1 if row['location'] == loc.replace('location_', '') else 0
                for col in feature_names:
                    if col not in input_dict:
                        input_dict[col] = 0
                input_list.append(input_dict)
            batch_input_df = pd.DataFrame(input_list)[feature_names]
            scaled = scaler.transform(batch_input_df)
            preds = model.predict(scaled)
            return preds

        predictions = batch_predict(batch_df)
        batch_df['Predicted Price (Lakh ₹)'] = np.round(predictions, 2)
        st.dataframe(batch_df)
        st.download_button("📥 Download Predictions as CSV", batch_df.to_csv(index=False), file_name="predictions.csv")

    except Exception as e:
        st.error(f"Error: {e}")
