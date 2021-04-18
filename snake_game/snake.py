# ################################
#   Copyright (c) 2021 Jim Bray
#       All Rights Reserved
# ################################
from turtle import Screen, Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        t = Turtle()
        t.penup()

        if position == (0, 0):
            t.color("Chartreuse4")
            t.shape("triangle")
            t.shapesize(0.75, 0.75, 8)
        else:
            t.color("Chartreuse")
            t.shape("square")
        t.setposition(position)
        self.segments.append(t)

    def extemd(self):
        self.add_segment(self.segments[- 1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if not self.head.heading() == DOWN:
            self.head.setheading(UP)

    def down(self):
        if not self.head.heading() == UP:
            self.head.setheading(DOWN)

    def left(self):
        if not self.head.heading() == RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if not self.head.heading() == LEFT:
            self.head.setheading(RIGHT)


if __name__ == "__main__":
    from time import sleep

    screen = Screen()
    screen.setup(height=600, width=600)
    screen.bgcolor("black")
    screen.title("The Snake Game")
    screen.tracer(0)
    snake = Snake()
    game_is_on = True
    while game_is_on:
        screen.update()
        sleep(0.1)
        snake.move()
        snake.up()
        snake.extemd()
        snake.left()
        snake.extemd()
