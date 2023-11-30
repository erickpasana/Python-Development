import requests
import json
import datetime
from alert_notification import EmailMessage

send_class = EmailMessage()
send_class.send_mail()




# bring_or_not = json.dumps(data['list'][2]['weather'][0]['id'], indent=4)
# for h in range(4):
# #     # id = h  #['id']['weather']
#     id = data['list'][h]['weather'][0]['id']#['id']
#     print(id)
#     print(data['list'][h]['dt_txt'])#
    # print(id[0]['id'])