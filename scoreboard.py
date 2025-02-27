from turtle import Turtle

# Define constants for scoreboard appearance
ALIGNMENT = "center"
FONTSTYLE = 'Arial'
FONTSIZE = 'normal'
X = 0
Y = 270

class Scoreboard(Turtle):
    # Initialize scoreboard object
    def __init__(self):
        super().__init__()
        self.score = 0  # Initialize score to 0
        self.color("white")  # Set text color to white
        self.penup()  # Lift pen to avoid drawing
        self.hideturtle()  # Hide turtle object
        self.teleport(X, Y)  # Move to initial position
        self.write(f"SCORE:{self.score}", align=ALIGNMENT, font=(FONTSTYLE, 20, FONTSIZE))  # Display initial score

    # Display game over message
    def game_over(self):
        self.teleport(0, 0)  # Move to center of screen
        self.color("violet")  # Set text color to violet
        self.write(f"GAME OVER", align="center", font=("arial", 50, "normal"))  # Display game over message

    # Update scoreboard with new score
    def update(self):
        self.score += 1  # Increment score by 1
        self.clear()  # Clear previous score display
        self.teleport(X, Y)  # Move back to initial position
        self.write(f"SCORE:{self.score}", align=ALIGNMENT, font=(FONTSTYLE, 20, FONTSIZE))  # Display updated score