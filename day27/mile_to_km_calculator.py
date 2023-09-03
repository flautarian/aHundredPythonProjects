from tkinter import *

def calculate_quant():
    calc = int(miles_input.get()) * 1.609
    km_result_label.config(text=f"{str(calc)}")


window = Tk()
window.title("Miles to Kilometer Calculator")
window.config(padx=20, pady=20)
# elements declaration

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calculate_btn = Button(text="Calculate", command=calculate_quant)
calculate_btn.grid(column=1, row=2)

window.mainloop()