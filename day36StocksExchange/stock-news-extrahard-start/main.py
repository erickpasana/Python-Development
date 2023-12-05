import smtplib
import requests
import json
import datetime
from SendMessage import Message
from stocks import Stocks
from news import News
# from stock_data import stock_data
from stocks_data_new_json import new_json_data

# x-------------------- Constants --------------------------x
MY_EMAIL = "omegakonstrukt@gmail.com"
PWD = "hxtf fjvb aext gsvy"
COMPANY_NAME = "Tesla Inc"
stock_data = Stocks(new_json_data)
news_data = News()

# # x-------------------- Message -------------------------------x
stock_data.stock()
yesterday_open = stock_data.yesterday_open
yesterday_close = stock_data.yesterday_close
otherday_open = stock_data.otherday_open
otherday_close = stock_data.otherday_close
latest_closing_diff = float(yesterday_close) - float(otherday_close)
percent_latest_closing_diff = round(abs(latest_closing_diff / float(yesterday_close) * 100), 4)
ARROW = None
ARROW_UP = "🔺"
ARROW_DOWN = "🔻"
if percent_latest_closing_diff > 0:
    ARROW = ARROW_UP
else:
    ARROW = ARROW_DOWN  

# x-------------------- Send Message -------------------------------x
formatted_news = news_data.news()

for news in formatted_news:
    headline = f"{stock_data.STOCK}: {ARROW}{percent_latest_closing_diff}%"
    # news_body = f"{headline}\nHeadline: {news['title']}.\n\nBrief: {news['description']}."
    news_body = f"{headline}\n{news}"
    # news_body = news_body.replace('\u2026', '...')
    # news_body = news_body.replace('\u2013', '-')
    # news_body = news_body.replace('\u2019', "'")
    # news_body1 = news_body1.encode('utf-8')
    Send_message = Message("TSLA Stocks", news_body)
    Send_message.sendMessage()
    print(news_body)


# print(ARROW)
# print(yesterday_close)
# print(otherday_close)
# print(latest_closing_diff)
# print(percent_latest_closing_diff)
# stock_data.ARROW
# print(news_data.news())


# data = new_json_data
# data = json.dumps(data["Time Series (Daily)"], indent=4)
# # data = json.dumps(data, indent=4)
# print(data)

# with open("stocks_data_new_json.py", "w") as file:
#     # convert the stocks_data to a string
#     data_str = json.dumps(stock_data.stock())
#     # write the data to the file
#     file.write(data_str)

"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


# print(stock_data.percentage_change)
# print(stock_data.stock())
# print(stock_data.percentage_change)

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 

