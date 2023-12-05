import requests
from datetime import datetime

#PWD iaOb9@xT#v5nVkSY
USERNAME = 'erick88'
TOKEN = 'iaOb9@xT#v5nVkSY'
# DATE = datetime.now().strftime("%Y%m%d")
DATE = datetime(year=2023, month=12, day=4)
TODAY = DATE.strftime("%Y%m%d")
pixela_end_point = 'https://pixe.la/v1/users'
parameters = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# create_account_response = requests.post(url=pixela_end_point, json=parameters)

graph_endpoint = f"{pixela_end_point}/{USERNAME}/graphs"
graph_config = {
    'id': 'graph1',
    'name': 'Daily Steps',
    'unit': 'steps',
    'type': 'int',
    'color': 'shibafu',
    'timezone': 'Asia/Manila'
}

header = {
    "X-USER-TOKEN": TOKEN
}

# add_graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=header)

id = 'graph1'
add_pixel = f"{graph_endpoint}/{id}"
# add_date = '20231205'
qty = '2556'
pixel_config = {
    'date': TODAY,
    'quantity': qty,
}

# add_pixel_response = requests.post(url=add_pixel, json=pixel_config, headers=header)

update_pixel_response =  requests.put(url=f"{graph_endpoint}/{id}/{TODAY}", json={'quantity': qty}, headers=header)

# delete_pixel_response = requests.delete(url=f"{graph_endpoint}/{id}/{TODAY}", headers=header)

print(update_pixel_response.status_code)
print(update_pixel_response.text)
# print(DATE)
print(TODAY)
# print(type(TODAY))
