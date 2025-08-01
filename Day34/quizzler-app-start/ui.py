THEME_COLOR = "#375362"
from quiz_brain import QuizBrain
from tkinter import *

class QuizInterface:
   def __init__(self, quiz: QuizBrain):
      self.window = Tk()
      
      self.quiz = quiz
      
      self.window.config(background=THEME_COLOR, padx=20, pady=20)
      self.window.title('Quizzler')
      self.score = 0
      
      self.label_score = Label(text="Score: " + str(self.score), bg=THEME_COLOR)
      self.label_score.grid(row=0, column=1)
      
      self.canvas = Canvas(width=300, height=250, background="white", highlightthickness=0)
      
      self.text = self.canvas.create_text(150, 125, width=280, text="", font=('Areal', 20, 'italic'), fill="black")
      self.canvas.grid(row=1, column=0, columnspan=2,padx=20, pady=20,)
      
      self.right_image = PhotoImage(file='images/true.png')
      self.right_btn = Button(image=self.right_image, highlightthickness=0, command=self.true_pressed)
      self.right_btn.grid(row=2 ,column=0, padx=20)
      self.wrong_image = PhotoImage(file='images/false.png')
      self.wrong_btn = Button(image=self.wrong_image, highlightthickness=0, command=self.false_pressed)
      self.wrong_btn.grid(row=2 ,column=1, pady=20)
      
      self.get_next_question()
      self.window.mainloop()
      
   def get_next_question(self):
      self.canvas.config(bg='white')
      if self.quiz.still_has_questions():   
         question = self.quiz.next_question()
         self.canvas.itemconfig(self.text, text=question)
      else:
         self.canvas.itemconfig(self.text, text="You've reached the end of the quiz.")
         self.right_btn.config(state="disabled")
         self.wrong_btn.config(state="disabled")
      
      
   def true_pressed(self):
      self.give_feedback( self.quiz.check_answer('True'))
      
   def false_pressed(self):
      self.give_feedback(self.quiz.check_answer('False'))
      
   def give_feedback(self, is_right):
      if is_right:
         self.canvas.config(bg='green')
         self.window.after(1000, self.change_bg_to_white)
         self.score += 1
         self.label_score.config(text="Score "+str(self.score) )
      else:
         self.canvas.config(bg='red')
         self.window.after(1000, self.change_bg_to_white)
         
   def change_bg_to_white(self):
      self.canvas.config(bg='white')
      self.get_next_question()
      