import requests

#PWD iaOb9@xT#v5nVkSY
USERNAME = 'erick88'
TOKEN = 'iaOb9@xT#v5nVkSY'  
pixela_end_point = 'https://pixe.la/v1/users'
parameters = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

graph_endpoint = f"{pixela_end_point}/{USERNAME}/graph"
graph_config = {
    'id': 'graph1',
    'name': 'Daily Steps',
    'unit': 'Steps',
    'type': 'int',
    'color': 'shibafu',
    'timezone': 'Asia/Manila'
}

header = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=header)

print(response.status_code)
print(response.text)

# response = requests.post(url=pixela_end_point, json=parameters)               