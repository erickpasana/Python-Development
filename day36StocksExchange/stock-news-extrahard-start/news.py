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
        # self.articles = news_data['articles']

    def news(self):
        NEWS_URL = "https://newsapi.org/v2/everything?"
        NEWS_API_KEY = "115ef21aaf38432fa21925fdc32ffddf"
        news_params = {
            'qInTitle': self.COMPANY_NAME,
            'apiKey': NEWS_API_KEY,
            # 'q': self.COMPANY_NAME,
            # 'from': '2023-12-10',
            # 'from': '',
            # 'from': '2023-12-01',
            # 'to': '2023-12-01',
            # 'sortBy': 'publishedAt',
        }
            
        news_response = requests.get(url=NEWS_URL, params=news_params)
        news_response.raise_for_status()
        news_data = news_response.json()
        self.title = news_data['articles'][0]['title']
        self.description = news_data['articles'][0]['description']
        self.articles = news_data['articles'][:3]
        # self.articles = json.dumps(self.articles, indent=4)
        formatted_articles = [f"Headline: {article['title']}\nBrief: {article['description']}" for article in self.articles]
        # return f"Status: {stocks_data['status']}  Total News: {stocks_data['totalResults']}"
        # return f"Article: {stocks_data['articles'][0]['description']}\n{stocks_data['articles'][0]['title']}"
        return formatted_articles