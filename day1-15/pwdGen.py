"""Password Generator Project"""

import random
import string

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

"""Easy"""

# n = nr_letters + nr_numbers + nr_symbols
# digits = 0
# # n = 0
# # s = 0
# pwd = ""
# for i in range(0, n):
#     if i < nr_letters:
#         pwd += (str(random.choice(letters)))
#         digits += 1
#     elif i >= nr_letters and i < nr_letters + 2:
#         pwd += (str(random.choice(symbols)))
#         digits += 1
#     elif i < n:
#         pwd += (str(random.choice(numbers)))
#         digits += 1
# print(pwd)

"""Hard"""

# type = [letters, numbers, symbols]
# n = nr_letters + nr_numbers + nr_symbols
# digits = 0

def password(n):
    letters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(letters) for i in range(n))
    
    # pwd = ""
    # l = 0
    # num = 0
    # s = 0
    # for i in range(0, n):
        # if i < nr_letters:
        # pwd += random.choice(random.choice(type))
        #     l += 1
        # elif i >= nr_letters and i < nr_letters + 2:
        #     pwd += (str(random.choice(type)))
        #     num += 1
        # elif i < n:
        #     pwd += (str(random.choice(type)))
        #     s += 1
    # random.shuffle(pwd)
    # pwd = "".join(pwd)
    # return pwd
pwd = password(16)
print(pwd)
print(len(pwd))