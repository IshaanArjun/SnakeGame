import time
from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    segments = []
    def __init__(self):

        for position in STARTING_POSITION:
            new_segment = Turtle(shape="square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(position)
            self.segments.append(new_segment)
        self.head = self.segments[0]
        self.tail = self.segments[2]

    def move(self):
        for item in range(len(self.segments) - 1, 0, -1):
            x = self.segments[item - 1].xcor()
            y = self.segments[item - 1].ycor()
            self.segments[item].goto(x, y)
            # time.sleep(.2)
        self.head.forward(MOVING_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def add_segment(self):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("white")
        x = self.tail.xcor()
        y = self.tail.ycor()
        if self.head.heading() == DOWN:
            y += 20
        if self.head.heading() == UP:
            y -=20
        if self.head.heading() == RIGHT:
            x -= 20
        if self.head.heading() != LEFT:
            x += 20
        new_segment.goto(x, y)
        self.segments.append(new_segment)
        self.tail = self.segments[len(self.segments) - 1]