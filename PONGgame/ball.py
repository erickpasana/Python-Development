from turtle import Turtle, Screen


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

    def move(self):
        self.goto(self.x/2-20, self.y/2-10)