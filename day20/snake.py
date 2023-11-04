from turtle import Turtle, Screen, clear
import turtle
from time import sleep

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]
        # color = self.color('white')
        # shape = Turtle('square')


    #TODO:  Body
    def create_snake(self):
        
        for position in STARTING_POSITION:
            segment = Turtle('square')
            segment.color('white')
            segment.penup()
            segment.goto(position)
            self.body.append(segment)

    def move(self):
            
        for bod in range(len(self.body)-1, 0, -1):
            new_x = self.body[bod -1].xcor()
            new_y = self.body[bod -1].ycor()
            self.body[bod].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        # self.body[0].left(90)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    # def restart():
    #     clear()




#TODO:  Move
# forwards =
# turn l/r = 0

