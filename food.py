"""
Written by Nahom Atnafu
Date: 12/22/2022
"""
from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(0.3, 0.3)
        self.color('blue')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        """places the food to a random location on the screen when
        the snake eats the food."""

        random_xcor = random.randint(-280, 280)
        random_ycor = random.randint(-280, 280)
        self.goto(random_xcor, random_ycor)
