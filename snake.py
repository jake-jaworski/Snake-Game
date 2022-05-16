from turtle import Turtle, Screen


class Snake:

    def __init__(self):
        self.position = [(0, 0), (-20, 0), (-40, 0)]
        self.squares = []
        self.create_segments()
        self.snakehead = self.squares[0]

    def create_segments(self):
        """Creates snake segments"""
        for i in range(3):
            new_square = Turtle(shape="square")
            new_square.color("white")
            new_square.penup()
            new_square.goto(self.position[i])
            self.squares.append(new_square)

    def move(self):
        for segment in range(len(self.squares) - 1, 0, -1):
            new_x = self.squares[segment - 1].xcor()
            new_y = self.squares[segment - 1].ycor()
            self.squares[segment].goto(new_x, new_y)
        self.snakehead.forward(20)

    def up(self):
        if self.snakehead.heading() != 270:
            self.snakehead.setheading(90)

    def down(self):
        if self.snakehead.heading() != 90:
            self.snakehead.setheading(270)

    def left(self):
        if self.snakehead.heading() != 0:
            self.snakehead.setheading(180)

    def right(self):
        if self.snakehead.heading() != 180:
            self.snakehead.setheading(0)

