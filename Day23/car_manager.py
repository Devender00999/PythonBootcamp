from turtle import Turtle
from typing import List
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
   def __init__(self):
      self.cars: List[Turtle] = []
      
   def generate_car(self, x_pos = 290):
      car = Turtle('square')
      car.penup()
      car.shapesize(1, 1.8)
      car.color(random.choice(COLORS))
      car.setheading(180)
      car.forward(10)
      car.goto(x_pos or 290, random.randint(-250, 250) + STARTING_MOVE_DISTANCE)
      self.cars.append(car)
      
   def move_cars(self): 
      for car in self.cars:
         if (car.xcor() < -320): 
            car.clear()
            self.cars.remove(car)
            continue
         car.setx(car.xcor() - MOVE_INCREMENT)
      
   