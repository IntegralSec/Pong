from turtle import Turtle

class Ball(Turtle):
    COLOR = 'red'
    SPEED = 10
    SHAPE = 'circle'
    MOVE_DISTANCE = 20
    heading = 0

    def __init__(self, screen_size_x, screen_size_y):
        super().__init__()
        self.penup()
        self.shape(self.SHAPE)
        self.color(self.COLOR)
        self.speed(self.SPEED)
        self.forward(self.MOVE_DISTANCE)

    def move(self):
        self.forward(self.MOVE_DISTANCE)