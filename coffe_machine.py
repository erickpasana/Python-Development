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
    print(f"{order.title()} comin' right up!")
    
def turn_off():
    return exit()

# def payment():

    
clear()
display = 'Ready'
ingredients = resources
water = ingredients['water']
milk = ingredients['milk']
coffee = ingredients['coffee']
cash = 0.00
penny = 0.00
nickel = 0.00
dime = 0.00
quarter = 0.00
report = f"water={water} milk={milk} coffee={coffee} cash={cash}"
# off = turn_off()
print("="*40)

# {'espresso': {'ingredients': {'water': 50, 'coffee': 18}, 'cost': 1.5}, 
# 'latte': {'ingredients': {'water': 200, 'milk': 150, 'coffee': 24}, 'cost': 2.5}, 'cappuccino': {'ingredients': {'water': 250, 'milk': 100, 'coffee': 24}, 'cost': 3.0}
# {'water': 300, 'milk': 200, 'coffee': 100}

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
    clear()
    serve(order)
    sleep(3)
    water -= coffeeMENU[order]['ingredients']['water']
    if order == 'espresso':
        pass
    else:
        milk -= coffeeMENU[order]['ingredients']['milk']
    coffee -= coffeeMENU[order]['ingredients']['coffee']
    cash += coffeeMENU[order]['cost']
    report = f"water={water} milk={milk} coffee={coffee} cash={cash}"

    print('x'*40)
    print(ingredients)
    print(report)
    turn_on = turn_on_off(report, water, milk, coffee)
    
    # if not turn_on:
    #     print("Out of order. Please check the Inventory")
print("Ooops...I need a refill!!!")
sleep(5)
clear()
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
