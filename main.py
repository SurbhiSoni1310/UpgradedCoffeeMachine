from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from art import logo
import os
from time import sleep
continue_loop = True
cup = Menu()
make_cup = CoffeeMaker()
money = MoneyMachine()
while continue_loop:
    print("Welcome to the coffee machine")
    print(logo)
    choice = input("Choose from the available items : "+cup.get_items()+": ")
    if choice == "report":
        make_cup.report()
        money.report()
        sleep(10)
        os.system("cls")
    else:
        drink = cup.find_drink(choice)
        if not drink:
            sleep(10)
            os.system("cls")
        else:
            if make_cup.is_resource_sufficient(drink):
                if money.make_payment(drink.cost):
                    make_cup.make_coffee(drink)
                    sleep(10)
                    os.system("cls")
                else:
                    sleep(10)
                    os.system("cls")
            else:
                sleep(10)
                os.system("cls")








