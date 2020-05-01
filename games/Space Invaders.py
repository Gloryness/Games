# Modules I'm using
import turtle
import winsound
import math
import random
import time

################################################################################ Images
alienimage = 'R:/# Python 3.8/Python Saves/Games/Images/Alien.gif'
bulletimage = 'R:/# Python 3.8/Python Saves/Games/Images/Bullet.gif'
playerimage = 'R:/# Python 3.8/Python Saves/Games/Images/Rocket.gif'
bulletspeed = 'R:/# Python 3.8/Python Saves/Games/Images/BulletSpeed.gif'
rocketspeed = 'R:/# Python 3.8/Python Saves/Games/Images/PlayerSpeed.gif'
alien2image = 'R:/# Python 3.8/Python Saves/Games/Images/AlienSpeed.gif'
rewindtime = 'R:/# Python 3.8/Python Saves/Games/Images/RewindTime.gif'
oppositeimage = 'R:/# Python 3.8/Python Saves/Games/Images/Opposite.gif'
prestigeimage = 'R:/# Python 3.8/Python Saves/Games/Images/Prestige.gif'
tick = 'R:/# Python 3.8/Python Saves/Games/Images/Tick.gif'
tick2 = 'R:/# Python 3.8/Python Saves/Games/Images/Tick2.gif'
yes2 = 'R:/# Python 3.8/Python Saves/Games/Images/YesPic.gif'
no2 = 'R:/# Python 3.8/Python Saves/Games/Images/NoPic.gif'
################################################################################ Sound
powerup = 'R:/# Python 3.8/Python Saves/Games/Sound/Powerup.wav'
incorrect = 'R:/# Python 3.8/Python Saves/Games/Sound/Wrong.wav'
explosion = 'R:/# Python 3.8/Python Saves/Games/Sound/Explosion.wav'
laser = 'R:/# Python 3.8/Python Saves/Games/Sound/Laser.wav'
enemysound = 'R:/# Python 3.8/Python Saves/Games/Sound/Enemy.wav'

# Set up the screen
wn = turtle.Screen()
wn.title("Space Invaders by Glory! :)")
wn.bgcolor("black")
wn.bgpic('R:/# Python 3.8/Python Saves/Games/Images/background.gif')

# Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

# Score + Prestige
score = 0
coins = 0
prestige = 0

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("yellow")
pen.penup()
pen.hideturtle()
pen.goto(0, 320)
pen.write("Score: {}       Coins: {}".format(score, coins), align="center", font=("Cooper Black", 20, "normal"))

# Second Pen
second_pen = turtle.Turtle()
second_pen.speed(0)
second_pen.color("cyan")
second_pen.penup()
second_pen.hideturtle()
second_pen.goto(100, 370)
second_pen.write("Press R for shop", align="right", font=("Cooper Black", 18, "normal"))

# Third Pen
third_pen = turtle.Turtle()
third_pen.speed(0)
third_pen.color("red")
third_pen.penup()
third_pen.hideturtle()
third_pen.goto(0, -390)
third_pen.write("This game is currently in BETA. Please expect bugs to occur!", align="center", font=("Cooper Black", 20, "normal"))

# Create the player
player = turtle.Turtle()
wn.addshape(playerimage)
player.shape(playerimage)
player.shapesize(stretch_wid=1.5)
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)
playerspeed = 15 # Default Speed

# Choose the number of aliens
number_of_aliens = 10
# Creates an empty list of aliens
aliens = []
# Add enemies to the list
for i in range(number_of_aliens):
    # Creates the alien
    aliens.append(turtle.Turtle())

for alien in aliens:
    wn.addshape(alienimage)
    alien.shape(alienimage)
    alien.penup()
    alien.speed(0)
    x = random.randint(-200, 250)
    y = random.randint(100, 250)
    alien.setposition(x, y)
alienspeed = 5 # Default Speed

# Create the bullet
bullet = turtle.Turtle()
wn.addshape(bulletimage)
bullet.shape(bulletimage)
bullet.penup()
bullet.goto(1000, 1000)
bullet.speed(0)
bulletsspeed = 9 # Default Speed

