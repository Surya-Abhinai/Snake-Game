from turtle import *


class Snake:

    def __init__(self):
        self.squares = []
        self.create_snake()

    def create_snake(self):
        x = 0
        for i in range(3):
            s = Turtle()
            s.pencolor("white")
            s.shape("square")
            s.shapesize(0.5, 0.5)
            s.fillcolor("white")
            s.penup()
            s.fd(x)
            x -= 10
            self.squares.append(s)

    def move(self):
        for j in range((len(self.squares) - 1), 0, -1):
            new_x = self.squares[j-1].xcor()
            new_y = self.squares[j-1].ycor()
            self.squares[j].goto(new_x, new_y)
        self.squares[0].fd(10)

    def up(self):
        if self.squares[0].heading() != 270:
            self.squares[0].setheading(90)

    def down(self):
        if self.squares[0].heading() != 90:
            self.squares[0].setheading(270)

    def right(self):
        if self.squares[0].heading() != 180:
            self.squares[0].setheading(0)

    def left(self):
        if self.squares[0].heading() != 0:
            self.squares[0].setheading(180)

    def increase_tail(self):
            s = Turtle()
            s.penup()
            s.pencolor("white")
            s.shape("square")
            s.shapesize(0.5, 0.5)
            s.fillcolor("white")
            s.goto(self.squares[-1].xcor(), self.squares[-1].ycor())
            self.squares.append(s)
