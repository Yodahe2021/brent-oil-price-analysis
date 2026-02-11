from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd
import os

app = Flask(__name__)
CORS(app)

# ROBUST PATHING: This finds the 'data' folder relative to this script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.abspath(os.path.join(BASE_DIR, '..', 'data'))

@app.route('/')
def home():
    return "Birhan Energies API is running! Available endpoints: /api/prices, /api/events, /api/analysis"

@app.route('/api/prices', methods=['GET'])
def get_prices():
    try:
        # MATCHING FILENAME: BrentOilPrices.csv (from your screenshot)
        file_path = os.path.join(DATA_DIR, 'BrentOilPrices.csv')
        df = pd.read_csv(file_path)
        
        # Clean data: handle Date format if needed
        data = df.tail(500).to_dict(orient='records') 
        return jsonify(data)
    except Exception as e:
        print(f"Error loading prices: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/events', methods=['GET'])
def get_events():
    try:
        # MATCHING FILENAME: external_events.csv
        file_path = os.path.join(DATA_DIR, 'external_events.csv')
        df = pd.read_csv(file_path)
        return jsonify(df.to_dict(orient='records'))
    except Exception as e:
        print(f"Error loading events: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/analysis', methods=['GET'])
def get_analysis():
    try:
        # MATCHING FILENAME: model_results.csv
        file_path = os.path.join(DATA_DIR, 'model_results.csv')
        
        # Check if file exists first to avoid crash
        if not os.path.exists(file_path):
            return jsonify([
                {"Metric": "Status", "Value": "Analysis results pending"},
                {"Metric": "Info", "Value": "Run Task 2 Notebook to generate"}
            ])
            
        df = pd.read_csv(file_path)
        return jsonify(df.to_dict(orient='records'))
    except Exception as e:
        print(f"Error loading analysis: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)

@app.route('/api/prices', methods=['GET'])
def get_prices():
    # ... load df ...
    data = df.tail(3000).to_dict(orient='records') # Increase to 3000 rows
    return jsonify(data)