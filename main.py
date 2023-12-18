import yfinance as yf
import pandas as pd

# Set display options to show all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Download historical data for the Dow
ticker_symbol = '^DJI'
start_date = '2023-01-01'
end_date = '2023-12-31'

dow_data = yf.download(ticker_symbol, start=start_date, end = end_date)

# print(dow_data[['Open', 'Close']])
# Extract day of the week from the index and count occurrences of Fridays (weekday=4)

#how many times friday is lower than thursday

# Filter and store only the rows corresponding to Thursday, Fridays and following monday
thursdays_data = dow_data[dow_data.index.dayofweek == 3][['Close']]
fridays_data = dow_data[dow_data.index.dayofweek == 4][['Close']]
mondays_data = dow_data[dow_data.index.dayofweek == 0][['Close']]

#how many times friday close is less than thursday close 
#store thurdays close in array
thursday_close_array = []
friday_close_array 	 = []
monday_close_array   = []

#appending the closing time in the array for Thursday, Friday, and 
for close_time in thursdays_data['Close']:
	thursday_close_array.append(close_time)

for close_time in fridays_data['Close']:
	friday_close_array.append(close_time)

for close_time in mondays_data['Close']:
	monday_close_array.append(close_time)

#problem for monday closing data since it is not the same lenth as Thursdat and frida


# Ensure both arrays have the same length
if len(thursday_close_array) == len(friday_close_array):
    # Initialize a counter for Fridays closing below Thursdays
    fridays_below_thursdays = 0

    # Iterate through Thursday and Friday closing prices simultaneously
    for thursday_close, friday_close in zip(thursday_close_array, friday_close_array):
        # Compare Friday's closing price with Thursday's closing price
        if friday_close < thursday_close:
            fridays_below_thursdays += 1

    print("Fridays closed below Thursdays " + str(fridays_below_thursdays) + " times.")
else:
    print("Arrays have different lengths.")
	

