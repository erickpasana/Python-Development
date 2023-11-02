from turtle import Turtle, Screen
import random
import dgons

kimmy = Turtle()
kimmy.shape('turtle')
kimmy.color('dark slate gray')
kimmy.fillcolor('seagreen')
kimmy.left(90)
kimmy.penup()
kimmy.forward(100)
kimmy.right(90)
kimmy.pendown()
# for i in range(3, 9):
# i = 3

dgons.polygons(kimmy, 10)
    
# rgb = random.randint(0, 255)
# kimmy.color('orange')
# for j in range(1, i + 1):
# tut.right(360/i)
# kimmy.forward(100)

screen = Screen()
screen.exitonclick()





# kimmy.p3()
# kimmy.circle(200)
# for _ in range(5):
#     kimmy.pendown()
#     kimmy.forward(10)
#     kimmy.penup()
#     kimmy.forward(10)