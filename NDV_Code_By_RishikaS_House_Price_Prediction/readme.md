
# 🏠 Real Estate Price Prediction Dashboard

An interactive web application built using **Streamlit** that predicts the price of a house based on various features such as area, bedrooms, amenities, and location. The app uses a machine learning model trained on a real estate dataset to provide accurate price predictions in real time.

---

## 📌 Project Features

- 🔮 Predict property price based on user inputs
  
- 🧠 Trained Random Forest Regressor model  

- 📂 Batch prediction from uploaded CSV files  

- 📊 Feature importance visualized using charts  

- 🎨 Styled UI with custom background and layout

---

## 🧰 Tech Stack

| Tool             | Purpose                     |
|------------------|-----------------------------|
| Python           | Programming Language        |
| Pandas, NumPy    | Data manipulation           |
| Scikit-learn     | Model training & evaluation |
| Matplotlib, Seaborn | Data visualization       |
| Joblib           | Model serialization         |
| Streamlit        | Web app development         |

---

## 🗂️ Dataset

- 📥 Source: [Housing Price Prediction – Kaggle](https://www.kaggle.com/datasets/harishkumardatalab/housing-price-prediction)

- 🔎 Features include:

   - Area (sq. ft)

  - Bedrooms, Bathrooms, Stories

  - Main road access, Guest room, Basement

  - Hot water heating, Air conditioning

  - Parking availability

  - Furnishing status, Preferred area

  - Location

---

## 🚀 How to Run the Project

### 🛠️ Local Setup

1. **Clone the repo**

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**
   ```bash
   streamlit run app.py
   ```

4. ✅ The app will open in your browser at `http://localhost:8501`either automatically or when you click on the link in your terminal.

---

## 📦 File Structure

```
├── app.py                   # Streamlit app script

├── model.pkl                # Trained model

├── encoders.pkl             # Encoded label mappings

├── sample_input.csv         # Sample input for batch prediction

├── requirements.txt         # Project dependencies

└── README.md                # Project documentation
```

---

## 📄 License

This project is under the MIT License.
