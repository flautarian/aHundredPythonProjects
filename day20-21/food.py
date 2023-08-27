from turtle import Turtle
from random import randint

class Food(Turtle):
    # Constructor
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.relocate()
        
    # Scoreboard relocation
    def relocate(self):
        self.goto(randint(-250, 250), randint(-250, 250))
    
    # Scoreboard update
    def got_taken(self, other):
        return abs(self.xcor() - other.xcor()) < 20 and abs(self.ycor() - other.ycor()) < 20
    