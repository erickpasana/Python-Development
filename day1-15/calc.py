from mywords import calc_logo
from time import sleep
from click import clear

clear()
logo = calc_logo
print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1/n2

operations = {
    '+': add, 
    '-': subtract,
    '*': multiply, 
    '/': divide,
}

"""Conventional while loop"""

n1 = int(input("Number please: "))
operator = input('operator: ')
n2 = int(input("Number please: "))
function = operations[operator]
answer = function(n1, n2)
print(f"{n1} {operator} {n2} = {answer}")
sleep(3)

compute_more = True
while compute_more:
    # clear()
    # print(f"{answer}")
    # n1 = answer
    new_n1 = input(f"Anymore calculations? If yes do you want to continue with the answer or do you want to start fresh? 'y' to continue; 'f' to continue fresh; 'n' to stop: ")
    if new_n1 == 'y':
        n1 = answer
    elif new_n1 == 'f':
        n1 = float(input("Number please: "))
    elif new_n1 == 'n':
        exit()
        # n1 = float(input("New number please: "))
    operator = input('Operator: ')
    print(f"{n1} {operator}")
    n2 = float(input("Number: "))
    print(f"{n1} {operator} {n2}")
    sleep(2)
    # print(f"{answer} {operator}")
    function = operations[operator]
    answer = function(n1, n2)
    print(f"{n1} {operator} {n2} = {answer}")
    cont_more = input("Anymore calculations? y/n: ")
    if cont_more == 'n':
        compute_more = False
        exit()

"""Recursion"""

# def calculator():
#     n1 = int(input("Number please: "))
#     operator = input('operator: ')
#     n2 = int(input("Number please: "))
#     function = operations[operator]
#     answer = function(n1, n2)
#     print(f"{n1} {operator} {n2} = {answer}")
#     sleep(3)
