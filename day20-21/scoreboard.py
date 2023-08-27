from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.goto(0, 250)
        self.updateScore(0)
        self.hideturtle()
        
    def updateScore(self, newScore):
        self.score = newScore
        self.clear()
        self.write(f"Score:{self.score}", align="center", font= ("Console", 20, "normal"))
        
    def addScorePoint(self):
        self.updateScore(self.score + 1)
    
    def start_game_over(self):
        gameoverLabel = Turtle()
        gameoverLabel.write("Game Over.", align="center", font= ("Console", 16, "normal"))