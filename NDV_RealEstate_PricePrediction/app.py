from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load('real_estate_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    location = request.form['location']
    area = float(request.form['area'])
    bath = int(request.form['bath'])
    bhk = int(request.form['bhk'])

    # Create a DataFrame with the same columns as during training
    input_df = pd.DataFrame([{
        'location': location,
        'total_sqft': area,
        'bath': bath,
        'bhk': bhk
    }])

    # Predict using the trained pipeline
    prediction = model.predict(input_df)
    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text=f'Estimated Price: ₹{output} Lakhs')

if __name__ == '__main__':
    app.run(debug=True)
