from turtle import Turtle,Screen

timmy = Turtle()
screen = Screen()

def move_forward():
    timmy.forward(20)

def move_backword():
    timmy.backward(20)

def move_right():
    timmy.right(90)

def move_left():
    timmy.left(90)

def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backword, "s")
screen.onkey(move_right, "a")
screen.onkey(move_left, "d")
screen.onkey(clear, "space")
screen.exitonclick()