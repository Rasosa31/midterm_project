# app.py
from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Cargar modelo y features
model = joblib.load('best_model.pkl')
features = joblib.load('data/features.pkl')

@app.route('/')
def home():
    return "API de Predicción de Precios - Enviar POST a /predict"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        df = pd.DataFrame([data])
        df = df[features]  # Asegurar orden
        pred = int(model.predict(df)[0])
        prob = float(model.predict_proba(df)[0][pred])
        return jsonify({
            'prediction': pred,
            'confidence': round(prob, 3),
            'meaning': '0 = SUBE mañana' if pred == 0 else '1 = BAJA mañana'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)