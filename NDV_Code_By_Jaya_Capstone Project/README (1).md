
# 🏠 Real Estate Price Prediction Dashboard

This is a simple and fun machine learning web app built using **Streamlit** that predicts house prices based on neighborhood and house features. It's powered by a **Random Forest model** trained on the **Boston Housing Dataset**.

---

##  Objective

To help anyone — even a 10-year-old! — understand how things like house size, air quality, and nearby facilities can affect the price of a house. Enter some easy values, click a button, and get a predicted price in **Indian Rupees (₹)**!

---

##  How to Run

###  Step 1: Install Python Libraries

Install all the required packages using this one command:


pip install -r requirements.txt


###  Step 2: Train the Model (run once)

python model_train.py


This saves:
- `boston_rf_model.pkl` (trained model)
- `boston_scaler.pkl` (preprocessing scaler)

###  Step 3: Launch the Web App

```bash
streamlit run app.py
```

It will open in your browser automatically at:  
`http://localhost:8501`

---

##  Features Explained (Input Questions)

| Feature | Description |
|--------|-------------|
| Neighborhood Safety | 0 = very safe, 100 = very unsafe |
| Open Land | 0 = no land, 100 = lots of land |
| Industries Nearby | 0 = no factories, 30 = many factories |
| Next to River | Better views may increase price |
| Air Pollution | 0 = clean air, 1 = very polluted |
| Number of Rooms | 1 = small home, 10 = big home |
| Age of Home | 0 = brand new, 100 = very old |
| Distance to Schools & Shops | 0 = very close, 15 = very far |
| Road Access | 1 = hard to reach, 24 = easy access |
| Tax Rate | 100 = low tax area, 800 = high tax |
| Student-Teacher Ratio | 10 = better schools, 30 = crowded schools |
| Neighborhood Diversity | 0 = less diversity, 400 = more diversity |
| Low Income % | 0 = wealthy area, 40 = poor area |

---

##  Output

You’ll get a predicted house price like:
```
💰 Your predicted house price is: ₹ 45,23,120.00
```

---

##  Project Files

```
📁 real_estate_dashboard/
├── app.py                # Streamlit web app
├── model_train.py        # Model training script
├── boston_rf_model.pkl   # Trained ML model
├── boston_scaler.pkl     # Scaler used for preprocessing
├── requirements.txt      # Python packages
├── README.md             # You're reading it!
```

---

##  Future Ideas

- Add map-based predictions
- Add images or icons for better engagement
- Use sliders for even smoother input

---

##  Author

Koruprolu Jayalakshmi 
Capstone Project – AI/ML Internship  
2025

---
