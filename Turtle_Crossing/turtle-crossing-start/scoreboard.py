from turtle import Turtle, Screen
from turtle import clear
from turtle import write
from time import sleep


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self, w, h):
        super().__init__()
        self.STARTING_POSITION = (-w/2+10, h/2-30)
        self.score = 0 # set the initial score to 0
        self.level = 1 # set the initial level to 1
        self.hideturtle() # hide the turtle object
        self.penup() # lift the pen up to avoid drawing a line
        self.goto(self.STARTING_POSITION) # move the scoreboard to the top left corner of the screen
        self.update_scoreboard() # update the scoreboard with the current score and level

    def update_scoreboard(self):
        # update the scoreboard with the current score and level
        self.clear() # clear the previous scoreboard
        self.write(f"Score: {self.score} Level: {self.level}", align="left", font=("Courier", 15, "normal")) # write the new scoreboard with the specified alignment and font

    def increase_score(self):
        # increase the score by 1 and update the scoreboard
        self.score += 1 # increase the score by 1
        self.update_scoreboard() # update the scoreboard with the new score

    def increase_level(self):
        # increase the level by 1 and update the scoreboard
        self.level += 1 # increase the level by 1
        self.update_scoreboard() # update the scoreboard with the new level

    def game_over(self):
        # display the game over message
        self.goto(0, 0) # move the scoreboard to the center of the screen
        self.write("GAME OVER", align="center", font=("Courier", 36, "normal")) # write the game over message with the specified alignment and font

