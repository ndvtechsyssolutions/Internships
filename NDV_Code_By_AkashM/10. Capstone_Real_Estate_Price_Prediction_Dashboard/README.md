🏠 Real Estate Price Prediction using Machine Learning

📁 Project Overview
    This capstone project aims to predict real estate prices in Bengaluru using machine learning. By analyzing housing data, we built a regression model that estimates the property price based on user inputs like location, area, and more.

📌 Objectives
    Perform EDA and preprocessing on Bengaluru house dataset
    Train multiple regression models

    Deploy the best model using a Streamlit dashboard for live predictions

📂 Folder Contents

    Bengaluru_House_Data.csv   - Raw housing dataset from Kaggle
    bengaluru_model.pkl        - Trained machine learning model using Linear Regression
    capstone_notebook.ipynb	   - Notebook containing data cleaning, EDA, model training, and evaluation
    app.py                     -Streamlit code for interactive web prediction app

📊 Features Used
    The model uses the following 8 features after encoding:

    area_type (encoded)

    availability (encoded)

    location (encoded)

    size (encoded)

    society (encoded)

    total_sqft

bath (Number of Bathrooms)

balcony (Number of Balconies)

🛠️ Model Training
    Dataset cleaned using median/mode filling for missing values

    Categorical variables encoded using LabelEncoder

    Features normalized using StandardScaler

    Models tried: Linear Regression, Decision Tree, and Random Forest

    Best Performance: Linear Regression (based on R², RMSE, MAE)

🚀 Deployment
    Frontend built using Streamlit

Accepts 8 feature inputs from user
Displays predicted price instantly using the trained model

🧪 How to Run
    # Step 1: Install dependencies
        pip install streamlit pandas numpy joblib
    # Step 2: Run the Streamlit app
        streamlit run app.py

📌 Sample Output
    💰 Predicted Price: ₹2.17 Lakhs

🧠 Insights
    Location and area size are the most influential factors in determining price.
    Preprocessing played a key role in boosting model performance.

🙏 Acknowledgment
    Dataset sourced from Kaggle - Bengaluru House Data