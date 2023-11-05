# main.py
import turtle # import the turtle module
from food import Food # import the food class

# create a screen object
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0) # turn off animation

# create a snake object
snake = turtle.Turtle()
snake.shape("square")
snake.color("white")
snake.penup()
snake.goto(0, 0)
snake.direction = "stop"

# create a food object
food = Food()

# create a score object
score = turtle.Turtle()
score.shape("square")
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Score: 0", align="center", font=("Arial", 24, "normal"))

# define a function to update the score
def update_score():
    global score_value
    score_value += 10
    score.clear()
    score.write(f"Score: {score_value}", align="center", font=("Arial", 24, "normal"))

# define a function to check collision
def check_collision():
    global game_over
    # check if the snake's head collides with the food
    if snake.distance(food) < 20:
        # increase the snake's length
        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        snake_segments.append(new_segment)
        # move the food to a new location
        food.move_to_new_location()
        # update the score
        update_score()
    # check if the snake's head collides with the wall or its body
    if snake.xcor() > 280 or snake.xcor() < -280 or snake.ycor() > 280 or snake.ycor() < -280:
        game_over = True
    for segment in snake_segments:
        if snake.distance(segment) < 20:
            game_over = True

# initialize some variables
snake_segments = [] # a list to store the snake's segments
score_value = 0 # a variable to store the score value
game_over = False # a variable to store the game state

# main game loop
while not game_over:
    screen.update() # update the screen
    check_collision() # check collision
    # move the snake
    snake.forward(20)
    if snake.direction == "up":
        snake.setheading(90)
    elif snake.direction == "down":
        snake.setheading(270)
    elif snake.direction == "left":
        snake.setheading(180)
    elif snake.direction == "right":
        snake.setheading(0)
    # move the snake's segments
    for i in range(len(snake_segments)-1, 0, -1):
        x = snake_segments[i-1].xcor()
        y = snake_segments[i-1].ycor()
        snake_segments[i].goto(x, y)
    if len(snake_segments) > 0:
        x = snake.xcor()
        y = snake.ycor()
        snake_segments[0].goto(x, y)

# display game over message
score.goto(0, 0)
score.write("Game Over", align="center", font=("Arial", 24, "normal"))

# keep the screen open until the user clicks on it
screen.exitonclick()
