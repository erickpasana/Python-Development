

# screen = Screen()
# screen.setup(width=1000, height=550)
# screen.bgcolor('black')
# screen.title('PONG Game')
# screen.tracer(0)

# paddle_R = Paddle()
# screen.update()


# screen.listen()
# screen.onkey(paddle_R.up, 'Up')
# # screen.onkey(paddle_R.down, 'Down')

# # game_is_on = True
# # while game_is_on:
# #     screen.update()
# paddle_R.move_up()




from turtle import Turtle, Screen
from time import sleep
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import sys
sys.path.append(r"C:\Users\flpas\OneDrive - Connection Systems Development\Python-Development\day21")

# #TODO: Create the screen
width=1000
height=550
screen = Screen()
screen.setup(width, height)
screen.bgcolor('black')
screen.title('PONG Game')
screen.tracer(0)
# screen.delay(0)

# #TODO: Create Paddle class
# paddle_R = Paddle(width, height)
# paddle_L = Paddle(-width, height)
# ball = Ball(width, height)
# screen.update()



# def play_pong():

#TODO: Create Paddle class
paddle_R = Paddle(width, height)
paddle_L = Paddle(-width, height)
ball = Ball(width, height)
R_score = Scoreboard(width, height)
L_score = Scoreboard(-width, height)
screen.update()

# #TODO: Move Paddle
screen.listen()
screen.onkeypress(paddle_R.go_up, 'Up')
screen.onkeypress(paddle_R.go_down, 'Down')
screen.onkeypress(paddle_L.go_up, 'o')
screen.onkeypress(paddle_L.go_down, 'l')
# screen.update()
game_is_on = True
while game_is_on:
    # screen.update()
    # screen.tracer(1)
    ball.move()
    sleep(0.15)
    screen.update()

#TODO: Detect ball collision with walls
    if ball.ycor() > height/2 - 20 or ball.ycor() < -height/2 + 30:
        ball.bounce_y()

#TODO: Detect ball collision with paddles
    if ball.distance(paddle_R) < 30 and ball.xcor() > 20:
    # if ball.distance(paddle_R) < 30 or ball.distance(paddle_L) < 30:
        # print("Made Contact")
        ball.bounce_x()
    if ball.distance(paddle_L) < 30 and ball.xcor() < -20:
    # if ball.distance(paddle_L) < 30:
        # print("Made Contact")
        ball.bounce_x()

#TODO: Paddle misses; out of bounds
    if ball.xcor() > width/2 - 20:
        L_score.add_score()
        ball.miss_reverse()

    if ball.xcor() < -width/2 + 20:
        R_score.add_score()
        ball.miss_reverse()
    # sleep(3)
    # game_is_on = False



# play_pong()



screen.exitonclick()
# Day 22

# Score class
# Paddles class
# Ball class

#TODO: Create ball an
# 
# d it' moves
#TODO: Keep score


