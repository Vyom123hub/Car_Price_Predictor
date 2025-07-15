from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    year = int(request.form['year'])
    km_driven = int(request.form['km_driven'])
    fuel_type = request.form['fuel_type']
    transmission = request.form['transmission']

    fuel_type_diesel = 1 if fuel_type == 'Diesel' else 0
    transmission_manual = 1 if transmission == 'Manual' else 0

    features = [year, km_driven, fuel_type_diesel, transmission_manual]
    prediction = model.predict([features])[0]
    prediction = round(prediction, 2)

    return render_template('index.html', prediction_text=f'Estimated Car Price: ₹ {prediction} lakhs')

if __name__ == "__main__":
    app.run(debug=True)
