from day15data import resources, MENU

def coffeeSelection():
    availableCoffees = []
    coffeesIndex = 1
    coffeeeSelection = ""
    while coffeeeSelection not in ["1", "2", "3", "4", "5"]:
        
        if len(availableCoffees) == 0:
            for ct in MENU.keys():
                if machineHasIngredientsForCoffee(MENU[ct]):
                    availableCoffees.append(f"[{coffeesIndex}]{ct}")
                    coffeesIndex += 1
                
        coffeeeSelection = input("Please choose your coffee type for more information:\n"+ "\n".join(availableCoffees) + "\n[4]Machine Report \n[5]Machine Refill")
        
        if coffeeeSelection not in ["1", "2", "3", "4", "5"]:
            print("Please introduce a valid option")
    return int(coffeeeSelection)

def machineHasIngredientsForCoffee(coffee):
    global globalResources
    for ing in coffee['ingredients'].keys():
        if coffee['ingredients'][ing] > globalResources[ing]:
            return False
    return True

def printReport():
    global globalResources
    print(f"Current resources:\n Coffee: {globalResources['coffee']} g\n Milk: {globalResources['milk']} ml\n Water: {globalResources['water']} ml")

def refillMachine():
    global globalResources
    globalResources['coffee'] = 500
    globalResources['milk'] = 1000
    globalResources['water'] = 1000

def getCoffeTypeByCode(coffeeChosen):
    return list(MENU.keys())[coffeeChosen-1]

def manageCoins(price):
    print(f"Total to pay: {price}")
    tenCents = int(input("Introduce 10 cents coins"))
    fifyCents = int(input("Introduce 50 cents coins"))
    euroCents = int(input("Introduce 1 Euro coins"))
    twoEuroCents = int(input("Introduce 2 Euro coins"))
    
    totalIntroduced = 0.0
    while totalIntroduced < price:
        totalIntroduced = calculateTotalIntroduced(tenCents, fifyCents, euroCents, twoEuroCents)
        print(f"Total introduced: {str(totalIntroduced)}")
        if totalIntroduced < price:
            print("I need more coins, returning quantity and re try")
        else:
            print(f"Total in return: {str(totalIntroduced - price)}")

def calculateTotalIntroduced(tenCents, fifyCents, euroCents, twoEuroCents):
    return (tenCents * 0.1) + (fifyCents * 0.5) + (euroCents) +  (twoEuroCents * 2)

def discountResources(ingredients):
    global globalResources
    for ing in ingredients.keys():
        globalResources[ing] -= ingredients[ing]
        
def coffeeMachine():
    global globalResources
    machinOperative = True
    print("Welcome to the coffee machine!")
    refillMachine()
    printReport()
    while machinOperative:
        coffeeChosen = coffeeSelection()
        if coffeeChosen == 4:
            printReport()
        elif coffeeChosen == 5:
            refillMachine()
            print("Machine frefilled! 💯")
        elif coffeeChosen > 0 and coffeeChosen < 4:
            coffeeSelected = getCoffeTypeByCode(coffeeChosen)
            manageCoins(MENU[coffeeSelected]['cost'])
            discountResources(MENU[coffeeSelected]['ingredients'])
            print(f"☕ Here is your {str(coffeeSelected)}!! ☕❤")

globalResources = resources

coffeeMachine()