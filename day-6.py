from day6helper import *

my_own_print("test")

# https://reeborg.ca/reeborg.html

# Basic example with loops

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

def move():
    print("moving!")
def turn_left():
    print("turning left!")

for n in range(0, 6):
    jump()
    
# or
n = 0

while n < 6:
    n += 1
    jump() 


# random jumps
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while at_goal() != "true":
    if front_is_clear():
        move()
    else:
        jump()

# random high jumps

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    move()
    turn_right()
    if wall_in_front():
        jump()
    else:
        move()
        turn_right()
        while wall_in_front() != "true":
            move()
        turn_left()

while at_goal() != "true":
    if front_is_clear():
        move()
    else:
        jump()


# final "lupita style"

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()