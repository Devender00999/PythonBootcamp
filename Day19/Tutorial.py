from turtle import Turtle, Screen

tim = Turtle()

screen = Screen()
tim.speed(0)

def move_forward():
   tim.forward(10)

def move_backward():
   tim.backward(10)
   
def clear():
   tim.clear()
   tim.penup()
   tim.home()
   tim.pendown()
   

def turn_left():
   tim.left(10)
   
def turn_right():
   tim.right(10)
   
screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='a', fun=turn_right)
screen.onkey(key='d', fun=turn_left)
screen.onkey(key='c', fun=clear)

screen.exitonclick()