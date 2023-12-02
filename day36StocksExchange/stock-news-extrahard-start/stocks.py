import requests
import json
import datetime

percentage_change = 0

class Stocks:

    def __init__(self):
        self.STOCKS_URL = "https://www.alphavantage.co/query?"
        self.STOCK = "TSLA"
        self.COMPANY_NAME = "Tesla Inc"
        self.percentage_change = 10
        self.volume = 0
        self.ARROW = ""

    def stock(self):
        ARROW_UP = "🔺"
        ARROW_DOWN = "🔻"
        AlphaVantageAPI_key = "7OL69V9EDPKCZ9AY"
        stocks_params = {
            'function': "TIME_SERIES_INTRADAY",
            'symbol': self.STOCK,
            'interval': '60min',
            'apikey': AlphaVantageAPI_key,
        }

        try:
            stocks_response = requests.get(url=self.STOCKS_URL, params=stocks_params)
            stocks_response.raise_for_status()
            stocks_data = stocks_response.json()
            # Get the latest data from the time series
            time_series = stocks_data["Time Series (60min)"]
            latest_time = max(time_series.keys())
            latest_data = time_series[latest_time]
            # Get the latest price, percentage change, and volume of the stock
            latest_price = float(latest_data["4. close"])
            previous_price = float(time_series[sorted(time_series.keys())[-2]]["4. close"])
            percentage_change = round(((latest_price - previous_price) / previous_price) * 100, 2)
            volume = int(latest_data["5. volume"])
            # Print the results
            print(f"The latest price of {self.STOCK} is ${latest_price}")
            print(f"The percentage change of {self.STOCK} is {percentage_change}%")
            print(f"The volume of {self.STOCK} is {volume}")
        except Exception as e:
            print(f"An error occurred: {e}")


        self.percentage_change = 90
        print(self.percentage_change)
        print(stocks_data)







        # # try:
        # stock_response = requests.get(url=self.STOCKS_URL, params=stocks_params)
        # stock_response.raise_for_status()
        # stocks_data = stock_response.json()
        # time_series = stocks_data["Time Series (60min)"]
        # # time_series = stocks_data['interval']["60min"]
        # latest_time = max(time_series.keys())
        # latest_data = time_series[latest_time]
        # # Get the latest price, percentage change, and volume of the stock
        # latest_price = float(latest_data["4. close"])
        # previous_price = float(time_series[sorted(time_series.keys())[-2]]["4. close"])
        # self.percentage_change = round(((latest_price - previous_price) / (previous_price)) * 100, 2)
        # percentage_change = round(((latest_price - previous_price) / (previous_price)) * 100, 2)
        # print(percentage_change)
        # volume = int(latest_data["5. volume"])
        # self.volume = int(latest_data["5. volume"])
        # # Print the results
        # # percentage = (f"The percentage change of {self.STOCK} is {self.percentage_change}%")
        # vol = f"The volume of {self.STOCK} is {volume}"
        # # if percentage_change > 0:
        # #     self.ARROW = ARROW_UP
        # # else:
        # #     self.ARROW = ARROW_DOWN
        # # return f"The latest price of {self.STOCK} is ${latest_price}\n{percentage}\n{vol}"
        # # return time_series

        # # except Exception as e:

        # # print(f"An error occurred: {e}")
        # # return f"An error occurred: {e}"