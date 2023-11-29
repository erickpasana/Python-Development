# Python Email/Message Sending

import smtplib

class EmailMessage:

    def __init__(self, subject, messagebody):
        MY_EMAIL = "omegakonstrukt@gmail.com"
        PWD = "hxtf fjvb aext gsvy"
        self.subject = subject
        self.messagebody = messagebody
        self.email_addr = MY_EMAIL
        self.pwd = PWD
        
    def send_mail(self):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=self.email_addr, password=self.pwd)
            connection.sendmail(from_addr=self.email_addr, to_addrs='laopasana@outlook.com', msg=f"Subject: {self.subject}\n{self.messagebody}")
            print('Succeess')
