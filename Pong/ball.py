from turtle import Turtle
from time import sleep

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.goto(0, 0)
        self.xmove = 10
        self.ymove = 10
        self.tempo = 0.1

    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.ymove = -self.ymove

    def bounce_x(self):
        self.xmove = -self.xmove

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
        self.tempo = 0.1
