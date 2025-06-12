import os
def add(n1, n2):
   return n1 + n2

def subtract(n1, n2):
   return n1 - n2

def multiply(n1, n2):
   return n1 * n2

def divide(n1, n2):
   return n1 / n2

operations = {
   "+": add,
   "-": subtract,
   "*": multiply,
   "/": divide,
}

def calculator():
   print("""
   _____________________
   |  _________________  |
   | | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
   | |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
   |  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
   | | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
   | |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
   | | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
   | |___|___|___| |___| | | |  \ '.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ '.___.'\  | |
   | | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|  |____|| || |  |________|  | || |   '._____.'  | |
   | |___|___|___| |___| | | |              | || |              | || |              | || |              | |
   | | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
   | |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
   |_____________________|
   """)

   result = 0
   choice = "n"
   while True:
      first_number = result
      if choice == 'n':
         os.system('clear')
         first_number = int(input("What's the first number?: "))
      for i in operations.keys():
         print(i)

      operation = input("Pick an option: ")
      
      if operation not in operations.keys():
         print("Invalid operation")
         continue
      second_number = int(input("What's the second number?: "))
      result = operations[operation](first_number, second_number)
      print(f"{first_number} {operation} {second_number} = {result}")
      choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
      
calculator()
   
   
   