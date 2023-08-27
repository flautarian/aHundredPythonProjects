from day15data import resources, MENU
from coffe_maker import CoffeeMaker

coffee_machine = CoffeeMaker()
  
def coffeeMachine():
    machinOperative = True
    print("Welcome to the coffee machine!")
    coffee_machine.refillMachine()
    coffee_machine.report()
    while machinOperative:
        coffeeChosen = coffee_machine.coffeeSelection()
        if coffeeChosen == 4:
            coffee_machine.report()
        elif coffeeChosen == 5:
            coffee_machine.refillMachine()
            print("Machine refilled!💯")
        elif coffeeChosen > 0 and coffeeChosen < 4:
            coffeeSelected = coffee_machine.getCoffeTypeByCode(coffeeChosen-1)
            coffee_machine.manageCoins(MENU[coffeeSelected]['cost'])
            coffee_machine.discountResources(MENU[coffeeSelected]['ingredients'])
            print(f"☕ Here is your {str(coffeeSelected)}!! ☕💕")
            
coffeeMachine()