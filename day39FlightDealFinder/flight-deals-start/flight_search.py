import os
import requests
import json
# from flight_data import FlightData

search_endpoint = 'https://api.tequila.kiwi.com/v2/search'
# flight_data_price = FlightData()
# data[0]['price']
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, city_from, city_to):
        self.endpoint = search_endpoint
        self.fly_from = f"fly_from=city:{city_from}"
        self.fly_to = f"fly_to=city:{city_to}"
        self.date_from='17/12/2024'
        self.date_to='23/12/2023' 
        self.headers = {
            # 'apikey': self.kiwi_API,
            'apikey': '2z6qJ-wObDBvJ93qovMh7TQRi246n1gx',
            'Content-Type': 'application/json',
        }

    def get_price(self):
        endpoint_to_use = f"{self.endpoint}?{self.fly_from}&{self.date_from}&{self.date_to}&{self.fly_to}"
        response = requests.get(endpoint_to_use, headers=self.headers)
        # print(response.text)
        flight_price = response.json()
        str_flight_price = flight_price['data'][0]['price']
        # flight_data_price.price = str_flight_price
        return str_flight_price
        

    def get_city(self):
        # self.request_body = {
        #     'term': self.city
        # }
        flight_response = requests.get(self.endpoint, params=self.request_body, headers=self.headers)
        # print(flight_response.text)
        flight_data = flight_response.json()
        return flight_data['locations'][0]['code']
        # return flight_data['locations'][0]['id']
