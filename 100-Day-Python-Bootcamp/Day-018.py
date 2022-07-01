# from turtle import Turtle 

# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")

# for _ in range(4):
#     timmy_the_turtle.forward(180)
#     timmy_the_turtle.right(90)


# screen = Screen()
# screen.exitonclick()

# Basic import, you need to say the module name and the name of the class
# import Turtle

#or
#keyword + module name + import + Thing in module
#from      + turtle     + import + Turtle
#or import everything
#from turtle import Turtle

#import turtle as t
#gives an alias

#Installing modules
#Hero module
#import heroes (doesn't work)
#heroes is not part of the python built in library

#import heroes

import turtle as t
import random

tim = t.Turtle()


# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# for _ in range(3):
#     tim.forward(100)
#     tim.right(120)

# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# for _ in range(5):
#     tim.forward(100)
#     tim.right(72)

# for _ in range(6):
#     tim.forward(100)
#     tim.right(60)

# for _ in range(7):
#     tim.forward(100)
#     tim.right(51.42)

# for _ in range(8):
#     tim.forward(100)
#     tim.right(45)

# for _ in range(9):
#     tim.forward(100)
#     tim.right(40)

# for _ in range(10):
#     tim.forward(100)
#     tim.right(36)

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3,11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)
