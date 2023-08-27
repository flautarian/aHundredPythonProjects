# ----Student avg size----

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

average = 0

for student_height in student_heights:
  average += student_height

print(round(average/len(student_heights)))


# ----HighScore----

# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

highscore = -1

for score in student_scores:
    if score > highscore:
        highscore = score

print("The highest score in the class is: " + str(highscore))

# ----Adding even numbers----

#Write your code below this row 👇

limit = 100
summatory = 0
for n in range(0, limit+1):
    if n % 2 == 0:
        summatory += n

print(summatory)

# ----FizzBuzz----

#Write your code below this row 👇

limit = 100

for n in range(1, limit+1):
    word = str(n)
    if n % 3 == 0 or n % 5 == 0:
        word = ""
        if n % 3 == 0:
            word = word + "Fizz"
        if n % 5 == 0:
            word = word + "Buzz"
    print(word)


# ----Create a password generator----

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""

for sentinel in range(0, nr_letters + nr_symbols + nr_numbers):
    if sentinel < nr_letters:
        password += letters[random.randint(0, len(letters)-1)]
    elif sentinel < nr_letters + nr_symbols:
        password += symbols[random.randint(0, len(symbols)-1)]
    elif sentinel < nr_letters + nr_symbols + nr_numbers:
        password += numbers[random.randint(0, len(numbers)-1)]

print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

print("Hardest password: " + ''.join(random.sample(password,len(password))))