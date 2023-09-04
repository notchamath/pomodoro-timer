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
timer = ""
is_timer_on = False


# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    reps = 0
    global is_timer_on
    is_timer_on = False

    window.after_cancel(timer)
    checkmarks.config(text="")
    title_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global is_timer_on
    if not is_timer_on:
        is_timer_on = True
        global reps
        reps += 1

        work_secs = WORK_MIN * 60
        short_break_secs = SHORT_BREAK_MIN * 60
        long_break_secs = LONG_BREAK_MIN * 60

        if reps % 8 == 0:
            count_down(long_break_secs)
            title_label.config(text="Break", fg=RED)
        elif reps % 2 == 0:
            count_down(short_break_secs)
            title_label.config(text="Break", fg=PINK)
        else:
            count_down(work_secs)
            title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    mins = math.floor(count / 60)
    secs = count % 60

    canvas.itemconfig(timer_text, text=f"{mins:02}:{secs:02}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        checkmarks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title("POMODORO")
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 140, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

# Title Label
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
title_label.grid(column=2, row=1)

# Start Button
start_btn = Button(text="Start", bg="white", font=(FONT_NAME, 10, "bold"), border=0, pady=5, padx=5,
                   command=start_timer)
start_btn.grid(column=1, row=3)

# Reset Button
reset_btn = Button(text="Reset", bg="white", font=(FONT_NAME, 10, "bold"), border=0, pady=5, padx=5,
                   command=reset_timer)
reset_btn.grid(column=3, row=3)

# Checkmarks
checkmarks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, "bold"))
checkmarks.grid(column=2, row=4)


window.mainloop()
