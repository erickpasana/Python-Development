

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
from paddle import Paddle
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
paddle_R = Paddle(width, height)
paddle_L = Paddle(-width, height)
# screen.update()

# #TODO: Move Paddle
screen.listen()
screen.onkeypress(paddle_R.go_up, 'Up')
screen.onkeypress(paddle_R.go_down, 'Down')
screen.onkeypress(paddle_L.go_up, 'w')
screen.onkeypress(paddle_L.go_down, 's')
# screen.update()

game_is_on = True
while game_is_on:
    # paddle_R.go_up()
    # paddle_R.move_down()
    screen.update()







screen.exitonclick()
# Day 22

# Score class
# Paddles class
# Ball class

#TODO: Create ball and it' moves
#TODO: Detect ball collision with walls
#TODO: Paddle misses
#TODO: Keep score


