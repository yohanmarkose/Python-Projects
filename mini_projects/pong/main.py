import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


BACKGROUND_COLOR = "black"
PADDLE_COLOR = "green"
BALL_COLOR = "blue"
MAX_SCORE = 4

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor(BACKGROUND_COLOR)  # sets the background color
screen.title("PONG")
screen.tracer(0)  # turns off the animation and pen image

pos_r_paddle = (350, 0)
r_paddle = Paddle(PADDLE_COLOR, pos_r_paddle)  # Right paddle

pos_l_paddle = (-350, 0)
l_paddle = Paddle(PADDLE_COLOR, pos_l_paddle)  # Left paddle

ball = Ball(BALL_COLOR)
score = Scoreboard()

screen.listen()
screen.onkeypress(fun=r_paddle.move_up, key="Up")
screen.onkeypress(fun=r_paddle.move_down, key="Down")

screen.onkeypress(fun=l_paddle.move_up, key="w")
screen.onkeypress(fun=l_paddle.move_down, key="s")

game_is_on = True
speed = 1
while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    # if ball collides with the wall
    if ball.ycor() >= 282 or ball.ycor() <= -282:
        ball.bounce_y()

    # if ball collides with the paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 330) or (ball.distance(l_paddle) < 50 and ball.xcor() < -330):
        ball.bounce_x() 

    if ball.xcor() > 380:  # passes right paddle
        score.l_point()
        score.update_score()
        ball.reset_position()

    elif ball.xcor() < -380:  # passes left paddle
        score.r_point()
        score.update_score()
        ball.reset_position()

    if score.r_score == MAX_SCORE or score.l_score == MAX_SCORE:
        score.completed_game(MAX_SCORE)




screen.exitonclick()