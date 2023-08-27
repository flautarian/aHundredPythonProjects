

from turtle import Turtle


class Player(Turtle):
    def __init__(self, position, speed = 10):
        super().__init__()
        self.goto(position)
        self.color("white")
        self.shape("square")
        self.shapesize(8, 1.5)
        self.speed("fastest")
        self.penup()
        self.accel = 0
        self.speed = speed
    
    def go_up(self):
        if self.ycor() + 10 < (300 - (self.shapesize()[0] * 10) / 2):
            self.accel = 1
    
    def go_down(self):
        if self.ycor() - 10 > -(300 - (self.shapesize()[0] * 10) / 2):
            self.accel = -1
            
    def release_accel(self):
        self.accel = 0
    
    def update(self):
        if -(300 - (self.shapesize()[0] * 10) / 2) <= self.ycor() + (self.speed * self.accel) <= (300 - (self.shapesize()[0] * 10) / 2):
            self.goto(self.pos()[0], self.pos()[1] + (self.speed * self.accel))
            
    def updateBot(self, ball):
        if (ball.accel[0] < 0 and self.xcor() > 0) or (ball.accel[0] > 0 and self.xcor() < 0):
            return
        if ball.ycor() - (self.shapesize()[0] * self.speed) / 2 < self.ycor():
            self.go_down()
            
        elif ball.ycor() + (self.shapesize()[0] * self.speed) / 2 > self.ycor():
            self.go_up()
        
        self.update()