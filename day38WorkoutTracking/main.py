import requests
import json


#x------------------------------- Constants --------------------------------------x
APP_ID = 'f5fb5329'
API_KEY = '17c8a9516aa3fa34abc7d1945dc7abfe'
GENDER = 'Male'
WEIGHT = 47
HEIGHT = 160
AGE = 56
End_POINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

#x------------------------------- Requests --------------------------------------x
exercise_text = input("Tell me which exercises you did: ")
exercise_params = {
    "query": exercise_text,
    'gender': GENDER,
    # 'weight': WEIGHT,
    # 'height': HEIGHT,
    'age': AGE,
}
# exercise_response = requests.post(url=End_POINT, json=dict)
headers = {
    # 'Content-Type': 'application/json',
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
    }

response = requests.post(url=End_POINT, json=exercise_params, headers=headers)
result = response.json()
print(json.dumps(result, indent=4))


# var request = require('request');
# var options = {
#     'method': 'POST',
#     'url': 'https://trackapi.nutritionix.com/v2/natural/exercise',
#     'headers': {
#     'Content-Type': 'application/json',
#     'x-app-id': ,
#     'x-app-key':
#     },
#     body: JSON.stringify({
#     "query": "swam for 1 hour"
# })