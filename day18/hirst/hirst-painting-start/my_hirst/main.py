from resources import color_list
import turtle
import random

colors = color_list()

# Create a new turtle object
t = turtle.Turtle()
t.shape('turtle')

# Hide the turtle shape
# t.hideturtle()

# Speed up the drawing
t.speed('fastest')

# Define the size of each dot in pixels
dot_size = 8

# Define the gap between each dot in pixels
gap = 25

# Define the list of colors as RGB tuples
# colors = [(246, 246, 246), (51, 107, 135), (165, 59, 48), (199, 93, 73), (144, 192, 208), (31, 40, 45), (12, 75, 100), (184, 134, 11), (229, 149, 99), (142, 69, 133)]

# Convert the RGB values to a range of 0 to 1
turtle.colormode(255)

# Move the turtle to the top left corner of the screen
t.penup()
t.goto(-140, 140)

# Loop through the rows and columns of the grid
for row in range(10):
    for col in range(10):
        # Choose a random color from the list
        color = random.choice(colors)
        
        # Set the color of the pen and fill to the chosen color
        t.color(color)
        t.fillcolor(color)
        
        # Draw a dot with the chosen color and size at the current position
        t.begin_fill()
        t.circle(dot_size)
        t.end_fill()
        
        # Move the turtle to the right by the dot size and gap
        t.forward(dot_size + gap)
    
    # Move the turtle to the next row by going back to the left edge and moving down by the dot size and gap
    t.backward((dot_size + gap) * 10)
    t.right(90)
    t.forward(dot_size + gap)
    t.left(90)
# Hide the turtle shape
t.hideturtle()
# Exit turtle when done
# turtle.done()
screen = turtle.Screen()
screen.exitonclick()

# print(colors)