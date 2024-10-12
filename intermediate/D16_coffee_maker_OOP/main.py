# practice with using others' code/libraries. this was a *tad* uncomfortable,
# but it's necessary to learn how to work with others' code

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

moneyMachineObj = MoneyMachine()
coffeeMakerObj = CoffeeMaker()
menuObj = Menu()

cont = True

while cont:
    prompt = input("\nWould would you like? (" + menuObj.get_items() + "): ").lower()

    if prompt == "off":
        cont = False
    elif prompt == "report":
        coffeeMakerObj.report()
        moneyMachineObj.report()
    else:
        drink = menuObj.find_drink(prompt)
        if drink != None:
            goTime = coffeeMakerObj.is_resource_sufficient(drink)
            if goTime:
                if moneyMachineObj.make_payment(drink.cost):
                    coffeeMakerObj.make_coffee(drink)