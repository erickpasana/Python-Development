from turtle import Turtle, Screen
from time import sleep
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

# TODO: Create a snake body
my_snake = Snake()
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




# TODO: Create snake food

# TODO: Detect collision with food

# TODO: Create a scoreboard

# TODO: Detect collision with wall

# TODO: Detect collision with body









screen.exitonclick()