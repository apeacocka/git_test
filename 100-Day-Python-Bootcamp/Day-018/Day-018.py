#Final Project

# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# print(colors)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle as turtle_module
import random

turtle_module.colormode(255)
tom = turtle_module.Turtle()
tom.speed('fastest')
tom.penup()
tom.hideturtle()
color_list = [(229, 228, 226), (225, 223, 224), (199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120), (202, 185, 190), (40, 72, 82), (46, 73, 62), (47, 66, 82)]

tom.setheading(225)
tom.forward(300)
tom.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tom.dot(20, random.choice(color_list))
    tom.forward(50)

    if dot_count % 10 == 0:
        tom.setheading(90)
        tom.forward(50)
        tom.setheading(180)
        tom.forward(500)
        tom.setheading(0)



screen = turtle_module.Screen()
screen.exitonclick()














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

# import turtle as t
# import random

# tim = t.Turtle()


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

# t.colormode(255)
# # colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# directions = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed("fastest")
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)

# for shape_side_n in range(3,11):
#     tim.color(random.choice(colors))
#     draw_shape(shape_side_n)

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color

# for _ in range(500):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

#Python Tuples
#like a list except it is carved in stone, can't change values.
#Creating a constant list
#You can put a tuple into a list to turn it into a list using a variable name
#

#Spirograph

# import turtle as t
# import random

# tim = t.Turtle()
# t.colormode(255)

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color

# tim.speed("fastest")

# def draw_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading() + size_of_gap)

# draw_spirograph(5)

# screen = t.Screen()
# screen.exitonclick()
