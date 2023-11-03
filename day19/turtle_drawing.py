# Import turtle module
import turtle
from turtle import *
# from click import clear

# Define a function to move the turtle forward
def go_forward():
    forward(10)

# Define a function to move the turtle backward
def go_backward():
    backward(10)

# Define a function to turn the turtle left
def turn_left():
    left(10)

# Define a function to turn the turtle right
def turn_right():
    right(10)

def restart():
    # turtle.clear()
    clear()
    penup()
    home()
    pendown()

# Set focus on the turtle screen
listen()
# kim = turtle.Turtle()
# kim.shape("turtle")
# kim.color("seagreen")


# Bind functions to arrow keys
onkey(go_forward, "Up")
onkey(go_backward, "Down")
onkey(turn_left, "Left")
onkey(turn_right, "Right")
onkey(restart, "c")

clear()
# Start the main loop of the window
mainloop()
