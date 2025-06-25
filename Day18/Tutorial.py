from turtle import Turtle, Screen
import turtle as t
import random

timmy = Turtle()
timmy.shape('turtle')

# Challenge 1
# for _ in range(4):
#    timmy.forward(100)
#    timmy.right(90)

# Challenge 2
# for _ in range(10):
#    timmy.forward(10)
#    # timmy.pencolor('white')
#    timmy.penup()
#    timmy.forward(10)
#    # timmy.pencolor("black")
#    timmy.pendown()

# Challenge 3
# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# for i in range(3, 11):
#    timmy.pencolor(random.choice(colors))
#    for j in range(i):
#       timmy.forward(100)
#       timmy.right(360/i)

def get_random_color():
   r = random.randint(0, 255)
   g = random.randint(0, 255)
   b = random.randint(0, 255)
   return (r, g, b)

t.colormode(255)
# Challenge 4
# timmy.pensize(10)
# directions = [0, 90, 180, 270]
# timmy.speed(0)
# for _ in range(200):
#    timmy.color(get_random_color())
#    timmy.setheading(random.choice(directions))
#    timmy.forward(20)

# Challenge 5
timmy.speed(0)
timmy.pensize(2)
for i in range(0, 361, 5):
   timmy.color(get_random_color())
   timmy.circle(100)
   timmy.setheading(i)
   
   
screen = Screen()
screen.exitonclick()