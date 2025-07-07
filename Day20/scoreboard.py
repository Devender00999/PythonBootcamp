from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Times', 14, 'bold')

class Scoreboard(Turtle):
   def __init__(self):
      super().__init__()
      self.score = 0
      self.highscore = self.get_score_from_file()
      self.pencolor('white')
      self.hideturtle()
      self.penup()
      self.update_scoreboard()
      
   def update_scoreboard(self):
      self.clear()
      self.goto(0, 280)
      self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

   def reset(self):
      if self.score > self.highscore:
         self.highscore = self.score
         self.save_score_to_file(self.highscore)
      self.score = 0
      self.update_scoreboard()

   # def game_over(self):
   #    self.goto(0, 0)
   #    self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
   
   def save_score_to_file(self, score):
      with open('data.txt', mode="w") as file:
         file.write(str(score))
   
   def get_score_from_file(self):
      score = 0
      with open('data.txt') as file:
         contents = file.read()
         score = int(contents) 
      return score
 
      
   
   def increase_score(self):
      self.score += 1
      self.update_scoreboard()