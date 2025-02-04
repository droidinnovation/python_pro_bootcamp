from pydoc import text
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
reps = 0
timer = "None"


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    start_btn.config(state=NORMAL)
    reset_btn.config(state=DISABLED)

    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    checkmark_done.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    short_brake_sec = SHORT_BREAK_MIN * 60
    long_brake_sec = LONG_BREAK_MIN * 60
    work_sec = WORK_MIN * 60

    if reps % 8 == 0:
        count_down(long_brake_sec)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_brake_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)

    start_btn.config(state=DISABLED)
    reset_btn.config(state=NORMAL)

def count_down(count):
    count_minute = math.floor(count/60)
    count_second = count % 60
    if count_second < 10:
        count_second = f"0{count_second}"

    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_second}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✓"
        checkmark_done.config(text=marks)

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
reset_btn = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
checkmark_done = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME,40))


canvas.grid(row=1, column=1)
timer_label.grid(row=0, column=1)
start_btn.grid(row=2, column=0, sticky="E")
reset_btn.grid(row=2, column=2, sticky="W")
checkmark_done.grid(row=3, column=1)

window.mainloop()