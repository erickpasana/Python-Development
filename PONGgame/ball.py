from turtle import Turtle, Screen
from time import sleep


class Ball(Turtle):

    def __init__(self, x, y):
        super().__init__()
        # self.body = Turtle('square')
        self.x = x
        self.y = y
        self.shape('circle')
        self.color('white')
        # self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(0, 0)
        self.x_move = 15
        self.y_move = 15

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        # if self.ycor() > self.y/2-20:
        #     new_y = self.ycor() - 10
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def miss_reverse(self):
        self.goto(0, 0)
        sleep(1)
        self.bounce_x()