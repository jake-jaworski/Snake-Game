from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # check is snake touches food
    if snake.snakehead.distance(food) < 17:
        food.refresh()
        score.increment_score()
        snake.extend_snake()

    # check if snake hit a wall
    if snake.snakehead.xcor() > 290 or snake.snakehead.xcor() < -290 or snake.snakehead.ycor() > 290 or snake.snakehead.ycor() <-290:
        score.reset_game()
        snake.reset_snake()

    # check if snake hit its own tail
    for i in snake.squares[1:]:
        if snake.snakehead.distance(i) < 10:
            score.reset_game()
            snake.reset_snake()





screen.exitonclick()