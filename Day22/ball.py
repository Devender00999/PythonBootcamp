from turtle import Turtle

class Ball(Turtle):
   def __init__(self):
      super().__init__('circle')
      self.shapesize(1, 1)
      self.color('white')
      self.penup()
      
   def move(self):
      self.goto(self.xcor() + 20, self.ycor() + 20)