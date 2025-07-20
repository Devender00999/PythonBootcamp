from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 30
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 10
reps = 0
timer_id = ''


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
   if (len(timer_id) > 0):
      start_button['state'] = 'active'

      # reseting timer text
      timer_text.config(text="Timer")

      # reseting timer 
      window.after_cancel(timer_id)

      # resetting canvas text
      canvas.itemconfig(canvas_text, text='00:00')
      
      # resetting check marks
      check_mark.config(text="")

      # resetting reps
      global reps
      reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
   global reps
   reps += 1
   if reps % 8 == 0:
      count = LONG_BREAK_MIN * 60
      timer_text.config(text="Break", fg=RED)
   elif (reps % 2 == 0):
      count = SHORT_BREAK_MIN * 60
      timer_text.config(text="Break", fg=PINK)
   else:
      timer_text.config(text="Work", fg=GREEN)
      count = WORK_MIN * 60

   start_button['state'] = 'disabled'
   count_down(count)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
   count_min = f"{math.floor(count / 60)}".rjust(2, '0')
   count_sec = f'{int(count % 60)}'.rjust(2, '0')
   canvas.itemconfig(canvas_text, text=f"{count_min}:{count_sec}")
   global timer_id
   if count > 0:
      timer_id = window.after(100, count_down, count - 1)
   else:
      start_timer()
      marks = ""
      work_sessions = math.floor(reps / 2)
      for _ in range(work_sessions):
         marks += '✔'
         check_mark.config(text=marks)

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
start_button = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
start_button.grid(row=2, column=0, padx=0, pady=0)

reset_button = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(row=2, column=2)

# pomodoro completed counter
check_mark = Label(text='', fg=GREEN, bg=YELLOW)
check_mark.grid(row=3, column=1)







window.mainloop()

