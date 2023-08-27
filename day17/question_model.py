class Question:
    def __init__(self, data) -> None:
        self.question = data['text']
        self.answer = bool(data['answer'])
        pass
    
    def response(self, answer):
        return self.answer == answer
    
    def printQuestion(self):
        print(self.question)