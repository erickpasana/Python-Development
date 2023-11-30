import requests
import json
import datetime
from alert_notification import EmailMessage

send_class = EmailMessage()
# # send_alert = send_class.send_mail()
# print(message())
send_class.send_mail()


# SUBJECT = "Weather Alert!!!"
# LAT = 10.296758
# LON = 124.789370
# API_key = '3e5771e5877ff5e32e79a8a089ea546d'
# PARAMS = {
#     "lat": LAT,
#     "lon": LON,
#     'appid': API_key,
#     'units': 'metric',
#     'cnt': 6,
# } 

# # d_url = f"https://api.openweathermap.org/data/2.5/weather?lat=10.296758&lon=124.789370&appid={API_key}"
# d_url = f"https://api.openweathermap.org/data/2.5/weather?"
# d_url_5_3 = f"https://api.openweathermap.org/data/2.5/forecast"


# # response = requests.get(url=d_url, params=PARAMS)
# response = requests.get(url=d_url_5_3, params=PARAMS)
# response.raise_for_status()
# # print(response.status_code)
# data = response.json()

# def message():
#     body = ""
#     for hour_data in data['list']:
#         # id = hour_data['weather'][0]['id']
#         id = hour_data['weather'][0]['id']
#         time = hour_data['dt_txt']

#         if int(id) < 701:
#         # if id < 701:
#             body += f"At {time}, it could rain.\n"
#             # print(body)
#             # send_class
#         else:
#             body += f"At {time}, could be sunny.\n"
#             # print(body)
#             # send_class
#     return print(body)



# bring_or_not = json.dumps(data['list'][2]['weather'][0]['id'], indent=4)
# for h in range(4):
# #     # id = h  #['id']['weather']
#     id = data['list'][h]['weather'][0]['id']#['id']
#     print(id)
#     print(data['list'][h]['dt_txt'])#
    # print(id[0]['id'])