import datetime as dt
import random
import pandas as pd
import numpy as np
from SendMessage import Message
# from data_list import quotes_list

# index = random.randint(0, len(quotes_list)-1)
# quote = quotes_list[index]
#x--------------------------------- Constants ---------------------------------------x

#x------------------------------- Get Message Body -----------------------------------x
data = pd.read_csv('data_list.csv')
q_index = random.randint(0, len(data)+1)
quote = f"{data.loc[q_index, 'Quote']} - {data.loc[q_index, 'Author']}"

#x--------------------------------- Send Message -----------------------------------x
subject = "Daily Quotes"
body = quote
email_list = ['laopasana@outlook.com', 'dodj_ortalla@yahoo.com']
send_msg = Message(subject, body, email_list)
send_msg.sendMessage()

#x--------------------------------- Run/Debug -----------------------------------x



print(quote)
# print(data.loc[53, 'Quote'])
# print(data.iloc[53, 0])
# print(quote)
# print(len(quotes_list))
# print(quotes_list[53])
# quotes_list.remove(quote)

# now = dt.datetime.now()
# weekday = now.strftime("%A")
# # year = now.year
# # month = now.month
# # # weekday = now.weekday()

# with open('quotes.txt', 'r') as test_txt:
#     data = test_txt.read()
#     data_list = data.split('\n')
#     # print(data_list)
#     # print(len(data_list))
# with open('data_list.py', 'w') as my_file:
#     # pickle.dump(data_list, my_file)
#     my_file.write(repr(data_list))