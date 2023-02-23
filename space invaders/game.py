#Imported items
import math
import random
import time
import pygame
import os
import threading
#variables go here
from threading import Thread
pygame.font.init();
pygame.mixer.init();
pygame.init();



#debugRect = pygame.Rect(); this'll do something later

#from pygame.locals import (
#K_UP,
##K_DOWN,
#K_LEFT,
#K_RIGHT,
#K_ESCAPE,
#K##_SPACE,
#K_T,
#KEYDOWN,
#QUIT
#)

# this checks for the path to use with stuff cuz it was wierd at my house
if os.path.exists("D:/programming stuff/space invaders"):
    hP = "D:/programming stuff/space invaders/";
else:
    hP = "";

# get which path to use cuz programming at home is diff
clock = pygame.time.Clock();
font = pygame.font.Font(hP + "fonts/PressStart2P-Regular.ttf", 32);
def numbererer(text):
    tempthing = font.render(text, False, (0, 255, 0));
    tempthing = pygame.transform.scale(tempthing, (font.size(text)[0] / 2, font.size(text)[1] / 2))
    return tempthing;

num = [
    numbererer("0"),
    numbererer("1"),
    numbererer("2"),
    numbererer("3"),
    numbererer("4"),
    numbererer("5"),
    numbererer("6"),
    numbererer("7"),
    numbererer("8"),
    numbererer("9"),
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9"
];


def randnum(s = 1, e = 15):
    return random.randint(s, e);

#Colors
RED = (255, 0, 0)
ORANGE = (255, 120, 0);
GREEN = (0, 255, 0)
DARK_GREEN = (1, 50, 32)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SPACE_BLUE = (31, 66, 119)
BGCOLOR = BLACK
STARCOLOR = WHITE
fps = 60;
gameState = "menu"; # can be "menu", "game", or "gameover"

sW, sH = 800, 600;
screen = pygame.display.set_mode((sW, sH));
mouseD = False;
mx, my = 0, 0;
opmode = False;
updatingLvl = False;

projectiles = [];
players = []; # multiplayer, if we have time
enemies = [];
text = [];

class camera:
    def __init__(this):
        this.shakeX = 0;
        this.shakeY = 0;
        this.shakeTime = 0;
        this.shakeStr = 5;
c = camera();

PLAYERSHIP = [pygame.image.load(hP + "images/player.png")];
PLRBULLET = [pygame.image.load(hP + "images/player bullet.png")];
ALIEN1 = [pygame.image.load(hP + "images/alien1-1.png"), pygame.image.load(hP + "images/alien1-2.png")];
#ALIEN2 = pygame.image.load(os.path.join("images", "alien2.png"))
ALIENDIE = pygame.image.load(hP + "images/alien death.png");
MOTHERSHIP = [pygame.image.load(hP + "images/mothership1-1.png"), pygame.image.load(hP + "images/mothership1-2.png")];
MOTHERSHIPDIE = pygame.image.load(hP + "images/mothership die.png");
TESTIMG = [pygame.image.load(hP + "images/test.png")];
PLAYERDIE = pygame.image.load(hP + "images/player die1-1.png")
BLANK = [pygame.image.load(hP + "images/blank.png")];


spd = sW / 600; #speed for player
mxspd = sW / 200; #player max speed
bspd = 10; #projectile speed
espd = 3; #enemy speed
maxBullets = 1;
lvl = 1;
score = 0;

# star thingys
STARX = 400
STARY = 300
# reserved for STARX random.randint(10, sW-10)
# reserver for STARY random.randint(10, sH-10)
STAR = pygame.Rect(STARX, STARY, 100, 100)
def star():
    pygame.draw.rect(screen, STARCOLOR, STAR)
    
star();


