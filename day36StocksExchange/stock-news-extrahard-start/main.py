import smtplib
import requests
import json
import datetime
from stocks import Stocks
from news import News

# x-------------------- Constants --------------------------x
MY_EMAIL = "omegakonstrukt@gmail.com"
PWD = "hxtf fjvb aext gsvy"
COMPANY_NAME = "Tesla Inc"

stock_data = Stocks()
news_data = News()
# print(stock_data.percentage_change)
# stock_data.stock()
print(stock_data.stock())
# news_data.news()
# headline = f"{stock_data.STOCK}: {stock_data.ARROW}{stock_data.percentage_change}"
# news_body = f"Headline: {news_data.title}.\nBrief: {news_data.description}."

# x-------------------- Send Message -------------------------------x
# with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#     connection.starttls()
#     connection.login(user=MY_EMAIL, password=PWD)
#     connection.sendmail(from_addr=MY_EMAIL, to_addrs='laopasana@outlook.com', msg=f"Subject: TSLA Stocks\n\n{headline}\n{news_body}")
#     print('Succeess')

# x-------------------- Message -------------------------------x
# print(f"{stock_data.STOCK}: {stock_data.ARROW}{stock_data.percentage_change}%")
# print(f"Headline: {news_data.title}.\nBrief: {news_data.description}.")
# connection.sendmail(from_addr=MY_EMAIL, to_addrs='laopasana@outlook.com', 
# msg=f"Subject: TSLA Stocks\n\n{headline}\n{news_body}"
# print(stock_data.percentage_change)
# print(stock_data.ARROW)
# print(stock_data.volume)






## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

