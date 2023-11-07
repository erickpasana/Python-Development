from turtle import Turtle, Screen



# x = 0
# y_coor = 0
# x_incre = x/2 - 20
# y_incre = y_coor/2 - y_coor/2
width = 20
height = 100
# STARTING_POSITION = [(x_incre, y_incre  + 40), (x_incre, y_incre  + 20), (x_incre, y_incre ), (x_incre, y_incre  - 20), (x_incre, y_incre  - 40)]
UP = 90
DOWN = 270
# LEFT = 180
# RIGHT = 0

class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        #     x_incre = x/2 + 20
        #     y_coor = y
        # else:
        # x = x
        # self.y_coor = y
        x_incre = x/2 - 20
        if x < 0:
            x_incre = x/2 + 10
            # x_incre *= -1
        self.y_incre = y/2 - y/2

        # self.body = Turtle('square')
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x_incre, 0)
        # self.create_paddle()
        # self.head = self.body[0]


    # def create_paddle(self):
        
    #     for position in STARTING_POSITION:
    #         self.add_segment(position)

    # def add_segment(self, position):
    #     segment = Turtle('square')
    #     segment.color('white')
    #     segment.penup()
    #     segment.goto(position)
    #     self.body.append(segment)

    # def stop_up(self):
    

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    
    # def left(self):
    #     if self.head.heading() != RIGHT:
    #         self.head.setheading(LEFT)
    # def right(self):
    #     if self.head.heading() != LEFT:
    #         self.head.setheading(RIGHT)
    # def up(self):
    #     # if self.head.heading() != DOWN:
    #     self.head.setheading(UP)
    # def down(self):
    #     # if self.head.heading() != UP:
    #     self.head.setheading(DOWN)

        



        # for bod in range(len(self.body)-1, 0, -1):
        #     new_x = self.body[bod -1].xcor()
        #     new_y = self.body[bod -1].ycor()
        #     self.body[bod].goto(new_x, new_y)
        # self.head.forward(MOVE_DISTANCE)