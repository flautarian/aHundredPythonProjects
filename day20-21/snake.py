from turtle import Turtle


class Snake:
    # Constructor
    def __init__(self) -> None:
        self.snake = Turtle()
        self.snake.shape("square")
        self.snake.color("green")
        self.snake_body = [Turtle(), Turtle(), Turtle(), Turtle(), Turtle(), Turtle(), Turtle(), Turtle()]
        self.snake.speed("fastest")
        self.snake.penup()
        xAxis = -10
        for bodypart in self.snake_body:
            bodypart.speed("fastest")
            bodypart.shape("square")
            bodypart.penup()
            bodypart.setpos(xAxis, 0)
            xAxis -= 10
    
    # Snake left pivot action
    def snake_left(self):
        self.snake.speed("fastest")
        self.snake.left(90)
        self.snake.speed("normal")

    # Snake right pivot action
    def snake_right(self):
        self.snake.speed("fastest")
        self.snake.right(90)
        self.snake.speed("normal")
    
    # Snake forward action
    def forward(self, quant):
        self.move_body()
        self.snake.forward(quant)
    
    # Snake part creation by apple eaten
    def add_point(self):
        newTail = Turtle()
        newTail.speed("fastest")
        newTail.shape("square")
        newTail.penup()
        newTail.goto(self.snake_body[len(self.snake_body)-1].pos())
        self.snake_body.append(newTail)
    
    # Body movement action
    def move_body(self):
        for i in range(len(self.snake_body)-1, 0, -1):
            newPos = self.snake_body[i-1].pos()
            self.snake_body[i].setpos(newPos[0],newPos[1])
        self.snake_body[0].goto(self.snake.pos()[0],self.snake.pos()[1])
        
    # body snake collision himself checker
    def collides_himself(self):
        for bodyPart in self.snake_body:
            if abs(self.snake.xcor() - bodyPart.xcor()) < 5 and abs(self.snake.ycor() - bodyPart.ycor()) < 5:
                return True
        return False