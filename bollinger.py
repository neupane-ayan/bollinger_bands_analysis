import numpy as np
import pandas as pd
import datetime as dt
import yfinance as yf
import matplotlib.pyplot as plt

# configurable data
print("???")
ticker = input("Enter ticker: ")
# num of days in moving average
n = 20
# num of std deviations
m = 2
end_date = dt.date.today()
start_date = dt.date(2021, 1, 1)
data = yf.download(ticker, start_date, end_date)

while True:
    data['typical_price'] = (data['High'] + data['Low'] + data['Close']) / 3
    data['moving_avg_n'] = data.iloc[:,6].rolling(window=n).mean()
    data['moving_std_n'] = data.iloc[:,6].rolling(window=n).std()
    data['upper_band'] = data['moving_avg_n'] + (m * data['moving_std_n'])
    data['lower_band'] = data['moving_avg_n'] - (m * data['moving_std_n'])

    #plotting:
    plt.plot(data['moving_avg_n'], color='black', alpha=0.8)
    plt.plot(data['upper_band'], color='blue', alpha=0.25)
    plt.plot(data['lower_band'], color='blue', alpha=0.25)
    plt.fill_between(data.index, data['upper_band'], data['lower_band'], color='blue', alpha=0.05)
    plt.title(ticker + " " + str(n) + ' day moving average')
    plt.show()

    #input for changing the moving averages
    try:
        temp = int(input("Update n moving average value: "))
    except:
        break
    if temp > 0:
        n = temp
    else:
        break