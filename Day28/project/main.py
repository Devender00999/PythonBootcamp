from tkinter import *
import time

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
def count_down(count):
   canvas.itemconfig(canvas_text, text=count)
   if count > 0:
      window.after(1000, count_down, count - 1)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# to draw item on a canvas 
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

# creating image 
tomato_image = PhotoImage(file="tomato.png")

# heading
timer_text = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
timer_text.grid(row=0, column=1)

# adding image and text in canvas
canvas.create_image(100, 112, image=tomato_image,)
canvas_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)

# start and reset buttons
start_button = Button(text="Start", highlightbackground=YELLOW, command=count_down(5))
start_button.grid(row=2, column=0, padx=0, pady=0)

reset_button = Button(text="Reset", highlightbackground=YELLOW)
reset_button.grid(row=2, column=2)

# pomodoro completed counter
check_mark = Label(text='✔', fg=GREEN, bg=YELLOW)
check_mark.grid(row=3, column=1)







window.mainloop()

