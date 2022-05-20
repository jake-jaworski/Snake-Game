from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.points = 0
        self.high_score = 0
        self.penup()
        self.hideturtle()
        self.color("green")
        self.goto((0, 265))
        self.score_update()

    def increment_score(self):
        self.points += 1
        self.score_update()

    def score_update(self):
        self.clear()
        self.write(f"Score: {self.points}  High Score: {self.high_score}", align="center", font=('Arial', 24, 'normal'))

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"Game over!", align="center", font=('Arial', 24, 'normal'))

    def reset_game(self):
        if self.points > self.high_score:
            self.high_score = self.points
        self.points = 0
        self.score_update()
