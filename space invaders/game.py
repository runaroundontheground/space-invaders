#Imported items
import math
import random
import time
import pygame
#variables go here
Font = pygame.font.Font("PressStart2P.ttf", 64)

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

gameState = "menu"; # can be "menu", "game", or "gameover"
sW, sH = 800, 600;
screen = pygame.display.set_mode((sW, sH));








class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("images/player.png").convert();
        #self.surf.set_colorkey((255, 255, 255), RLEACCEL); whats this do
        self.rect = self.surf.get_rect();
        



    def update(self, Pkeys):
        if Pkeys[K_UP]:
            self.rect.move_ip(0, -5);
        if Pkeys[K_DOWN]:
            pass


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__();
        self.surf = pygame.image.load("images/big.png").convert();
        #thing above again, fixes something?


class BG(pygame.sprite.Sprite):
    def __init__(self):
        super(BG, self).__init__();
        self.surf = pygame.image.load("images/bg.png").convert();
        
        
           
pygame.mixer.init();
pygame.init();
clock = pygame.time.Clock();






#menu things

def menu():
    menu_text = Font.render("SPACE INVADERS", True, (0, 255, 255))
    screen.blit(menu_text, (190, 250))
    

while gameState == "menu":
    menu()

#input thingys
def onClick(x = 0, y = 0):
    global mx, my, gameState
    #mD = True;
    print(str(x) + ", " + str(y));
    if mx > -84 and mx < 19 and my > -72 and my < -50:
        print("start clicked");
        #gameState = "game";

def mouseMove(event):
    global mx, my, sW, sH
    mx, my = event.x, event.y;
    print(mx - (sW / 2));
    





#this is where we call things, don't assign values / functions below here




while gameState == "game":
    pass

#while gameState == "gameover":
#   pass










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