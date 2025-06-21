# Coffee machine project
from resources import MENU,resources


total_money = 0

# TODO 3: print report
def print_report():
   """print report"""
   print(f'Water: {resources['water']}ml')
   print(f'Milk: {resources['milk']}ml')
   print(f'Coffee: {resources['coffee']}g')
   print(f'Money: ${total_money:.2f}')

# TODO 4: check resources sufficient
def is_resource_sufficient(order_ingredients):
   """Check if resources are sufficient"""
   for item in order_ingredients:
      if resources[item] < order_ingredients[item]:
         print(f'Sorry there is not enough {item}.')
         return False
   return True

# TODO 5: Process Coins: to calculate total monetary value of coins
def process_coins():
   """Return total calculateed money from coins"""
   try:
      print("Please insert coins.")
      quaters = int(input("How many quaters?: ")) # $0.25
      dimes = int(input("How many dimes?: ")) # $0.10
      nickles = int(input("How many nickles?: ")) # $0.05
      pennies = int(input("How many pennies?: ")) # 0.01
      total = (quaters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
      return total
   except ValueError:
      print('Invalid Coin. Please try again.')
      
# TODO 6: Check transaction successful
def is_transaction_successful(money_received, drink_cost):
   if money_received < drink_cost:
      return False
   
   global total_money
   total_money += drink_cost
   
   change = money_received - drink_cost
   if (change > 0): 
      print(f"Here is ${change:.2f} dollars in change.")
   return True

# to run the coffee machine
is_on = True

# TODO 7: Make Coffee
def make_coffee():
   for item in order_ingredients:
      resources[item] -= order_ingredients[item]
   print(f'Here is your latte ☕️ Enjoy!')

while is_on:
   # TODO 1: Prompt user to ask about coffee
   coffee = input("What would you like?(espresso/latte/cappuccino): ").lower()
   
   # TODO 2: Turn off the coffee machine by entering "off" to the prompt
   if coffee == 'off':
      break
   
   if coffee == 'report':
      print_report()
      continue
   
   # TODO 7.1 process coffee
   if coffee in MENU.keys():
      
      order_ingredients = MENU[coffee]['ingredients']
      if not is_resource_sufficient(order_ingredients):
         continue
      users_money = process_coins()
      
      if not is_transaction_successful(users_money, MENU[coffee]['cost']):
         continue
         
      make_coffee()

   else:
      print(f"{coffee} is not available.")
               
   

