from turtle import Turtle, Screen
from turtle import clear
from turtle import write
from time import sleep
# from snake import Snake

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(self.x/4, self.y/2 - 30)
        self.update_score()

    def update_score(self):
        self.write(f"Score= {self.score}", align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        # self.penup()
        # self.clear()
        self.goto(0, 0)
        self.write(f"Game over!", align=ALIGNMENT)