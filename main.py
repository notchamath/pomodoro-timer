from tkinter import *
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

# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title("POMODORO")
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 140, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

# Title Label
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
title_label.grid(column=2, row=1)

# Start Button
start_btn = Button(text="Start", bg="white", font=(FONT_NAME, 10, "bold"))
start_btn.grid(column=1, row=3)

# Reset Button
reset_btn = Button(text="Reset", bg="white", font=(FONT_NAME, 10, "bold"))
reset_btn.grid(column=3, row=3)

# Checkmarks
checkmarks = Label(text="✔", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, "bold"))
checkmarks.grid(column=2, row=4)


window.mainloop()
