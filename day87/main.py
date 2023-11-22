import turtle

# Set up the screen
wn = turtle.Screen()
wn.title("Breakout")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

# Paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Ball
ball = turtle.Turtle()
ball.speed(40)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 3
ball.dy = -3

col_counter = 0

# Bricks
bricks = []

for y in range(6):
    for x in range(24):
        brick = turtle.Turtle()
        brick.speed(0)
        brick.shape("square")
        brick.color("blue")
        brick.penup()
        brick.goto(-250 + 25 * x, 200 - 20 * y)
        bricks.append(brick)

# Paddle movement
def move_paddle_left():
    x = paddle.xcor()
    x -= 20
    if x < -290:
        x = -290
    paddle.setx(x)

def move_paddle_right():
    x = paddle.xcor()
    x += 20
    if x > 290:
        x = 290
    paddle.setx(x)
    
def check_borders():
    if ball.xcor() > 290:
        ball.setx(290)
        ball.dx *= -1

    if ball.xcor() < -290:
        ball.setx(-290)
        ball.dx *= -1

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.goto(0, 0)
        ball.dy *= -1

# Keyboard bindings
wn.listen()
wn.onkeypress(move_paddle_left, "Left")
wn.onkeypress(move_paddle_right, "Right")

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    check_borders()

    # Paddle and ball collisions
    if abs(ball.xcor() - paddle.xcor()) < 25 and abs(ball.ycor() - paddle.ycor()) < 25 and col_counter == 0:
        ball.sety(ball.ycor() + ball.dy)
        ball.dy = 3
        col_counter = 10
        
    if col_counter > 0:
        col_counter-=1
        
    # Ball and brick collisions
    for brick in bricks:
        if brick.distance(ball) < 20:
            brick.goto(1000, 1000)  # Move the brick out of the screen
            ball.dy *= -1
            bricks.remove(brick)

    # Check for win
    if len(bricks) <= 0:
        wn.exitonclick()
        print("You win!")

# Keep the window open
wn.mainloop()
