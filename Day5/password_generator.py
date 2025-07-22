import random

# password generater
letters = [
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
  'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
  'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = [
  '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=',
  '+', '[', ']', '{', '}', '\\', '|', ';', ':', '\'', '"', ',', '<',
  '.', '>', '/', '?', '`', '~'
]

print('Welcome to the PyPassword Generator!')

nr_letters = int(input('How many letters would you like in your password?\n'))
nr_symbols = int(input('How many symbols would you like?\n'))
nr_numbers = int(input('How many numbers would you like?\n'))

# nr_letters = 8
# nr_symbols = 2
# nr_numbers = 2
# password = ""
# for i in range(nr_letters):
#    password += random.choice(letters)
   
# for i in range(nr_symbols):
#    password += random.choice(symbols)
   
# for i in range(nr_numbers):
#    password += random.choice(numbers)
   
# print("Your password is: " + password)

# li_chars = [letters, numbers, symbols]
# total = nr_letters + nr_symbols + nr_numbers
# password = ''
# for i in range(total):
#    random_charlist = random.randint(0, len(li_chars) - 1)
#    choice = random.choice(li_chars[random_charlist])
#    password += choice
   
#    if (random_charlist == 0):
#       nr_letters -= 1
#    if (random_charlist == 1):
#       nr_numbers -= 1
#    if (random_charlist == 2):
#       nr_symbols -= 1
      
#    if (nr_letters == 0 and letters in li_chars):
#       li_chars.pop(li_chars.index(letters))
#    if (nr_numbers == 0 and numbers in li_chars):
#       li_chars.pop(li_chars.index(numbers))
#    if (nr_symbols == 0 and symbols in li_chars):
#       li_chars.pop(li_chars.index(symbols))

def generate_password(nr_letters, nr_symbols, nr_numbers ):
   letters = [
      'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
      'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
      'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
      'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
   ]

   numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

   symbols = [
   '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=',
   '+', '[', ']', '{', '}', '\\', '|', ';', ':', '\'', '"', ',', '<',
   '.', '>', '/', '?', '`', '~'
   ]
   password_list = []
   random_letters = [random.choice(letters) for _ in range(nr_letters)]
   random_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
   random_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

   password_list = random_letters + random_symbols + random_numbers
   random.shuffle(password_list)

   password = "".join(password_list)
   return password

print(generate_password(nr_letters, nr_symbols, nr_numbers))