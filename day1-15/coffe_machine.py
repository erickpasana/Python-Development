from resources import coffee_emoji, coffeeMENU, resources
from  click import clear
from time import sleep


#   TODO 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
"""Turn ON FUNCTION --> Ready
                    --> Out Of Order
Prompt"""



def turn_on_off(report, water, milk, coffee):
    if water >= 300 and milk >= 150 and  coffee >= 24:
        # display = 'Ready'
        print('Ready')
        return True
    else:
        print(report)
        return False
    
def menu():
    if turn_on:
        print("""
        Menu:
        Espresso = $1.50
        Latte = $2.50
        Cappuccino =$3.00
        """)
    
def serve(order):
    print(f"{order.title()} comin' right up!☕")
    
def turn_off():
    return exit()

def payment():
        """Processes the payment"""
        total_money = int(input("How many quarters?: ")) * 0.25
        total_money += int(input("How many dimes?: ")) * 0.1
        total_money += int(input("How many nickels?: ")) * 0.05
        total_money += int(input("How many pennies?: ")) * 0.01
        return total_money

def change(price, money):
    # price =
    # penny = 0.01
    # nickel = 0.05
    # dime = 0.01
    # quarter = 0.25
    # amount = sum([penny*pennies, nickel*nickels, dime*dimes, quarter*quarters])
    change = round(money - price, 2)
    if money > price:
        return print(f"Your change is ${change:.2f}.")
    elif money == price:
        return print(f"You gave the exact amount.")
    else:
        return


    
clear()
display = 'Ready'
ingredients = resources
water = ingredients['water']
milk = ingredients['milk']
coffee = ingredients['coffee']
price = 0.00
penny = 0.01
nickel = 0.05
dime = 0.10
quarter = 0.25
# cash = sum([penny, nickel, dime, quarter])
cash = 0.00
report = f"water={water} milk={milk} coffee={coffee} cash={cash}"
print(report)
# off = turn_off()
print("="*40)

# {'espresso': {'ingredients': {'water': 50, 'coffee': 18}, 'cost': 1.5}, 
# 'latte': {'ingredients': {'water': 200, 'milk': 150, 'coffee': 24}, 'cost': 2.5}, 'cappuccino': {'ingredients': {'water': 250, 'milk': 100, 'coffee': 24}, 'cost': 3.0}
# {'water': 300, 'milk': 200, 'coffee': 100}

money = 0.00
turn_on = turn_on_off(report, water, milk, coffee)
print(turn_on)
while turn_on:
    print('Start')
    print(report)
    menu()
    order = input("What's your order?: ")
    if order == 'off':
        clear()
        exit()
    # payment
    price = coffeeMENU[order]['cost']
    print(f"That would be ${price:.2f}. Please insert coins.")
    # sleep(5)
    while money < price:
        # quarters = int(input("How many quarters?: "))
        # dimes = int(input("How many dimes?: "))
        # nickels = int(input("How many nickels?: "))
        # pennies = int(input("How many pennies?: "))
        money = payment()
        # money = sum([penny*pennies, nickel*nickels, dime*dimes, quarter*quarters])
        print(f"Your money is ${money:.2f}.")
        if money < price:
            print("Your money is less than the price. Please add more.")
        # print(f"Your money is ${money}.")
        change(price, money)
        sleep(5)
    # clear()
    # cash += price
    serve(order)
    sleep(3)
    water -= coffeeMENU[order]['ingredients']['water']
    if order == 'espresso':
        pass
    else:
        milk -= coffeeMENU[order]['ingredients']['milk']
    coffee -= coffeeMENU[order]['ingredients']['coffee']
    cash += coffeeMENU[order]['cost']
    report = f"water={water} milk={milk} coffee={coffee} cash=${cash:.2f}"

    print('x'*40)
    print(ingredients)
    print('x'*40)
    print(report)
    print('x'*40)
    turn_on = turn_on_off(report, water, milk, coffee)
    print(input("Continue?"))
    
    # if not turn_on:
    #     print("Out of order. Please check the Inventory")
print("Ooops...I need a refill!!!")
sleep(5)
# clear()
print("Out of order. Please check the machine inventory.")

# def turn_off():






# TODO 2. Opeartion:
"""Serving Mix/Function to include resources/"""
# a. If the transaction is successful and there are enough resources to make the drink the user selected, then the ingredients to make the drink should be deducted from the coffee machine resources.

# def operation():

# def serve():


# TODO 3. Report.

# File resources:
    # File Acctg

# 4. Check resources sufficient?

# 5. Process coins.
"""Payment"""
# 6. Check transaction successful?


# TODO#8. Turn off the Coffee Machine by entering “off” to the prompt.
