from turtle import Turtle
from random import randint

POSSIBLE_WAYS = [280, 240, 200, 160, 120, 80, 40 ,0, -40, -80, -120]

class Car(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True, color: str = "white", xaxis: int = 0, speed: int = 0) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.first_x_axis = xaxis
        self.shape("square")
        self.shapesize(2, 5)
        self.penup()
        self.relocate_car()
        self.speed("fastest")
        self.color(color)
        self.left(180)
        self.speed = speed
        
    def update(self):
        self.forward(self.speed)
        if self.xcor() < -500:
            self.relocate_car()
            
    def relocate_car(self):
       self.setpos(self.first_x_axis, POSSIBLE_WAYS[randint(0, len(POSSIBLE_WAYS)-1)]) 