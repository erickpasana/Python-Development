"""Days in Month"""

def is_leap_year(year):
    result = False
    if year % 4 == 0:
        # if year % 100 == 0:
        result = True
    return result

# TODO: Add more code here 👇
def days_in_month(year, month):
    year = is_leap_year(year)
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
    if year == True:
        month_days[1] = 29
    return month_days[month - 1]

#🚨 Do NOT change any of the code below 
year = int(input("Give the year: ")) # Enter a year
month = int(input("Give the month: ")) # Enter a month
days = days_in_month(year, month)
print(days)