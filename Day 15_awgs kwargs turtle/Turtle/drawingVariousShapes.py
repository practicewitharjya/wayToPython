from turtle import Turtle,Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.pensize(2)
colors = ["Red", "Yellow", "Green", "Blue","Pink", "Purple"]

def draw_shapes(num_of_sides):
    for _ in range(num_of_sides):
        angle = 360/num_of_sides
        tim.forward(100)
        tim.right(angle)

for shape_side in range(3, 11):
    tim.color(random.choice(colors))
    draw_shapes(shape_side)






screen = Screen()
screen.exitonclick()