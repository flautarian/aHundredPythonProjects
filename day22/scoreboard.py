from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.updateScore(0, 0)
        self.hideturtle()
        
    def updateScore(self, newPlayerOneScore, newPlayerTwoScore):
        self.playerOneScore = newPlayerOneScore
        self.playerTwoScore = newPlayerTwoScore
        self.clear()
        self.write(f"{self.playerOneScore} - {self.playerTwoScore}", align="center", font= ("Console", 20, "normal"))
        
    def addScorePoint(self, playerPoint):
        if playerPoint == 1:
            self.updateScore(self.playerOneScore + 1, self.playerTwoScore)
        elif playerPoint == 2:
            self.updateScore(self.playerOneScore, self.playerTwoScore + 1)