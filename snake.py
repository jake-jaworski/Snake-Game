from turtle import Turtle, Screen
POSITION = [(0, 0), (-20, 0), (-40, 0)]

class Snake:

    def __init__(self):
        self.squares = []
        self.create_snake()
        self.snakehead = self.squares[0]

    def create_snake(self):
        """Creates snake segments"""
        for position in POSITION:
            self.add_square(position)

    def add_square(self, position):
        new_square = Turtle(shape="square")
        new_square.color("white")
        new_square.penup()
        new_square.goto(position)
        self.squares.append(new_square)

    def extend_snake(self):
        self.add_square(self.squares[-1].position())

    def move(self):
        for segment in range(len(self.squares) - 1, 0, -1):
            new_x = self.squares[segment - 1].xcor()
            new_y = self.squares[segment - 1].ycor()
            self.squares[segment].goto(new_x, new_y)
        self.snakehead.forward(20)

    def reset_snake(self):
        for square in self.squares:
            square.goto(800, 800)
        self.squares.clear()
        self.create_snake()
        self.snakehead = self.squares[0]

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

