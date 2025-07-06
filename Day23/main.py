import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# turtle 
turtle = Player()

scoreboard = Scoreboard()

screen.listen()

screen.onkey(turtle.move_up, 'Up')


game_is_on = True
i = 1
car_manager = CarManager()
car_manager.create_car(200)
car_manager.create_car(250)
car_manager.create_car(120)
car_manager.create_car(200)
while game_is_on:
   time.sleep(0.1)
   car_manager.move_cars()
   screen.update()
   
   # generating car
   if (i % 6 == 0):
      car_manager.create_car()
   i += 1 
   
   # detect collision with cars
   for car in car_manager.cars:
      if turtle.distance(car) < 20:
         game_is_on = False
         
   # detect collision with finish line
   if turtle.ycor() > FINISH_LINE_Y:
      turtle.goto_start()
      car_manager.speed_up()
      scoreboard.update_score()
         
         
screen.exitonclick()
      