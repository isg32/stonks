import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import yfinance as yf
from datetime import datetime, timedelta

print("\n")
print("*************************************")
print("Microproject: FML > 216400316010")
print("Topic : Stock Market prediction model")
print("**************************************\n")

choice = int(input("Select one of the below company for retriving data > \n 1. Infosys (infy)\n 2. Apple (AAPL)\n > "))

if (choice == 1):

    symbol = "INFY"
    end_date = datetime.now().date() - timedelta(days=1)
    start_date = end_date - timedelta(days=30)  # Adjust the number of days as needed

    print("\nDownloading Data...\n")

    data = yf.download(tickers=symbol, start=start_date, end=end_date)

    # Check if data is available
    if data.empty:
        print("No data available for the specified time period.")
    else:
        # Extract features and target
        closing_prices = data["Close"]
        features = closing_prices[:-1]  # Use all but the last closing price
        target = closing_prices[1:]  # Predict the next day's closing price

        # Train the model
        model = LinearRegression()
        model.fit(features.values.reshape(-1, 1), target.values.reshape(-1, 1))

        # Fetch real-time data for tomorrow
        tomorrow = end_date + timedelta(days=1)
        data_tomorrow = yf.download(tickers=symbol, start=tomorrow, end=tomorrow + timedelta(days=1))

        if data_tomorrow.empty:
            print("No data available for tomorrow.")
        else:
            closing_price_today = closing_prices[-1]
            closing_price_tomorrow = data_tomorrow["Close"].iloc[0]
            # Predict tomorrow's price
            prediction_tomorrow = model.predict([[closing_price_today]])[0][0]
            inrpred = ("{:.2f}".format(prediction_tomorrow * 82.61))
            inrclos = ("{:.2f}".format(closing_price_today * 82.61))
            print("\n***********************************************************")
            print("Predicted Closing Price of Infosys for Tomorrow:", inrpred, "₹" )
            print("Closing Price of Infosys today:", inrclos, "₹" )
            print("************************************************************")



if (choice == 2):
    symbol = "AAPL"
    end_date = datetime.now().date() - timedelta(days=1)
    start_date = end_date - timedelta(days=30)  # Adjust the number of days as needed

    print("\nDownloading Data...\n")

    data = yf.download(tickers=symbol, start=start_date, end=end_date)
    # Check if data is available
    if data.empty:
        print("No data available for the specified time period.")
    else:
        # Extract features and target
        closing_prices = data["Close"]
        features = closing_prices[:-1]  # Use all but the last closing price
        target = closing_prices[1:]  # Predict the next day's closing price

         # Train the model
        model = LinearRegression()
        model.fit(features.values.reshape(-1, 1), target.values.reshape(-1, 1))

        # Fetch real-time data for tomorrow
        tomorrow = end_date + timedelta(days=1)
        data_tomorrow = yf.download(tickers=symbol, start=tomorrow, end=tomorrow + timedelta(days=1))

        if data_tomorrow.empty:
            print("No data available for tomorrow.")
        else:
            closing_price_today = closing_prices[-1]
            closing_price_tomorrow = data_tomorrow["Close"].iloc[0]
            # Predict tomorrow's price
            prediction_tomorrow = model.predict([[closing_price_today]])[0][0]
            inrpred = ("{:.2f}".format(prediction_tomorrow * 82.61))
            inrclos = ("{:.2f}".format(closing_price_today * 82.61))
            print("\n***********************************************************")
            print("Predicted Closing Price of Apple for Tomorrow:", inrpred, "₹" )
            print("Closing Price of Apple today:", inrclos, "₹" )
            print("************************************************************")
