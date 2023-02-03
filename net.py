from turtle import Turtle

class Net(Turtle):
    min_x = 500
    max_x = 500
    min_y = 500
    max_y = 500
    MOVE_DISTANCE = 20
    NET_WIDTH = 5
    COLOR = "grey"

    def __init__(self, screen_size_x, screen_size_y):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color(self.COLOR)
        self.speed("slow")


        self.min_x = (screen_size_x / 2) * -1
        self.max_x = screen_size_x / 2
        self.min_y = (screen_size_y / 2) * -1
        self.max_y = screen_size_y / 2

        self.goto(0, self.max_y)
        self.pendown()
        self.pensize(self.NET_WIDTH)
        self.setheading(270)
        self.forward(screen_size_y)



