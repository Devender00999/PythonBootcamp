from turtle import Turtle, Screen
from typing import List

positions = [(0, -10), (0, -20), (0, -30), (0, -40), (0, -50)]
Y_POSITION = 10

class Paddle(Turtle):
   def __init__(self, direction, screen: Screen):
      super().__init__()
      self.segments: List[Turtle] = []
      self.direction = direction
      self.create_paddle()
      self.head = self.segments[0]
      
      
      # turtle2.color('white')
   def create_paddle(self):
      for position in positions:
         segment: Turtle = Turtle('square')
         segment.penup()
         segment.shapesize(0.5 ,0.5)
         segment.color('white')
         x_position = -370 if self.direction == 'l' else 370
         segment.goto(x_position, position[1])
         self.segments.append(segment)
         
   def move_up(self):
      for i in range(len(self.segments) - 1, 0, -1):
         self.segments[i].goto(self.segments[i - 1].position())
      self.head.setheading(90)
      self.head.forward(20)
      self.screen.update()
   
   def move_down(self):
      for i in range(len(self.segments) - 1, 0, -1):
         self.segments[i].goto(self.segments[i - 1].position())
      # self.head.setheading(0)
      self.head.backward(20)
      self.screen.update()
      
      
      
         
   
      