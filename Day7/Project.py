import random
# Hangman
words = [
    # Easy words
    "apple", "chair", "house", "tiger", "green",
    "pizza", "cloud", "bread", "movie", "beach",
    
    # Medium words
    "blanket", "thunder", "monster", "mailbox", "journey",
    "sandals", "curtain", "diamond", "ketchup", "laptop",
    
    # Hard words
    "avalanche", "labyrinth", "chandelier", "astronaut", "psychology",
    "whirlwind", "crocodile", "submarine", "espresso", "knapsack",
    
    # Tricky spelling or silent letters
    "knight", "rhythm", "island", "gnome", "receipt",
    "debris", "choir", "pneumonia", "tsunami", "gnarly"
]

chosen_word = random.choice(words)
user_guesses = ['-']*len(chosen_word)

zero = """
  +---+
  |   |
      |
      |
      |
      |
========="""

one = """
  +---+
  |   |
  O   |
      |
      |
      |
=========
"""

two = """
  +---+
  |   |
  O   |
 /    |
      |
      |
=========
"""

three = """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
"""


four = """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
"""


five = """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
"""

six = """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
"""

mistakes = [zero, one, two, three, four, five, six]

life_count = 0
print("""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/
                   """)

print("Word to guess: ", "".join(user_guesses))


while life_count < 6:
   choice = input('Guess a letter: ').lower()
   if choice in user_guesses:
      print(f"You've already guessed {choice}")
      print(mistakes[life_count])
   elif choice in chosen_word:
      for i in range(len(chosen_word)):
         if chosen_word[i] == choice:
            user_guesses[i] = choice
      print("".join(user_guesses))
      print(mistakes[life_count])
      print(f"****************************{6 - life_count}/6 LIVES LEFT****************************")

   else: 
      life_count += 1
      print(f"You guessed {choice}, that's not in the word. You lose a life.")
      print(mistakes[life_count])
      if (life_count != 6):
         print(f"****************************{6 - life_count}/6 LIVES LEFT****************************")
      else:
         print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")


   if "".join(user_guesses) == chosen_word:
      print(chosen_word)
      print("You Win!!")
      break


