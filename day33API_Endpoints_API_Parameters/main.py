import requests
import datetime

response = requests.get(url='http://api.open-notify.org/iss-now.json')
response.raise_for_status()
data = response.json()
data = data['timestamp']
dt = datetime.datetime.fromtimestamp(data)
print(dt)