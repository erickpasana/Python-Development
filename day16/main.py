# from turtle import Turtle, Screen
from time import sleep
from prettytable import PrettyTable

# kimmy = Turtle()
# print(kimmy)
# kimmy.color('red')
# kimmy.fd(100)
# sleep(3)

# kimmy.shape('turtle')
# kimmy.color('blue')
# kimmy.bk(100)
# sleep(3)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
table = PrettyTable()
table.add_column('Pokemon Name', ['Pikachu8', 'Squirtle,', 'EWF'])
table.add_column('Type', ['Elec', 'Water','Fire'])

# table.add_column('coulumn name3', 'row3')
# table.delete_table(table)
table.align = 'l'
print(table)