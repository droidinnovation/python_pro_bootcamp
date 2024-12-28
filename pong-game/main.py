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

screen.listen()
screen.onkey(r_paddle.go_up(), "Up")
screen.onkey(r_paddle.go_down(), "Down")

screen.onkey(l_paddle.go_up(), "w")
screen.onkey(l_paddle.go_down(), "s")

ball = Ball()


is_on_game = True
while is_on_game:
    time.sleep(0.5)
    screen.update()
    ball.move()



screen.exitonclick()