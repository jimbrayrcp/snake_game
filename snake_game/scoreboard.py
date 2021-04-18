# ################################
#   Copyright (c) 2021 Jim Bray
#       All Rights Reserved
# ################################
from turtle import Turtle

FONT = ("courier", 22, "normal")
ALIGN = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.penup()
        self.color("white")
        self.setposition(0, 270)
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        text = f"SCORE: {self.score}"
        self.write(text, move=False, align=ALIGN, font=FONT)

    def game_over(self):
        text = f"GAME OVER"
        self.setposition(0, 0)
        self.write(text, move=False, align=ALIGN, font=FONT)

    def add_to_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()


if __name__ == "__main__":
    from turtle import Screen
    from time import sleep
    screen = Screen()
    screen.setup(height=600, width=600)
    screen.bgcolor("black")
    screen.tracer(0)
    score = Scoreboard()
    sleep(3)
    score.add_to_score()
    screen.exitonclick()
