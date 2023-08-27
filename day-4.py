
# ----Random toss----

#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
	 
#Write the rest of your code below this line 👇
import random

randInt = random.randint(0,1)

if randInt == 0:
    print("Tails")
else:
    print("Heads")

# ----Random payer selector----

# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
randomName = random.randint(0, len(names))

print(names[randomName] + " is going to buy the meal today!")

# ----Treasure mark pointer----

# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
xAxis = int(position[0])-1
yAxis = int(position[1])-1
map[yAxis][xAxis] = "X"

#Write your code above this row 👆


# ----Paper rock scissors game!----

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

rockCombinations = [0, -1, 1]
paperCombinations = [1, 0, -1]
scissorsCombinations = [-1, 1, 0]

combinatoryConditions = [rockCombinations, paperCombinations, scissorsCombinations]

playerChoose = int(input("Test your might!! [1: Rock, 2: Paper, 3: Scissors]"))

if playerChoose == 1:
    print(rock)
elif playerChoose == 2:
    print(paper)
else:
    print(scissors)

print("|---------------VS---------------|")

randomChoose = random.randint(1,3)

if randomChoose == 1:
    print(rock)
elif randomChoose == 2:
    print(paper)
else:
    print(scissors)

matchResult = combinatoryConditions[playerChoose-1][randomChoose-1]

if matchResult == 0:
    print("DRAW!!")
elif matchResult < 0:
    print("Player lose!!")
else:
    print("Player WINS!!")