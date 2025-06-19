# to create a game of higher lower 

from art import higer_lower, vs
from game_data import data
import random

# Todo 1: print art for higher lower
print(higer_lower)

# TODO 2: initialize score with 0, is_winning with True
score = 0
is_winning = True
first, second = random.choices(data, k = 2)

# TODO 3: Run a loop until is_winning is True

def is_user_wrong(choice, score):
   """Check if user selected wrong choice"""
   if choice == 'a' and first['follower_count'] < second['follower_count']:
      print(f"Sorry, that's wrong. Final score: {score}")
      return True
   elif choice == 'b' and first['follower_count'] > second['follower_count']:
      print(f"Sorry, that's wrong. Final score: {score}")
      return True
   return False

def format_data(account):
   return f"{account['name']}, {account['description']}, from {account['country']}"
   

   

while is_winning:
   print(f"Compare A: {format_data(first)}")
   print(vs)
   print(f"Against B: {format_data(second)}")
   choice = input("Who has more followers? Type 'A' or 'B': ").lower()

   if is_user_wrong(choice, score):
      break
   
   score += 1
   print(f"You're right! Current Score: {score}")
   first = second
   data.remove(first)
   second = random.choice(data)