# Move the player left + right - Functions
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = - 280
    player.setx(x)


def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = + 280
    player.setx(x)

def fire_bullet():
    bullet.showturtle()
    x = player.xcor()
    y = player.ycor()
    y += 40
    x += 0
    bullet.goto(x, y)
    winsound.PlaySound(laser, winsound.SND_ASYNC)


def isCollision(t1, t2): # Collision function (inaccurate)
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))  # LOL NO CRAP I HAD TO SEARCH THIS UP
    if distance < 62:
        return True
    else:
        return False

def alienpos(var, list): # Set aliens to a CERTAIN location
    var.showturtle()
    wn.tracer(0)
    list[0].setposition(227, 210)
    list[1].setposition(97, 158)
    list[2].setposition(190, 180)
    list[3].setposition(-175, 250)
    list[4].setposition(250, 140)
    list[5].setposition(-50, 205)
    list[6].setposition(160, 141)
    list[7].setposition(-125, 109)
    list[8].setposition(16, 210)
    list[9].setposition(54, 242)
    wn.tracer(1, 10)

############################################################################################
# Can now add onto this in functions
yespic = turtle.Turtle()
nopic = turtle.Turtle()
requirement_pen = turtle.Turtle()
confirm_pen = turtle.Turtle()
confirm_info_pen = turtle.Turtle()
second_confirm_info_pen = turtle.Turtle()
check = turtle.Turtle()
check2 = turtle.Turtle()
requirement = 100
presnum = 0
bulletnum = 18
lowbulletnum = 9
playernum = 30
lowplayernum = 15
timeplus = 110
alienstop = 0
aliennum = 5
scoreplus = 1
coinplus = 1
alienplus = 100
aliendefault = 1
timedefault = 1
oppositedefault = 1
############################################################################################

# Fourth Pen
fourth_pen = turtle.Turtle()
fourth_pen.speed(0)
fourth_pen.color("white")
fourth_pen.penup()
fourth_pen.hideturtle()
fourth_pen.goto(0, -330)
fourth_pen.write("Bullet Speed: {}   Player Speed: {}   Alien Speed: {}".format(bulletsspeed, playerspeed, alienspeed), align="center", font=("Cooper Black", 20, "normal"))

# Prestige Pen
prestige_pen = turtle.Turtle()
prestige_pen.speed(0)
prestige_pen.color("green")
prestige_pen.penup()
prestige_pen.hideturtle()
prestige_pen.goto(320, 370)
prestige_pen.write("Prestige: {}".format(prestige), align="right", font=("Cooper Black", 18, "normal"))

class Prestige:

    @staticmethod
    def prestigereset():
        global alien
        global prestige
        global requirement
        global score
        global coins
        global alienspeed
        global aliennum
        global bulletsspeed
        global playerspeed
        global coinplus
        global alienplus
        global aliendefault, timedefault, oppositedefault
        aliendefault = 1
        timedefault = 1
        oppositedefault = 1
        alienplus = 100
        alienspeed = 5
        aliennum = 5
        score = 0
        coins = 0
        requirement += 100
        coinplus += 1
        pen.clear()
        pen.write("Score: {}       Coins: {}".format(score, coins), align="center", font=("Cooper Black", 20, "normal"))
        fourth_pen.clear()
        fourth_pen.write("Bullet Speed: {}   Player Speed: {}   Alien Speed: {}".format(bulletsspeed, playerspeed, alienspeed), align="center", font=("Cooper Black", 20, "normal"))
        prestige += 1
        prestige_pen.clear()
        prestige_pen.write("Prestige: {}".format(prestige), align="right", font=("Cooper Black", 18, "normal"))

    @staticmethod
    def addone():
        global prestige
        global alienspeed
        global playerspeed
        global bulletsspeed
        global presnum
        global bulletnum
        global lowbulletnum
        global playernum
        global lowplayernum
        global timeplus
        bulletnum += 1
        lowbulletnum += 1
        playernum += 1
        lowplayernum += 1
        presnum += 1
        bulletsspeed = lowbulletnum
        playerspeed = lowplayernum
        timeplus += 5
        fourth_pen.clear()
        fourth_pen.write("Bullet Speed: {}   Player Speed: {}   Alien Speed: {}".format(bulletsspeed, playerspeed, alienspeed), align="center", font=("Cooper Black", 20, "normal"))


