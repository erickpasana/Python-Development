from turtle import Turtle, Screen
from turtle import clear
from click import clear
from time import sleep
from snake import Snake
from scoreboard import Scoreboard
import sys
sys.path.append(r"C:\Users\flpas\OneDrive - Connection Systems Development\Python-Development\day21")
from food import Food
# day21\food.py

screen = Screen()
screen.setup(width=600, height=550)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

# TODO: Create a snake body
my_snake = Snake()
food = Food()
score_board = Scoreboard()
high_score = 0
# screen.update()

# TODO: Move the snake
screen.listen()
screen.onkey(my_snake.left, 'Left')
screen.onkey(my_snake.right, 'Right')
screen.onkey(my_snake.up, 'Up')
screen.onkey(my_snake.down, 'Down')
# screen.onkey(my_snake.down, 'Down')

game_is_on = True
while game_is_on:
    # heading = my_snake.setheading(0)
    screen.update()
    sleep(.1)
    my_snake.move()
    if my_snake.head.distance(food) < 15:
        food.new_loc()
        score_board.add_score()
        if score_board.score > score_board.high_score_now:
            print('nomnomnom')
            score_board.change_high_score()
            score_board.high_score_now = score_board.high_score()
        score_board.update_score()
        my_snake.extend()
    if my_snake.head.xcor() > 295 or my_snake.head.ycor() > 295 or my_snake.head.xcor() < -295 or my_snake.head.ycor() < -295:
        # screen.clear()
        score_board.reset()
        my_snake.reset()
        # high_score = score_board.reset()
        # my_snake.clear()
        # food.clear()
        # game_is_on = False
    for seg in my_snake.body[2:]:
        if my_snake.head.distance(seg) < 10:
            score_board.reset()
            my_snake.reset()
            # high_score = score_board.reset()
            # game_is_on = False

    # game_is_on = False for seg in my_snake.body[2:] if my_snake.head.distance(seg) < 10:




# clear()
score_board.reset()




# TODO: Create snake food

# TODO: Detect collision with food

# TODO: Create a scoreboard

# TODO: Detect collision with wall

# TODO: Detect collision with body


screen.exitonclick()