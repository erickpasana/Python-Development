import requests
import os
import json

# publish = https://docs.google.com/spreadsheets/d/e/2PACX-1vS7GbYQ9lt4DV5wsiN9-RVep3t99gcAj6M_3HteNvFfiQL414gDPBDmRUH-9lLhnhW_F0aUJdbiBMSo/pubhtml

project_sheet = f'flightdeals/prices'
sheety_end_point = f'https://api.sheety.co/b17d3c0b422c3d51ecc6636c25073af5/{project_sheet}'

class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self, row_id, iata_code):
        self.end_point = os.environ.get("sheety_end_point")
        self.row_id = row_id
        self.iata_code = iata_code
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
        response = requests.get(self.end_point)
        data = response.json()
        request_body = {
            "price": {
                # 'city': 'Manila',
                "iataCode": self.iata_code,
                # "lowestPrice": 350,
            }
        }
        # row_id = row['id']
        edit_IATA = requests.put(f"{self.end_point}/{self.row_id}", json=request_body, headers=self.sheety_header)
        print(edit_IATA.text)


#         request_body = {
#     "price": {
#         # 'city': 'Manila',
#         "iataCode": 'Testing',
#         # "lowestPrice": 350,
#     }
# }
        
# for i, row in enumerate(data['prices']):
    #     # print(edit_IATA.text)