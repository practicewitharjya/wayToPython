from turtle import Turtle,Screen


screen = Screen()
screen.setup(width=500, height= 400)
screen.title("Its a Race")
userinput = screen.textinput(title= "It's a challenge", prompt="Which Turtle will win the race")
# print("User input was", userinput)
colorsList = ["red", "yellow", "green", "blue", "purple", "orange"]
y_positions = [-70, -40, -10, 20, 50, 80]

for index in range(0,6):  #0,1,2,3,4,5
    timmy = Turtle(shape="turtle")
    timmy.color(colorsList[index])
    timmy.penup()
    timmy.goto(x=-230,y=y_positions[index])



screen.exitonclick()