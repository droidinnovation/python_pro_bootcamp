from turtle import Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

is_on_game = True

while is_on_game:
    time.sleep(0.1)
    screen.update()

