from turtle import Screen
import time
from paddle import Paddle
from ball import Ball


screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong game by @NguyenQuang")
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle(side=(350,0))
l_paddle = Paddle(side=(-350,0))
ball = Ball()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

screen.listen()

is_on_game = True
while is_on_game:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect r-paddle misses
    if ball.xcor() > 380:
        ball.reset_position()

    # Detect l-paddle misses
    if ball.xcor() < -380:
        ball.reset_position()

screen.exitonclick()