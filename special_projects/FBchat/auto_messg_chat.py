import datetime as dt
import random
import fbchat
from getpass import getpass
# import smtplib

#x--------------------------------- Constants ---------------------------------------x
username = "brodpete13@gmail.com"
PWD = 'UF3PyGBQxX4u'

#x------------------------------- Get Message Body -----------------------------------x


#x--------------------------------- Send Message -----------------------------------x
# now = dt.datetime.now()
# weekday = now.strftime("%A")
# # year = now.year
# # month = now.month
# # # weekday = now.weekday()

# if weekday == 'Tuesday':
#     index = random.randint(0, 102)
#     with open('quotes.txt', 'r') as file:
#         quotes = file.readlines()
#         quote = random.choice(quotes)
#         email_body = quote

#     with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#         connection.starttls()
#         connection.login(user=MY_EMAIL, password=PWD)
#         connection.sendmail(from_addr=MY_EMAIL, to_addrs="laopasana@outlook.com", msg=f"Subject: Monday Inspirational Quote\n\n{quote}")

#     print(weekday)
#     print(email_body)





# client = fbchat.Client(username, getpass())
# client = fbchat.Client(username, PWD)
# name = "Frederick Pasana"
# users = client.getUsers(name) # returns a list of matching users
# # user = users[0] # get the first user from the list
# user = name # get the first user from the list
# print(user.uid) # print the user ID