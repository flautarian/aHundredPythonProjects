from turtle import Turtle
from random import randint
from car import Car

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
STARTING_X_POSITION = 450
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.cars = []
        
    def add_new_car(self):
        self.cars.append(Car(color= COLORS[randint(0, 5)], xaxis=STARTING_X_POSITION, speed=randint(10, 15)))
        
    def update(self):
        for car in self.cars:
            car.update()
            
    def any_collides_turtle(self, turtle):
        for car in self.cars:
            if abs(turtle.xcor() - car.xcor()) < 60 and abs(turtle.ycor() - car.ycor()) < 40:
                return True
        return False
