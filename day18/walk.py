import random
import turtle
from turtle import Turtle, Screen
from day18.steps_in_walk_spiro import direction, line_len, colour

kim = turtle.Turtle()
kim.shape('turtle')
kim.color('dark turquoise')
kim.speed('fast')
turtle.colormode(255)

n = 100
width = 5.0
count = 1
for _ in range(n + 1):
    kim.color(colour())
    # kim.pencolor(colour())
    kim.width(width)
    direction(kim)
    line_len(kim)
    # width += 0.5
    # print(count)
    # count += 1


screen = Screen()
screen.exitonclick()





# TODO: direction
# TODO: line width
# TODO: random color
# TODO: 