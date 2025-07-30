THEME_COLOR = "#375362"
from tkinter import *

class QuizInterface:
   def __init__(self):
      self.window = Tk()
      self.window.config(background=THEME_COLOR, padx=20, pady=20)
      self.window.title('Quizzler')
      self.score = 0
      
      self.label_score = Label(text="Score: " + str(self.score), bg=THEME_COLOR)
      self.label_score.grid(row=0, column=1)
      
      self.canvas = Canvas(width=300, height=250, background="white", highlightthickness=0)
      
      self.text = self.canvas.create_text(150, 125, text='Quiz Question', font=('Areal', 20, 'italic'), fill="black")
      self.canvas.grid(row=1, column=0, columnspan=2,padx=20, pady=20,)
      
      self.right_image = PhotoImage(file='images/true.png')
      self.right_btn = Button(image=self.right_image, highlightthickness=0)
      self.right_btn.grid(row=2 ,column=0, padx=20)
      
      self.wrong_image = PhotoImage(file='images/false.png')
      self.wrong_btn = Button(image=self.wrong_image, highlightthickness=0)
      self.wrong_btn.grid(row=2 ,column=1, pady=20)
      
      self.window.mainloop()
      
      