class obj:
    
    def __init__(this, x = sW / 2, y = sH / 2, hp = 1.0, color = GREEN, img = BLANK, w = 32, h = 32, anim = False, deathImg = ALIENDIE, animDelay = 10):
        
        this.x = x;
        this.y = y;
        this.xv = 0.0;
        this.yv = 0.0;
        this.hp = hp;
        this.color = color;
        this.w = w;
        this.h = h;
        this.img = img;
        this.dieDelay = 0;
        this.deathImg = deathImg;
        this.rect = pygame.rect.Rect(int(this.x), int(this.y), int(this.w), int(this.h));
        this.anim = anim;
        this.dead = False;
        this.rect.x, this.rect.y = 0, 0;
        this.angle = 0;
        
        
        if anim:
            this.animDelay = animDelay;
            this.animDel = animDelay;
            this.maxAnim = len(this.img);
            this.currentAnim = 0;
            for i in this.img:
                
                i = pygame.transform.scale(i, (this.w, this.h));
                this.rect.width = this.w;
                this.rect.height = this.h;
                i.fill(this.color, this.rect, 1);
                
            
                
        else:
            
            this.img = this.img[0];
            this.img = pygame.transform.scale(this.img, (this.w, this.h))
            
            
            
            this.rect.x = 0;
            this.rect.y = 0;
            
            this.img.fill(this.color, this.rect, 1);
            
            
        
        
        this.rect = pygame.rect.Rect(int(this.x), int(this.y), int(this.w), int(this.h));
        
    def deathAnim(this):
        this.img = this.deathImg;
        this.img = pygame.transform.scale(this.img, (this.w, this.h));
        
        this.rect.x = 0;
        this.rect.y = 0;
        this.rect.width = this.w + this.w / 3;
        this.rect.height = this.h;
        
        
        
        this.img.fill(WHITE, this.rect, 1);
        this.dead = True;
        this.dieDelay = 20;
            
            

def createText(textVal = "none", x = sW / 2, y = sH / 2, centered = True, color = GREEN, size = 1.0):
    
    global text, font;
    n = obj(x, y, color);
    sizing = [size, size];
    n.img = font.render(textVal, False, n.color);
    n.text = textVal;
    
    n.w, n.h = font.size(textVal);
    
    if centered and x == sW / 2:
        n.x -= n.w / 2;
    
    n.rect.x = int(n.x);
    n.rect.y = int(n.y);
    
    n.img = pygame.transform.scale(n.img, (n.w * sizing[0], n.h * sizing[1]));
    
    n.rect.width, n.rect.height = n.w, n.h;
    
    
    text.append(n);
    

def createEnemy(x = sW / 2, y = sH / 2, hp = 1.0, color = GREEN, img = BLANK, w = 32, h = 32, xv = 0, yv = 0, type = "norm", anim = False):
    
    global enemies;
    n = obj(x, y, hp, color, img, w, h, anim = anim);
    n.type = type;
    if (n.type == "norm"): n.scoreVal = 10;
    elif (n.type == "mShip"): n.scoreVal = 100;
    else: n.scoreVal = 10;
    n.xv = xv;
    
    
    enemies.append(n);

def createEnemyRow(x = 15, y = 45, count = 8, img = BLANK, color = GREEN, anim = False, column = [0,0,0]):
    
    global espd
    k = 0;
    j = column;
    xVal = x;
    yVal = y;
    xv = espd;
    
    for i in j: #idk how to use for loops in this way any other way
        while k < count:
            createEnemy(xVal, yVal, img = img, color = color, xv = xv, type = "norm", anim = anim);
            xVal += 64;
            k += 1;
        
        xVal = 15;
        k = 0;
        yVal += 32;
        
        



def createProj(x = sW / 2, y = sH / 2, hp = 1.0, color = GREEN, img = BLANK, w = 3, h = 16, dmgT = "plr", yv = -5, xv = 0):
    
    global projectiles;
    n = obj(x, y , hp, color, img, w, h);
    n.dmgT = dmgT;
    n.yv = yv;
    n.xv = xv;
    n.rect.height += 50;
    n.img.fill(n.color, None);
    
    projectiles.append(n);

