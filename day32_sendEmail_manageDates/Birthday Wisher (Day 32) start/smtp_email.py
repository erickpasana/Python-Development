import smtplib
import datetime as dt
import random

MY_EMAIL = "omegakonstrukt@gmail.com"
PWD = "hxtf fjvb aext gsvy"

# connection = smtplib.SMTP("smtp.gmail.com", 587)
# connection.starttls()
# connection.login(user=MY_EMAIL, password=PWD)
# connection.sendmail(from_addr=MY_EMAIL, to_addrs="laopasana@outlook.com", msg="Subject: Hello\n\nThis is the body of my test email.")
# connection.close()

#x--------------------------------- Constants ---------------------------------------x
# MY_EMAIL = "omegakonstrukt@gmail.com"
# PWD = "hxtf fjvb aext gsvy"
# connection = smtplib.SMTP("smtp.gmail.com")
#463xJUlY8hq3   "hxtf fjvb aext gsvy"
#x------------------------------- Get Email Body -------------------------------------x


#x--------------------------------- Send Email ---------------------------------------x
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
