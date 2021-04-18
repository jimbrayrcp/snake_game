# ################################
#   Copyright (c) 2021 Jim Bray
#       All Rights Reserved
# ################################
import random
from turtle import Turtle

BOUND = 275
STRETCH = 0.5


class Food(Turtle):
    def __init__(self):
        super(Food, self).__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(stretch_wid=STRETCH, stretch_len=STRETCH)
        self.speed(0)
        self.refresh()

    def refresh(self):
        rand_x = random.randint(-BOUND, BOUND)
        rand_y = random.randint(-BOUND, BOUND)
        self.goto(rand_x, rand_y)


if __name__ == "__main__":
    food = Food()
