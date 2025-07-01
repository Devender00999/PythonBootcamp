from turtle import Screen
from paddle import Paddle
from ball import Ball
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

screen.listen()
screen.onkey(leftPaddle.move_up, 'w')
screen.onkey(leftPaddle.move_down, 's')

screen.onkey(rightPaddle.move_up, 'Up')
screen.onkey(rightPaddle.move_down, 'Down')

game_is_on = True
while game_is_on:
   ball.move()
   screen.update()
   time.sleep(0.1)



# create the ball and make it move
# creating score board
# detecting collision with bat and ball 
# detecting collition with top and bottom ball to reflect the ball
# detecting collision with  right left wall 
# score to player two



screen.exitonclick()