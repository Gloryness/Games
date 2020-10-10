import turtle
import winsound
import random
colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow", "white"]
filename = 'assets/sound/PongSnakeSound.wav'


"""
<------>
ACROSS = X
UP AND DOWN = Y
x, y for position
350 for right and -350 for left
"""

wn = turtle.Screen() # This will make the screen and make sure the s is capitalized in Screen()
wn.title("Pong by Glory :)") # Creates the title in the top of the screen
wn.bgcolor("black") # Sets the background color for the screen
wn.setup(width=800, height=600) # Sets the height + width for the screen
wn.tracer(0) # stops the window from updating - speeds up the game a bit.

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle() # turtle.Turtle - turtle for module name and Turtle for class name.
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0) # vertically centered

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1 # every time ball moves it moves by 2 pixels
ball.dy = 0.1

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Cooper Black", 24, "normal"))

# Second Pen
pen_a = turtle.Turtle()
pen_a.speed(0)
pen_a.color("white")
pen_a.penup()
pen_a.hideturtle()
pen_a.goto(0, -260)
pen_a.write("Press R to make ball change colour!", align="center", font=("Cooper Black", 14, "normal"))

# Function
def paddle_a_up():
    y = paddle_a.ycor() # returns the y cordinate
    y += 20 # add 20 pixels to the y cordinate
    paddle_a.sety(y)
    if y > 240:
        y = 240
        paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor() # returns the y cordinate
    y -= 20 # removes 20 pixels to the y cordinate
    paddle_a.sety(y)
    if y < -230:
        y = -230
        paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor() # returns the y cordinate
    y += 20 # removes 20 pixels to the y cordinate
    paddle_b.sety(y)
    if y > 240:
        y = 240
        paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor() # returns the y cordinate
    y -= 20 # removes 20 pixels to the y cordinate
    paddle_b.sety(y)
    if y < -230:
        y = -230
        paddle_b.sety(y)

def changeballcolour():
    color = random.choice(colors)
    ball.color(color)


# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_a_up, "a")
wn.onkeypress(paddle_a_down, "d")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
wn.onkeypress(paddle_b_up, "Left")
wn.onkeypress(paddle_b_down, "Right")
wn.onkeypress(changeballcolour, "r")


# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound(filename, winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound(filename, winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        winsound.PlaySound('assets/sound/PongSound.wav', winsound.SND_ASYNC)
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Cooper Black", 24, "normal"))
        if score_a > 1:
            ball.goto(0, 0)
            ball.dx += 0.1
            ball.dy += 0.1
            ball.setx(ball.xcor() + ball.dx)
            ball.sety(ball.ycor() + ball.dy)

        elif score_a > 2:
            ball.goto(0, 0)
            ball.dx += 0.1
            ball.dy += 0.1
            ball.setx(ball.xcor() + ball.dx)
            ball.sety(ball.ycor() + ball.dy)

        elif score_a > 3:
            ball.goto(0, 0)
            ball.dx += 0.1
            ball.dy += 0.1
            ball.setx(ball.xcor() + ball.dx)
            ball.sety(ball.ycor() + ball.dy)

        elif score_a > 4:
            ball.goto(0, 0)
            ball.dx += 0.1
            ball.dy += 0.1
            ball.setx(ball.xcor() + ball.dx)
            ball.sety(ball.ycor() + ball.dy)

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        winsound.PlaySound('assets/sound/PongSound.wav', winsound.SND_ASYNC)
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Cooper Black", 24, "normal"))
        if score_b > 1:
            ball.goto(0, 0)
            ball.dx += 0.1
            ball.dy += 0.1
            ball.setx(ball.xcor() + ball.dx)
            ball.sety(ball.ycor() + ball.dy)

        elif score_b > 2:
            ball.goto(0, 0)
            ball.dx += 0.1
            ball.dy += 0.1
            ball.setx(ball.xcor() + ball.dx)
            ball.sety(ball.ycor() + ball.dy)

        elif score_b > 3:
            ball.goto(0, 0)
            ball.dx += 0.1
            ball.dy += 0.1
            ball.setx(ball.xcor() + ball.dx)
            ball.sety(ball.ycor() + ball.dy)

        elif score_b > 4:
            ball.goto(0, 0)
            ball.dx += 0.1
            ball.dy += 0.1
            ball.setx(ball.xcor() + ball.dx)
            ball.sety(ball.ycor() + ball.dy)



    # Paddle and ball collision
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound(filename, winsound.SND_ASYNC)

    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound(filename, winsound.SND_ASYNC)