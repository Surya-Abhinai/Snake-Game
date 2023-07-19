from turtle import *
import time
from Snake import Snake
from Food import Food
from Scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
A = Scoreboard()
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
    if snake.squares[0].xcor() > 280 or snake.squares[0].xcor() < -280 or snake.squares[0].ycor() > 285 or \
            snake.squares[0].ycor() < -280:
        A.game_over()
        game_is_on = False
    for i in snake.squares[1:]:
        if snake.squares[0].distance(i) == 0:
            A.game_over()
            game_is_on = False
    if snake.squares[0].distance(food) < 10:
        food.refresh()
        A.increase_score()
        snake.increase_tail()

screen.exitonclick()
