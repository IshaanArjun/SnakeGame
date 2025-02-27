from turtle import Turtle
import random

# Define Food class, inheriting from Turtle
class Food(Turtle):

    # Initialize Food object
    def __init__(self):
        super().__init__()  # Call Turtle's __init__ method
        self.shape("turtle")  # Set shape to turtle
        self.penup()  # Lift pen to avoid drawing
        self.shapesize(stretch_wid=1, stretch_len=1)  # Set shape size
        self.color("purple")  # Set color to purple
        # Generate random initial position
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)  # Move to initial position

    # Refresh Food object's position
    def refresh(self):
        # Generate new random position
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)  # Move to new position