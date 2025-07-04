import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# turtle 
turtle = Player()

screen.listen()

screen.onkey(turtle.move_up, 'Up')


game_is_on = True
i = 1
car_manager = CarManager()
car_manager.generate_car(200)
car_manager.generate_car(250)
car_manager.generate_car(120)
car_manager.generate_car(200)
while game_is_on:
   time.sleep(0.1)
   car_manager.move_cars()
   screen.update()
   
   # generating car
   if (i % 6 == 0):
      car_manager.generate_car()
   i += 1 
   
   # detect collision with cars
   for car in car_manager.cars:
      print(turtle.distance(car))
      if turtle.distance(car) < 10:
         game_is_on = False
         
      