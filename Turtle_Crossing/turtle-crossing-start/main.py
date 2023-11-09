import time
from turtle import Screen
from turtle import Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

width=600
height=400

#TODO: Create the screen
screen = Screen()
screen.setup(width=width, height=height)
screen.tracer(0)

#TODO: Create Turtle player and it' moves
# Create a turtle player that starts at the bottom of the screen and listen for the "Up" keypress to move the turtle north. If you get stuck, check the video walkthrough in Step 3.
kim = Player(width, height)
cars = CarManager(width, height)
scoreboard = Scoreboard(width, height)
# tut = Turtle()
screen.listen()
screen.onkeypress(kim.move_up, 'Up')
screen.onkeypress(kim.move_down, 'Down')

# TODO: Create Car class and moves fatter every higher level. No cars 50x up and down. 
# Create cars that are 20px high by 40px wide that are randomly generated along the y-axis and move to the left edge of the screen. No cars should be generated in the top and bottom 50px of the screen (think of it as a safe zone for our little turtle). Hint: generate a new car only every 6th time the game loop runs. If you get stuck, check the video walkthrough in Step 4

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    cars.create_car()
    cars.move_cars()
    if kim.is_at_finish_line():
    # if kim.ycor() > height/2 - 20:
        # print(kim.ycor())
        kim.is_at_finish_line()
        cars.level_up()
        scoreboard.increase_score()
        scoreboard.increase_level()
    if cars.check_collision(kim):
        scoreboard.game_over()
        game_is_on = False

    screen.update()



screen.exitonclick()

# Scoreboard 
# Cars
# Turtle player




#TODO: Detect  turtle collision with car
# Detect when the turtle player collides with a car and stop the game if this happens. If you get stuck, check the video walkthrough in Step 5.

#TODO: Scoring
# Detect when the turtle player has reached the top edge of the screen (i.e., reached the FINISH_LINE_Y). When this happens, return the turtle to the starting position and increase the speed of the cars. Hint: think about creating an attribute and using the MOVE_INCREMENT to increase the car speed. If you get stuck, check the video walkthrough in Step 6.



