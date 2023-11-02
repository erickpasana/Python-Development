import random
import turtle

def polygons(tut, n):
    
    colour = [ "red", "blue", "green", "yellow", "purple", "orange", "white", "black" ]

    for i in range(3, n + 1):
        tut.color(random.choice(colour))
        for j in range(1, i + 1):
            tut.right(360/i)
            tut.forward(100)

