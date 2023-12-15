import os
import requests
import json
from flight_search import FlightSearch

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, city):
        self.kiwi_API = os.environ.get('KiwiPartnersTequila_API')
        self.kiwi_endpoint = 'https://api.tequila.kiwi.com/locations/query'
        self.headers = {
            # 'apikey': self.kiwi_API,
            'apikey': '2z6qJ-wObDBvJ93qovMh7TQRi246n1gx',
            'Content-Type': 'application/json',
        }
        self.city = city
        self.id = ''
        self.price = 0
        self.departure_airport_code = ''
        self.departure_city = ''

    def get_code(self):
        self.request_body = {
            'term': self.city
        }
        flight_response = requests.get(self.kiwi_endpoint, params=self.request_body, headers=self.headers)
        # print(flight_response.text)
        flight_data = flight_response.json()
        return flight_data['locations'][0]['code']
        # return flight_data['locations'][0]['id']