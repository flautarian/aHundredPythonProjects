from quiz_brain import QuizGame

quizGame = QuizGame()

while quizGame.areQuestionsLeft():
    quizGame.iterateRound()

quizGame.printFinalResult()