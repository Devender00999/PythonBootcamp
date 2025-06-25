from turtle import Turtle, Screen
import turtle as t
import colorgram
import random

t.colormode(255)
# extracted_colors = colorgram.extract('hirst.webp', 30)
colors = [(242, 243, 245), (230, 228, 224), (236, 241, 238), (241, 236, 240), (198, 159, 116), (70, 92, 129), (147, 85, 53), (218, 210, 116), (138, 160, 191), (178, 160, 38), (184, 146, 164), (28, 32, 46), (58, 34, 23), (120, 70, 93), (139, 175, 154), (77, 115, 79), (143, 25, 16), (186, 97, 82), (61, 31, 42), (121, 27, 41), (45, 58, 94), (177, 96, 114), (102, 119, 170), (34, 52, 45), (100, 160, 85), (214, 175, 192), (216, 181, 173), (160, 209, 191), (67, 86, 23), (219, 206, 8)]
# for color in extracted_colors:
#    colors.append((color.rgb.r, color.rgb.g, color.rgb.b))

tim = Turtle()
tim.hideturtle()
tim.speed('fastest')
screen = Screen()
screen.setup(600, 500)
x = -250
y = -210
tim.teleport(x, y)

for i in range(10):
   for i in range(10):
      tim.dot(20, random.choice(colors))
      tim.penup()
      tim.forward(50)
      tim.pendown()
   y += 40
   tim.teleport(x, y)
   

screen.exitonclick()