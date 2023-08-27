#Data Types

# String
stringNumber = "40"
print("stringNumber is " + str(type(stringNumber)))
print("string number:" + stringNumber)

# Integer
integerNumber = 35
print("integerNumber is " + str(type(integerNumber)))
print("integer number:" + str(integerNumber))

# Float
floatNumber = 3.141516
print("floatNumber is " + str(type(floatNumber)))
print("float number:" + str(floatNumber))

# Boolean
boolNumber = int(stringNumber) == 40
print("boolNumber is " + str(type(boolNumber)))
print("stringNumber is 40? -> " + str(boolNumber))


# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆
####################################
#Write your code below this line 👇
if len(two_digit_number) > 1:
    two_digit_number = two_digit_number
    first = int(two_digit_number[0])
    second = int(two_digit_number[1])
    result = first + second
    print(result)

""" PEMDAS
Parenthesis
Exponent
Multiplication 
or
Division
Addition
or
Substraction """

# ----BMI calc----

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = int(weight)/float(height)**2
print(int(bmi))

# ----Days left until 90 calc----

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
leftYears = 90 - int(age)
days = leftYears * 365
weeks = leftYears * 52
months = leftYears * 12
print("You have " + str(days) + " days, " + str(weeks) + " weeks, and " + str(months) + " months left.")


# ----Bill calc----

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator")
amount = input("What was the total bill?")
tipP = ""
while tipP not in  ["10","12","15"]:
    tipP = input("What percentage tip would yo like to give? 10, 12 or 15?")

persons = input("How many people to split the bill?")

payPerPerson = (float(amount) / int(persons)) * float("1." + tipP)

print("total amount per person: " + str(payPerPerson))
