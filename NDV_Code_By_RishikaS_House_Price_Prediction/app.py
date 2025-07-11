import streamlit as st
import pandas as pd
import joblib
import numpy as np
import matplotlib.pyplot as plt

# Load model and encoders
model = joblib.load(r"C:\Users\RISHIKA\Downloads\model.pkl")
encoders = joblib.load(r"C:\Users\RISHIKA\Downloads\encoders.pkl")

# Set page config and background styling
st.set_page_config(page_title="🏡 Real Estate Price Predictor", layout="centered")

# Custom background and header using updated Streamlit selector
st.markdown(
    """
    <style>
    .stApp {
        background: url("https://images.unsplash.com/photo-1600585154340-be6161a56a0c") no-repeat center center fixed;
        background-size: cover;
    }

    /* ❌ Removed blurry overlay */
    /* .stApp::before {
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(255, 255, 255, 0.75);
        z-index: 0;
    } */

    .main, .block-container {
        position: relative;
        z-index: 1;
        background-color: rgba(255, 255, 255, 0.95); /* You can make this more transparent if needed */
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    }

    h1 {
        color: #004D40;
        text-align: center;
    }

    .stButton button {
        background-color: #26A69A;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.5rem 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.title("🏠 Real Estate Price Prediction App")
st.markdown("Use the form below to get an estimated price for your dream home.")

# Form layout
with st.form("prediction_form"):
    st.subheader("🔍 Property Details")
    col1, col2 = st.columns(2)

    with col1:
        area = st.number_input("📐 Area (sq. ft)", min_value=100)
        bedrooms = st.slider("🛏️ Bedrooms", 1, 10)
        bathrooms = st.slider("🛁 Bathrooms", 1, 10)
        stories = st.selectbox("🏢 Stories", [1, 2, 3, 4])
        parking = st.slider("🚗 Parking Spaces", 0, 4)
        mainroad = st.selectbox("🛣️ Main Road", ["Yes", "No"])

    with col2:
        guestroom = st.selectbox("🧳 Guest Room", ["Yes", "No"])
        basement = st.selectbox("🏚️ Basement", ["Yes", "No"])
        hotwaterheating = st.selectbox("🔥 Hot Water Heating", ["Yes", "No"])
        airconditioning = st.selectbox("❄️ Air Conditioning", ["Yes", "No"])
        prefarea = st.selectbox("📍 Preferred Area", ["Yes", "No"])
        furnishingstatus = st.selectbox("🛋️ Furnishing Status", ["Unfurnished", "Semi-Furnished", "Furnished"])
        location = st.selectbox("🌆 Location", ["downtown", "suburb", "countryside"])

    submitted = st.form_submit_button("🔮 Predict Price")

    if submitted:
        # Encode input using saved encoders
        input_dict = {
            "area": area,
            "bedrooms": bedrooms,
            "bathrooms": bathrooms,
            "stories": stories,
            "mainroad": encoders["mainroad"].transform([mainroad.lower()])[0],
            "guestroom": encoders["guestroom"].transform([guestroom.lower()])[0],
            "basement": encoders["basement"].transform([basement.lower()])[0],
            "hotwaterheating": encoders["hotwaterheating"].transform([hotwaterheating.lower()])[0],
            "airconditioning": encoders["airconditioning"].transform([airconditioning.lower()])[0],
            "parking": parking,
            "prefarea": encoders["prefarea"].transform([prefarea.lower()])[0],
            "furnishingstatus": encoders["furnishingstatus"].transform([furnishingstatus.lower()])[0],
            "location": encoders["location"].transform([location.lower()])[0]
        }

        input_df = pd.DataFrame([input_dict])
        prediction = model.predict(input_df)[0]

        st.success(f"💰 **Estimated Property Price:** ₹ {int(prediction):,}")

        # Feature importance chart
        st.subheader("📊 Feature Importance")
        feat_imp = pd.Series(model.feature_importances_, index=input_df.columns)
        st.bar_chart(feat_imp)

# Divider
st.markdown("---")
st.header("📂 Batch Prediction (Upload CSV)")

uploaded_file = st.file_uploader("Upload a CSV file with property details", type=["csv"])
if uploaded_file is not None:
    try:
        batch_data = pd.read_csv(uploaded_file)
        for col in encoders:
            if col in batch_data.columns:
                batch_data[col] = batch_data[col].astype(str).str.lower()
                batch_data[col] = encoders[col].transform(batch_data[col])
        predictions = model.predict(batch_data)
        batch_data["Predicted Price"] = [f"₹ {int(p):,}" for p in predictions]
        st.success("✅ Batch Prediction Complete!")
        st.dataframe(batch_data)
    except Exception as e:
        st.error(f"❌ Error: {e}")
