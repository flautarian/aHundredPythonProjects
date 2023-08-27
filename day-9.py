# Stundents qualitfier system

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

# Create an empty dictionary called student_grades.
student_grades = {}

# Write your code below to add the grades to student_grades.👇
for key in student_scores:
    result = "Outstanding"
    if student_scores[key] <= 70:
        result = "Fail"
    elif student_scores[key] <= 80:
        result = "Acceptable"
    elif student_scores[key] <= 90:
        result = "Exceeds Expectations"
        
    student_grades[key] = result
    
# 🚨 Don't change the code below 👇
print(student_grades)

# Nested dictionaries and lists

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(name, length, list):
    newTravel = {
        "country": name,
        "visits": length,
        "cities": list
    }
    travel_log.append(newTravel)



#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

# Blind auction system

from art import hammer
print(hammer)

def createAuction(dictionary):
    name = input("What's your name?\n")
    bid = int(input("What's your bid?\n"))
    if dictionary["bestBid"] < bid:
        dictionary["bestBid"] = bid
        dictionary["bestPlayer"] = name
    # question to set another bid
    repeatQuestion = input("Is there another bid to declare? [y, n]\n")
    if(repeatQuestion == 'y'):
        dictionary = createAuction(dictionary)
    return dictionary
    
    
result = {"bestBid": 0, "bestPlayer" : "nobody"}
print(str(result))
result = createAuction(result)
print(str(result))
print("the audion has ended, the winner is " + result["bestPlayer"] + " by " + str(result["bestBid"]) + "$")