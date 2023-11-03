from turtle import *

def new_turtle(tut, color, x, y):
    # y_axis = [y, y+40, y-40, y+80, y-80]
    # y_coord = y
    tut = Turtle()
    tut.shape("turtle")
    tut.color(color)
    tut.penup()
    tut.goto(x, y)
    return tut