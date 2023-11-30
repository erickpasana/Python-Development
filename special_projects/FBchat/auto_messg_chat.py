import datetime as dt
import random
import fbchat
from getpass import getpass
# import smtplib

username = "brodpete13@gmail.com"
client = fbchat.Client(username, getpass())
name = "Frederick Pasana"
friends = client.getUsers(name)
friend = friends[0]
msg = "Hello"
sent = client.send(friend.uid, msg)
if sent:
    print("Message sent successfully!")

# username = input("Username: ")
# client = fbchat.Client(username, getpass())
# name = input("Name: ")
# friends = client.getUsers(name) # return a list of names
# friend = friends[0]
# msg = input("Message: ")
# sent = client.send(friend.uid, msg)
# if sent:
#     print("Message sent successfully!")


#x--------------------------------- Constants ---------------------------------------x


#x------------------------------- Get Message Body -----------------------------------x


#x--------------------------------- Send Message -----------------------------------x
now = dt.datetime.now()
weekday = now.strftime("%A")
# year = now.year
# month = now.month
# # weekday = now.weekday()

if weekday == 'Tuesday':
    index = random.randint(0, 102)
    with open('quotes.txt', 'r') as file:
        quotes = file.readlines()
        quote = random.choice(quotes)
        email_body = quote

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PWD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="laopasana@outlook.com", msg=f"Subject: Monday Inspirational Quote\n\n{quote}")

    print(weekday)
    print(email_body)
