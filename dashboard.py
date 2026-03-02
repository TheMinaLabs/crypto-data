import streamlit as st
import duckdb
import pandas as pd

# 1. Use the absolute path discovered in profiles.yml
DB_PATH = '/Users/mirnadellamonicaioshida/Desktop/crypto_data/data/crypto_vault.duckdb'

st.set_page_config(page_title="VeraTrade Analytics", layout="wide")
st.title("📈 VeraTrade: Crypto Analytics")
st.markdown("Real-time insights from our **DuckDB + dbt + Dagster** Lakehouse.")

try:
    # 2. Extract data safely using a context manager
    with duckdb.connect(DB_PATH, read_only=True) as con:
        # Specify 'main.' just to be 100% safe with dbt schemas
        # Swapping 'recorded_at' for 'processed_at'
        df = con.execute("SELECT * FROM main.fct_crypto_prices ORDER BY processed_at DESC").df()
    
    st.success("Successfully connected to the Production Lakehouse!")

    # 3. Key Metrics (BTC & ETH)
    col1, col2 = st.columns(2)
    tickers = df['ticker'].unique()
    
    # Loop through the unique tickers to build the metric cards
    for i, ticker in enumerate(tickers[:2]):
        latest = df[df['ticker'] == ticker].iloc[0]
        cols = [col1, col2]
        # Note: using 'price_eur' which matches dbt model column name
        cols[i].metric(f"{ticker} Current Price", f"€{latest['price_eur']:,.2f}")

    # 4. Visual Price Trends
    st.subheader("Price Trends")
    # Swapping 'recorded_at' for 'processed_at' in the chart
    st.line_chart(df, x='processed_at', y='price_eur', color='ticker')

    # 5. Data Quality Audit View 
    st.subheader("🔍 Data Quality Audit")
    st.write("Current records in the analytical mart:")
    st.dataframe(df, use_container_width=True)

except Exception as e:
    st.error(f"Catalog Error: {e}")
    st.info(f"Make sure you've run 'dbt run' and that the file exists at: {DB_PATH}")