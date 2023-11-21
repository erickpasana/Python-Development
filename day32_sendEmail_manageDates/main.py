import smtplib
import datetime as dt
import pandas as pd
import csv
import os
import random
import pathlib

#x----------------------- CONSTANTS ------------------------x
# 1. Update the birthdays.csv with your friends & family's details. 
LETTERS_PATH = pathlib.Path(r"C:\Users\flpas\OneDrive - Connection Systems Development\Python-Development\day32_sendEmail_manageDates\letter_templates")
BIRTHDAY_PATH = pathlib.Path(r"C:\Users\flpas\OneDrive - Connection Systems Development\Python-Development\day32_sendEmail_manageDates\birthdays.csv")
DATA = pd.read_csv(BIRTHDAY_PATH)
PERSONS_LIST = DATA.to_dict('records')
NOW = dt.datetime.now()
MY_EMAIL = "omegakonstrukt@gmail.com"
PWD = "hxtf fjvb aext gsvy"

#x----------------------- Date check, names ------------------------x
# 2. Check if today matches a birthday in the birthdays.csv
# names_birtdays_today = [person['name'] for person in PERSONS_LIST]
# is_birthday = True
# for nl in PERSONS_LIST:
#     if nl['month'] == NOW.month and nl['day'] == NOW.day:
#         names_birtdays_today.append({nl['name']: nl['email']})
# to_greet_name = random.choice(names_birtdays_today)
# print(names_birtdays_today)
# print(PERSONS_LIST[0]['name'])

#x----------------------- Draft letter with changed names ------------------------x
def letter_email(to_greet_name):
    letters = []
    for file in os.listdir(LETTERS_PATH):
        # if file.endswith(".txt"):
        letters.append(file)
        
    letter_file_name = random.choice(letters)
    actual_letter_draft = f"{LETTERS_PATH}\\{letter_file_name}"

    with open(actual_letter_draft, 'r') as file:
        letter = file.read()
        # letter_draft = draft_file.read()
        letter = letter.replace("[NAME],\n", f"{to_greet_name},\n")
        letter = letter.replace("Angela", "Erick\n")
        # print(letter)
        return letter

#x----------------------- Send letters ------------------------x
for dict in PERSONS_LIST:
    if dict['month'] == NOW.month and dict['day'] == NOW.day:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PWD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=dict['email'], msg=f"Subject: Happy Birthday\n\n{letter_email(dict['name'])}")
            print(dict['name'])
            print(dict['email'])



##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)



