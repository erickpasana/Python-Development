from turtle import Turtle, Screen

kimmy = Turtle()
kimmy.shape('turtle')
kimmy.color('dark slate gray')
kimmy.fillcolor('seagreen')
for _ in range(4):
    kimmy.forward(100)
    kimmy.right(90)
    # kimmy.forward(100)
    # kimmy.setheading(180)
    # kimmy.forward(100)
    # kimmy.setheading(90)
    # kimmy.forward(100)

screen = Screen()
screen.exitonclick()