def createMShip(x = sW / 2, y = sH / 2, hp = 1.0, color = (0, 150, 0), img = MOTHERSHIP, w = 64, h = 64, deathImg = MOTHERSHIPDIE, anim = False):

    global enemies
    n = obj(x, y, hp, color, img, w, h, deathImg = deathImg, anim = anim);
    n.y = randnum(0, 100);
    n.scoreVal = 100;

    if randnum(0,1) == 1:
        n.x = -n.w;
        n.xv = 5;
    else: 
        n.x = sW;
        n.xv = -5
    
    n.type = "mShip";


    enemies.append(n);
        




 




plr = obj(sW / 2 - 32, sH - 32, 1.0, GREEN, PLAYERSHIP, 32, 32, deathImg = PLAYERDIE);
plr.shootDel = 0;
plr.shootCount = 1;
plr.lives =  3;





def plrInput():
    
    #player movement
    global sW, sH, spd, bspd, mxspd, opmode;
    keys = pygame.key.get_pressed();



    # fun shooty mode:
    if keys[pygame.K_t]:
        opmode = True;
        
        
    if keys[pygame.K_d] and plr.x < sW: #go right
        if plr.xv < mxspd:
            plr.xv += spd;

    if keys[pygame.K_a] and plr.x > -plr.w: #go left
       if plr.xv > -mxspd:
        plr.xv -= spd;
    
    if keys[pygame.K_w] and plr.y > sH - 50: # go up
        if plr.yv > -mxspd:
            plr.yv -= spd;
            
    if keys[pygame.K_s] and plr.y < sH - plr.h: # go down
        if plr.yv < mxspd:
            plr.yv += spd;


    if (not keys[pygame.K_d] and not keys[pygame.K_a]) or (keys[pygame.K_d] and keys[pygame.K_a]) or abs(plr.xv) > mxspd:
        plr.xv -= plr.xv / 5;
    if (not keys[pygame.K_w] and not keys[pygame.K_s]) or (keys[pygame.K_w] and keys[pygame.K_s]) or abs(plr.yv) > mxspd:
        plr.yv -= plr.yv / 5;

    if plr.x < -plr.w: # push player outta the left edge of the screen
        plr.x = sW;
        #plr.xv = 0.0;
        
    if plr.x > sW - plr.w: # push player outta the right edge of the screen
        plr.x = sW - plr.w;
        
        
    if plr.y > sH - plr.h: # push player outta the bottom edge of the screen
        plr.y = sH - plr.h;
        plr.yv = 0.0;
    
    if plr.y < sH - 50: # push player outta the top limit of ur movement
        plr.y = sH - 50;
        plr.yv = 0.0;
        
    if (keys[pygame.K_SPACE] or mouseD) and plr.shootDel == 0: #shoot a bullet if there's not a playr bullet alread on screen
        if (plr.shootCount >= 3): 
            tempColor = RED;
            tempVel = -15;
            plr.shootCount = 0;
            c.shakeStr = 10;
        else: 
            tempColor = WHITE;
            tempVel = -10;
            c.shakeStr = 5;
        if opmode:
            tempVel = -30;
            tempColor = ORANGE;
            c.shakeStr = 8;
        createProj(x = plr.x + plr.w/2 - 2.5, y = plr.y, img = TESTIMG, dmgT = "plr", yv = tempVel, color = tempColor);
        
        plr.shootDel = 50 - randnum(0, 10);
        plr.shootCount += 1;
        c.shakeTime = 3;
        if opmode:
            plr.shootDel = 5;
            createProj(x = plr.x + plr.w/2 - 2.5, y = plr.y, img = TESTIMG, dmgT = "plr", yv = tempVel, color = tempColor, xv = 2);
            createProj(x = plr.x + plr.w/2 - 2.5, y = plr.y, img = TESTIMG, dmgT = "plr", yv = tempVel, color = tempColor, xv = -2);
        

    
   
   
 # check for collisions, anything can use this

