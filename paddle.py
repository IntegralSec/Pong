from turtle import Turtle
import random


class Paddle(Turtle):
    window_left = -450
    window_right = 450
    window_bottom = -250
    window_top = 250
    MOVE_DISTANCE = 10
    PADDLE_SIZE = 3
    paddle_side = "left"
    COLOR = "white"

    def __init__(self, screen_size_x, screen_size_y, paddle_side):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color(self.COLOR)
        self.shapesize(stretch_len=1, stretch_wid=self.PADDLE_SIZE)
        self.speed("fastest")

        self.window_left = (screen_size_x / 2) * -1
        self.window_right = screen_size_x / 2
        self.window_bottom = (screen_size_y / 2) * -1
        self.window_top = screen_size_y / 2
        self.paddle_side = paddle_side
        self.go_to_start()

    def go_to_start(self):
        # Choose a side for the paddle to start on
        if self.paddle_side == "left":
            self.goto(self.window_left + 100, 0)
        elif self.paddle_side == "right":
            self.goto(self.window_right - 100, 0)
        elif self.paddle_side == 0:
            self.goto(self.window_left + 100, 0)
        else:
            self.goto(self.window_right - 100, 0)

    def move(self, direction):
        ycor = self.ycor()
        ceiling = self.window_top
        floor = self.window_bottom
        # Stay in bounds
        if direction == 'down':
            # Allow down only
            if ycor <= -210:
                return
            else:
                self.goto(self.xcor(), (ycor - self.MOVE_DISTANCE))

        if direction == 'up':
            if ycor >= 220:
                return
            else:
                self.goto(self.xcor(), (ycor + self.MOVE_DISTANCE))
