# paint calc

#Write your code below this line 👇
import math

def paint_calc(height, width, cover):
    result = math.ceil((height * width) / cover)
    print("You'll need " + str(result) + " cans of paint.")


#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

# prime number checker

#Write your code below this line 👇

def prime_checker(number):
    count = 0
    for n in range(1, number+1):
        if number % n == 0:
            count +=1
        if count > 2:
            print("It's not a prime number.")
            return
    print("It's a prime number.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)


# Caesar cipher
import string 


def translateText(plaintext, shift):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)
        
        

operation = ""
while operation not in ["E", "D", "encode", "encrypt", "decode", 'decrypt']:
    operation = input("type encode [E] to encrypt and decode [D] to decrypt")

phrase = input("Introduce the text to " + operation)

alteration = 0
if operation in ['decode', 'D', 'decrypt']:
    # decode things
    alteration = -3
else:
    #encode things
    alteration = 3
    
result = translateText(phrase, alteration)

print("Your text now is " + result)