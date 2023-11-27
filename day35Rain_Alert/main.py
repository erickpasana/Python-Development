import requests
import json

LAT = 10.296758
LON = 124.789370
# API_key = '47596f2505bc76850330927570dbf604'
API_key = '3e5771e5877ff5e32e79a8a089ea546d'
PARAMS = {
    "lat": LAT,
    "lon": LON,
    'appid': API_key,
    'units': 'metric',
    'cnt': 4,
} 

# d_url = f"https://api.openweathermap.org/data/2.5/weather?lat=10.296758&lon=124.789370&appid={API_key}"
# https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid={API key}
d_url = f"https://api.openweathermap.org/data/2.5/weather?"
d_url_5_3 = f"https://api.openweathermap.org/data/2.5/forecast?"


# response = requests.get(url=d_url, params=PARAMS)
response = requests.get(url=d_url_5_3, params=PARAMS)
response.raise_for_status()
# print(response.status_code)

data = response.json()
# bring_or_not = json.dumps(data['list'][2]['weather'][0]['id'], indent=4)
for h in range(4):
#     # id = h  #['id']['weather']
    id = data['list'][h]['weather'][0]['id']#['id']
    print(id)
    print(data['list'][h]['dt_txt'])#[0]['id']
    # print(id[0]['id'])

    # if int(id) < 701:
    if id < 701:
        print("Bring an unbrella.")
    else:
        print("Just bring, just in case.")

# print(json.dumps(data['list'][2]['weather'], indent=4))#['id']
# print(Hr_3_cut_off[2])
# print(data['list'])