from turtle import Screen
import time
from paddle import Paddle
from net import Net
from ball import Ball

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

# ==============================
# Global Variables
# ==============================
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 500
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

screen.listen()
screen.onkeypress(right_paddle_up, 'Up')
screen.onkeypress(left_paddle_up, 'w')
screen.onkeypress(right_paddle_down, 'Down')
screen.onkeypress(left_paddle_down, 's')

counter = 0



def run_game_loop():
    while game_running:
        ball.move()
        screen.update()
        time.sleep(0.2)
    screen.exitonclick()

if __name__ == "__main__":
    run_game_loop()