def button(x, y):
    global coins
    global bulletsspeed
    global playerspeed
    global alienspeed
    global alien
    global prestige
    global requirement
    global presnum
    global bulletnum
    global lowbulletnum
    global playernum
    global lowplayernum
    global timeplus
    global alienstop
    global aliennum
    global alienplus
    global aliendefault, timedefault, oppositedefault
    print(x, y)
    if x < -306 and x > -478 and y > 232 and y < 399: # Bullet Dupe
        if bulletsspeed == bulletnum:
            if prestige == presnum:
                if coins >= 100 or coins <= 100:
                    duplicate_pen = turtle.Turtle()
                    duplicate_pen.speed(0)
                    duplicate_pen.color("red")
                    duplicate_pen.penup()
                    duplicate_pen.hideturtle()
                    duplicate_pen.goto(0, 0)
                    duplicate_pen.write("Sorry, it seems you've\n   bought this already.", align="center", font=("Cooper Black", 25, "normal"))
                    winsound.PlaySound(incorrect, winsound.SND_ASYNC)
                    time.sleep(1)
                    duplicate_pen.clear()

    if x < -306 and x > -478 and y > 232 and y < 399: # Bullet Success
        if bulletsspeed == lowbulletnum:
            if prestige == presnum:
                if coins >= 100:
                    bulletsspeed = bulletnum
                    coins -= 100
                    alienplus -=100
                    if alienspeed < 0:
                        alienspeed += 1
                        aliennum += 1
                    if alienspeed > 0:
                        alienspeed -= 1
                        aliennum -= 1
                    fourth_pen.clear()
                    fourth_pen.write("Bullet Speed: {}   Player Speed: {}   Alien Speed: {}".format(bulletsspeed, playerspeed, alienspeed), align="center", font=("Cooper Black", 20, "normal"))
                    pen.clear()
                    pen.write("Score: {}       Coins: {}".format(score, coins), align="center", font=("Cooper Black", 20, "normal"))
                    success_pen = turtle.Turtle()
                    success_pen.speed(0)
                    success_pen.color("#64f57c")
                    success_pen.penup()
                    success_pen.hideturtle()
                    success_pen.goto(0, 0)
                    success_pen.write("You have successfully purchased\n      x2 Bullet Speed for 100 coins!", align="center", font=("Cooper Black", 25, "normal"))
                    winsound.PlaySound(powerup, winsound.SND_ASYNC)
                    time.sleep(2.5)
                    success_pen.clear()

    if x < -306 and x > -478 and y > 232 and y < 399: # Bullet Error
        if coins <= 99:
            if bulletsspeed == lowbulletnum:
                if prestige == presnum:
                    error_pen = turtle.Turtle()
                    error_pen.speed(0)
                    error_pen.color("red")
                    error_pen.penup()
                    error_pen.hideturtle()
                    error_pen.goto(0, 0)
                    error_pen.write("Sorry, the required coins\n            for this is 100.", align="center", font=("Cooper Black", 25, "normal"))
                    winsound.PlaySound(incorrect, winsound.SND_ASYNC)
                    time.sleep(1)
                    error_pen.clear()

    if x < -306 and x > -478 and y > 232 and y < 399 and bulletsspeed >= bulletnum: # Bullet Tick
        wn.addshape(tick)
        check.shape(tick)
        check.penup()
        wn.tracer(0)
        check.showturtle()
        check.goto(-300, 330)
        wn.tracer(1, 10) # ORIGINAL VALUE
        check.speed(0)

    if x < -306 and x > -478 and y > 59 and y < 222: # Player Dupe
        if playerspeed == playernum:
            if coins >= 200 or coins <= 199:
                if prestige == presnum:
                    duplicate_pen = turtle.Turtle()
                    duplicate_pen.speed(0)
                    duplicate_pen.color("red")
                    duplicate_pen.penup()
                    duplicate_pen.hideturtle()
                    duplicate_pen.goto(0, 0)
                    duplicate_pen.write("Sorry, it seems you've\n   bought this already.", align="center", font=("Cooper Black", 25, "normal"))
                    winsound.PlaySound(incorrect, winsound.SND_ASYNC)
                    time.sleep(1)
                    duplicate_pen.clear()

    if x < -306 and x > -478 and y > 59 and y < 222: # Player Error
        if coins <= 199:
            if playerspeed == lowplayernum:
                if prestige == presnum:
                    error_pen = turtle.Turtle()
                    error_pen.speed(0)
                    error_pen.color("red")
                    error_pen.penup()
                    error_pen.hideturtle()
                    error_pen.goto(0, 0)
                    error_pen.write("Sorry, the required coins\n            for this is 200.", align="center", font=("Cooper Black", 25, "normal"))
                    winsound.PlaySound(incorrect, winsound.SND_ASYNC)
                    time.sleep(1)
                    error_pen.clear()

    if x < -306 and x > -478 and y > 59 and y < 222: # Player Success
        if coins >= 200:
            if playerspeed == lowplayernum:
                if prestige == presnum:
                    playerspeed = playernum
                    coins -= 200
                    alienplus -= 200
                    if alienspeed < 0:
                        alienspeed += 2
                        aliennum += 2
                    if alienspeed > 0:
                        alienspeed -= 2
                        aliennum -= 2
                    fourth_pen.clear()
                    fourth_pen.write("Bullet Speed: {}   Player Speed: {}   Alien Speed: {}".format(bulletsspeed, playerspeed, alienspeed), align="center", font=("Cooper Black", 20, "normal"))
                    pen.clear()
                    pen.write("Score: {}       Coins: {}".format(score, coins), align="center", font=("Cooper Black", 20, "normal"))
                    success_pen = turtle.Turtle()
                    success_pen.speed(0)
                    success_pen.color("#64f57c")
                    success_pen.penup()
                    success_pen.hideturtle()
                    success_pen.goto(0, 0)
                    success_pen.write("You have successfully purchased\n      x2 Player Speed for 200 coins!", align="center", font=("Cooper Black", 25, "normal"))
                    winsound.PlaySound(powerup, winsound.SND_ASYNC)
                    time.sleep(2.5)
                    success_pen.clear()

    if x < -306 and x > -478 and y > 59 and y < 222 and playerspeed >= playernum: # Player Tick
        wn.addshape(tick2)
        check2.shape(tick2)
        check2.penup()
        wn.tracer(0)
        check2.showturtle()
        check2.goto(-300, 140)
        wn.tracer(1, 10) # ORIGINAL VALUE
        check2.speed(0)

    if x < -306 and x > -478 and y > -113 and y < 45 and coins <= 299: # Alien Error
        error_pen = turtle.Turtle()
        error_pen.speed(0)
        error_pen.color("red")
        error_pen.penup()
        error_pen.hideturtle()
        error_pen.goto(0, 0)
        error_pen.write("Sorry, the required coins\n            for this is 300.", align="center", font=("Cooper Black", 25, "normal"))
        winsound.PlaySound(incorrect, winsound.SND_ASYNC)
        time.sleep(1)
        error_pen.clear()

    if x < -306 and x > -478 and y > -113 and y < 45 and coins >= 300: # Alien Success
        alienspeed *= 2
        aliennum *= 2
        coins -= 300
        alienplus -= 300
        if alienspeed < 0:
            alienspeed += 3
            aliennum += 3
        if alienspeed > 0:
            alienspeed -= 3
            aliennum -= 3
        fourth_pen.clear()
        fourth_pen.write("Bullet Speed: {}   Player Speed: {}   Alien Speed: {}".format(bulletsspeed, playerspeed, alienspeed), align="center", font=("Cooper Black", 20, "normal"))
        pen.clear()
        pen.write("Score: {}       Coins: {}".format(score, coins), align="center", font=("Cooper Black", 20, "normal"))
        winsound.PlaySound(powerup, winsound.SND_ASYNC)
        if aliendefault == 1:
            success_pen = turtle.Turtle()
            success_pen.speed(0)
            success_pen.color("#64f57c")
            success_pen.penup()
            success_pen.hideturtle()
            success_pen.goto(0, 0)
            success_pen.write("You have successfully purchased\n        x2 Alien Speed for 300 coins!\n                 [STACKABLE]", align="center", font=("Cooper Black", 25, "normal"))
            time.sleep(2.5)
            success_pen.clear()
            aliendefault += 1

    if coins < 0: # Makes sure its never a negative number
        coins = 0
        pen.clear()
        pen.write("Score: {}       Coins: {}".format(score, coins), align="center", font=("Cooper Black", 20, "normal"))

    if x > 310 and x < 468 and y > 194 and y < 350: # Time Error
        if coins <= 99:
            error_pen = turtle.Turtle()
            error_pen.speed(0)
            error_pen.color("red")
            error_pen.penup()
            error_pen.hideturtle()
            error_pen.goto(0, 0)
            error_pen.write("Sorry, the required coins\n            for this is 100.", align="center", font=("Cooper Black", 25, "normal"))
            winsound.PlaySound(incorrect, winsound.SND_ASYNC)
            time.sleep(1)
            error_pen.clear()

    if x > 310 and x < 468 and y > 194 and y < 350: # Time Success
        if coins >= 100:
            if prestige == presnum:
                for alien in aliens:
                    x2 = random.randint(-200, 250)
                    y2 = random.randint(timeplus, 270)
                    alien.setposition(x2, y2)
                coins -= 100
                alienplus -= 100
                if alienspeed < 0:
                    alienspeed += 1
                    aliennum += 1
                if alienspeed > 0:
                    alienspeed -= 1
                    aliennum -= 1
                pen.clear()
                pen.write("Score: {}       Coins: {}".format(score, coins), align="center", font=("Cooper Black", 20, "normal"))
                winsound.PlaySound(powerup, winsound.SND_ASYNC)
                if timedefault == 1:
                    success_pen = turtle.Turtle()
                    success_pen.speed(0)
                    success_pen.color("#64f57c")
                    success_pen.penup()
                    success_pen.hideturtle()
                    success_pen.goto(0, 0)
                    success_pen.write("You have successfully purchased\n          a REWIND for 100 coins!\n                     [INFINITE]", align="center", font=("Cooper Black", 25, "normal"))
                    time.sleep(2.5)
                    success_pen.clear()
                    timedefault += 1

    if x > 310 and x < 468 and y > 14 and y < 172: # Opposite Error
        if coins <= 99:
            error_pen = turtle.Turtle()
            error_pen.speed(0)
            error_pen.color("red")
            error_pen.penup()
            error_pen.hideturtle()
            error_pen.goto(0, 0)
            error_pen.write("Sorry, the required coins\n            for this is 100.", align="center", font=("Cooper Black", 25, "normal"))
            winsound.PlaySound(incorrect, winsound.SND_ASYNC)
            time.sleep(1)
            error_pen.clear()

    if x > 310 and x < 468 and y > 14 and y < 172: # Opposite Success
        if coins >= 100:
            if prestige == presnum:
                coins -= 100
                alienspeed *= -1
                aliennum *= -1
                alienplus -= 100
                if alienspeed < 0:
                    alienspeed += 1
                    aliennum += 1
                if alienspeed > 0:
                    alienspeed -= 1
                    aliennum -= 1
                pen.clear()
                pen.write("Score: {}       Coins: {}".format(score, coins), align="center", font=("Cooper Black", 20, "normal"))
                winsound.PlaySound(powerup, winsound.SND_ASYNC)
                if oppositedefault == 1:
                    success_pen = turtle.Turtle()
                    success_pen.speed(0)
                    success_pen.color("#64f57c")
                    success_pen.penup()
                    success_pen.hideturtle()
                    success_pen.goto(0, 0)
                    success_pen.write("   You have successfully purchased\n          an OPPOSITE DIRECTION\n                    for 100 coins!\n                      [INFINITE]", align="center", font=("Cooper Black", 25, "normal"))
                    time.sleep(2.5)
                    success_pen.clear()
                    oppositedefault += 1


    if x > -464 and x < -317 and y > -185 and y < -145: # Prestige Start On Click
        for alien in aliens:
            alien.hideturtle()
            alienspeed = alienstop
        # Yes
        wn.addshape(yes2)
        yespic.shape(yes2)
        yespic.showturtle()
        yespic.penup()
        wn.tracer(0)
        yespic.goto(-120, 0)
        yespic.speed(0)
        wn.tracer(1, 10)
        # No
        wn.addshape(no2)
        nopic.shape(no2)
        nopic.showturtle()
        nopic.penup()
        wn.tracer(0)
        nopic.goto(120, 0)
        nopic.speed(0)
        wn.tracer(1, 10)
        # Are You Sure Pen
        confirm_pen.speed(0)
        confirm_pen.color("red")
        confirm_pen.penup()
        confirm_pen.hideturtle()
        confirm_pen.goto(0, 60)
        confirm_pen.write("Are you sure?", align="center", font=("Cooper Black", 24, "normal"))
        # Requirement Pen
        requirement_pen.speed(0)
        requirement_pen.color("orange")
        requirement_pen.penup()
        requirement_pen.hideturtle()
        requirement_pen.goto(0, 110)
        requirement_pen.write("REQ: {} coins".format(requirement), align="center", font=("Cooper Black", 24, "normal"))
        # Information Pen
        confirm_info_pen.speed(0)
        confirm_info_pen.color("red")
        confirm_info_pen.penup()
        confirm_info_pen.hideturtle()
        confirm_info_pen.goto(0, -80)
        confirm_info_pen.write("This will reset stats, purchases and coins!", align="center", font=("Cooper Black", 18, "normal"))
        # Second Information Pen
        second_confirm_info_pen.speed(0)
        second_confirm_info_pen.color("orange")
        second_confirm_info_pen.penup()
        second_confirm_info_pen.hideturtle()
        second_confirm_info_pen.goto(0, -190)
        second_confirm_info_pen.write("   +1 to your bulletspeed and the playerspeed.  \n             Will also make REWIND TIME\n                    more powerful by 4%.\n   For every prestige, +1 more coin every kill.", align="center", font=("Cooper Black", 18, "normal"))

    if x > 53 and x < 187 and y > -39 and y < 43: # Prestige NO Option
        if yespic.isvisible():
            yespic.hideturtle()
            nopic.hideturtle()
            requirement_pen.clear()
            confirm_pen.clear()
            confirm_info_pen.clear()
            second_confirm_info_pen.clear()
            for alien in aliens:
                alien.showturtle()
                alienspeed = aliennum

    if x > -190 and x < -53 and y > -48 and y < 48: # Prestige YES Option
        if coins >= requirement:
            if yespic.isvisible():
                Pres = Prestige()
                Pres.prestigereset() # Referring to 1 of the objects in the class 'Prestige'
                Pres.addone() # Referring to 1 of the objects in the class 'Prestige'
                yespic.hideturtle()
                nopic.hideturtle()
                check.hideturtle()
                check2.hideturtle()
                requirement_pen.clear()
                confirm_pen.clear()
                confirm_info_pen.clear()
                second_confirm_info_pen.clear()
                for alien in aliens:
                    alien.showturtle()
                    xa = random.randint(-200, 250)
                    ya = random.randint(100, 250)
                    alien.setposition(xa, ya)

    if x > -190 and x < -53 and y > -48 and y < 48: # Prestige YES Option
        if coins < requirement:
            if yespic.isvisible():
                yespic.hideturtle()
                nopic.hideturtle()
                check.hideturtle()
                check2.hideturtle()
                requirement_pen.clear()
                confirm_pen.clear()
                confirm_info_pen.clear()
                second_confirm_info_pen.clear()
                error_pen = turtle.Turtle()
                error_pen.speed(0)
                error_pen.color("red")
                error_pen.penup()
                error_pen.hideturtle()
                error_pen.goto(0, 0)
                error_pen.write("Cannot prestige. You do not have {} coins.".format(requirement), align="center", font=("Cooper Black", 20, "normal"))
                winsound.PlaySound(incorrect, winsound.SND_ASYNC)
                time.sleep(2)
                error_pen.clear()
                for alien in aliens:
                    alien.showturtle()
                    alienspeed = aliennum

