import turtle
import random
# from turtle import Turtle, Screen
from steps_in_walk_spiro import direction, line_len, colour

kim = turtle.Turtle()
kim.shape('turtle')
kim.color('dark turquoise')
kim.speed('fast')
turtle.colormode(255)

n = 25
width = 5.0
# count = 1
for _ in range(360//n):
    kim.color(colour())
    kim.circle(100)
    kim.left(30)



screen = turtle.Screen()
screen.exitonclick()