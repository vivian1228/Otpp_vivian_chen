import numpy as np
import pandas as pd
import yfinance as yf

def download_and_standardize(tickers, start_date, end_date):
    # Download data
    data = yf.download(tickers, start=start_date, end=end_date)['Adj Close']
    
    # Standardize the data
    standardized_data = (data - data.mean()) / data.std()
    
    return standardized_data

def create_new_series(data, rho):
    X = data.iloc[:, 0]  # Assume first column is S&P 500
    Y = data.iloc[:, 1]  # Assume second column is USD/CAD
    Z = rho * X + np.sqrt(1 - rho**2) * Y
    return Z

# Settings
tickers = ['^GSPC', 'USDCAD=X']
start_date = "2019-12-31"
end_date = "2023-12-31"
rho = 0.5  # Desired correlation

# Execute the function
data = download_and_standardize(tickers, start_date, end_date)
new_series_Z = create_new_series(data, rho)

# Output
print(new_series_Z.head())  # Display first few rows of the new series Z
