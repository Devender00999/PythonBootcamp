# Tutle Race
from turtle import Turtle, Screen
import random

sheldon = Turtle('turtle')
sheldon.color('red')
sheldon.penup()

leonard = Turtle('turtle')
leonard.color('yellow')
leonard.penup()


penny = Turtle('turtle')
penny.color('pink')
penny.penup()


howard = Turtle('turtle')
howard.color('blue')
howard.penup()


raj = Turtle('turtle')
raj.color('purple')
raj.penup()



sheldon.teleport(-240, -150)
leonard.teleport(-240, -100)
penny.teleport(-240,-50)
raj.teleport(-240, 0)
howard.teleport(-240, 50)



def we_have_winner():
   if sheldon.pos()[0] > 200:
      return 'sheldon'
   elif leonard.pos()[0] > 200:
      return 'leonard' 
   elif penny.pos()[0] > 200:
      return 'penny' 
   elif raj.pos()[0] > 200:
      return 'raj'
   elif howard.pos()[0] > 200:
      return 'howard' 
   return 'no_one'
 

screen = Screen() 
screen.setup(width=500, height=400)
winner = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?")

while we_have_winner() == 'no_one':
   print(sheldon.pos()[0])
   sheldon.forward(random.randint(10, 20))
   leonard.forward(random.randint(10, 20))
   penny.forward(random.randint(10, 20))
   raj.forward(random.randint(10, 20))
   howard.forward(random.randint(10, 20))


if winner.lower() == we_have_winner():
   print('You guessed it right.')
else:
   print(f"You lose, {we_have_winner()} has won the race")
   
screen.exitonclick()