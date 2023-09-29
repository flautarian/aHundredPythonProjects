class Question:
    def __init__(self, data) -> None:
        self.question = data['question'].replace("&quot;", "\"")
        self.answer = bool(data['correct_answer'] == "True")
        pass
    
    def response(self, answer):
        return self.answer == answer
    
    def printQuestion(self):
        return self.question