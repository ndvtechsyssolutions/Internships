import os
import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler

# Auto-train if model not found
if not os.path.exists("boston_rf_model.pkl") or not os.path.exists("boston_scaler.pkl"):
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), "real_estate.csv"))  # ✅ Properly indented
    features = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']
    X = df[features]
    y = df["MEDV"]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    joblib.dump(model, "boston_rf_model.pkl")
    joblib.dump(scaler, "boston_scaler.pkl")
else:
    model = joblib.load("boston_rf_model.pkl")
    scaler = joblib.load("boston_scaler.pkl")

# Streamlit UI
st.title("🏠 House Price Predictor")

CRIM = st.number_input("Neighborhood Safety (0 = very safe, 100 = unsafe)", min_value=0.0, max_value=100.0, value=0.1)
ZN = st.number_input("Open Land Around Home (0 = none, 100 = lots of land)", min_value=0.0, max_value=100.0, value=12.5)
INDUS = st.number_input("Nearby Industries (0 = none, 30 = many)", min_value=0.0, max_value=30.0, value=7.0)
CHAS = st.selectbox("Is the house next to a river? (Better view = more price)", ["No", "Yes"])
CHAS = 1 if CHAS == "Yes" else 0
NOX = st.number_input("Air Pollution (0 = clean air, 1 = polluted)", min_value=0.0, max_value=1.0, value=0.5)
RM = st.number_input("Number of Rooms (1 = small home, 10 = big home)", min_value=1.0, max_value=10.0, value=6.0)
AGE = st.number_input("House Age (0 = new, 100 = very old)", min_value=0.0, max_value=100.0, value=60.0)
DIS = st.number_input("Distance to Schools/Stores (0 = near, 15 = far)", min_value=0.0, max_value=15.0, value=4.0)
RAD = st.number_input("Access to Main Roads (1 = difficult, 24 = easy)", min_value=1, max_value=24, value=5)
TAX = st.number_input("Tax Amount Paid (100 = low tax, 800 = high tax)", min_value=100, max_value=800, value=300)
PTRATIO = st.number_input("Student-Teacher Ratio Nearby", min_value=10.0, max_value=30.0, value=18.0)
B = st.number_input("Neighborhood Diversity (0 = less, 400 = more)", min_value=0.0, max_value=400.0, value=390.0)
LSTAT = st.number_input("Low Income Population % (0 = wealthy, 40 = poor)", min_value=0.0, max_value=40.0, value=12.0)

if st.button("🎯 Predict My House Price"):
    input_data = np.array([[CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO, B, LSTAT]])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)
    price_inr = prediction[0] * 1000 * 83  # Convert to INR (approx)
    st.success(f"💰 Your predicted house price is: ₹ {price_inr:,.2f}")
