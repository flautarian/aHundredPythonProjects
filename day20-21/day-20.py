from turtle import Turtle, Screen

from scoreboard import Scoreboard
from food import Food
from snake import Snake

import time

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen = Screen()
screen.setup(height=600, width=600)
screen.title("My total snake py")
screen.tracer(0)
screen.listen()
screen.colormode(255)

game = 0

screen.onkey(key="a", fun=snake.snake_left)
screen.onkey(key="d", fun=snake.snake_right)

while game == 0:
    snake.forward(20)
    
    if food.got_taken(snake.snake):
        snake.add_point()
        scoreboard.addScorePoint()
        food.relocate()
        
    screen.update()
    
    if abs(snake.snake.xcor()) > 280 or abs(snake.snake.ycor()) > 280 or snake.collides_himself():
        game = -1
        scoreboard.start_game_over()
    
    time.sleep(0.075)

screen.exitonclick()