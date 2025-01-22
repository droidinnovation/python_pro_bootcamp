# from playground import add
#
# result_add = add(1,2,8,9,8)
# print(result_add)

from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

my_label = Label(text="I am a Label", font=('Arial', 14, 'bold'))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="Text change")

def btn_click():
    print("Click my button")
    my_label.config(text=my_input.get())

my_button = Button(text="Click me", command=btn_click)
my_button.pack()

my_input = Entry(width=10)
my_input.pack()
print(my_input.get())



window.mainloop()