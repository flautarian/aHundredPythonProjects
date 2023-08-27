import subprocess, platform, re, emoji
from random_word import RandomWords

stages = ['''
  +---+
  |   |
 🥶   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
 😨   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
 🙄   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
 🤨   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
 😗   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
 🙂   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

def clearScreen():
    if platform.system()=="Windows":
        if platform.release() in {"10", "11"}:
            subprocess.run("", shell=True) #Needed to fix a bug regarding Windows 10; not sure about Windows 11
            print("\033c", end="")
        else:
            subprocess.run(["cls"])
    else: #Linux and Mac
        print("\033c", end="")
        

def unlockLetter(letter, phrase, obfuscatedPhrase):
    newPhrase = ""
    for l in range(0, len(phrase)):
        if obfuscatedPhrase[l] != "_":
            newPhrase += obfuscatedPhrase[l]
        elif phrase[l] == letter:
            newPhrase += phrase[l]
        else:
            newPhrase += "_"
    return newPhrase
        
# Generating a random word

r = RandomWords()

patternWord = r'^[a-zA-Z]$'
wordToGuess = r.get_random_word()
wordGuessed = ""

# Create obfuscated word
for l in range(0, len(wordToGuess)):
    wordGuessed += "_"
    
print("We will try to get " + wordToGuess)

gameStatus = 0
alreadySaidLetters = ""
lives = 6

while gameStatus == 0:
    print(emoji.emojize(stages[lives]))
    print(wordGuessed)
    letter = input("Guess the word!")
    if re.match(patternWord, letter):
        # check if already said letter
        if alreadySaidLetters.find(letter) != -1:
            print("Already said letter, try another!")
        else:    
            alreadySaidLetters += letter
            # check if word in phrase
            if wordToGuess.find(letter) != -1:
                print("Good one!!" + emoji.emojize(":winking_face:"))
                wordGuessed = unlockLetter(letter, wordToGuess, wordGuessed)
            else:
                print("What a shame!! not a good word, -1 lives")
                lives -= 1
                
            # check if game end
            if wordGuessed.find("_") == -1:
                gameStatus = 1
            elif lives <= 0:
                gameStatus = -1
    else:
        print("Invalid character.... Try again!")
        
if gameStatus > 0:
    print("CONGRATULATIONS!!!, the word was " + wordGuessed + "!!!! 🥳")
else:
    print(emoji.emojize(stages[lives]))
    print("Game lost.... the prase was " + wordToGuess + " 😭")
    
