import random
from turtle import Turtle, Screen

sensi = Turtle()
sensi.speed('fast')
sensi.pensize(15)
screen = Screen()
screen.colormode(255)
directions = [0, 90, 180, 270]


def rand_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    color = (red, green, blue)
    return color


for _ in range(200):
    sensi.color(rand_color())
    sensi.forward(40)
    sensi.setheading(random.choice(directions))

screen.exitonclick()
