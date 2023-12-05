import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Message:

# x-------------------- Attributes --------------------------x
    def __init__(self, subject, body, ):   #Arrow
        self.MY_EMAIL = "omegakonstrukt@gmail.com"
        self.PWD = "hxtf fjvb aext gsvy"
        self.SUBJECT = subject
        self.BODY = body

# x-------------------- Send Message -------------------------------x
    def sendMessage(self):
        msg = MIMEMultipart()
        msg['Subject'] = self.SUBJECT
        msg['From'] = self.MY_EMAIL
        msg['To'] = 'laopasana@outlook.com'
        text = self.BODY
        part1 = MIMEText(text, 'plain', 'utf-8')
        msg.attach(part1)

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=self.MY_EMAIL, password=self.PWD)
            # connection.sendmail(from_addr=self.MY_EMAIL, to_addrs='laopasana@outlook.com', msg=f"Subject: {self.SUBJECT}\n\n{self.BODY}")
            connection.send_message(msg)
            print('Success')






            
    # def sendMessage(self):
    #     with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    #         connection.starttls()
    #         connection.login(user=self.MY_EMAIL, password=self.PWD)
    #         # connection.sendmail(from_addr=MY_EMAIL, to_addrs='laopasana@outlook.com', msg=f"Subject: TSLA Stocks\n\n{headline}\n{news_body}")
    #         connection.sendmail(from_addr=self.MY_EMAIL, to_addrs='laopasana@outlook.com', msg=f"Subject: {self.SUBJECT}\n\n{self.BODY}")      #\n\n{news_body1}
    #         print('Success')

# ARROW = None
# ARROW_UP = "🔺"
# ARROW_DOWN = "🔻"
# if percent_latest_closing_diff > 0:
#     ARROW = ARROW_UP
# else:
#     ARROW = ARROW_DOWN  

# Create the container email message.
# msg = MIMEMultipart()
# msg['Subject'] = 'Subject with emoji 📧'
# msg['From'] = 'your_email@example.com'
# msg['To'] = 'recipient_email@example.com'

# # Create a text/plain message with UTF-8 encoding for emojis.
# text = 'Hello, this is a message with an emoji 👋'
# part1 = MIMEText(text, 'plain', 'utf-8')

# # Attach parts into message container.
# msg.attach(part1)

# # Send the email via your SMTP server.
# with smtplib.SMTP('smtp.example.com') as server:
#     server.send_message(msg)