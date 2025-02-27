from turtle import Screen
from scoreboard import Scoreboard
from snake import Snake
from food import Food
import time

# Set up the game screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # Turn off animation

# Initialize game objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Set up keyboard controls
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

# Game loop
game_over = False
while not game_over:
    screen.update()
    time.sleep(.1)  # Delay for smooth animation
    snake.move()

    # Check for collision with food
    if snake.head.distance(food) < 15:
        scoreboard.update()
        food.refresh()
        snake.add_segment()

    # Check for collision with wall or self
    if (snake.head.xcor() >= 299 or snake.head.xcor() <= -299 or
            snake.head.ycor() >= 299 or snake.head.ycor() <= -299):
        game_over = True
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 3:
            game_over = True

# Display game over message
scoreboard.game_over()

# Exit game
screen.exitonclick()