def shop():
    global alienspeed
    global alienstop
    global aliennum
    global bulletsspeed
    global playerspeed
    while True:  # Pause the aliens from moving for a little
        alienspeed = alienstop
        break  # If it wont break then it'll just crash the program
    second_pen.clear()
    prestige_pen.clear()
    prestige_pen.speed(0)
    prestige_pen.color("green")
    prestige_pen.penup()
    prestige_pen.hideturtle()
    prestige_pen.goto(60, 370)
    prestige_pen.write("Prestige: {}".format(prestige), align="right", font=("Cooper Black", 18, "normal"))
    # Clearing the screen and creating are new one.
    shop_win = turtle.Screen()
    shop_win.title("Space Invaders by Glory! :)")
    shop_win.bgcolor("black")
    shop_win.setup()
    # Setting up the x2 bullet
    bullet2 = turtle.Turtle()
    shop_win.addshape(bulletspeed)
    bullet2.shape(bulletspeed)
    bullet2.penup()
    bullet2.setposition(-390, 315)
    bullet2.speed(0)
    # Setting up the x2 Player speed
    rocket = turtle.Turtle()
    shop_win.addshape(rocketspeed)
    rocket.shape(rocketspeed)
    rocket.penup()
    rocket.setposition(-390, 140)
    rocket.speed(0)
    # Setting up the x2 alien speed
    alien2 = turtle.Turtle()
    shop_win.addshape(alien2image)
    alien2.shape(alien2image)
    alien2.penup()
    alien2.setposition(-390, -35)
    alien2.speed(0)
    # Setting up prestige
    prestige2 = turtle.Turtle()
    shop_win.addshape(prestigeimage)
    prestige2.shape(prestigeimage)
    prestige2.penup()
    prestige2.setposition(-390, -165)
    prestige2.speed(0)
    # Setting up the Rewind Time
    rewind = turtle.Turtle()
    shop_win.addshape(rewindtime)
    rewind.shape(rewindtime)
    rewind.penup()
    rewind.setposition(392, 270)
    rewind.speed(0)
    # Setting up Opposite Direction
    opposite = turtle.Turtle()
    shop_win.addshape(oppositeimage)
    opposite.shape(oppositeimage)
    opposite.penup()
    opposite.setposition(392, 90)
    opposite.speed(0)
    # Making sure all these are cleared
    yespic.hideturtle()
    nopic.hideturtle()
    check.hideturtle()
    check2.hideturtle()
    requirement_pen.clear()
    confirm_pen.clear()
    confirm_info_pen.clear()
    second_confirm_info_pen.clear()
    # Changing the alien speed back to normal
    alienspeed = aliennum
    # Listening for click
    shop_win.onscreenclick(button, 1)
    shop_win.listen()

