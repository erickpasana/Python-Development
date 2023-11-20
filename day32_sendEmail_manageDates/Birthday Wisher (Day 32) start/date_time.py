import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
# weekday = now.weekday()
weekday = now.strftime("%A")
print(weekday)