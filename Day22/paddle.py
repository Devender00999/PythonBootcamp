from turtle import Turtle, Screen
from typing import List


class Paddle(Turtle):
   def __init__(self, direction, screen: Screen):
      super().__init__('square')
      self.screen = screen
      self.direction = direction
      self.color('white')
      self.penup()
      if (direction == 'l'):
         self.goto(-350, 0)
      else:
         self.goto(350, 0)
      self.shapesize(5, 1)
      

         
   def move_up(self):
      self.setposition(self.xcor(), self.ycor() + 20)
      self.screen.update()
   
   def move_down(self):
      self.setposition(self.xcor(), self.ycor() - 20)
      self.screen.update()
      
      
      
      
         
   
      