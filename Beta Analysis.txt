import yfinance as yf

# List of ASX tickers (for example, you can replace these with actual tickers you're interested in)
asx_tickers = ['CBA.AX', 'BHP.AX', 'ANZ.AX']

# Function to get the beta from Yahoo Finance
def get_beta(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info
    return info.get('beta', 'Beta not available')

# Extract and print the beta for each stock
for ticker in asx_tickers:
    beta = get_beta(ticker)
    print(f"Beta for {ticker}: {beta}")