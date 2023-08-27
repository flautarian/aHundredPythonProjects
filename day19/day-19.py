from turtle import Turtle, Screen
from random import randint

timmy = Turtle()
timmy.shape("turtle")
screen = Screen()

def move_forward():
    timmy.forward(25)
    
def move_up():
    reset_orientation()
    timmy.left(90)
    move_forward()
    
def move_down():
    reset_orientation()
    timmy.right(90)
    move_forward()
    
def move_left():
    reset_orientation()
    timmy.left(180)
    move_forward()
    
def move_right():
    reset_orientation()
    move_forward()

def clear_screen():
    timmy.setpos(0, 0)
    reset_orientation()
    timmy.clear()
    
def reset_orientation():
    timmy.setheading(0)
    
screen.listen()
# Etch a Scketch
""" timmy.speed(0)
screen.onkey(key="w", fun=move_up)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="s", fun=move_down)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear_screen) """

# Turtle race!

def random_forward():
    global whoWon
    if whoWon < 0:
        for turtle in turtles:
            turtle.forward(randint(1, 25))
            if turtle.pos()[0] > 295 :
                whoWon = turtles.index(turtle)
                turtle.color("gold")
        
turtles = [Turtle(), Turtle(), Turtle(), Turtle(), Turtle()]
timmy.color("white")
whoWon = -1
posY = 300

for turtle in turtles:
    turtle.color(["red", "orange", "blue", "green", "aquamarine"][turtles.index(turtle) % 5])
    turtle.shape("turtle")
    turtle.penup()
    turtle.setpos(-350, posY)
    turtle.pendown()
    posY -= 150


screen.onkey(key="space", fun=random_forward)

timmy.shape("turtle")

screen.exitonclick()