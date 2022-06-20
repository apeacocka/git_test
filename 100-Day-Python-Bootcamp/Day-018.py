from turtle import Turtle 

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")

for _ in range(4):
    timmy_the_turtle.forward(180)
    timmy_the_turtle.right(90)


screen = Screen()
screen.exitonclick()
