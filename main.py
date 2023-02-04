import random
from turtle import Screen
import time
from paddle import Paddle
from net import Net
from ball import Ball
from score import Score


# ==============================
# Static Variables
# ==============================
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 500


# ==============================
# Helper Functions
# ==============================
def left_paddle_up():
    left_paddle.move('up')


def left_paddle_down():
    left_paddle.move('down')


def right_paddle_up():
    right_paddle.move('up')


def right_paddle_down():
    right_paddle.move('down')


def wall_collision():
    window_right = (SCREEN_WIDTH / 2) - 10
    window_left = ((SCREEN_WIDTH / 2) - 10) * -1
    window_top = (SCREEN_HEIGHT / 2) - 12
    window_bottom = ((SCREEN_HEIGHT / 2) - 20) * -1

    if ball.xcor() < window_left:
        # Score for right player
        right_score.increment()
        ball.next_round()
        return

    if ball.xcor() > window_right:
        # Score for left player
        left_score.increment()
        ball.next_round()
        return

    if ball.ycor() <= window_bottom:
        ball.bounce()
        return

    if ball.ycor() >= window_top:
        ball.bounce()
        return


def paddle_collision():
    print("Left Paddle Y = " + str(left_paddle.ycor()))
    left_paddle_x = left_paddle.xcor()
    right_paddle_x = right_paddle.xcor()
    if right_paddle_x <= ball.xcor():
        print("Right Paddle X Collision")
    if left_paddle_x >= ball.xcor():
        print("Left Paddle X Collision")


# ==============================
# Other Global Variables
# ==============================
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
game_running = True

# ==============================
# Game Objects
# ==============================

left_paddle = Paddle(SCREEN_WIDTH, SCREEN_HEIGHT, "left")
right_paddle = Paddle(SCREEN_WIDTH, SCREEN_HEIGHT, "right")
net = Net(SCREEN_WIDTH, SCREEN_HEIGHT)
ball = Ball(SCREEN_WIDTH, SCREEN_HEIGHT)
right_score = Score('right')
left_score = Score('left')
screen.listen()
screen.onkeypress(right_paddle_up, 'Up')
screen.onkeypress(left_paddle_up, 'w')
screen.onkeypress(right_paddle_down, 'Down')
screen.onkeypress(left_paddle_down, 's')
counter = 0


def run_game_loop():
    while game_running:
        wall_collision()
        paddle_collision()
        time.sleep(0.05)
        screen.update()
        ball.move()
    screen.exitonclick()


if __name__ == "__main__":
    run_game_loop()

