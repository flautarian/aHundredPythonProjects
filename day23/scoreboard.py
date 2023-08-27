FONT = ("Courier", 24, "normal")

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-250, 250)
        self.updateScore(0)
        self.hideturtle()
        
    def updateScore(self, score):
        self.score = score
        self.clear()
        self.write(f"Level: {self.score}", align="center", font= FONT)
        
    def addScorePoint(self):
        self.updateScore(self.score + 1)