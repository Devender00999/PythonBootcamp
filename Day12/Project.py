import random
# Guessing the number
print("""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ' _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|        
      """)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

num = random.randint(1, 100)
print( num)

# To-Do
# Print the welcome message
# generate a random number between 1 and 100
# take input for dificulty level
# assign total guess based on difficulty
# Run a loop till guess become 0
#     ask user for guessing the number
#     check if number is equal to generated number print you will
#     if number is greater than generated number print too high ask to guess again
#     if number is less than generated number print too low ask to guess again
# after loop print the number and you lose

def check_answer(guess, answer):
   if guess == answer:
      print("You got it! The answer was 58.")
      return
   elif guess > answer:
      print('Too high. \nGuess again.')
   else:
      print('Too low. \nGuess again.')

def guess_the_number():
   choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

   total_guesses = 10 if choice == 'easy' else 5

   while total_guesses > 0:
      print(f'You have {total_guesses} attempts remaining to guess the number.')
      guess = int(input('Make a guess: '))
      check_answer(guess, num)
      total_guesses -= 1

   print("You've run out of guesses. run again.")

guess_the_number()