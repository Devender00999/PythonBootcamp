# Black jack
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = []
bot_cards = []

def get_random_card():
   return random.choice(cards)

def print_final_score():
   print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}")
   print(f"Bot's final hand: {user_cards}, final score: {sum(user_cards)}")
   
def check_blackjack_or_greater(cards):
   should_continue = True
   user_cards_sum = sum(cards)
   if user_cards_sum == 21:
      print_final_score()
      print("You win 😄")
   elif user_cards_sum > 21:
      print_final_score()
      print('You went over. You lose 😭')
   else:
      should_continue = False
   return should_continue

should_continue = True
while should_continue:
   choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n' ").lower()
   if choice == 'n':
      break
   user_cards = random.choices(cards, k = 2)
   bot_cards = random.choices(cards, k = 2)
   print(f'You cards {user_cards}, current score: {sum(user_cards)}')
   print(f"Bot's first card {bot_cards[0]}")
   user_cards_sum = sum(user_cards)
   if check_blackjack_or_greater(user_cards):
      continue
   
   should_pick = input("Type 'y' to get another card, type 'n' to pass: ")
   while should_pick == 'y':
      user_cards.append(get_random_card())
      if check_blackjack_or_greater(user_cards):
         break

   