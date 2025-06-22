from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
menu = Menu()
coffee_maker = CoffeeMaker()

is_on = True
while is_on:
    # TODO 1: Prompt user to ask about coffee
    options = menu.get_items()
    choice = input(f"What would you like?({options}): ").lower()

    # TODO 2: Turn off the coffee machine by entering "off" to the prompt
    if choice == "off":
        is_on = False

    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    # TODO 7.1 process coffee
    else:
        drink = menu.find_drink(choice)
        if drink:
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
        else:
            print(f"{choice} is not available.")
