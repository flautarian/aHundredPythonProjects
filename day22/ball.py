from turtle import Turtle


class Ball(Turtle):
    def __init__(self, shape: str = "square", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.color("white")
        self.shapesize(1.5, 1.5)
        self.accel= (0.5,1)
        
    def update(self):
        self.check_borders()
        self.goto(self.xcor() + 10 * self.accel[0], self.ycor() + 10 * self.accel[1])
    
    def check_borders(self):
        if -(300 - (self.shapesize()[0] * 10) / 2) <= self.ycor() + (10 * self.accel[1]) <= (300 - (self.shapesize()[0] * 10) / 2):
            self.accel = (self.accel[0], self.accel[1])
        else:
            self.accel = (self.accel[0], self.accel[1] * -1)
            
    def switch_x_axis(self, orientation):
        self.accel = (orientation, self.accel[1])
        
    def collides(self, other):
        return abs(self.xcor() - other.xcor()) < 40 and abs(self.ycor() - other.ycor()) < 40