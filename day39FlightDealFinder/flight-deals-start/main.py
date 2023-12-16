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

# ----------------------print City: Price--------------------x
# for i, row in enumerate(data['prices']):
#     city_from = 'LON'
#     city_to = row['iataCode']
#     flight_price = FlightSearch(city_from, city_to)
#     flight_price.get_price()
#     #flight_data.price
#     flight_data = FlightData()
#     print(f"{row['city']}: £{flight_price.get_price()}")

#x------------------------------- Notification ------------------------------------x
import sys
msg_path = r"C:\Users\flpas\OneDrive - Connection Systems Development\Python-Development"
sys.path.insert(0, msg_path)#\SendMessage.py
from SendMessage import Message
subject = 'Cheap Flights'
email_list = ['laopasana@outlook.com', ]#'dodj_ortalla@yahoo.com'

for i, row in enumerate(data['prices']):
    city_from = 'LON'
    city_to = row['iataCode']
    flight_price = FlightSearch(city_from, city_to)
    floor_price = row['lowestPrice']
    actual_price = flight_price.get_price()
    body = f"""
    Low price alert! Only ${actual_price} to fly
    from Manila to {row['city']}."""
    print(f"{floor_price} : {actual_price}")
    if actual_price < floor_price:
        email_msg = Message(subject, body, email_list)
        email_msg.sendMessage()


"""
Price

Departure City Name

Departure Airport IATA Code

Arrival City Name

Arrival Airport IATA Code

Outbound Date

Inbound Date
"""


    # flight_data = FlightData()
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