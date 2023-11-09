from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self, w, h):
        super().__init__()
        self.hideturtle() # hide the turtle object
        self.w = w
        self.h = h
        self.cars = [] # create an empty list to store the cars
        self.car_speed = 5 # set the initial speed of the cars

    def create_car(self):
        # create a new car object and add it to the list of cars
        random_chance = random.randint(1, 6) # generate a random number between 1 and 6
        if random_chance == 1: # only create a car 1 out of 6 times
            new_car = Turtle("square") # create a new turtle object with a square shape
            new_car.shapesize(stretch_wid=1, stretch_len=2) # stretch the shape to make it look like a car
            new_car.penup() # lift the pen up to avoid drawing a line
            new_car.color(random.choice(COLORS)) # choose a random color from a list of colors
            random_y = random.randint(-int(self.h/2) + 50, int(self.h/2) -50) # generate a random y-coordinate
            new_car.goto(300, random_y) # move the car to the right edge of the screen with the random y-coordinate
            self.cars.append(new_car) # add the car to the list of cars

    def move_cars(self):
        # move all the cars in the list to the left
        for car in self.cars: # loop through each car in the list
            car.backward(self.car_speed) # move the car backward by the car speed

    def level_up(self):
        # increase the speed of the cars as the game progresses
        self.car_speed += 5 # increase the car speed by 10

    def check_collision(self, player):
        # check if any car has collided with the player
        for car in self.cars: # loop through each car in the list
            if car.distance(player) < 20: # check the distance between the car and the player
                return True # return True if the distance is less than 20 pixels
        return False # return False otherwise
