from turtle import *
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.4, stretch_wid=0.4)
        self.color("red")
        self.refresh()

    def refresh(self):
        x = random.randint(-250,250)
        y = random.randint(-250,250)
        self.goto(x, y)