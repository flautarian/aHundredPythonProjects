from art import higherlower, vs
from day14data import data
import random


gameState = 0

contests = [
    {"Cristiano Ronaldo", 78000}
]

def decissionChecker(decision, contestOne, contestTwo):
    if decision == 'A':
        if contestOne['follower_count'] > contestTwo['follower_count']:
            print(f"Correct!!, { writeDecisionDesc(contestOne, contestTwo) }")
        else:
            print(f"Incorrect, { writeDecisionDesc(contestTwo, contestOne) }")
    elif decision == 'B':
        if contestTwo['follower_count'] > contestOne['follower_count']:
            print(f"Correct!!, { writeDecisionDesc(contestTwo, contestOne) }")
        else:
            print(f"Incorrect, { writeDecisionDesc(contestOne, contestTwo) }")
    else:
        print("Incorrect response, let's pass to another question!")
        
def writeDecisionDesc(contestWinner, contestLoser):
    return f"{contestWinner['name']} with {contestWinner['follower_count']}k has more followers than {contestLoser['name']} with {contestLoser['follower_count']}k!!"

def GetRandomContest():
    return random.choice(data)
        
def printVs(contestOne, contestTwo):
    print("Who has more followers!?")
    printContest(contestOne)
    print(vs)
    printContest(contestTwo)
    
def printContest(contest):
    print(f" {contest['name']}, from {contest['country']} is a {contest['description']}")

while gameState == 0:
    print(higherlower)
    contestOne = GetRandomContest()
    contestTwo = GetRandomContest()
    
    printVs(contestOne, contestTwo)
    
    decissionChecker(input("Decide who has more followers! A or B?"), contestOne, contestTwo)
    
    