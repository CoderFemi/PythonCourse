from turtle import Turtle, Screen

sensei = Turtle()
screen = Screen()


def move_forwards():
    sensei.forward(10)


def move_backwards():
    sensei.backward(10)


def turn_left():
    new_heading = sensei.heading() + 10
    sensei.setheading(new_heading)


def turn_right():
    new_heading = sensei.heading() - 10
    sensei.setheading(new_heading)


def clear():
    sensei.clear()
    sensei.penup()
    sensei.home()
    sensei.pendown()


screen.listen()
screen.onkey(move_forwards, "Up")
screen.onkey(move_backwards, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(clear, "c")

screen.exitonclick()
