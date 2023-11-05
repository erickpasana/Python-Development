from turtle import Screen
from time import sleep
from snake import Snake
import sys
sys.path.append(r"C:\Users\flpas\OneDrive - Connection Systems Development\Python-Development\day21")
from food import Food
# day21\food.py

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

# TODO: Create a snake body
my_snake = Snake()
food = Food()
# screen.update()

# TODO: Move the snake
screen.listen()
screen.onkey(my_snake.left, 'Left')
screen.onkey(my_snake.right, 'Right')
screen.onkey(my_snake.up, 'Up')
screen.onkey(my_snake.down, 'Down')
screen.onkey(my_snake.down, 'Down')

game_is_on = True
while game_is_on:
    # heading = my_snake.setheading(0)
    screen.update()
    sleep(.1)
    my_snake.move()
    if my_snake.head.distance(food) < 15:
        food.new_loc()
        print('nomnomnom')





# TODO: Create snake food

# TODO: Detect collision with food

# TODO: Create a scoreboard

# TODO: Detect collision with wall

# TODO: Detect collision with body









screen.exitonclick()