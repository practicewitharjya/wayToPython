from turtle import Turtle,Screen

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title("Welcome To Snake Game")
starting_position = [(0, 0), (-20, 0), (-40, 0)]
game_is_on = True
segments = []

for position in starting_position:
    new_segment = Turtle('square')
    new_segment.color('white')
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)


while game_is_on:
    for seg in segments:
        seg.forward(20)







screen.exitonclick()
