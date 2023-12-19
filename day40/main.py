"""Welcome to Connection Systems Flight Deals.
What is your first name?
What is your last name?
What is your email address?
Kindly confirm your email address?
kiml@gmail.com
"""
import time
import sys

# add_user_path = r"C:\Users\flpas\OneDrive - Connection Systems Development\Python-Development\day39FlightDealFinder\flight-deals-start"
add_user_path = r"C:\Users\flpas\OneDrive - Connection Systems Development\Python-Development\day39FlightDealFinder\flight-deals-start"
sys.path.insert(0, add_user_path)
from data_manager import DataManager

end_point = 'https://api.sheety.co/b17d3c0b422c3d51ecc6636c25073af5/flightdeals/users'
#------------------------------ Process -----------------------------x

print('Welcome to Connection Systems Flight Deals')
firstname = input("What is your first name?\n")
lastname = input("What is your last name?\n")

n = 0
email_entry = False
while not email_entry:
    email = input("What is your email address?\n")
    confirm_email = input("Kindly reenter your email address to confirm?\n")
    if confirm_email == email:
        print("You're in the club.")
        add_user = DataManager(firstname, lastname, email)
        add_user.add_user()
        time.sleep(2)
        email_entry = True
    else:
        if n == 2:
            print("You have reached 5 attempts. Kindly recover your email address and try again.\n")
            time.sleep(3)
            break
        else:
            print('Your confirmation does not match your email.')
            n += 1
            print(n)
            print('\n')
#------------------------------ End -----------------------------x
            
time.sleep(2)
exit()
#------------------------------ Debug -----------------------------x
            
# sys_path = 'C:\\Users\\flpas\\OneDrive - Connection Systems Development\\Python-Development\\day39FlightDealFinder\\flight-deals-start'
# print(firstname)
# print(lastname)
# print(email)
# print(sys.path)
# print(sys_path)
# print(add_user_path)
