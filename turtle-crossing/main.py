from turtle import Screen
import time
from player import Player

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

screen.onkey(player.go_up,"Up")
screen.listen()

is_on_game = True
while is_on_game:
    time.sleep(0.1)
    screen.update()

