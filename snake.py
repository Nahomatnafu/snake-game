"""
Written by Nahom Atnafu
Date: 12/22/2022

"""

from turtle import Turtle

#  constants
STARTING_POSITIONS = [(0, 0), (-10, 0), (-20, 0)]


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """This function creates a snake segment using the add segment method."""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """This function adds a new segment at the end of the snake's body"""
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.shapesize(0.5, 0.5, 0.5)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """This function extends the snake's body by adding a new segment to the
        last segment of the snake."""
        self.add_segment(self.segments[-1].position())

    def move_forward(self):
        """This function moves the snake's head forward
         It also lets the rest of the snake's body follow the head."""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(10)

    def up(self):
        """ This function moves the snake object up
        but only if the snake object is not heading down(270 degrees)"""

        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        """ This function moves the snake object down
                but only if the snake object is not heading up (90 degrees)"""
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        """ This function moves the snake object to the right
                but only if the snake object is not heading left (180 degrees)"""
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        """ This function moves the snake object to the left
                but only if the snake object is not heading right (0 degrees)"""
        if self.head.heading() != 0:
            self.head.setheading(180)
