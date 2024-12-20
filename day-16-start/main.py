# from turtle import Turtle, Screen
#
# timmy = Turtle()
# timmy.shape("turtle")
# # timmy.color('red', 'DarkOrchid')
# timmy.color('coral')
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# from prettytable import PrettyTable
#
# table = PrettyTable()
# table.add_column("Pokemon Name", ["Pikachu", "Squirtle","Charmander"])
# table.add_column("Type",["Electric","Water", "Fire"])
#
# print(table)

# from turtle import Turtle, Screen
import turtle as t
import random

turtle = t.Turtle()


def draw_square(size):
    turtle_drawer = t.Turtle()
    turtle_drawer.forward(size)
    turtle_drawer.right(90)
    turtle_drawer.forward(size)
    turtle_drawer.right(90)
    turtle_drawer.forward(size)
    turtle_drawer.right(90)
    turtle_drawer.forward(size)

def draw_dash_line(number_of_dash, distance_a_dash):
    turtle_drawer = t.Turtle()
    for _ in range(number_of_dash):
        turtle_drawer.forward(distance_a_dash)
        turtle_drawer.penup()
        turtle_drawer.forward(distance_a_dash)
        turtle_drawer.pendown()

def draw_a_shapes(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        turtle.forward(100)
        turtle.right(angle)

def random_colour():
    """Return a random color (r,g,b)"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    # Type Tuple
    color = (r,g,b)
    return color


# colours =  ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen",
#             "wheat", "SlateGray", "SeaGreen"]
# directions = [0, 90, 180, 270]
# turtle.pensize(10)
# turtle.speed("normal")

# t.colormode(255)

# for shape_line_n in range(3,6):
#     turtle.color(random.choice(colours))
#     draw_a_shapes(shape_line_n)

# for _ in range(100):
#     # turtle.color(random.choice(colours))
#     turtle.color(random_colour())
#     turtle.forward(30)
#     turtle.setheading(random.choice(directions))

t.colormode(255)
turtle.speed("fastest")

def draw_spirograph(size_of_gap, radius_circle):
    for _ in range(int(360/size_of_gap)):
        turtle.color(random_colour())
        turtle.circle(radius_circle)
        turtle.setheading(turtle.heading() + size_of_gap)


draw_spirograph( 5, 50)

window = t.Screen()
# draw_square(100)
# draw_dash_line(15,10)
# draw_a_shapes(5)
window.exitonclick()





