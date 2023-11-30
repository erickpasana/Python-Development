# Python Email/Message Sending
import smtplib
import requests
import json
import datetime

SUBJECT = "Weather Alert!!!"
MY_EMAIL = "omegakonstrukt@gmail.com"
PWD = "hxtf fjvb aext gsvy"
LAT = 10.296758
LON = 124.789370
API_key = '3e5771e5877ff5e32e79a8a089ea546d'
PARAMS = {
    "lat": LAT,
    "lon": LON,
    'appid': API_key,
    'units': 'metric',
    'cnt': 6,
}
# d_url = f"https://api.openweathermap.org/data/2.5/weather?lat=10.296758&lon=124.789370&appid={API_key}"
d_url = f"https://api.openweathermap.org/data/2.5/weather?"
d_url_5_3 = f"https://api.openweathermap.org/data/2.5/forecast"

response = requests.get(url=d_url_5_3, params=PARAMS)
response.raise_for_status()
data = response.json()

class EmailMessage:

    def __init__(self):
        self.subject = SUBJECT
        self.messagebody = ""
        # self.messagebody = message()
        self.email_addr = MY_EMAIL
        self.pwd = PWD

    def message(self):
        # self.messagebody = "self_message2"
        body = ""
        for hour_data in data['list']:
            id = hour_data['weather'][0]['id']
            time = hour_data['dt_txt']
            if int(id) < 701:
                body += f"At {time}, it could rain.\n"
            else:
                body += f"At {time}, could be sunny.\n"
        
        self.messagebody = body
        print(self.messagebody)
        
    def send_mail(self):
        self.message()
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=self.email_addr, password=self.pwd)
            connection.sendmail(from_addr=self.email_addr, to_addrs='laopasana@outlook.com', msg=f"Subject: {self.subject}\n\n{self.messagebody}") #
            connection.quit()
            print('Success')
