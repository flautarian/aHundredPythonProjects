# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆
numberType = ""
if number % 2 != 0: print('This is an odd number.')
else: print('This is an even number.')


# ----BMI calc V2----

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = int(weight)/float(height)**2
if bmi < 18.5:
  print("Your BMI is " + str(round(bmi)) + ", you are underweight.")
elif  bmi < 25:
  print("Your BMI is " + str(round(bmi)) + ", you have a normal weight.")
elif bmi < 30:
  print("Your BMI is " + str(round(bmi)) + ", you are slightly overweight.")
elif bmi < 35:
  print("Your BMI is " + str(round(bmi)) + ", you are obese.")
else:
  print("Your BMI is " + str(round(bmi)) + ", you are clinically obese.")
  
# ----Leap year----

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
divFour = year % 4 == 0
divHundred = year % 100 == 0
divFourHundred = year % 400 == 0
if divFour and (divHundred != True or divFourHundred):
    print("Leap year.")
else:
    print("Not leap year.")
    

# ----Python Pizza!----

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
finalPizzaPrice = 0
if size == 'M':
    finalPizzaPrice= 20
    if add_pepperoni.lower() == 'y':
        finalPizzaPrice += 3
elif size == 'L':
    finalPizzaPrice = 25
    if add_pepperoni.lower() == 'y':
        finalPizzaPrice += 3
else:
    finalPizzaPrice = 15
    if add_pepperoni.lower() == 'y':
        finalPizzaPrice += 2

if extra_cheese.lower() == 'y':
    finalPizzaPrice += 1

print("Your final bill is: $" + str(finalPizzaPrice) + ".")

# ----Love Calculator!----

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

trueCount = 0
trueWord = "TRUE"
for i in trueWord:
    trueCount += name1.lower().count(i.lower())
    trueCount += name2.lower().count(i.lower())

loveWord = "LOVE"
loveCount = 0

for y in loveWord:
    loveCount += name1.lower().count(y.lower())
    loveCount += name2.lower().count(y.lower())

finalScore = int(str(trueCount) + str(loveCount))

finalPhrase = ""

if finalScore < 50:
    finalPhrase = ", you are alright together."
elif  finalScore < 100:
    finalPhrase = "."
else:
    finalPhrase = ", you go together like coke and mentos."

print("Your score is " + str(trueCount) + str(loveCount) + finalPhrase)

# ----Treasure Island game!----

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

answer = input("Left or right? L or R")
if answer.lower() == "r" or answer.lower() == "right" or (answer != 'l' and answer != "left"):
    print("Fall into a hole, Game Over")
    exit(0)

print("You step in front of a lake, you can see a boat coming at the distance")
answer = input("Swim or Wait? S or W")

if answer.lower() == "s" or answer.lower() == "swim" or (answer != 'w' and answer != "wait"):
    print("You fell attacked by a hunger troat, Game Over")
    exit(0)


print("You crossed the lake in the boat and you step in front of a house with three different colour doors, which one do you want to cross?")

answer = input("Red, Blue or Yeallow? R or B or Y")

if answer.lower() == "b" or answer.lower() == "blue":
    print("You found monsters in there and they eat you, Game Over")
    exit(0)


if answer.lower() == "r" or answer.lower() == "red":
    print("You found the room entire full of fire and you fell burned, Game Over")
    exit(0)

if answer != 'y' and answer != "yellow":
    print("You tried to watch throught a window and fell by a monkey attack, Game Over")
    exit(0)

print("You have found the treasure! Congratulations!! :D")




