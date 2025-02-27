from turtle import Turtle
from turtledemo.clock import setup
ALIGNMENT = "center"
FONTSTYLE = 'Arial'
FONTSIZE = 'normal'
X = 0
Y = 270

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.teleport(X,Y)
        self.write(f"SCORE:{self.score}",align= ALIGNMENT,font=(FONTSTYLE, 20, FONTSIZE))

    def game_over(self):
        self.teleport(0,0)
        self.color("violet")
        self.write(f"GAME OVER", align="center", font=("arial", 50, "normal"))

    def update(self):
        self.score += 1
        self.clear()
        self.teleport(X, Y)
        self.write(f"SCORE:{self.score}", align=ALIGNMENT, font=(FONTSTYLE, 20, FONTSIZE))