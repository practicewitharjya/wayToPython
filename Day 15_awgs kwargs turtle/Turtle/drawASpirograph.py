import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

tim.speed("fastest")

for _ in range(36):
    tim.color(random_color())
    tim.circle(100)
    current_heading = tim.heading()+10
    tim.setheading(current_heading)






screen = t.Screen()
screen.exitonclick()