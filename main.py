from turtle import  Screen
from food import Food
from scoreboard import Scoreboard
import time
from snake import Snake
screen = Screen()
screen.title("Snake game")
screen.setup(width=500, height=500)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    if snake.head.xcor() > 245 or snake.head.xcor() < -245 or snake.head.ycor() > 245 or snake.head.ycor() < -245:
        is_game_on = False
        scoreboard.game_over()

    for turtle in snake.turtles[1:]:
        if snake.head.distance(turtle) < 10:
            is_game_on = False
            scoreboard.game_over()

