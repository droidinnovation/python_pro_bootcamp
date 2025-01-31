from tkinter import *

def convert():
    try:
        km = round(float(mile_input.get()) * 1.60934, 2)
        km_result.config(text=f"{km}"   )
    except ValueError:
        print("Invalid input! Please enter a valid number (integer or float).")


window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=30, pady=20)

mile_input = Entry(width=7)
mile_input.grid(column=1, row=0)

mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

km_result = Label(text="0")
km_result.grid(column= 1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2 , row=1)

btn_calculate = Button(text="Calculate", command=convert)
btn_calculate.grid(column= 1, row=2)

window.mainloop()
