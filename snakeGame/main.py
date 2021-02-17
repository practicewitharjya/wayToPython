from turtle import Turtle,Screen

from snakeGame.food import Food
from snakeGame.snake import Snake
from snakeGame.scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Welcome To My Snake Game")
screen.tracer(0)

snake = Snake()
food =Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #Detect Collision
    if snake.head.distance(food)< 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect Collision with Wall
    if snake.head.xcor()> 280 or snake.head.xcor() < -280 or snake.head.ycor()> 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #Detect Collision with its own Tail
    # if snake head collides with any of its own segment in the tailside:
    #     trigger Game_Over
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) <10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()