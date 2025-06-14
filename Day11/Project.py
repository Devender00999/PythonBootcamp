# Black jack
import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = []
bot_cards = []

def get_random_card():
   return random.choice(cards)

def print_final_score():
   print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}")
   print(f"Bot's final hand: {bot_cards}, final score: {sum(bot_cards)}")
   
def check_blackjack_or_greater(cards, is_bot = False):
   should_continue = True
   user_cards_sum = sum(cards)
   user = "Bot" if is_bot else "You" 
   if user_cards_sum == 21:
      print_final_score()
      print(f"{user} win with a Blackjack😄")
   elif user_cards_sum > 21:
      print_final_score()
      print(f"{user} went over. {user} lose 😭")
   else:
      should_continue = False
   return should_continue

def print_cards():
   print(f'You cards {user_cards}, current score: {sum(user_cards)}')
   print(f"Bot's first card {bot_cards[0]}")

should_continue = True
while should_continue:
   choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n' ").lower()
   if choice == 'n':
      break
   os.system("clear")
   print("""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      '------'                           |__/         
   """)
   user_cards = random.choices(cards, k = 2)
   bot_cards = random.choices(cards, k = 2)
   print_cards()
   user_cards_sum = sum(user_cards)
   if check_blackjack_or_greater(user_cards):
      continue
   should_pick = 'y'
   while should_pick == 'y' and user_cards_sum < 21:
      should_pick = input("Type 'y' to get another card, type 'n' to pass: ")
      if should_pick != 'y':
         break
      
      user_cards.append(get_random_card())
      print_cards()
      user_cards_sum = sum(user_cards)

   if check_blackjack_or_greater(user_cards):
         continue      
   while True:
      bot_cards_sum = sum(bot_cards)
      if check_blackjack_or_greater(bot_cards, True):
         break
      
      if bot_cards_sum > user_cards_sum:
         print_final_score()
         print('You lose 😭')
         break
         
      bot_cards.append(get_random_card())


         

   