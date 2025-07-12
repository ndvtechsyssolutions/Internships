import os
import streamlit as st
import numpy as np
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# -----------------------------
# Auto-train model if not found
# -----------------------------
model_path = "real_estate_model.pkl"
scaler_path = "real_estate_scaler.pkl"

if not os.path.exists(model_path) or not os.path.exists(scaler_path):
    st.warning("Training model... Please wait ⏳")
    
    # Load dataset (assumed to be in the same folder)
    csv_path = os.path.join(os.path.dirname(__file__), "real_estate.csv")
    df = pd.read_csv(csv_path)

    # Use selected features from dataset
    features = ['RM', 'LSTAT', 'PTRATIO', 'TAX', 'DIS']
    X = df[features]
    y = df['MEDV']  # Target is median house price in $1000s

    # Preprocess
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Train model
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Save model and scaler
    joblib.dump(model, model_path)
    joblib.dump(scaler, scaler_path)

    st.success("Model trained and ready ✅")
else:
    # Load saved model and scaler
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)

# -----------------------------
# Streamlit UI
# -----------------------------

st.set_page_config(page_title="🏠 Real Estate Price Dashboard", layout="centered")
st.title("🏠 Real Estate Price Prediction Dashboard")
st.markdown("Enter the property details below to predict the house price (in ₹).")

# Input sliders
rm = st.slider("How many rooms?", min_value=1.0, max_value=10.0, value=6.0)
lstat = st.slider("% of low-income people nearby (0 = rich, 40 = poor)", min_value=0.0, max_value=40.0, value=12.0)
ptratio = st.slider("Students per teacher (10 = good, 30 = crowded)", min_value=10.0, max_value=30.0, value=18.0)
tax = st.slider("Property tax (100 = low, 800 = high)", min_value=100, max_value=800, value=300)
dis = st.slider("Distance to major services (0 = near, 15 = far)", min_value=0.0, max_value=15.0, value=4.0)

input_data = np.array([[rm, lstat, ptratio, tax, dis]])

# Predict
if st.button("💰 Predict Price"):
    scaled_input = scaler.transform(input_data)
    prediction = model.predict(scaled_input)[0]
    price_inr = prediction * 1000 * 83  # Convert to INR
    st.success(f"💸 Predicted House Price: ₹ {price_inr:,.2f}")
