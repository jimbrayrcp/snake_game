# ################################
#   Copyright (c) 2021 Jim Bray
#       All Rights Reserved
# ################################

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from time import sleep

BOUND = 280
screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.1)
    snake.move()

    # Detect Food Collision
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extemd()
        score.add_to_score()

    # Detect Wall Collision
    if snake.head.xcor() > BOUND or snake.head.xcor() < - BOUND or \
            snake.head.ycor() > BOUND or snake.head.ycor() < - BOUND:
        game_is_on = False
        score.game_over()

    # Detect Tail Collision
    snake_slice = snake.segments[1:]
    for segment in snake_slice:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
