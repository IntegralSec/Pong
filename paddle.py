from turtle import Turtle
import random


class Paddle(Turtle):
    min_x = 500
    max_x = 500
    min_y = 500
    max_y = 500
    MOVE_DISTANCE = 10
    paddle_side = "left"
    COLOR = "white"

    def __init__(self, screen_size_x, screen_size_y, paddle_side):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color(self.COLOR)
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.speed("fastest")

        self.min_x = ( screen_size_x / 2) * -1
        self.max_x = screen_size_x / 2
        self.min_y = (screen_size_y / 2) * -1
        self.max_y = screen_size_y / 2
        self.paddle_side = paddle_side
        self.go_to_start()

    def go_to_start(self):
        # Choose a side for the paddle to start on
        if self.paddle_side == "left":
            self.goto(self.min_x + 100, 0)
        elif self.paddle_side == "right":
            self.goto(self.max_x - 100, 0)
        elif self.paddle_side == 0:
            self.goto(self.min_x + 100, 0)
        else:
            self.goto(self.max_x - 100, 0)

    def move(self, direction):
        if direction == "up":
            self.goto(self.xcor(), (self.ycor() + self.MOVE_DISTANCE))
        elif direction == "down":
            self.goto(self.xcor(), (self.ycor() - self.MOVE_DISTANCE))

    def random_move(self):
        random_x = random.randint(self.min_x, self.max_x)
        random_y = random.randint(self.min_y, self.max_y)
        self.goto(random_x, random_y)