from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
# Components
# Ping pong ball
# Ping pong paddle
# score board


# Setup screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Ping Pong Game!")
screen.tracer(0)

# creating paddle that goes up and down 
leftPaddle = Paddle('l', screen)
rightPaddle = Paddle('r', screen)
ball = Ball()
screen.update()

# score
scoreboard = Scoreboard() 

screen.listen()
screen.onkey(leftPaddle.move_up, 'w')
screen.onkey(leftPaddle.move_down, 's')

screen.onkey(rightPaddle.move_up, 'Up')
screen.onkey(rightPaddle.move_down, 'Down')

game_is_on = True
while game_is_on:
   time.sleep(0.08)
   print(ball.ycor(), ball.xcor())

   # detect collision with wall
   if ball.ycor() >= 280 or ball.ycor() <= -280:
      ball.bounce_y()
      
   # detect collision with the paddle
   print(ball.distance(rightPaddle))
   if ball.distance(rightPaddle) <= 50 and ball.xcor() > 320 or ball.distance(leftPaddle) <= 50 and ball.xcor() < -320:
      ball.bounce_x()
      
   # detect ball collision with right wall
   if ball.xcor() > 380:
      ball.reset_position()
      ball.bounce_x()
      scoreboard.increase_l_point()
   
   # detect ball collision with left wall
   if ball.xcor() < -380:
      ball.reset_position()
      ball.bounce_x()
      scoreboard.increase_r_point()


   ball.move()
   screen.update()



# create the ball and make it move
# creating score board
# detecting collision with bat and ball 
# detecting collition with top and bottom ball to reflect the ball
# detecting collision with  right left wall 
# score to player two



screen.exitonclick()