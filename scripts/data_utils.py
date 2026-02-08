import pandas as pd
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def load_and_clean_data(file_path):
    """Loads CSV, handles errors, and cleans dates."""
    if not os.path.exists(file_path):
        logging.error(f"File not found: {file_path}")
        raise FileNotFoundError(f"Missing data file at {file_path}")

    try:
        df = pd.read_csv(file_path)
        # Ensure correct date format
        df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
        df.sort_values('Date', inplace=True)
        df.set_index('Date', inplace=True)
        # Professional cleaning
        df = df.ffill().bfill()
        logging.info("Data loaded and cleaned successfully.")
        return df
    except Exception as e:
        logging.error(f"Unexpected error loading data: {e}")
        return None

def calculate_returns(df):
    """Calculates daily percentage returns."""
    if 'Price' not in df.columns:
        logging.error("Column 'Price' missing from DataFrame")
        return None
    df['Returns'] = df['Price'].pct_change()
    return df