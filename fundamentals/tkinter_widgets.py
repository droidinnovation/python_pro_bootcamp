from tkinter import *

# Creating a new window and configurations
window = Tk()
window.title("Widget examples")
window.minsize(width=500, height=500)

# Label
label = Label(text="This is old text")
label.config(text="This is new Label")
label.pack()

# Button
def btn_action():
    print("Do somethings")
# call btn_action() when press
button = Button(text="Click me", command=btn_action)
button.pack()

# Entries one-line text entry widgets
entry = Entry(width=30)
# add some text to entry
entry.insert(index=END, string="Some text to begin with.")
# get text in entry
print(entry.get())
entry.pack()

# Text - multi-lines text entry
text = Text(height=5, width=30)
# put cursor in textbox
text.focus()
text.insert(END, "Example of multi-line text entry")
# get current value in textbox at line 1, character 0
print(text.get(1.0, END))
text.pack()

# SpinBox
def spinbox_selected():
    print(spinbox.get())

spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_selected)
spinbox.pack()

# Scale
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()
scale.config(orient=HORIZONTAL)

# Check Button
def on_checkbutton_changed():
    print(checked_state.get())
checked_state = IntVar()
check_button = Checkbutton(text="Is on?", variable= checked_state, command=on_checkbutton_changed)
check_button.pack()

# Radio Button
def radio_button_used():
    print(radio_button_state.get())
radio_button_state = IntVar()
radio_button1 = Radiobutton(text="Option1", variable=radio_button_state, value=1, command=radio_button_used)
radio_button2 = Radiobutton(text="Option2", variable=radio_button_state, value=2, command=radio_button_used)
radio_button1.pack()
radio_button2.pack()

# ListBox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))
    # print(event)
fruits = ["Apple", "Pear", "Orange", "Banana", "Strawberry","Water melon"]
listbox = Listbox(height=len(fruits))
for item in fruits:
    listbox.insert(fruits.index(item), item)

listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()


window.mainloop()