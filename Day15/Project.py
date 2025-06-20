# Coffee machine project
from resources import MENU,resources


total_money = 0

# TODO 3: print report
def print_report():
   print(f'Water: {resources['water']}ml')
   print(f'Milk: {resources['milk']}ml')
   print(f'Coffee: {resources['coffee']}g')
   print(f'Money: ${total_money}')

# TODO 4: check resources sufficient
def has_enough_resources(coffee):
   if resources['water'] < MENU[coffee]['ingredients']['water']:
      print('Sorry there is not enough water.')
      return False
   if coffee != 'espresso' and resources['milk'] < MENU[coffee]['ingredients']['milk']:
      print('Sorry there is not enough milk.')
      return False
   if resources['coffee'] < MENU[coffee]['ingredients']['coffee']:
      print('Sorry there is not enough coffee.')
      return False
   return True

# TODO 5: Process Coins

# TODO 6: Check transaction successful

# TODO 7: Make Coffee
# TODO 7.1 process coffee
# TODO 7.2 print coffee message


# to run the coffee machine
is_machine_running = True

while is_machine_running:
   # TODO 1: Prompt user to ask about coffee
   coffee = input("What would you like?(espresso/latte/cappuccino): ").lower()
   
   # TODO 2: Turn off the coffee machine by entering "off" to the prompt
   if coffee == 'off':
      break
   
   if coffee == 'report':
      print_report()
   
   
   
   
   
   

