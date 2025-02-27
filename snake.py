import time
from turtle import Turtle

# Define constants for snake movement and positioning
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# Define Snake class
class Snake:
    # Initialize snake segments list
    segments = []

    # Initialize Snake object
    def __init__(self):
        # Create initial snake segments
        for position in STARTING_POSITION:
            new_segment = Turtle(shape="square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(position)
            self.segments.append(new_segment)
        # Set head and tail segments
        self.head = self.segments[0]
        self.tail = self.segments[-1]

    # Move snake
    def move(self):
        # Move each segment to the position of the previous segment
        for i in range(len(self.segments) - 1, 0, -1):
            x = self.segments[i - 1].xcor()
            y = self.segments[i - 1].ycor()
            self.segments[i].goto(x, y)
        # Move head segment forward
        self.head.forward(MOVING_DISTANCE)

    # Change snake direction to up
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    # Change snake direction to down
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    # Change snake direction to left
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    # Change snake direction to right
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    # Add new segment to snake
    def add_segment(self):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("white")
        # Calculate position for new segment based on snake direction
        x = self.tail.xcor()
        y = self.tail.ycor()
        if self.head.heading() == DOWN:
            y += 20
        elif self.head.heading() == UP:
            y -= 20
        elif self.head.heading() == RIGHT:
            x -= 20
        elif self.head.heading() == LEFT:
            x += 20
        new_segment.goto(x, y)
        self.segments.append(new_segment)
        self.tail = self.segments[-1]