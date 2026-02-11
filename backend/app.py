from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd
import os

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.abspath(os.path.join(BASE_DIR, '..', 'data'))

# API Documentation:
# GET /api/prices   - Returns JSON list of Date and Price.
# GET /api/events   - Returns list of historical events for overlays.
# GET /api/analysis - Returns model-detected change points and stats.

@app.route('/api/prices')
def get_prices():
    df = pd.read_csv(os.path.join(DATA_DIR, 'BrentOilPrices.csv'))
    return jsonify(df.tail(3000).to_dict(orient='records'))

@app.route('/api/events')
def get_events():
    df = pd.read_csv(os.path.join(DATA_DIR, 'external_events.csv'))
    return jsonify(df.to_dict(orient='records'))

@app.route('/api/analysis')
def get_analysis():
    path = os.path.join(DATA_DIR, 'model_results.csv')
    df = pd.read_csv(path) if os.path.exists(path) else pd.DataFrame([{"Metric": "N/A", "Value": "N/A"}])
    return jsonify(df.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)