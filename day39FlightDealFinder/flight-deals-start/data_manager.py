import requests
import os
import json

# publish = https://docs.google.com/spreadsheets/d/e/2PACX-1vS7GbYQ9lt4DV5wsiN9-RVep3t99gcAj6M_3HteNvFfiQL414gDPBDmRUH-9lLhnhW_F0aUJdbiBMSo/pubhtml

sheety_end_point = f'https://api.sheety.co/b17d3c0b422c3d51ecc6636c25073af5'
project_sheet = f'flightdeals/prices'
# project_sheet = 'walks/workouts'

class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.end_point = os.environ.get("end_point")
        self.sheety_header = {
            'Content-Type': 'application/json',
            "Authorization": "Basic RXJpY2s4ODpHR25oQzdAeERCdGpiN15V",
    }

    def add_row(self):
        # sheety_end_point = os.environ.get(f"{self.end_point}/{self.project_sheet}")
        # request_body = {
        #     "workout": {
        #         "date": DATE,
        #         "time": TIME,
        #         "exercise": result['exercises'][0]["name"].title(),
        #         "duration": result['exercises'][0]["duration_min"],
        #         "calories": result["exercises"][0]["nf_calories"],
        #     }
        # }


        # sheety_response = requests.post(sheety_end_point, json=sheet_inputs, headers=sheety_header)
        # sheety_response = requests.post(sheety_end_point, json=request_body, headers=sheety_header)
        sheety_response = requests.get(self.end_point, headers=self.sheety_header)

        sheety_result = sheety_response.json()
        return json.dumps(sheety_result, indent=4)
    
    def edit_row_data(self):
#         request_body = {
#     "price": {
#         'city': 'Manila',
#         "iataCode": 'Testing',
#         "lowestPrice": 350,
#     }
# }
        request_body = {
    "price": {
        # 'city': 'Manila',
        "iataCode": 'Testing',
        # "lowestPrice": 350,
    }
}
        response = requests.get(self.end_point)
        data = response.json()

        for i, row in enumerate(data['prices']):
            row_id = row['id']
            edit_IATA = requests.put(f"{self.end_point}/{row_id}", json=request_body, headers=self.sheety_header)
            # print(edit_IATA.text)
        
        # sheety_add = requests.post(self.end_point, json=request_body, headers=self.sheety_header)
        # print(sheety_add.text)
        response = requests.get(self.end_point)
        data = response.json()
        print(json.dumps(data, indent=4))
        # print(self.end_point)