# Keyboard bindings
wn.listen()
wn.onkeypress(move_left, "a")
wn.onkeypress(move_right, "d")
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")
wn.onkeypress(fire_bullet, "space")
wn.onkeypress(shop, "r")

# Main game loop
while True:

    if coins < 0: # Makes sure its never a negative number
        coins = 0
        pen.clear()
        pen.write("Score: {}       Coins: {}".format(score, coins), align="center", font=("Cooper Black", 20, "normal"))

    for alien in aliens:
        # Move the enemy
        x = alien.xcor()
        x += alienspeed
        alien.setx(x)

        # Move the enemy back and down
        if alien.xcor() > 260:
            # Move all enemies down
            for e in aliens:
                y = e.ycor()
                y -= 40
                e.sety(y)
            # Change enemy direction
            alienspeed *= -1
            aliennum *= -1
            fourth_pen.clear()
            fourth_pen.write("Bullet Speed: {}   Player Speed: {}   Alien Speed: {}".format(bulletsspeed, playerspeed, alienspeed), align="center", font=("Cooper Black", 20, "normal"))

        if alien.xcor() < -260:
            # Move all enemies down
            for e in aliens:
                y = e.ycor()
                y -= 40
                e.sety(y)
            # Change enemy direction
            alienspeed *= -1
            aliennum *= -1
            fourth_pen.clear()
            fourth_pen.write("Bullet Speed: {}   Player Speed: {}   Alien Speed: {}".format(bulletsspeed, playerspeed, alienspeed), align="center", font=("Cooper Black", 20, "normal"))

        # Detect the bullet
        if isCollision(bullet, alien):
            bullet.hideturtle()
            winsound.PlaySound(enemysound, winsound.SND_ASYNC)
            # Reset the enemy
            alien.hideturtle()
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            alien.showturtle()
            alien.setposition(x, y)
            bullet.showturtle()
            score += scoreplus
            coins += coinplus
            pen.clear()
            pen.write("Score: {}       Coins: {}".format(score, coins), align="center", font=("Cooper Black", 20, "normal"))
            # Move the bullet
        else:
            b = bullet.ycor()
            b += bulletsspeed  # 9 is the starter bullet speed
            bullet.sety(b)

        if score >= alienplus:
            if alienspeed < 0:
                alienspeed -= 1
                aliennum -= 1
            if alienspeed > 0:
                alienspeed += 1
                aliennum += 1
            fourth_pen.clear()
            fourth_pen.write("Bullet Speed: {}   Player Speed: {}   Alien Speed: {}".format(bulletsspeed, playerspeed, alienspeed), align="center", font=("Cooper Black", 20, "normal"))

        if score >= alienplus:
            alienplus += 100

        # Check to see if the bullet has gone to the top
        if bullet.ycor() > 275:
            bullet.hideturtle()

        if isCollision(player, alien) or alien.ycor() < -250: # Game over function
            player.hideturtle()
            for alien in aliens:
                alien.hideturtle()
                alienspeed = alienstop
            winsound.PlaySound(explosion, winsound.SND_ASYNC)
            countdown = 5
            game_over_pen = turtle.Turtle()
            game_over_pen.speed(0)
            game_over_pen.penup()
            game_over_pen.color("red")
            game_over_pen.hideturtle()
            game_over_pen.goto(0, 50)
            game_over_pen.write("GAME OVER! Restarting in {}".format(countdown), align="center", font=("Cooper Black", 20, "normal"))
            for i in range(5): # Does this 5 times
                time.sleep(1)
                countdown -= 1
                game_over_pen.clear()
                game_over_pen.write("GAME OVER! Restarting in {}".format(countdown), align="center", font=("Cooper Black", 20, "normal"))
            game_over_pen.clear()
            if countdown == 0:
                for alien in aliens:
                    alien.showturtle()
                    xaa = random.randint(-200, 250)
                    yaa = random.randint(100, 250)
                    alien.setposition(xaa, yaa)
                    player.showturtle()
                    aliennum = 5
                    score = 0
                    coins = 0
                    alienspeed = aliennum
                    bulletsspeed = lowbulletnum
                    playerspeed = lowplayernum
                    check.hideturtle()
                    check2.hideturtle()
                    fourth_pen.clear()
                    fourth_pen.write("Bullet Speed: {}   Player Speed: {}   Alien Speed: {}".format(bulletsspeed, playerspeed, alienspeed), align="center", font=("Cooper Black", 20, "normal"))
                    pen.clear()
                    pen.write("Score: {}       Coins: {}".format(score, coins), align="center", font=("Cooper Black", 20, "normal"))

wn.mainloop()