import streamlit as st
import yfinance as yf
import pandas as pd

# Example list — replace with full ASX tickers
ASX_TICKERS = ['CBA.AX', 'BHP.AX', 'ANZ.AX']

st.title("ASX 5‑Year Beta Downloader 📊")

@st.cache_data
def fetch_betas(tickers):
    data = {}
    for t in tickers:
        info = yf.Ticker(t).info
        beta = info.get('beta', None)
        data[t] = beta
    df = pd.DataFrame.from_dict(data, orient='index', columns=['5Y Beta'])
    df.index.name = 'Ticker'
    return df

beta_df = fetch_betas(ASX_TICKERS)
st.write("Here are the beta values Yahoo Finance provides:")
st.table(beta_df)

# Prepare CSV for download
@st.cache_data
def to_csv_bytes(df: pd.DataFrame) -> bytes:
    return df.to_csv().encode('utf-8')

csv_bytes = to_csv_bytes(beta_df)

st.download_button(
    label="📥 Download beta values as CSV",
    data=csv_bytes,
    file_name="asx_5y_betas.csv",
    mime="text/csv"
)
