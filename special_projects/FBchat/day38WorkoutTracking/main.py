import requests
import json
from datetime import datetime as dt
import os


#x------------------------------- Constants --------------------------------------x
APP_ID = 'f5fb5329'
API_KEY = '17c8a9516aa3fa34abc7d1945dc7abfe'
sheety_Username = 'Erick88'
sheety_pwd = 'GGnhC7@xDBtjb7^U'
GENDER = 'Male'
WEIGHT = 47
HEIGHT = 160
AGE = 56
DATE = dt.now().strftime("%d/%m/%Y")
TIME = dt.now().strftime("%X")

#x------------------------------- Requests --------------------------------------x
End_POINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
# user_input = input("Tell me which exercises you did: ")
user_input = 'Meditating'
exercise_params = {
    "query": user_input,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
}
headers = {
    'Content-Type': 'application/json',
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
    }

# response = requests.post(End_POINT, json=exercise_params, headers=headers)
# result = response.json()
# print(json.dumps(result, indent=4))

#x------------------------------- Add Row --------------------------------------x
# sheety_end_point = 'https://api.sheety.co/b17d3c0b422c3d51ecc6636c25073af5/walks/workouts'
sheety_end_point = os.environ.get('SHEETY_END_POINT')
# request_body = {
#     "workout": {
#         "date": DATE,
#         "time": TIME,
#         "exercise": result['exercises'][0]["name"].title(),
#         "duration": result['exercises'][0]["duration_min"],
#         "calories": result["exercises"][0]["nf_calories"],
#     }
# }
# for exercise in result["exercises"]:
#     sheet_inputs = {
#         "workout": {
#             "date": DATE,
#             "time": TIME,
#             "exercise": exercise["name"].title(),
#             "duration": exercise["duration_min"],
#             "calories": exercise["nf_calories"]
#         }
#     }

# sheety_header = {
#     'Content-Type': 'application/json',
#     }

# sheety_response = requests.post(sheety_end_point, json=sheet_inputs, headers=sheety_header)
# sheety_response = requests.post(sheety_end_point, json=request_body, headers=sheety_header)

# sheety_result = sheety_response.json()
# print(json.dumps(sheety_result, indent=4))

#x------------------------------- Edit Row --------------------------------------x
# sheety_end_point_edit = 'https://api.sheety.co/b17d3c0b422c3d51ecc6636c25073af5/walks/workouts/5'
# request_body = {
#     "workout": {
#         "exercise": 'Running',
#     }
# }
# sheety_header = {
#     'Content-Type': 'application/json',
#     }
# sheety_response = requests.put(sheety_end_point_edit, json=request_body, headers=sheety_header)

# sheety_result = sheety_response.json()
# print(json.dumps(sheety_result, indent=4))

#x------------------------------- Edit Row --------------------------------------x
# sheety_end_point_delete = 'https://api.sheety.co/b17d3c0b422c3d51ecc6636c25073af5/walks/workouts/5'
# sheety_header = {
#     'Content-Type': 'application/json',
#     "Authorization": "Basic RXJpY2s4ODpHR25oQzdAeERCdGpiN15V"
#     }

# sheety_response = requests.delete(sheety_end_point_delete)

#x------------------------------- Get Records --------------------------------------x
sheety_Auth_header = {
    'Content-Type': 'application/json',
    "Authorization": "Basic RXJpY2s4ODpHR25oQzdAeERCdGpiN15V"
    }
sheety_response_records = requests.get(sheety_end_point, headers=sheety_Auth_header)
sheety_records = sheety_response_records.json()
print(json.dumps(sheety_records, indent=4))