def collide(r, x = 0, y = 0, useList = False, list = projectiles):
    
    if useList:
        for i in list:
            if pygame.Rect.collidepoint(r, int(i.x), int(i.y)):
                return True;
    else:
        return pygame.Rect.collidepoint(r, x, y);


        
    
def plrFrame():
    
    
    plr.x += plr.xv;
    plr.y += plr.yv;
    
    plr.rect.x = int(plr.x);
    plr.rect.y = int(plr.y);
    
    
    
    for i in projectiles:
        if collide(plr.rect, i.x, i.y) and i.dmgT == "enemy":
            plr.deathAnim();
    

    plrInput();
    
    if plr.shootDel > 0:
        plr.shootDel -= 1;


def enemyFrame(this):
    
    global score;
    
    this.x += this.xv;
    this.y += this.yv;
    
    this.rect.x = this.x;
    this.rect.y = this.y;
    
    if this.type == "norm":
        if randnum(1, 300 - lvl) == 1:
            createProj(this.x + this.w / 2, this.y, img = TESTIMG, dmgT = "enemy", yv = 5);
    
    if this.type == "mShip":
        if this.x > sW or this.x < -this.w:
            enemies.remove(this)
            

    if not this.dead and this.type == "norm":
        
        if this.x >= sW - this.w or this.x <= 0:
            if this.x >= sW - this.w:
                this.xv = -espd;
            if this.x <= 0:
                this.xv = espd;
            this.y += randnum(6, lvl + 9)
            if randnum(1, 1) == 1 and enemies[0] == this:
                createMShip();
    
    if this.y > plr.y:
        plr.deathAnim();
            

    if this.dead:
        this.xv, this.yv = 0, 0;

    if this.dieDelay > 0:
        this.dieDelay -= 1;
        if this.dieDelay == 0:
            enemies.remove(this);
            
     # check for touching player projectile
    for i in projectiles:
        if collide(this.rect, i.x, i.y) and this.dieDelay == 0 and i.dmgT == "plr":
            score += this.scoreVal;
            this.deathAnim();
            if not opmode: projectiles.remove(i);
    
    # other things gonna happen here

    #mothership things

def mShipFrame():
    pass

    if enemies.x <= sW or enemies.x >= 5:
        pass
        
    
def cameraFrame():
    if (c.shakeTime > 0): 
        c.shakeTime -= 1;
        c.shakeX += randnum(0,c.shakeStr);
        c.shakeY += randnum(0,c.shakeStr);
    
    if (c.shakeTime == 0):
        c.shakeX -= round(c.shakeX / 5);
        c.shakeY -= round(c.shakeY / 5);
    


# collision is already handled by pygame, don't do anything about it for now

def projFrame(this):
    
    this.x += this.xv;
    this.y += this.yv;
    
    this.rect.x = this.x;
    this.rect.y = this.y;
    
    if this.y < 0 or this.y > sH or this.x < 0 or this.x > sW:
        projectiles.remove(this);
    
def textFrame(this):
    
    if collide(this.rect, mx, my) and this.text == "Start" and mouseD:
        setupGame();
        
        

# create the menu's text
def makeMenu():
    
    createText("Space Invaders", y = 100);
    createText("Start", y = 274);
    
    
    

    
def setupGame():
    global text, gameState, score;
    text = [];
    
    createEnemyRow(img = ALIEN1, anim = True);
    i = 3;
    while i > 0:
        screen.fill(BGCOLOR);
        createText(str(i), y = sH / 2 - 20);
        screen.blit(text[0].img, (int(text[0].x), int(text[0].y)));
        pygame.display.update();
        time.sleep(0.5);
        text = [];
        
        i -= 1;
    screen.fill(BGCOLOR);
    createText("Start!", y = sH / 2 - 20)
    screen.blit(text[0].img, (int(text[0].x), int(text[0].y)), special_flags = 0);
    pygame.display.update();
    time.sleep(0.5);
    text = [];
    
    createText("Score: ", x = 10, y = 10, size = 0.5);
    
    gameState = "game";
    
