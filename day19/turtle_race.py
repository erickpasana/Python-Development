from turtle import *
from resources import new_turtle
import random

screen = Screen()
screen.setup(width=500, height=400)
x = -230
y = 80
# y_axis = [y, y+40, y-40, y+80, y-80]
names = ['kim', 'man', 'lit', 'chit', 'ric']
colors = ['red', 'blue', 'orange', 'brown', 'green',]
all_turtles = []
# all_turtles = {}

for i in range(5):
    all_turtles.append(new_turtle(names[i], colors[i], x, y))
    # new_turtle(names[i], colors[i], x, y)
    # all_turtles[names[i]] = x
    y -= 40
    

user_bet = screen.textinput(title="Make your bet", prompt="Whick turtle would you bet on?. Enter color: ")
is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 220:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The winning color is {winning_color}.")
            else:
                print(f"You've lost! The winning color is {winning_color}.")

        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)











# kim = new_turtle('kim', 'red', -230, 0)
# man = new_turtle('man', 'blue', -230, 40)
# lit = new_turtle('lit', 'orange', -230, -40)
# chit = new_turtle('chit', 'brown', -230, 80)
# ric = new_turtle('ric', 'green', -230, -80)


screen.exitonclick()
