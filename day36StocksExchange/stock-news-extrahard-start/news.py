import requests
import json
import datetime

class News:

    def __init__(self):
        # self.STOCKS_URL = "https://www.alphavantage.co/query?"
        self.STOCK = "TSLA"
        self.COMPANY_NAME = "Tesla Inc"
        self.title = ""
        self.description = ""

    def news(self):
        NEWS_URL = "https://newsapi.org/v2/everything?"
        NEWS_API_KEY = "115ef21aaf38432fa21925fdc32ffddf"
        news_params = {
            'q': self.COMPANY_NAME,
            # 'from': '2023-12-10',
            # 'from': '',
            'from': '2023-12-01',
            'to': '2023-12-01',
            'sortBy': 'publishedAt',
            'apiKey': NEWS_API_KEY,
        }
            
        news_response = requests.get(url=NEWS_URL, params=news_params)
        # news_response = requests.get(url=NEWS_URL)
        news_response.raise_for_status()
        stocks_data = news_response.json()
        self.title = stocks_data['articles'][0]['title']
        self.description = stocks_data['articles'][0]['description']
        # print(f"Status: {stocks_data['status']}   Total Results: {stocks_data['totalResults']}")
        # return f"Status: {stocks_data['status']}  Total News: {stocks_data['totalResults']}"
        # return f"Article: {stocks_data['articles'][0]['description']}\n{stocks_data['articles'][0]['title']}"
        # return stocks_data