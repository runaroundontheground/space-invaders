#Imported items
import math
import random
import time
import turtle
#variables go here
s = turtle.getscreen();
t = turtle.Turtle();
sW, sH = 1000, 800;
s.setup(sW, sH);



big1 = "images/biggreen1.gif";
style = ["Press Start 2P", 14, 'normal'];
t.fillcolor("green");
t.pencolor("green");
turtle.register_shape(big1);
turtle.bgcolor("black");
t.speed(0);
t.penup();
t.hideturtle();



gameState = "menu"; # can be "menu", "game", or "gameover"

class object:
    def __init__(self, x = 0.0, y = 0.0, size = 1.0, color = "black", health = 1.0):
        self.x = x;
        self.y = y;
        self.size = size;
        self.color = color;
        self.health = health;
    #can't do size, can't do color (unless it's just a normal object)


enemies = [];
destructibles = [];




t.setpos(-100, 100);
#menu things

def drawMenu():
    titleT = t;
    titleStyle = style;
    titleStyle[1] = 30;
    titleT.setpos(-280, 230);
    titleT.color("limegreen");
    titleT.write("SPACE INVADERS", font = titleStyle);
    start_pen = t
    start_pen.color("limegreen")
    start_pen.setposition(-80, -80)
    titleStyle[1] = 15;
    start_pen.write("START", font = titleStyle)
    exit_pen = t
    exit_pen.color("limegreen")
    exit_pen.setposition(-65, -160)
    titleStyle[1] = 15;
    exit_pen.write("EXIT", font = titleStyle)
        

#while gameState == "menu":
    #drawMenu();
drawMenu();
t.showturtle();
#canvas = turtle.getcanvas();
time.sleep(1);
while True:
    testingT = t;
    canvas = turtle.getcanvas();
    mouseX = canvas.winfo_pointerx();
    mouseY = canvas.winfo_pointery();
    testingT.setpos(int(mouseX - sW), int(-mouseY + (sH / 1.5)));
    #t.write("test", font = style);









"""
#actual game
while gameState == "game":
    t.shape(big1);
    time.sleep(0.01);
    t.write("Press Start", font = style);
    time.sleep(0.01);

def drawBorder():
    border_pen.color=("black")
    border_pen.pensize=(5)
    border_pen.speed=(0)
    border_pen.penup
    border_pen.setpos(700,650)
    border_pen.pendown
    for side in range(4):
        border_pen.fd(1400)
        border_pen.lt(1300)
    border_pen.hideturtle()


defining player
player= turtle.Turtle
player.shape("playerImage")
player.speed(0)
player.penup
player.setpos(0,-500)
player.setheading(90)
playerSpeed = 10

turtle.listen()
def playerMoveRight:
    fd(10)
screen.onkey(playerMoveRight, "d")

def playerMoveLeft:
    fd(-10)
screen.onkey(playerMoveLeft, "a")

    

defining small enemy
some how need to spawn 16 of then in different locations
smallEnemy = turtle.Turtle
smallEnemy.shape("smallGuy.gif")
smallEnemy.speed(0)
smallEnemy.setpos("-300 - 300, 500 - 300")
smallEnemy.setheading(90)
smallEnemySpeed = 5

defining big enemy
some how need to spawn 8 of then in different locations
bigEnemy = turtle.Turtle
bigEnemy.shape("BigGuy.gif")
bigEnemy.speed(0)
bigEnemy.setpos("-300 - 300, 200")
bigEnemy.setheading(90)
bigEnemySpeed = 5

"""

#game over
aaa = input("type things");
print(aaa);
#stuff
#s().bye();