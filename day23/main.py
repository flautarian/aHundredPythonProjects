import time
from turtle import Screen
from scoreboard import Scoreboard
from player import Player
from car_manager import CarManager

screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)
screen.listen()

turtle = Player()
scoreboard = Scoreboard()
screen.onkeypress(key="space", fun=turtle.accelerate)
screen.onkeyrelease(key="space", fun=turtle.stop)

carManager = CarManager()

def add_cars(quant):
    for i in range(quant):
        carManager.add_new_car()

add_cars(8)

game_is_on = True

while game_is_on:
    turtle.update()
    if turtle.has_completed_level():
        scoreboard.addScorePoint()
        turtle.reset_pos()
        add_cars(1)
    if carManager.any_collides_turtle(turtle):
        game_is_on = False
    carManager.update()
    time.sleep(0.1)
    screen.update()

screen.exitonclick()