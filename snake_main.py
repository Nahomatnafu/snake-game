"""
Written by Nahom Atnafu
Date: 12/22/2022

Instructions:
Use the arrow keys to play the game.
"""

# imports
import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard


# setting up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

# instances of objects in the game
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# keyboard set-up
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


game_on = True

while game_on:
    screen.update()
    time.sleep(0.07)
    snake.move_forward()

    #  Detecting collision with food.
    if snake.head.distance(food) < 12:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #  Detecting collision with wall.
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 \
            or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_on = False
        scoreboard.game_over()

    #  Detecting collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 5:
            game_on = False
            scoreboard.game_over()


screen.exitonclick()
