from turtle import Turtle, Screen
from turtle import clear
from turtle import write
from time import sleep
# from snake import Snake

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")
score = 0


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.high_score_now = self.high_score()
        self.goto(0, 220)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score= {self.score}   Hi_Score= {self.high_score_now}", align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def high_score(self):
        with open('data.txt', 'r') as file:
            result = int(file.read())
            return result

    def change_high_score(self):
        with open('data.txt', 'w') as file:
            file.write(str(self.score))
            self.update_score()
            # return high_score_figure

    def reset(self):
        self.clear()
        # if self.score > self.high_score:
        #     self.change_high_score()
            # print("Score")
            # self.high_score = int(self.change_high_score())
        # self.goto(0, 0)
        self.score = 0
        self.update_score()
        # return self.high_score()


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"Game over!", align=ALIGNMENT)
