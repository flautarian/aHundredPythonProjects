#Exception Handling

import os


script_dir = os.path.dirname(__file__)

try:
    
    # Try to load file
    file = open(f"{script_dir}/a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    
    # If file not found we create one and write something
    file = open(f"{script_dir}/a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    
    # if key error we notify about than
    print(f"The key {error_message} does not exist.")
else:
    
    # If try fails this will be called
    content = file.read()
    print(content)
finally:
    
    # Finally will ever execute at finals
    raise TypeError("This is an error that I made up.")

#BMI Example

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)