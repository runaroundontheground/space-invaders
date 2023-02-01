#Imported items
import math
import random
import time
import turtle
#variables go here

s = turtle.getscreen();
t = turtle.Turtle();
mx, my, mD = 0, 0, False;
gameState = "menu"; # can be "menu", "game", or "gameover"
sW, sH = 1000, 800;
s.setup(sW, sH);
big1 = "images/biggreen1.gif";
playerImg = "images/player.gif";
style = ["Press Start 2P", 14, 'normal'];
t.fillcolor("green");
t.pencolor("green");
turtle.register_shape(big1);
turtle.bgcolor("black");
t.speed(0);
t.penup();
t.hideturtle();










class object(object):
    def __init__(self, x = 0.0, y = 0.0, size = 1.0, color = "black", health = 1.0, shape = big1):
        self.x = x;
        self.y = y;
        self.xv = 0;
        self.yv = 0;
        self.size = size;
        self.color = color;
        self.health = health;
        self.shape = shape;
        
class player(object):
    def __init__(self, x = 0.0, y = 0.0, size = 1.0, color = "black", health = 1.0, shape = playerImg):
        super().__init__(x, y, size, color, health, shape);
        self.subClass = "player";
    #can't do size, can't do color (unless it's just a normal object)


enemies = [];
objects = [];
projectiles = [];
players = [];
players.append(player(25));
print(players[0].x);

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
    thing = False;


#input thingys
def onClick(x = 0, y = 0):
    global mx, my, gameState
    #mD = True;
    print(str(x) + ", " + str(y));
    if mx > -84 and mx < 19 and my > -72 and my < -50:
        print("start clicked");
        #gameState = "game";

def onRelease(x = 0, y = 0):
    #mD = False;
    print("mouse released");

def onDrag(x = 0, y = 0):
    pass


def mouseMove(event):
    global mx, my, sW, sH
    mx, my = event.x, event.y;
    print(mx - (sW / 2));
    

turtle.onscreenclick(onClick);
turtle.onrelease(onRelease);
turtle.ondrag(onDrag);

canvas = turtle.getcanvas();
canvas.bind("<Motion>", mouseMove);


#this is where we call things, don't assign values / functions below here

thing = True;
while gameState == "menu":
    drawMenu();

    


time.sleep(1);

while gameState == "game":
    testT = t
    testStyle = style
    testT.setpos(0, 0)
    testT.color("Blue")
    testT.write("Testing", font =testStyle)


#while gameState == "gameover":
#    overT = t
#    overStyle = style
#    overStyle[1] = 30
#    overT.setpos(-280, 230)
#    overT.color("red")
#    overT.write("GAME OVER", font = overStyle)










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
    border_pen.setpos(500,400)
    border_pen.pendown
    for side in range(4):
        border_pen.fd(1000)
        border_pen.lt(800)
    border_pen.hideturtle()

#defining player
player= turtle.Turtle
player.shape(playerImg)
player.speed(0)
player.penup
player.setpos(0,-350)
player.setheading(90)
playerSpeed = 10

#defining bullet
def bullet:
    bullet = turtle.Turtle
    bullet.shape("bullet.gif")
    bullet.speed(0)
    bullet.penup
    bullet.setpos(player.pos, -340)
    bullet.setheading(90)
    bulletSpeed = 20

#player movement
turtle.onkeypress("a")
while turtle.onkeypress("a") = true:
    player.setpos -= 10
    if player.position = -500:
        break

turtle.onkeypress("d")
while turtle.onkeypress("d") = true:
    player.setpos += 10
    if player.position = 500:
        break
turtle.onkeypress("space")
if turtle.onkeypress("space") = true:
    bullet

#defining small enemy
#some how need to spawn 16 of then in different locations
smallEnemy = turtle.Turtle
smallEnemy.shape("smallGuy.gif")
smallEnemy.speed(0)
smallEnemy.setpos("0,330")
smallEnemy.setheading(90)
smallEnemySpeed = 5

#defining big enemy
#some how need to spawn 8 of then in different locations
bigEnemy = turtle.Turtle
bigEnemy.shape(Big1)
bigEnemy.speed(0)
bigEnemy.setpos("0, 280")
bigEnemy.setheading(90)
bigEnemySpeed = 5


#defining motherShip
if num = 6:
    motherShip = turtle.Turtle
    motherShip.shape("mothership.gif")
    motherShip.speed(0)
    motherShip.setpos("-500, 390")
    motherShip.setheading(90)


"""

#game over
aaa = input("type things");
print(aaa);
#stuff
#s().bye();