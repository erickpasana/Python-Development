import datetime as dt
import random
from SendMessage import Message
from data_list import quotes_list

#x--------------------------------- Constants ---------------------------------------x

#x------------------------------- Get Message Body -----------------------------------x
index = random.randint(0, len(quotes_list)-1)
quote = quotes_list[index]

#x--------------------------------- Send Message -----------------------------------x
subject = "Daily Quotes"
body = quote
email_list = ['laopasana@outlook.com', 'dodj_ortalla@yahoo.com']
send_msg = Message(subject, body, email_list)
send_msg.sendMessage()




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