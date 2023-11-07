from turtle import Turtle, Screen
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('red')
        self.speed('fast')
        # self.location = self.goto(random.randint(-280, 280), random.randint(-280, 280))
        self.new_loc()

    def new_loc(self):
        x_axis = random.randint(-280, 280)
        y_axis = random.randint(-280, 280)
        self.location = self.goto(x_axis, y_axis)
        