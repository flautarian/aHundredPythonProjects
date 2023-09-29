import os
from tkinter import messagebox
import password_generator
from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
script_dir = os.path.dirname(__file__)
current_keys = []

def insert_data(web, username, password):
    current_keys.append({
            "website": web,
            "username": username,
            "password": str(password).replace("\n", "")
        })

with open(script_dir + "/keys.txt") as names_file:
    keys = names_file.readlines()
    for pair in keys:
        pair_deconstructed = pair.split("|")
        insert_data(pair_deconstructed[0], pair_deconstructed[1], pair_deconstructed[2])

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    new_password = password_generator.generate_password(35, 35, 35, True)
    password_form_value.delete(0,END)
    password_form_value.insert(0,new_password)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    
    web = web_form_value.get()
    username = username_form_value.get()
    password = password_form_value.get()
    
    if None in [web, username, password] or "" in [web, username, password]:
        messagebox.showinfo(title="Alert", message="Validate all fields.")
        return
    
    is_ok = messagebox.askokcancel(title=web, message=f"These are the details entered: \nEmail: {username} "
                                                      f"\nPassword: {password} \nIs it ok to save?")
    if is_ok:
        insert_data(web, username, password)
        
        with open(script_dir + "/keys.txt", mode="w") as new_keys:
            for key in current_keys:
                new_keys.write(f"{key['website']}|{key['username']}|{key['password']}\n")
        
        web_form_value.delete(0, END)
        username_form_value.delete(0, END)
        password_form_value.delete(0, END)
        messagebox.showinfo(title="Success", message="Password added successfully!.")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50)


title_label = Label(text="Password vault", fg=GREEN, font=(FONT_NAME, 25))
title_label.grid(column=0, row=0, columnspan=4)

canvas = Canvas(width=200, height=224, highlightthickness=0)
logo_img = PhotoImage(file=f"{script_dir}/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=0, row=1, columnspan=4)

# ---WEB---#
web_label = Label(text="Website:", font=(FONT_NAME, 10))
web_label.grid(column=0, row=3)

web_form_value = Entry(font=(FONT_NAME, 10), width=25)
web_form_value.grid(column=2, row=3, columnspan=2)

# ---EMAIL/USERNAME---#

username_label = Label(text="Enail/ Username:", font=(FONT_NAME, 10))
username_label.grid(column=0, row=4)

username_form_value = Entry(font=(FONT_NAME, 10), width=25)
username_form_value.grid(column=2, row=4, columnspan=2)


# ---PASSWORD---#

password_label = Label(text="Password:", font=(FONT_NAME, 10))
password_label.grid(column=0, row=5)

password_form_value = Entry(font=(FONT_NAME, 10), width=15, show="*")
password_form_value.grid(column=2, row=5)

random_button = Button(text="Random", command=generate_password, width=9)
random_button.grid(column=3, row=5)


# ---ADD---#

add_button = Button(text="Add", width=50, command=save_password)
add_button.grid(column=0, row=6, columnspan=4)


window.mainloop()