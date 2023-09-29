import os
from tkinter import *

from quiz_brain import QuizGame

THEME_COLOR = "#375362"
THEME_FILL_COLOR = "#ffffff"
FONT_NAME = "Courier"


def start_game_ui():
    quizGame = QuizGame()

    def response_true():
        response = quizGame.iterateRound("True")
        
        if "Incorrect" in response:
            canvas.config(bg="red")
        else:
            canvas.config(bg="green")
            
        trivia_score_text.config(text=f"Score:{quizGame.questions_answered}")
        canvas.itemconfig(trivia_question_text, text=response)
        window.after(3000, ask_new_question)
        
    def response_false():
        response = quizGame.iterateRound("False")
        
        if "Incorrect" in response:
            canvas.config(bg="red")
        else:
            canvas.config(bg="green")
        
        trivia_score_text.config(text=f"Score:{quizGame.questions_answered}")
        canvas.itemconfig(trivia_question_text, text=response)
        window.after(3000, ask_new_question)
        
    def ask_new_question():
        canvas.config(bg="white")
        quizGame.makeAQuestion()
        canvas.itemconfig(trivia_question_text, text=quizGame.current_question.question)

    script_dir = os.path.dirname(__file__)

    window = Tk()
    window.title("Trivia app!!")
    window.config(padx=20, pady=20, bg=THEME_COLOR)

    # elements declaration

    canvas = Canvas(width=300, height=250, bg=THEME_COLOR, highlightthickness=0, background="white")
    
    trivia_score_text = Label(text=f"Score:{quizGame.user_score}", font=(FONT_NAME, 10, "normal"))
    trivia_score_text.grid(column=1, row=1)
    
    trivia_question_text = canvas.create_text(150, 125, width=250, text="Question", fill="black", font=(FONT_NAME, 15, "italic"))
    canvas.grid(column=0, row=2, columnspan=3)
    

    ok_img = PhotoImage(file=f"{script_dir}/images/true.png")
    go_btn = Button(command=response_true, image=ok_img )
    go_btn.grid(column=0, row=3, pady=15)


    ko_img = PhotoImage(file=f"{script_dir}/images/false.png")
    ok_btn = Button(command= response_false, image=ko_img)
    ok_btn.grid(column=2, row=3, pady=15)
    
    # start collecting first question to grab it from UI
    ask_new_question()

    window.mainloop()