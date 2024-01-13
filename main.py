from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Objects and methods

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()

game_is_on = True

# Listens for input and controls snake accordingly

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Shows snake movement

while game_is_on:
    screen.update()
    time.sleep(0.2)

    snake.move()

    # Detects Collisions with food

    if snake.head.distance(food) < 15:
        food.reset_food()
        scoreboard.add_score()

    # Detects Collisions with boundary

    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        scoreboard.reset_scoreboard()
        snake.reset()

# Detects  Collisions with tail
for segment in snake.segments:
    if segment == snake.head:
        pass
    elif snake.head.distance(segment) < 10:
        scoreboard.reset_scoreboard()
        snake.reset()

screen.exitonclick()
