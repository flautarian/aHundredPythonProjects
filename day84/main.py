import time
import turtle

# Function to draw the Tic Tac Toe grid
def draw_grid():
    turtle.speed(0)
    turtle.penup()
    turtle.goto(0, 150)
    turtle.pendown()
    for _ in range(4):
        turtle.forward(150)
        turtle.right(90)
        
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)
    
    for _ in range(4):
        turtle.forward(50)
        turtle.right(90)
    
    for _ in range(3):
        turtle.forward(150)
        turtle.right(90)
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(150)    
        turtle.left(180)
    
    turtle.penup()
    turtle.goto(0, 150)
    turtle.pendown()
    
    for _ in range(3):
        turtle.right(90)
        turtle.forward(150)
        turtle.left(90)
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(150)    
        turtle.right(90)
    
    turtle.write("Tic Tac Toe", align="center", font=("Arial", 24, "normal"))
    turtle.penup()
    turtle.goto(signal[0] * 50 + 25, signal[1] * 50 + 25)

# Function to draw an X at a specific position
def draw_x(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(15)
    for _ in range(4):
        turtle.forward(25)
        turtle.backward(25)
        turtle.left(90)
    turtle.setheading(0)
    turtle.penup()

# Function to draw an O at a specific position
def draw_o(x, y):
    turtle.penup()
    turtle.goto(x, y - 25)
    turtle.pendown()
    turtle.circle(25)
    turtle.penup()

# Create the game board
board = [[' ' for _ in range(3)] for _ in range(3)]
signal = [0, 2]

# Function to check if the game is over
def is_game_over():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return True
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return True
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return True
    return False

# Function to handle player's move
def play(x, y, player):
    if board[x][y] == ' ':
        if player == 'X':
            draw_x(x * 50 + 25, y * 50 + 25)
            board[x][y] = 'X'
        else:
            draw_o(x * 50 + 25, y * 50 + 25)
            board[x][y] = 'O'
        return True
    return False

def move_signal(x, y):
    global signal
    signal_aux = [signal[0], signal[1]]
    signal_aux[0] += x
    signal_aux[1] += y
    if all(x <= 2 and x >= 0 for x in signal_aux):
        signal = signal_aux
        
    print(signal)
    turtle.goto(signal[0] * 50 + 25, signal[1] * 50 + 25)
    
def move_up():
    move_signal(0, 1)
    
def move_down():
    move_signal(0, -1)
    
def move_left():
    move_signal(-1, 0)
    
def move_right():
    move_signal(1, 0)
    
def set_piece():
    global current_player
    row, col = int(signal[0]), int(signal[1])
    if 0 <= row < 3 and 0 <= col < 3:
        if play(row, col, current_player):
            current_player = 'O' if current_player == 'X' else 'X'

# Initialize the Turtle screen
draw_grid()

screen = turtle.Screen()
screen.setup(height=600, width=600)
screen.tracer(0)
screen.listen()
screen.colormode(255)

screen.listen()

screen.onkey(key="w", fun=move_up)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="s", fun=move_down)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="space", fun=set_piece)

# Main game loop
current_player = 'X'
while not is_game_over():
    screen.update()
    time.sleep(0.075)


screen.exitonclick()
turtle.done()
