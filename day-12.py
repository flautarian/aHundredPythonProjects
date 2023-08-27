
# Guessing number game !
import random

print("Welcome to the Number Guessing game!")
difficulty = input("Choose level, easy or hard?")
attempts = 10
if difficulty == "hard":
    attempts = 5
    
number_to_guess = random.randint(0,100)
print(f"NUMBER: {number_to_guess}")
game_state = 0
    
def checkResults(number_player, number_to_guess):
    # get global attempts value to change it in block
    global attempts
    # guess results consequences
    if number_player == number_to_guess:
        print(f"exactly, you nailed the number {number_player}!! YOU WON 😎!!")
        return 1
    else:
        attempts -= 1
        if attempts <= 0:
            print(f"No attempts left, you lose 😭, the number was {number_to_guess}")
            return -1
        else:
            if number_player > number_to_guess:
                print(f"{number_player} is too high, try a lesser number")
            else:
                print(f"{number_player} is too low, try a higher number")
    return 0

def checkGameState(game_state):
    if game_state > 0:
        print("exactly, you nailed the number!")
    else:
        print("no more attempts, you lost")

while game_state == 0:
    print(f"you have {attempts} to guess the number, try out!")
    number_player = input("Make a guess between 0 and 100: \n")
    game_state = checkResults(int(number_player), int(number_to_guess))