def createLvl():
    
    for i in text:
        if i.text == "Level " + str(lvl) + "!": text.remove(i); break;
    



def gameOver():
    createText("Game Over", y = 274)
    time.sleep(5.0)
    
def newLvl():
    global lvl, text, fps;
    lvl += 1;
    
    createText("Level " + str(lvl) + "!");
    lvlT = threading.Timer(interval = 1, function = createLvl);
    lvlT.start();
    
    
    createEnemyRow(img = ALIEN1, anim = True);



def screenThings():
    screen.fill(BGCOLOR) # clears the stuff off the screen, disable this if you want to see something fun...
    # render things
    global enemies, projectiles
    
    cameraFrame();
    
    for i in text:
        textFrame(i);
        screen.blit(i.img, (int(i.x + c.shakeX), int(i.y + c.shakeY)))
    if gameState == "game":
        screen.blit(plr.img, (int(plr.x + c.shakeX), int(plr.y + c.shakeY)));
        pygame.draw.line(screen, (50,50,50), (plr.x + plr.w / 2 + c.shakeX, plr.y + 7 + c.shakeY), (plr.x + plr.w / 2 + c.shakeX, 0));
        scorespot = 0;
        for i in str(score):
            screen.blit(num[int(i)], (107 + scorespot, 10));
            thingy = font.size(num[int(i) + 10]);
            scorespot += thingy[0] / 2;
        
        for i in enemies:
            
            if i.anim:
                if (not i.dead): image = i.img[i.currentAnim];
                else: image = i.img;
                i.rect.x = 0;
                i.rect.y = 0;
                i.rect.w = i.w;
                i.rect.h = i.h;
                image = pygame.transform.scale(image, (i.w, i.h));
                image.fill(i.color, i.rect, 1);
                
                
                screen.blit(image, (int(i.x + c.shakeX), int(i.y + c.shakeY)));
                if (i.animDel > 0): i.animDel -= 1;
                if (i.animDel == 0):
                    i.animDel = i.animDelay;
                    i.currentAnim += 1;
                    if (i.currentAnim == i.maxAnim): i.currentAnim = 0;
                    
            else:
                screen.blit(i.img, (int(i.x), int(i.y)));
            
        for i in projectiles:
            screen.blit(i.img, (int(i.x), int(i.y)));
            
    # show mouse position
    mpos = font.render(str(pygame.mouse.get_pos()[0]) + " " + str(pygame.mouse.get_pos()[1]), False, BLUE)
    mposW = int(mpos.get_size()[0] / 4);
    mposH = int(mpos.get_size()[1] / 4);
    mpos = pygame.transform.scale(mpos, (mposW, mposH))
    screen.blit(mpos, (int(mx) + 30, int(my)));
    pygame.display.update();
    pygame.display.flip();
    

def game():
    global enemies, projectiles
    plrFrame();
    
    
    if (len(enemies) == 0 and not updatingLvl): newLvl();
    
    for i in enemies:
        if not updatingLvl: enemyFrame(i);
        
        
    for i in projectiles:
        projFrame(i);
        
    
    
#this is where we call things, don't assign values / functions below here

makeMenu();

pygame.display.set_caption("space invaders go weeee");









running = True;

while running:
    
    screenThings();
    clock.tick(fps);
    
    mx, my = pygame.mouse.get_pos();
    
    
    
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False;
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos());
            mouseD = True;
            
        if event.type == pygame.MOUSEBUTTONUP:
            mouseD = False;
            
    if gameState == "menu":
        pass
        
    if gameState == "game":
        game();
pygame.quit();





