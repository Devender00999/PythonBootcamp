from turtle import Turtle
from typing import List
MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake():
   
   def __init__(self):
      self.segments: List[Turtle] = []
      self.create_snake()
      self.head = self.segments[0]
      
   def create_snake(self):
      for position in STARTING_POSITIONS:
         new_segment = Turtle('square')
         new_segment.color('white')
         new_segment.penup()
         new_segment.goto(position)
         new_segment.speed(0)
         self.segments.append(new_segment)

   def move(self):
      for i in range(len(self.segments) - 1, 0, -1):
         self.segments[i].goto(self.segments[i - 1].position())
      self.head.forward(MOVE_DISTANCE)
      
   def up(self):
      if self.head.heading() != DOWN:
         self.head.setheading(UP)
   def down(self):
      if self.head.heading() != UP:
         self.head.setheading(DOWN)

   def left(self):
      if self.head.heading() != RIGHT:
         self.head.setheading(LEFT)
   
   def right(self):
      if self.head.heading() != LEFT:
         self.head.setheading(RIGHT)