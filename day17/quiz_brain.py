from data import question_data
from question_model import Question
from random import randint

class QuizGame:
    def __init__(self):
        self.user_score = 0
        self.questions_created = 0
        self.questions_answered = 0
        self.questions = question_data
        
    def makeAQuestion(self):
        questionChosenIndex = randint(0, len(self.questions)-1)
        question = self.questions[questionChosenIndex]
        self.currentQuestion = Question(question)
        self.questions.pop(questionChosenIndex)
        
    def areQuestionsLeft(self):
        return len(self.questions) > 0
    
    def iterateRound(self):
        print("Let's make a question!!")
        self.makeAQuestion()
        self.currentQuestion.printQuestion()
        currentResponseInput = input("What do you response, True [T] or False [F]?")
        self.questions_created += 1
        if self.currentQuestion.response(currentResponseInput in ["T", "t", "true", "True"]):
            self.questions_answered += 1
            print(f"Correct!, your score is {self.questions_answered}/{self.questions_created} Let's see another one")
        else:
            print(f"Incorrect... your score is {self.questions_answered}/{self.questions_created} Let's see another one")
    
    def printFinalResult(self):
        print(f"No questions left, your final result is {self.questions_answered}/{self.questions_created}")