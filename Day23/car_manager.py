from turtle import Turtle
from typing import List
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
   def __init__(self):
      self.cars: List[Turtle] = []
      self.car_speed = MOVE_INCREMENT
      
   def create_car(self, x_pos = 290):
      car = Turtle('square')
      car.shapesize(stretch_wid=1, stretch_len=2)
      car.penup()
      car.color(random.choice(COLORS))
      car.forward(10)
      random_y = random.randint(-250, 250)
      car.goto(x_pos or 300, random_y + STARTING_MOVE_DISTANCE)
      self.cars.append(car)
      
   def move_cars(self): 
      for car in self.cars:
         if (car.xcor() < -320): 
            car.clear()
            self.cars.remove(car)
            continue
         car.backward(self.car_speed)
         
   def speed_up(self):
      self.car_speed += MOVE_INCREMENT
      
      
   