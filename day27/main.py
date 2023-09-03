import tkinter

window = tkinter.Tk()

window.title("First GUI program!")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="Hello Label!", font=("Arial", 24, "italic"))

my_label.pack()

window.mainloop()