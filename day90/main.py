from tkinter import *
import tkinter

window = Tk()
window.title("The autokiller writter")
window.config(padx=50, pady=50)

count = 5

def kill_writter():
    miles_input.delete("1.0", tkinter.END)
    
def countdown():
    global count, text
    # change text in label        
    miles_label['text'] = f"Hey fadafaka!! ONLY {count} remaining!!!"
    text = "test"
    count -= 1
    if count >= 0:
        # call countdown again after 1000ms (1s)
        window.after(1000, countdown)
    else:
        kill_writter()
        count = 5
        window.after(1000, countdown)

def reboot_timer():
    global count
    miles_label['text'] = f"Hey fadafaka!! ONLY {count} remaining!!!"
    count = 5
    

# elements declaration

text = StringVar()
text.trace("w", reboot_timer)

miles_label = Label(text="time to kill writter")
miles_label.grid(column=0, row=0)

miles_input = Text(width=100)
miles_input.bind('<KeyPress>', lambda *args: reboot_timer())
miles_input.grid(column=0, row=1)

countdown()
window.mainloop()