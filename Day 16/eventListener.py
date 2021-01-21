from turtle import Turtle,Screen

timmy = Turtle()
screen = Screen()

def move_forward():
    timmy.forward(20)


screen.listen()
screen.onkey(move_forward, "space")
screen.exitonclick()