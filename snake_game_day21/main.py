from turtle import Screen, Turtle
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("My Snake game")
screen.tracer(0)

starting_positions = [(0,0),(-20,0),(-40,0)]
segments = []

for position in starting_positions:
     turtle = Turtle("square")
     turtle.color("white")
     turtle.penup()
     turtle.goto(position)
     segments.append(turtle)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg in segments:
        seg.forward(20)


screen.exitonclick()

