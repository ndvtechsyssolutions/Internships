<!DOCTYPE html>
<html>
<head>
    <title>Real Estate Price Predictor</title>
    <style>
        body {
            font-family: Arial;
            background-color: #f2f9ff;
            text-align: center;
            padding-top: 50px;
        }
        input, select {
            padding: 10px;
            margin: 10px;
            width: 200px;
            font-size: 16px;
        }
        .box {
            border: 2px solid #0099cc;
            display: inline-block;
            padding: 20px;
            border-radius: 12px;
            background-color: white;
        }
        .result {
            margin-top: 20px;
            font-size: 24px;
            font-weight: bold;
            color: #000066;
        }
    </style>
</head>
<body>

    <h1>🏠 Real Estate Price Estimator</h1>
    <form method="post" action="/predict">
        <div class="box">
            <input type="number" name="area" placeholder="Enter area (sqft)" required><br>
            <select name="bhk" required>
                <option value="">Select BHK</option>
                <option>1</option><option>2</option><option>3</option><option>4</option><option>5</option>
            </select><br>
            <input type="number" name="age" placeholder="Enter age of house" required><br>
            <button type="submit" style="padding: 10px 30px; font-size: 16px;">Predict</button>
        </div>
    </form>

    {% if predicted_price %}
        <div class="result">Estimated Price: {{ predicted_price }}</div>
    {% endif %}

</body>
</html>


app.js

from flask import Flask, render_template, request
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load trained model and scaler
model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    area = float(request.form['area'])
    bhk = int(request.form['bhk'])
    age = int(request.form['age'])

    input_df = pd.DataFrame([[area, bhk, age]], columns=['area', 'bhk', 'age'])
    input_scaled = scaler.transform(input_df)
    prediction = model.predict(input_scaled)[0]
    price_lakhs = prediction / 100000

    return render_template('index.html', predicted_price=f"₹{price_lakhs:,.2f} Lakhs")

if __name__ == '__main__':
    app.run(debug=True)
