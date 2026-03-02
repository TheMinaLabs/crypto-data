import pandas as pd
import requests
import os

# Create data directory if it doesn't exist
os.makedirs('data', exist_ok=True)

def fetch_data():
    print("Fetching data from CoinGecko...")
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=eur"
    response = requests.get(url).json()

    df = pd.DataFrame([
        {"ticker": "BTC", "price": response["bitcoin"]["eur"]},
        {"ticker": "ETH", "price": response["ethereum"]["eur"]}
    ])

    # Save as Parquet (The 2026 Industry Standard)
    df.to_parquet('data/raw_coin_data.parquet')
    print("Success! Data saved to data/raw_coin_data.parquet")

if __name__ == "__main__":
    fetch_data()