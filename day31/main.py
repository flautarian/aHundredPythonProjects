BACKGROUND_COLOR = "#B1DDC6"

import json
import os
import random
import time
import pandas
from tkinter import *


script_dir = os.path.dirname(__file__)
random_line = 0

try:
    with open(script_dir + "/keys.txt") as cards:
        current_banned_cards = json.load(cards)
except FileNotFoundError:
    print("file not found, creating one")
    file = open(script_dir + "/keys.txt", "w")
    file.write("[]")
    file.close()
    with open(script_dir + "/keys.txt") as cards:
        current_banned_cards = json.load(cards)

def show_card():
    global random_line, flip_timer
    window.after_cancel(flip_timer)
    random_line = random.choice([i for i in range(0,len(csv_pandas_translations.values)) if i not in current_banned_cards])
    regenerate_card('French', random_line, card_front_img)
    flip_timer = window.after(3000, func=flip_card)
    
def flip_card():
    global random_line
    regenerate_card('English', random_line, card_back_img)
    
def remove_current_card_and_regenerate():
    global random_line
    current_banned_cards.append(random_line)
    with open(script_dir + "/keys.txt", mode="w") as file:
        json.dump(current_banned_cards, file, indent=4)
    show_card()
    
def regenerate_card(lang, random_line, img):
    canvas.itemconfig(card_image, image=img)
    canvas.itemconfig(title_card, text=f"{lang}")
    canvas.itemconfig(word_card, text=f"{csv_pandas_translations[lang][random_line]}")
    

script_dir = os.path.dirname(__file__)

try:
    csv_pandas_translations = pandas.read_csv(f"{script_dir}/data/french_words.csv")
except FileNotFoundError:
    print("translations file not found")
    
window = Tk()
window.title("Language card game")
window.config(padx=25, pady=25)

canvas = Canvas(width=800, height=600, highlightthickness=0)

right_img = PhotoImage(file=f"{script_dir}/images/right.png")
wrong_img = PhotoImage(file=f"{script_dir}/images/wrong.png")
card_back_img = PhotoImage(file=f"{script_dir}/images/card_back.png")

card_front_img = PhotoImage(file=f"{script_dir}/images/card_front.png")
card_image = canvas.create_image(0, 0, image=card_front_img, anchor="nw")
canvas.grid(column=0, row=1, columnspan=3)

title_card = canvas.create_text(400, 100, text="Title", font=("Ariel", 40, "italic"))
word_card = canvas.create_text(400, 250, text="Text", font=("Ariel", 30, "italic"), width=700)

right_button = Button(image=right_img, background=BACKGROUND_COLOR, highlightthickness=0, command=remove_current_card_and_regenerate)
right_button.grid(column=0, row= 2)

wrong_button = Button(image=wrong_img, background=BACKGROUND_COLOR, highlightthickness=0, command=show_card)
wrong_button.grid(column=2, row= 2)

index_csv = 0

flip_timer = window.after(3000, func=flip_card)

show_card()

window.mainloop()
