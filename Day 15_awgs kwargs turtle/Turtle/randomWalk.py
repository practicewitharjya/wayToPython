from turtle import Turtle,Screen
import random

tim = Turtle()
tim.pensize(10)
tim.speed("fastest")
colors = ["Red", "Yellow", "Green", "Blue","Pink", "Purple"]
directions = [0, 90, 180, 270]

for _ in range(50):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(directions))



screen = Screen()
screen.exitonclick()