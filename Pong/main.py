from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(width=800, height=600)
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(right_paddle.move_down, "Down")
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(left_paddle.move_down, "s")
screen.onkey(left_paddle.move_up, "w")

game_is_on = True
while game_is_on:
    time.sleep(ball.tempo)
    screen.update()
    ball.move()

    if ball.ycor() > 287 or ball.ycor() < -287:
        ball.bounce_y()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 335:
        ball.bounce_x()
        scoreboard.r_point()
        ball.tempo *= 0.9

    if ball.distance(left_paddle) < 50 and ball.xcor() < -335:
        ball.bounce_x()
        scoreboard.l_point()
        ball.tempo *= 0.8


    if ball.xcor() > 390:
        ball.reset_position()

    if ball.xcor() < -390:
        ball.reset_position()



screen.exitonclick()