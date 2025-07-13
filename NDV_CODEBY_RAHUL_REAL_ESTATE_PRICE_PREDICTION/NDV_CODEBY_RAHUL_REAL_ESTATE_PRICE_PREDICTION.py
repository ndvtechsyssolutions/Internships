## app.py


from flask import Flask, render_template, request
import joblib

app = Flask(__name__)
model = joblib.load('real_estate_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    area = float(request.form['area'])
    bedrooms = int(request.form['bedrooms'])
    age = int(request.form['age'])
    prediction = model.predict([[area, bedrooms, age]])
    return render_template('index.html', prediction_text=f'Estimated Price: ₹{prediction[0]:,.2f} Lakhs')

if __name__ == '__main__':
    app.run(debug=True)

## model.py

import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression

# Sample data (Area in sqft, Bedrooms, Age in years, Price in ₹L)
data = pd.DataFrame({
    'area': [1000, 1500, 2000, 1200, 1800],
    'bedrooms': [2, 3, 4, 2, 3],
    'age': [5, 10, 15, 7, 12],
    'price': [50, 75, 100, 60, 85]
})

X = data[['area', 'bedrooms', 'age']]
y = data['price']

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, 'real_estate_model.pkl')
print("Model saved as real_estate_model.pkl")

## index.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Real Estate Price Predictor</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(to right, #f0f2f5, #c9d6ff);
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .container {
            background-color: #ffffff;
            padding: 40px 50px;
            border-radius: 15px;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
            text-align: center;
            width: 350px;
        }

        h2 {
            margin-bottom: 30px;
            color: #333;
        }

        label {
            display: block;
            margin-top: 15px;
            margin-bottom: 5px;
            color: #444;
            text-align: left;
        }

        input[type="number"] {
            width: 100%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 8px;
            font-size: 14px;
        }

        input[type="submit"] {
            margin-top: 25px;
            background-color: #4a90e2;
            color: white;
            padding: 12px 20px;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            cursor: pointer;
            width: 100%;
            transition: background 0.3s ease;
        }

        input[type="submit"]:hover {
            background-color: #357ABD;
        }

        h3 {
            margin-top: 20px;
            color: #28a745;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Real Estate Price Predictor</h2>
        <form action="/predict" method="post">
            <label for="area">Area (sq ft):</label>
            <input type="number" id="area" name="area" required>

            <label for="bedrooms">Bedrooms:</label>
            <input type="number" id="bedrooms" name="bedrooms" required>

            <label for="age">Age (in years):</label>
            <input type="number" id="age" name="age" required>

            <input type="submit" value="Predict Price">
        </form>
        {% if prediction_text %}
            <h3>{{ prediction_text }}</h3>
        {% endif %}
    </div>
</body>
</html>
