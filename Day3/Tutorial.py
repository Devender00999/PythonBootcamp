# Python Pizza

print('Welcome to Python Pizza Deliveries!')
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want ppepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0

# pizza size
if size == 'S': 
   bill += 15
elif size == 'M':
   bill += 20
elif size == 'L':
   bill += 25
else:
   print('You typed wrong inputs')

# pepperoni
if pepperoni == 'Y':
   if size == 'S':
      bill += 2
   else:
      bill += 3

# extra cheese
if extra_cheese == 'Y':
   bill += 1
   
print(F"Your final bill is ${bill}.")





