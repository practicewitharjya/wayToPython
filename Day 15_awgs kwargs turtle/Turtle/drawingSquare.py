from turtle import Turtle,Screen

tim = Turtle()
tim.shape("turtle")
tim.color("Blue")

def move():
    tim.forward(250)
    tim.left(90)

for _ in range(4):
    move()







screen = Screen()
screen.exitonclick()
