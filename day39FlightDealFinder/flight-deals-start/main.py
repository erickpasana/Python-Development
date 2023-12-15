#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import requests
from data_manager import DataManager
from pprint import pprint
from flight_search import FlightSearch
from flight_data import FlightData

#x------------------------------- Sheety Requests ------------------------------------x
sheety = DataManager('id', 'flight_code')
# sheet_data = sheety.add_row()

# iata_code = flight_code.get_code()

# print(sheety.edit_row_data())
# £
# response = requests.get(sheety.end_point)
# data = response.json()
# for i, row in enumerate(data['prices']):
#     flight_code = FlightData(row['city'])
#     row_id = row['id']
#     print(f"{row['city']}: £{0}")

#x------------------------------- Flight Search ------------------------------------x
fls = FlightSearch()
# fls.price()


    # edit_IATA = requests.put(f"{self.end_point}/{row_id}", json=request_body, headers=self.sheety_header)
    # print(edit_IATA.text)

    # request_body = {
    #     "price": {
    #         # 'city': 'Manila',
    #         "iataCode": flight_code.get_code(),
    #         # "lowestPrice": 350,
    #     }
    # }
    # sheety.edit_row_data()
    # sheety = DataManager(row['id'], flight_code.get_code())