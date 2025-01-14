import requests
import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("MARKETDATA_API_KEY")

if not API_KEY:
    raise ValueError("API key not found. Please store your API key in a .env file.")

# Define the base URL
url = "https://api.marketdata.app/v1/options/chain/AAPL/"
params = {
    "symbol": "AAPL",         
    "start_date": "2023-01-01",  # Start date (optional)
    "end_date": "2025-01-17",    # End date (optional)
    "type": "call",          
    "apikey": API_KEY,
    "format": "csv"
}
response = requests.get(url, params=params)
if response.status_code == 200:
    # Save the CSV content to a file
    csv_filename = f"option_data/options_{params['symbol']}.csv"
    with open(csv_filename, "wb") as file:
        file.write(response.content)
    print(f"CSV data saved to {csv_filename}")
else:
    print(f"Error: {response.status_code} - {response.text}")

