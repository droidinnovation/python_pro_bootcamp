from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from scoreboad import Scoreboard

screen = Screen()
screen.title("Turtle Crossing game")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()


screen.onkey(player.go_up,"Up")
screen.listen()

is_on_game = True
while is_on_game:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            is_on_game = False
            scoreboard.game_over()


    # Detect when crossing successfully
    if player.is_at_finish_line():
        player.goto_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()