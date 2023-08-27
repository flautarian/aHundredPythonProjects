""" from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape('turtle')
timmy.color("coral")
timmy.forward(100)

print(timmy)

my_screen = Screen()

print(my_screen.canvheight)

my_screen.exitonclick() """


from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon name", ["PK1", "PK2"])
table.attributes

print(table)