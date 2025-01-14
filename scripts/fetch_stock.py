import yfinance as yf
import pandas as pd
import numpy as np
import argparse

# Step 1: Fetch historical stock data
def fetch_stock_data(ticker, start_date, end_date):
    print(f"Fetching data for {ticker}...")
    data = yf.download(ticker, start=start_date, end=end_date)
    return data

# Step 2: Calculate realized volatility
def calculate_realized_vol(data, window=30):
    data['Returns'] = data['Adj Close'].pct_change()
    data['Realized Vol'] = data['Returns'].rolling(window=window).std() * np.sqrt(252)
    return data

# Step 3: Simulate implied volatility (for demo purposes)
def add_dummy_implied_vol(data):
    data['Implied Vol'] = np.random.uniform(0.2, 0.4, len(data))  # Example data
    return data

def main():
    parser = argparse.ArgumentParser(description="Fetch stock data")
    parser.add_argument("ticker", type=str, help="Stock ticker")
    parser.add_argument("start_date", type=str, help="Start date (YYYY-MM-DD)")
    parser.add_argument("end_date", type=str, help="End date (YYYY-MM-DD)")
    args = parser.parse_args()

    data = fetch_stock_data(args.ticker, args.start_date, args.end_date)
    data = calculate_realized_vol(data)
    data = add_dummy_implied_vol(data)

    # save as csv
    data.to_csv(f"{args.ticker}_data.csv")

if __name__ == "__main__":
    main()
