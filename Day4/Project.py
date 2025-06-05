import random

# scissor, paper, rock

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))

rps_choices = [rock, paper, scissor]

if (user_choice >= 0 and user_choice <= 2):
   print('You chose:')
   print(rps_choices[user_choice])

   computer_choice = random.randint(0, 2)

   print('Computer chose:')
   print(rps_choices[computer_choice])
   
   if (user_choice == computer_choice):
      print("It's a draw")
   elif (user_choice == 0 and computer_choice == 2) or (user_choice == 2 and computer_choice == 1) or (user_choice == 1 and computer_choice == 0):
      print('You win')
   else:
      print('You lose')
else:
   print('Invalid Choice')



# if user_choice == computer_choice:
   # print('It's )
