# 🏡 Real Estate Price Prediction Dashboard

An end-to-end machine learning dashboard that predicts real estate prices based on property features such as location, square footage, number of bathrooms, and BHK (bedroom-hall-kitchen). This project uses a trained regression model and is deployed with an interactive interface built using **Streamlit**.

---

## 📌 Features

- 🔍 Real-time price prediction for custom inputs
- 📍 Intelligent location handling with one-hot encoding
- 🏠 Inputs supported: Location, Total Sqft, Bathrooms, BHK
- 🧠 Trained and evaluated multiple regression models
- 🎯 Random Forest selected as the final model
- 🌐 Streamlit-based interactive UI

---

## 🧠 Dataset Summary

- **Name**: Bengaluru House Price Dataset
- **Source**: [Kaggle](https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data)
- **Total Records**: 13,320 entries
- **Target**: `price` (in Lakhs ₹)

Sample columns used:
- `location`
- `total_sqft`
- `bath`
- `size` → transformed into BHK
- `price`

---

## 🧪 Model Training & Evaluation

Three regression models were trained and tested:

| Model            | RMSE   | MAE   | R² Score |
|------------------|--------|-------|----------|
| Linear Regression | 93.07  | 43.40 | 0.51     |
| Decision Tree     | 90.64  | 36.40 | 0.54     |
| **Random Forest** ✅ | **82.90**  | **33.26** | **0.61**     |

✅ **Best Model**: **Random Forest Regressor**  
📁 Saved as: `models/price_predictor.pkl`

---

## 🚀 How to Run the App Locally

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/Real_Estate_Price_Predictor.git
cd Real_Estate_Price_Predictor
```
### Step 2: Set Up Virtual Environment
```
python3 -m venv .venv
source .venv/bin/activate  # For Mac/Linux
```
### Step 3: Install Dependencies
```
pip install -r requirements.txt
```
### Step 4: Launch the App
```
python -m streamlit run app/streamlit_app.py
```
## 📸 Screenshots
![UI Screenshot](assets/screenshots/ui1.png)

## 🙋‍♂️ Author

**Suryesh Pandey**  
B.Sc. Computing — **Bennett University**  
Capstone Project - AI & ML Intern (NDVTechsys)

