from turtle import Turtle
# from scoreboard import Scoreboard

# STARTING_POSITION = (0, -h/2)
MOVE_DISTANCE = 10
# FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self, w, h):
        super().__init__()
        self.STARTING_POSITION = (0, -h/2+20)
        self.FINISH_LINE_Y = h/2
        self.shape("turtle") # change the shape to a turtle
        self.color("green") # change the color to green
        self.penup() # lift the pen up to avoid drawing a line
        self.goto(self.STARTING_POSITION) # move the player to the bottom of the screen
        self.setheading(90) # set the heading to 90 degrees (facing up)
        # self.is_at_finish_line()

    def move_up(self):
        # move the player up by 10 pixels
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
    
    def move_down(self):
        # move the player down by MOVE_DISTANCE pixels
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def is_at_finish_line(self):
        # check if the player has reached the top of the screen
        if self.ycor() > self.FINISH_LINE_Y - 20:
            self.goto(self.STARTING_POSITION)
            return True
        else:
            return False
        
    def go_to_start(self):
        # reset the player's position to the bottom of the screen
        self.goto(0, self.S)


