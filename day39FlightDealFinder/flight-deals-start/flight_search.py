import os
import requests
import json
from flight_data import FlightData

search_endpoint = 'https://api.tequila.kiwi.com/v2/search'
# data[0]['price']
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self,):
        self.endpoint = search_endpoint
        self.fly_from = 'city:LON'
        
        self.date_from='16/12/2024'
        self.date_to='03/05/2024' 
        self.headers = {
            # 'apikey': self.kiwi_API,
            'apikey': '2z6qJ-wObDBvJ93qovMh7TQRi246n1gx',
            'Content-Type': 'application/json',
        }

    def price(self):
        endpoint_to_use = f"{self.endpoint}?{self.fly_from}&{self.date_from}&{self.date_to}"
        print(endpoint_to_use)
        response = requests.get(endpoint_to_use, headers=self.headers)
        print(response.text)
        # get_price = response.json()
        # print(json.dumps(get_price, indent=4))#'data'[0]['price']

        def get_id(self):
            # self.request_body = {
            #     'term': self.city
            # }
            flight_response = requests.get(self.kiwi_endpoint, params=self.request_body, headers=self.headers)
            # print(flight_response.text)
            flight_data = flight_response.json()
            return flight_data['locations'][0]['code']
            # return flight_data['locations'][0]['id']
