# import fbchat
# from getpass import getpass

import fbchat
from getpass import getpass

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