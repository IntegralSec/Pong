from turtle import Turtle


class Score(Turtle):

    score = 0
    ALIGN = "Center"
    FONT = ('Courier', 18, 'normal')
    MOVE_DISTANCE = 20
    X_POS = -250
    Y_POS = 210

    def __init__(self, side='left'):
        super().__init__()
        if side == 'right':
            self.X_POS = 250
        self.penup()
        self.color("white")
        self.goto(self.X_POS, self.Y_POS)

        self.write_score(0)
        self.hideturtle()




    def increment(self, increment_value=1):
        self.score += increment_value
        self.write_score(self.score)

    def get_score(self):
        return self.score

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score} ", False, align=self.ALIGN, font=self.FONT)

    def write_score(self, value):
        self.clear()
        self.write(f"Score: {value} ", False, align=self.ALIGN, font=self.FONT)
