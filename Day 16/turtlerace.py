from turtle import Turtle,Screen
import random

is_race_started = False
screen = Screen()
screen.setup(width=500, height= 400)
screen.title("Its a Race")
userinput = screen.textinput(title= "It's a challenge", prompt="Which Turtle will win the race")
# print("User input was", userinput)
colorsList = ["red", "yellow", "green", "blue", "purple", "orange"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for index in range(0,6):  #0,1,2,3,4,5
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colorsList[index])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_positions[index])
    all_turtle.append(new_turtle)

if userinput:
    is_race_started = True

while is_race_started:
    for turtle in all_turtle:
        if turtle.xcor() >230:
            is_race_started = False
            winner_turtle = turtle.pencolor()
            if winner_turtle == userinput.lower():
                print(f"You are the winner! {winner_turtle} is the winner!")
            else:
                print(f"You loose the Game! {winner_turtle} is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)



screen.exitonclick()