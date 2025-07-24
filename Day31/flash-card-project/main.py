BACKGROUND_COLOR = "#B1DDC6"

from tkinter import * 

window = Tk()
window.title('Flashy')

window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# creating canvas for image

canvas = Canvas(width=800, height= 526, bg=BACKGROUND_COLOR, highlightthickness=0)

front_image = PhotoImage(file="./images/card_front.png")
# canvas.create_image(400, 263, image=front_image)

canvas.create_text(400,150, text='French', font=('Ariel', 50, 'italic'), fill="black")
canvas.create_text(400,263, text='trouve', font=('Ariel', 60, 'italic'), fill="black")

canvas.grid(row=0, column=0, columnspan=2)

# wrong button
wrong_image = PhotoImage(file="./images/wrong.png")
wrong_btn = Button(image=wrong_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR)
wrong_btn.grid(row=1, column=0)

# right button
right_image = PhotoImage(file="./images/right.png")
right_btn = Button(image=right_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, highlightcolor=BACKGROUND_COLOR)
right_btn.grid(row=1, column=1)




window.mainloop()


