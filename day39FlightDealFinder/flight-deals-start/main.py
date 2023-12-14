#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import requests
from data_manager import DataManager
from pprint import pprint
from flight_search import FlightSearch

#x------------------------------- Sheety Requests ------------------------------------x
sheety = DataManager()
# sheet_data = sheety.add_row()
flight_code = FlightSearch()

print(sheety.edit_row_data())
