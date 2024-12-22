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
    for seg_num in range(len(segments)-1, 0 , -1):
        new_x = segments[seg_num -1].xcor()
        new_y = segments[seg_num -1].ycor()
        segments[seg_num].goto(new_x, new_y)

    segments[0].forward(20)
    segments[0].left(90)


screen.exitonclick()

