import smtplib
import requests
import json
import datetime


class Message:

# x-------------------- Attributes --------------------------x
    def __init__(self, subject, body):
        self.MY_EMAIL = "omegakonstrukt@gmail.com"
        self.PWD = "hxtf fjvb aext gsvy"
        self.SUBJECT = subject
        self.BODY = body

# x-------------------- Send Message -------------------------------x
    def sendMessage(self):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=self.MY_EMAIL, password=self.PWD)
            # connection.sendmail(from_addr=MY_EMAIL, to_addrs='laopasana@outlook.com', msg=f"Subject: TSLA Stocks\n\n{headline}\n{news_body}")
            connection.sendmail(from_addr=self.MY_EMAIL, to_addrs='laopasana@outlook.com', msg=f"Subject: {self.SUBJECT}\n\n{self.BODY}")      #\n\n{news_body1}
            print('Success')

    