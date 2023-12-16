#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import requests
from data_manager import DataManager
from pprint import pprint
from flight_search import FlightSearch
from flight_data import FlightData

pound_sign = '£'

#x------------------------------- Sheety Requests ------------------------------------x
sheety = DataManager('id', 'flight_code')
response = requests.get(sheety.end_point)
data = response.json()
for i, row in enumerate(data['prices']):
    city_from = 'LON'
    city_to = row['iataCode']
    flight_price = FlightSearch(city_from, city_to)
    flight_price.get_price()
    #flight_data.price
    flight_data = FlightData()
    print(f"{row['city']}: £{flight_price.get_price()}")
    # print(f"{row['city']}: £{flight_data.price}")
    # edit_IATA = requests.put(f"{self.end_point}/{row_id}", json=request_body, headers=self.sheety_header)
    # print(edit_IATA.text)

#x------------------------------- Flight Search ------------------------------------x
# fls = FlightSearch()
# print(fls.get_price())
# fl_dt_price = FlightData()
# print(fl_dt_price.price)
#x------------------------------- Flight Search ------------------------------------x





    # request_body = {
    #     "price": {
    #         # 'city': 'Manila',
    #         "iataCode": flight_code.get_code(),
    #         # "lowestPrice": 350,
    #     }
    # }
    # sheety.edit_row_data()
    # sheety = DataManager(row['id'], flight_code.get_code())