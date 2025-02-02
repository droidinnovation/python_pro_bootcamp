from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def start_timer():
    count_down(5 * 60)

def count_down(count):
    count_minute = math.floor(count/60)
    count_second = count % 60
    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_second}")
    if count > 0:
        window.after(1000, count_down, count - 1)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Poromodo")
window.config(padx=100,pady=50,bg=YELLOW)

canvas = Canvas(width=200,height=224, background=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,130,text="00:00",fill="white", font=(FONT_NAME,35,"bold"))

timer_label = Label(text="Timer", foreground=GREEN, background=YELLOW, font=(FONT_NAME, 45))

start_btn = Button(text="Start", bg=YELLOW, highlightbackground=YELLOW, command=start_timer)
reset_btn = Button(text="Reset", highlightbackground=YELLOW)
checkmark_done = Label(text="✔", fg=GREEN, bg=YELLOW, font=(FONT_NAME,40))


canvas.grid(row=1, column=1)
timer_label.grid(row=0, column=1)
start_btn.grid(row=2, column=0, sticky="E")
reset_btn.grid(row=2, column=2, sticky="W")
checkmark_done.grid(row=3, column=1)

window.mainloop()