import os
from tkinter import messagebox
from tkinter import *
import time

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#42c262"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

script_dir = os.path.dirname(__file__)
current_word = 0
second="40"
remaining_time = 0

with open(script_dir + "/words.txt") as names_file:
    words = names_file.readlines()
    current_word = 0
    
def start_timer():
    global second, remaining_time, current_word
    current_word = 0
    word_typer_value.delete(0, END)
    change_word_to_type()
    remaining_time = int(second)
    update_timer()
        
def update_timer() :
    global remaining_time, current_word
    if remaining_time > 0:
        timer_label.config(text=f"Time Left: {remaining_time} seconds")
        remaining_time -= 1
        window.after(1000, update_timer)  # Schedule the update after 1000 milliseconds (1 second)
    else:
        timer_label.config(text="Time's up!")
        messagebox.showinfo("Time Countdown", f"Time's up!!, your record now is {current_word}")

def try_process_word(self):
    global remaining_time
    if remaining_time <= 0:
        return
    else:    
        word_to_type = word_to_type_value.get()
        word_typed = word_typer_value.get()
        if word_to_type == word_typed:
            word_typer_value.delete(0, END)
            change_word_to_type()
        
def change_word_to_type() :
    global words, current_word
    word_to_type_value.delete(0, END)
    word_to_type_value.insert(0, words[current_word].strip())
    current_word += 1


        
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Key type velocity test")
window.config(padx=100, pady=50)

window.bind('<Return>', func=try_process_word)


title_label = Label(text="velocity typing test", fg=GREEN, font=(FONT_NAME, 25))
title_label.grid(column=0, row=0, columnspan=4)

canvas = Canvas(width=200, height=224, highlightthickness=0)
logo_img = PhotoImage(file=f"{script_dir}/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=0, row=1, columnspan=4)



# ---TIMER INDICATOR---#
timer_label = Label(text="Timer", font=(FONT_NAME, 10), textvariable=second)
timer_label.grid(column=0, row=2)

# ---WORD TO TYPE LABEL ---#
word_to_type_label = Label(text="Word to type:", font=(FONT_NAME, 10))
word_to_type_label.grid(column=0, row=3)

word_to_type_value = Entry(font=(FONT_NAME, 10), width=25) # , state="disabled"
word_to_type_value.grid(column=2, row=3, columnspan=2)

# ---TYPE LABEL---#

word_typer_label = Label(text="Type the word", font=(FONT_NAME, 10))
word_typer_label.grid(column=0, row=4)

word_typer_value = Entry(font=(FONT_NAME, 10), width=25)
word_typer_value.grid(column=2, row=4, columnspan=2)

# --- BUTTON ---#

add_button = Button(text="Start timer", width=50, command=start_timer)
add_button.grid(column=0, row=6, columnspan=4)


window.mainloop()