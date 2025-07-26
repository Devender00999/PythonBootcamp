BACKGROUND_COLOR = "#B1DDC6"

from tkinter import * 
import pandas
import random

window = Tk()
window.title('Flashy')

window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# creating canvas for image

canvas = Canvas(width=800, height= 526, bg=BACKGROUND_COLOR, highlightthickness=0)

translations = pandas.read_csv('data/french_words.csv').to_dict(orient='records')

front_image = PhotoImage(file="./images/card_front.png")
back_image = PhotoImage(file="./images/card_back.png")
image = canvas.create_image(400, 263, image=front_image)

title = canvas.create_text(400,150, text='French', font=('Ariel', 50, 'italic'), fill="black")
word_text = canvas.create_text(400,263, text='trouve', font=('Ariel', 60, 'bold'), fill="black")


canvas.grid(row=0, column=0, columnspan=2)
current_word = ''

def get_random_word():
   global current_word
   current_word = random.choice(translations)
   canvas.itemconfig(image, image=front_image)
   canvas.itemconfig(title, text='French', fill="black")
   canvas.itemconfig(word_text, text=current_word['French'], fill="black")

   window.after(3000, show_translation)
   
def show_translation():
   canvas.itemconfig(title, text='English', fill='white')
   canvas.itemconfig(word_text, text=current_word['English'], fill="white")
   canvas.itemconfig(image, image=back_image)

   
def has_learnt():
   get_random_word()
   words_to_learn = translations.remove(current_word)
   df = pandas.DataFrame(words_to_learn)
   df.to_csv('words_to_learn.csv')
   
   
   

# wrong button
wrong_image = PhotoImage(file="./images/wrong.png")
wrong_btn = Button(image=wrong_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=get_random_word)
wrong_btn.grid(row=1, column=0)

# right button
right_image = PhotoImage(file="./images/right.png")
right_btn = Button(image=right_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, highlightcolor=BACKGROUND_COLOR, command=has_learnt)
right_btn.grid(row=1, column=1)

get_random_word()


window.mainloop()


