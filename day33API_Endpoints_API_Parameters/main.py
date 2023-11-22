import requests
import smtplib
import datetime
import pytz

# 10.296758,124.789370
MY_LAT = 10.29675
MY_LNG = 124.78936
API = 'https://api.sunrise-sunset.org/json'
MY_EMAIL = "omegakonstrukt@gmail.com"
PWD = "hxtf fjvb aext gsvy"

PARAMETERS = {
    'lat': MY_LAT,
    'lng': MY_LNG,
    'formatted': 0
}

def viewable_time():
    #Determine if the ISS is at a viewable time
    response = requests.get(url=API, params=PARAMETERS, )
    response.raise_for_status()
    data = response.json()
    sunrise = data['results']['sunrise']
    sunset = data['results']['sunset']
    sunrise_dt = datetime.datetime.fromisoformat(sunrise)
    sunset_dt = datetime.datetime.fromisoformat(sunset)
    sunset_dt = sunset_dt.replace(tzinfo=pytz.timezone("Asia/Manila"))
    utc_8 = datetime.timedelta(hours=8)
    sunset_dt_8 = sunset_dt + utc_8
    td = datetime.timedelta(hours=3)
    tplus = sunset_dt_8 + td
    time_now = datetime.datetime.now()
    time_now = time_now.replace(tzinfo=pytz.timezone("Asia/Manila"))
    
    if time_now > sunset_dt_8 and time_now < tplus:
        return True
    else:
        return False


def ISS_view_loc():
    response = requests.get(url='http://api.open-notify.org/iss-now.json')
    response.raise_for_status()
    data = response.json()
    lat = float(data['iss_position']['latitude'])
    lng = float(data['iss_position']['longitude'])
    if lat > MY_LAT-3 and lat < MY_LAT+3 and lng > MY_LNG-3 and lng < MY_LNG+3:
        return True
    else:
        return False

def email_notification():
    if viewable_time() == True and ISS_view_loc() == True:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PWD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs='laopasana@outlook.com', msg=f"Subject: ISS View\n\nView the ISS now!!!")
            print('Succeess')

email_notification()
print(ISS_view_loc())
print(viewable_time())



# lat (float): Latitude in decimal degrees. Required.
# lng (float): Longitude in decimal degrees. Required.
# date (string): Date in YYYY-MM-DD format. Also accepts other date formats and even relative date formats. If not present, date defaults to current date. Optional.
# callback (string): Callback function name for JSONP response. Optional.
# formatted (integer): 0 or 1 (1 is default). Time values in response will be expressed following ISO 8601 and day_length will be expressed in seconds. Optional.

# {
#   "message": "success", 
#   "timestamp": UNIX_TIME_STAMP, 
#   "iss_position": {
#     "latitude": CURRENT_LATITUDE, 
#     "longitude": CURRENT_LONGITUDE
#   }
# }
