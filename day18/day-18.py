from turtle import Screen, Turtle
from random import randint
import colorgram

def forward_dashed(turtle, longitude):
    for _ in range(longitude):
        turtle.forward(10)
        turtle.penup()
        turtle.forward(10)
        turtle.pendown()

def draw_shape(sides, turtle):
    for _ in range(0, sides):
        turtle.color(["red", "yellow", "blue", "green"][_ % 4])
        forward_dashed(turtle, 5)
        turtle.left(360/sides)

def do_draw_polygon(turtle):
    sides = int(input("How many sides do you want to show? (min 3)"))
    draw_shape(sides, turtle)
        
def do_random_walk(iterations, turtle):
    for _ in range(0, iterations):
        meters = randint(1, 10)
        next_orientation = randint(0, 360)
        turtle.color(["red", "yellow", "blue", "green"][_ % 4])
        forward_dashed(turtle, meters)
        turtle.left(next_orientation)

def do_stylograph(turtle, iterations, size):
    turtle.position()
    turtle.speed("fastest")
    for _ in range(0, iterations):
        turtle.color(["red", "yellow", "blue", "green", "aquamarine"][_ % 5])
        turtle.circle(size)
        turtle.left(360/iterations)

def do_draw_hirst_painting(turtle):
    colors = colorgram.extract('C:/Users/fgiacconi/Documents/Documentación/Python100/day18/colors.jpg', 25)
    color = 0
    xAxis = -350
    yAxis = -300
    turtle.penup()
    for y in range(0, 15):
        for x in range(0, 15):
            turtle.color(colors[color % 25].rgb)
            color += 1
            
            turtle.setpos(xAxis, yAxis)
            turtle.dot(20)
            xAxis += 50
        yAxis += 50
        xAxis = -350
        

timmy = Turtle()
timmy.shape("turtle")
screen = Screen()
screen.colormode(255)

# poligon generator

# do_draw_polygon(timmy)

# Random walk
    
# do_random_walk(10, timmy)

# Stylogrpahic

# do_stylograph(timmy, 100, 150)

do_draw_hirst_painting(timmy)

screen.exitonclick()