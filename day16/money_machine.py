import prettytable

class MoneyMachine:
    """Models the algorithm that balances de money of the machine"""
    def __init__(self):
        self.money_got = 0.0
        
    def report(self):
        """Report of the current money balance of the machine"""
        print(f"Current machine balance {self.money_got}€")
    
    def calculateTotalIntroduced(self, tenCents, fifyCents, euroCents, twoEuroCents):
        return (tenCents * 0.1) + (fifyCents * 0.5) + (euroCents) +  (twoEuroCents * 2)
      
    def manageCoins(self, price):
        """Management of the coins respect the price to introduce"""
        print(f"Total to pay: {price}")
        tenCents = int(input("Introduce 10 cents coins"))
        fifyCents = int(input("Introduce 50 cents coins"))
        euroCents = int(input("Introduce 1 Euro coins"))
        twoEuroCents = int(input("Introduce 2 Euro coins"))
        
        totalIntroduced = 0.0
        while totalIntroduced < price:
            totalIntroduced = self.calculateTotalIntroduced(tenCents, fifyCents, euroCents, twoEuroCents)
            print(f"Total introduced: {str(totalIntroduced)}")
            if totalIntroduced < price:
                print("I need more coins, returning quantity and re try")
            else:
                print(f"Total in return: {str(totalIntroduced - price)}")
        
        self.money_got += price
        
        