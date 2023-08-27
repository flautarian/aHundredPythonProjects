# Leap year days in month

""" def is_leap(year):
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            return True
    return False  


month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  

def days_in_month(year, month):
    days = month_days[month-1]
    if is_leap(year):
        days += 1
    return days
  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days) """

# Calculator
from art import calc
print(calc)

statusCalc = True
firstNumber = "Starting Value"
secondNumber = ""
result = 0
operation = ""

def add(f,s):
    return float(f) + float(s)

def subtract(f,s):
    return float(f) - float(s)

def divide(f,s):
    return float(f) / float(s)

def multiply(f,s):
    return float(f) * float(s)

operations = {
    "+" : add,
    "-" : subtract,
    "/" : divide,
    "*" : multiply,
}

def PrintResult(fn, sn, op, res):
    print(f"{fn} {op} {sn} = {res}")

print("Welcome to the calc!!")

while statusCalc == True:
    # Get first operand if starting program
    if firstNumber == "Starting Value":
        firstNumber = input("Intrduce the first number")
    # Get operation type    
    operation = input("introduce the operation [+,-,*,/]")
    # Get second operand
    secondNumber = input("Introduce the second number")
    # Calc
    symbolCalc = operations[operation]
    result = symbolCalc(firstNumber, secondNumber)
    PrintResult(str(firstNumber), secondNumber, operation, str(result))
    againQuestion = input("Do you want to continue calculating? [Y, N]").lower()
    
    if againQuestion in  ["y", "yes"]:
        print("Let's calc starting by the last result: " + str(result))
        firstNumber = result
    else:
        statusCalc = False
        print("BYE! :D")
    
    