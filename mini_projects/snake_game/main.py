import time
import random

from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Score_Board

BACKGROUND_COLOR = "orange"
SNAKE_COLOR = "green"
FOOD_COLOR = "blue"


screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor(BACKGROUND_COLOR)  # sets the background color
screen.title("My Snake Game")
screen.tracer(0)  # turns off the animation and pen image

snake = Snake(SNAKE_COLOR)  # Creates the snake of a certain color
food = Food(FOOD_COLOR)  # Creates food of a certain color at random loc
score_board = Score_Board()

# key mapping - controls
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)  # controls how fast the snake moves
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        score_board.increase_score()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score_board.game_over()
        screen.update()
        time.sleep(2)
        snake.reset()
        score_board.reset()
        #  game_is_on = False
        

    # Detect collision with tail
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 7:
            # game_is_on = False
            score_board.game_over()
            screen.update()
            time.sleep(2)
            snake.reset()
            score_board.reset()

screen.exitonclick()