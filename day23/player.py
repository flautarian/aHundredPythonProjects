from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.speed("fast")
        self.shape("turtle")
        self.left(90)
        self.penup()
        self.accel = 0
        self.setpos(STARTING_POSITION)
    
    def go_forward(self, speed):
        self.forward(speed)
        
    def has_completed_level(self):
        return self.ycor() > FINISH_LINE_Y
    
    def reset_pos(self):
        self.setpos(STARTING_POSITION)
        
    def accelerate(self):
        self.accel = 1
        
    def stop(self):
        self.accel = 0
    
    def update(self):
        self.go_forward(self.accel * MOVE_DISTANCE)