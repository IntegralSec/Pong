import random
from turtle import Turtle
from math import ceil

class Ball(Turtle):
    COLOR = 'red'
    SPEED = 0
    SHAPE = 'circle'
    MOVE_DISTANCE = 19

    def __init__(self, screen_size_x, screen_size_y):
        super().__init__()
        self.penup()
        self.shape(self.SHAPE)
        self.color(self.COLOR)
        self.speed(self.SPEED)
        self.setpos(0, 0)
        self.next_round()

    def move(self):
        self.forward(self.MOVE_DISTANCE)

    def next_round(self):
        random_angle = random.randint(0, 360)
        if random.randint(0, 1):
            self.left(random_angle)
        else:
            self.right(random_angle)
        self.setpos(0, 0)

    def bounce(self):
        the_heading = self.heading()
        new_heading = ceil((the_heading * 2) * random.random())
        if the_heading > 0 and the_heading <= 90:
            self.right(the_heading * 2)
        elif the_heading > 90 and the_heading <= 180:
            self.right(the_heading * 2 )
        elif the_heading > 180 and the_heading <= 270:
            self.right(the_heading * 2)
        elif the_heading > 270 and the_heading <= 359:
            self.right(the_heading * 2)

        #self.forward(self.MOVE_DISTANCE + 5)



