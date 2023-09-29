import json
import requests
from data import question_data
from question_model import Question
from random import randint

class QuizGame:
    def __init__(self):
        self.user_score = 0
        self.questions_created = 0
        self.questions_answered = 0
        
        response = requests.get(url="https://opentdb.com/api.php?amount=20&type=boolean")
        if response.ok:
            json_body = response.json()
            self.questions = json_body["results"]
        else:
            self.questions = question_data
        
    def makeAQuestion(self):
        questionChosenIndex = randint(0, len(self.questions)-1)
        question = self.questions[questionChosenIndex]
        self.current_question = Question(question)
        self.questions.pop(questionChosenIndex)
        
    def areQuestionsLeft(self):
        return len(self.questions) > 0
    
    def iterateRound(self, response):
        self.questions_created += 1
        if self.current_question.response(response in ["T", "t", "true", "True"]):
            self.questions_answered += 1
            return f"Correct!, your score is {self.questions_answered}/{self.questions_created} Let's see another one"
        else:
            return f"Incorrect... your score is {self.questions_answered}/{self.questions_created} Let's see another one"
    
    def printFinalResult(self):
        print(f"No questions left, your final result is {self.questions_answered}/{self.questions_created}")