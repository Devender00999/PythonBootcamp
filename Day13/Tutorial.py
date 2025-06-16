import random
import maths
# def my_function():
#    for i in range(1, 20):
#       if i == 20:
#          print('You got it.')

# try:
#    age = int(input('How old are you?'))
# except ValueError: 
#    print("You have typed invalid number.")     

def mutate(a_list):
   b_list = []
   new_item = 0
   for item in a_list:
      new_item = item * 2
      new_item += random.randint(1, 3)
      new_item = maths.add(new_item, item)
      b_list.append(new_item)
   print(b_list)
   
mutate([1,2,3,4])
   
    
# Describe the problem - write your answers as comments
# Reproduce the bug
# Play Computer and run the code line by line
# Fix the error 
# Print is your friend
# Use a debugger
# Take a break
# Ask a friend
# Run Often
# Search online
