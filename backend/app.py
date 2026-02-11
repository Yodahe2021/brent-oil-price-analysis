from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd
import os

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.abspath(os.path.join(BASE_DIR, '..', 'data'))

def standard_response(data=None, error=None):
    """Returns a consistent JSON structure for the frontend."""
    return jsonify({"data": data, "error": error})

@app.route('/api/prices', methods=['GET'])
def get_prices():
    """
    Endpoint: GET /api/prices
    Description: Returns sampled historical oil prices.
    Query Params: None
    """
    try:
        file_path = os.path.join(DATA_DIR, 'BrentOilPrices.csv')
        df = pd.read_csv(file_path)
        # Downsample to 2000 points for responsiveness
        data = df.iloc[::max(1, len(df)//2000)].to_dict(orient='records')
        return standard_response(data=data)
    except Exception as e:
        return standard_response(error=str(e)), 500

@app.route('/api/events', methods=['GET'])
def get_events():
    """Endpoint: GET /api/events | Returns geopolitical event list."""
    try:
        df = pd.read_csv(os.path.join(DATA_DIR, 'external_events.csv'))
        return standard_response(data=df.to_dict(orient='records'))
    except Exception as e:
        return standard_response(error=str(e)), 500

@app.route('/api/analysis', methods=['GET'])
def get_analysis():
    """Endpoint: GET /api/analysis | Returns model results."""
    try:
        path = os.path.join(DATA_DIR, 'model_results.csv')
        if not os.path.exists(path):
            return standard_response(data=[{"Metric": "Status", "Value": "Pending"}])
        df = pd.read_csv(path)
        return standard_response(data=df.to_dict(orient='records'))
    except Exception as e:
        return standard_response(error=str(e)), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)