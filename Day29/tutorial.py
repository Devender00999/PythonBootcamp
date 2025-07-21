from tkinter import *
from tkinter import messagebox

window = Tk()
window.config(width=400, height=400)

# r = Label(bg="red", width=20, height=5)
# r.grid(row=0, column=0)

# g = Label(bg="green", width=20, height=5)
# g.grid(row=1, column=1)

# b = Label(bg="blue", width=40, height=5)

def show_message():
   messagebox.askquestion("What is this", "Question")

# # columnspan
# b.grid(row=2, column=0, columnspan=2)
button = Button(text='Click me!!', command=show_message)
button.grid(row=0,column=0)



window.mainloop()
