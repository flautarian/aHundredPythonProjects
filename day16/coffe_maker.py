from money_machine import MoneyMachine

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

class CoffeeMaker:
    """Models the machine that makes the coffee"""
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
        self.money_machine = MoneyMachine()

    def report(self):
        """ Prints a report of all resources. """
        print(f"Current resources:\n Coffee: {self.resources['coffee']} g\n Milk: {self.resources['milk']} ml\n Water: {self.resources['water']} ml")
        self.money_machine.report()

    def is_resource_sufficient(self, drink):
        """ Returns True when order can be made, False if ingredients are insufficient. """
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make
    
    def coffeeSelection(self):
        """ Display the coffee selection available of the machine """
        availableCoffees = []
        coffeesIndex = 1
        coffeeeSelection = ""
        while coffeeeSelection not in ["1", "2", "3", "4", "5"]:
            
            if len(availableCoffees) == 0:
                for ct in MENU.keys():
                    if self.machineHasIngredientsForCoffee(MENU[ct]):
                        availableCoffees.append(f"[{coffeesIndex}]-{ct}")
                        coffeesIndex += 1
                    
            coffeeeSelection = input("Please choose your coffee type for more information:\n"+ "\n".join(availableCoffees) + "\n[4]-Machine Report \n[5]-Machine Refill")
            
            if coffeeeSelection not in ["1", "2", "3", "4", "5"]:
                print("Please introduce a valid option")
        return int(coffeeeSelection)

    def machineHasIngredientsForCoffee(self, coffee):
        """ Returns if the machine has enough ngredients in machine to display the coffee """
        for ing in coffee['ingredients'].keys():
            if coffee['ingredients'][ing] > self.resources[ing]:
                return False
        return True

    def make_coffee(self, order):
        """Produces the selected coffee with their consequences on the machine"""
        self.discountResources(self, order.ingredients)
        print(f"Here is your {order.name} ☕️. Enjoy!")
        
    def discountResources(self, ingredients):
        """Deducts the required ingredients from the resources."""
        for ing in ingredients.keys():
            self.resources[ing] -= ingredients[ing]
    
    def refillMachine(self):
        """ Refills the resources of the machine """
        self.resources['coffee'] = 500
        self.resources['milk'] = 1000
        self.resources['water'] = 1000

    def getCoffeTypeByCode(self, coffeeChosen):
        """ Returns the name of the coffee by the code chosen """
        return list(MENU.keys())[coffeeChosen]
    
    def manageCoins(self, price):
        """ Coin management when a price is demanded """
        self.money_machine.manageCoins(price)
