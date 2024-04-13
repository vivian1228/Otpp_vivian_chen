import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import yfinance as yf
import matplotlib.pyplot as plt

# Define the ticker symbols for the assets you are interested in
tickers = {
    'S&P 500': '^GSPC',
    'S&P GSCI': '^SPGSCI',
    'Gold': 'GC=F',
    'US 10Y Treasury': '^TNX',
}

# Calculate two years ago from today
two_years_ago = datetime.now() - timedelta(days=2*365)

# Fetch historical data
data = {ticker: yf.Ticker(symbol).history(start=two_years_ago) for ticker, symbol in tickers.items()}

# Example: Print the head of the S&P 500 data
# print(data['S&P 500'].head())
# print(data['CA 10Y Treasury'])


# Check column names
# print(data['S&P 500'].columns)
#
column_name = 'Close'

# Extract the specified column from each DataFrame and store in a new DataFrame
new_df = pd.DataFrame({key: df[column_name] for key, df in data.items()})

# print(new_df.head())

ticker_symbol = 'XGB.TO'
# Create a ticker object
xgb = yf.Ticker(ticker_symbol)
# Download historical 'Close' values
xgb_data = xgb.history(start=two_years_ago)['Close']
xgb_df=pd.DataFrame(xgb_data)

xgb_df.rename(columns={'Close': 'CA 10Y Treasury'}, inplace=True)

data_hist=pd.merge(new_df,xgb_df, on='Date', how='outer')
data_hist=data_hist.dropna()
print(data_hist.head())  #----- data history ready------


# ask user for asse mix % input:

input_string = input("Enter your asset mix percentages separated by slashes (e.g., 10/10/10/10/60): ")
# Split the input string into a list based on the slash separator
percentages = input_string.split('/')
# Convert the list of strings to a list of integers
percentages = [int(p) for p in percentages]
# Check if the percentages sum to 100
if sum(percentages) == 100:
    print("Valid asset mix:", percentages)
else:
    print("Error: The percentages do not sum to 100. Please enter valid percentages.")
percentages = [int(p) for p in percentages]
# Create a pandas Series from the list of percentages
asset_mix_series = pd.Series(percentages)
print(asset_mix_series)
#----- asset mix input ready------

stock_values_now = pd.Series(data_hist.tail(1).values.ravel())
shares_hld= asset_mix_series/stock_values_now * 10**7
shares_hld = shares_hld.round().astype(int)  #rounding

print(shares_hld)
#----- share size ready------

# random draw
def random_sim():
    stock_values_i = pd.Series(data_hist.sample().values.ravel())
    pnl = ((asset_mix_series /stock_values_now * stock_values_i) * 10**6 )- 10**8
    return(pnl.sum())

sim_df=[]
for i in range (500):
    sim_df.append({'input': i, 'pnl': random_sim()})
sim_df=pd.DataFrame(sim_df)

print(sim_df.head())


VaR_9995 = np.percentile(sim_df['pnl'], 100 - 99.95)
print(VaR_9995)


# Plotting the histogram
plt.figure(figsize=(10, 6))
plt.hist(sim_df['pnl'], bins=30, alpha=0.7, color='blue')
plt.title('Simulated PnL Distribution')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()