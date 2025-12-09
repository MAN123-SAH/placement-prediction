# app.py

from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

# Load the trained model
model_path = 'model.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract data from form as floats (to avoid ValueError for 9.5, 7.2 etc.)
    features = [float(x) for x in request.form.values()]
    
    # Convert to numpy array
    final_features = np.array([features])

    # Model prediction
    prediction = model.predict(final_features)[0]

    # Convert prediction output to text
    output = 'Placed' if prediction == 1 else 'Not Placed'

    return render_template('index.html', prediction_text=f"Prediction: {output}")

if __name__ == "__main__":
    app.run(debug=True)
