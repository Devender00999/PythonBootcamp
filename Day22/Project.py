from turtle import Screen
from paddle import Paddle
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
paddle = Paddle('l', screen)
screen.update()

screen.listen()
screen.onkey(paddle.move_up, 'Up')
screen.onkey(paddle.move_down, 'Down')



# create the ball and make it move
# creating score board
# detecting collision with bat and ball 
# detecting collition with top and bottom ball to reflect the ball
# detecting collision with  right left wall 
# score to player two



screen.exitonclick()