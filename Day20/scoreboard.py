from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Times', 14, 'bold')

class Scoreboard(Turtle):
   def __init__(self):
      super().__init__()
      self.score = 0
      self.pencolor('white')
      self.hideturtle()
      self.penup()
      self.update_scoreboard()
      

   def update_scoreboard(self):
      self.clear()
      self.goto(0, 280)
      self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

   def game_over(self):
      self.goto(0, 0)
      self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
      
   
   def increase_score(self):
      self.score += 1
      self.update_scoreboard()