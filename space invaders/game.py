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

# sounds

SNIPER = pygame.mixer.Sound("sounds/sniper.mp3");
GETSHOTGUN = pygame.mixer.Sound("sounds/get shotgun.wav");
AMMOOUT = pygame.mixer.Sound("sounds/no ammo for other guns.wav");
BASICSHOT = pygame.mixer.Sound("sounds/basic shot.mp3");
SHOTGUN = pygame.mixer.Sound("sounds/shotgun.mp3");
SMG = pygame.mixer.Sound("sounds/smg shot.mp3");
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
elif os.path.exists("C:/space invaders/"):
    hP = "C:/space invaders/";
else: hP = "";

# get which path to use cuz programming at home is diff
clock = pygame.time.Clock();
font = pygame.font.Font(hP + "fonts/PressStart2P-Regular.ttf", 32);
def numbererer(text):
    tempthing = font.render(text, False, (0, 255, 0));
    tempthing = pygame.transform.scale(tempthing, (int(font.size(text)[0] / 2), int(font.size(text)[1] / 2)));
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
rainbow_counter = 0
rainTrue = True
def rainbow():
    r = randnum(0, 255)
    g = randnum(0, 255)
    b = randnum(0, 255)
    return (r, g, b)

if rainTrue == True:
    rainbow_counter += 1
    if rainbow_counter > 5:
        RAINBOW = rainbow()
        rainbow_counter = 0

RAINBOW = rainbow()
RED = (255, 0, 0)
ORANGE = (255, 120, 0);
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (1, 50, 32)
BLUE = (0, 0, 255)
SPACE_BLUE = (31, 66, 119)
PURPLE = (230, 230, 250)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BLUE = (3, 107, 252)
GRAY = (50, 50, 50);
BGCOLOR = BLACK
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
 
#images
PLAYERSHIP = [pygame.image.load(hP + "images/player.png")];
PLRBULLET = [pygame.image.load(hP + "images/player bullet.png")];
ALIEN1 = [pygame.image.load(hP + "images/alien1-1.png"), pygame.image.load(hP + "images/alien1-2.png")];
ALIEN2 = [pygame.image.load(hP + "images/alien2-1.png"), pygame.image.load(hP + "images/alien2-2.png")];
ALIENDIE = pygame.image.load(hP + "images/alien death.png");
MOTHERSHIP = [pygame.image.load(hP + "images/mothership1-1.png"), pygame.image.load(hP + "images/mothership1-2.png")];
MOTHERSHIPDIE = pygame.image.load(hP + "images/mothership die.png");
TESTIMG = [pygame.image.load(hP + "images/test.png")];
PLAYERDIE = pygame.image.load(hP + "images/player die1-1.png")
BLANK = [pygame.image.load(hP + "images/blank.png")];
STARS = [pygame.image.load(hP + "images/bg.png")]


spd = sW / 600; #speed for player
mxspd = sW / 200; #player max speed
bspd = 10; #projectile speed
espd = 3; #enemy speed
maxBullets = 1;
lvl = 1;
score = 0;


def dist(o1, o2):
    return math.sqrt((o1.x - o2.x)**2 + (o1.y - o2.y)**2);



class obj:
    
    def __init__(this, x = sW / 2, y = sH / 2, hp = 1.0, color = GREEN, img = BLANK, w = 32, h = 32, anim = False, deathImg = ALIENDIE, animDelay = 10):
        
        this.x = int(x);
        this.y = int(y);
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
        this.visible = True;
        
        
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
        this.rect.width = this.w;
        this.rect.height = this.h;
        
        
        
        this.img.fill(WHITE, this.rect, 1);
        this.dead = True;
        this.dieDelay = 20;
    


    def kaplooey(this, deathDist = 100):
        for i in projectiles:
            if dist(this, i) < deathDist:
                projectiles.remove(i);
        if dist(this, plr) < deathDist:
            plr.deathAnim();
            plrDie();
        for i in enemies:
            if dist(this, i) < deathDist:
                i.deathAnim();
        
            
            

def createText(textVal = "none", x = sW / 2, y = sH / 2, centered = True, color = GREEN, size = 1.0, special = "none"):
    
    global text, font;
    n = obj(x, y, color);
    sizing = [size, size];
    n.img = font.render(textVal, False, n.color);
    n.text = textVal;
    n.special = special;
    n.w, n.h = font.size(textVal);
    
    
    
    n.rect.x = int(n.x);
    n.rect.y = int(n.y);
    
    n.img = pygame.transform.scale(n.img, (n.w * sizing[0], n.h * sizing[1]));
    if centered and x == sW / 2:
        n.x -= n.w / 2;
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
    n.yv = yv;
    
    
    enemies.append(n);

def createEnemyRow(x = 15, y = 45, count = 8, img = BLANK, color = GREEN, anim = False, column = [0,0,0]):
    
    global espd, lvl;
    k = 0;
    j = column;
    xVal = x;
    yVal = y;
    xv = espd + lvl;
    
    for i in j: #idk how to use for loops in this way any other way
        while k < count:
            createEnemy(xVal, yVal, img = img, color = color, xv = xv, type = "norm", anim = anim);
            xVal += 64;
            k += 1;
        
        xVal = 15;
        k = 0;
        yVal += 32;
        
        



def createProj(x = sW / 2, y = sH / 2, hp = 1.0, color = GREEN, img = BLANK, w = 3, h = 16, dmgT = "plr", yv = -5, xv = 0, pierce = False, powerUp = False):
    
    global projectiles;
    n = obj(x, y , hp, color, img, w, h);
    n.dmgT = dmgT;
    n.yv = yv;
    n.xv = xv;
    n.pierce = pierce;
    n.rect.height += 50;
    n.img.fill(n.color, None);
    n.powerUp = powerUp;
    
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
        



def makeBG():
    randC = WHITE;
    global bg1, bg2;
    if randnum(1, 5) == 1: randC = WHITE;
    if randnum(1, 5) == 2: randC = ORANGE;
    if randnum(1, 5) == 3: randC = GREEN;
    if randnum(1, 5) == 4: randC = YELLOW;
    if randnum(1, 5) == 5: randC = PURPLE;
    bg1 = obj(color = randC, img = STARS, w = sW, h = sH + 200, x = 0, y = -200);
    bg2 = obj(color = randC, img = STARS, w = sW, h = sH + 200, x = 0, y = bg1.y - (sH + 200));
    
 
makeBG();



plr = obj(sW / 2 - 32, sH - 32, 1.0, GREEN, PLAYERSHIP, 32, 32, deathImg = PLAYERDIE);
plr.tempW = plr.w;
plr.tempH = plr.h;
plr.shootDel = 0;
plr.shootCount = 1;
plr.lives = 3;
plr.scoreNeed = 2000;

plr.laser = False;
plr.laserX1, plr.laserY1, plr.laserX2, plr.laserY2 = 0,0,0,0;
plr.laserColor = GRAY;
plr.laserShoot = False;
plr.laserAmmo = 10;

plr.shotgun = False;
plr.shotgunAmmo = 20;

plr.smg = False;
plr.smgAmmo = 20;

plr.grenade = False;
plr.grenades = 3;




def plrInput():
    
    #player movement
    global sW, sH, spd, bspd, mxspd, opmode, fps;
    keys = pygame.key.get_pressed();



    # fun shooty mode:
    if keys[pygame.K_t]: opmode = True;
    if keys[pygame.K_p]: plrDie();
    if keys[pygame.K_i] and not plr.laser: plr.laser = True; plr.shotgun = False; plr.smg = False; plr.laserAmmo = 10;
    if keys[pygame.K_u] and not plr.shotgun: plr.shotgun = True; plr.laser = False; plr.smg = False; plr.shotgunAmmo = 10; pygame.mixer.Sound.play(GETSHOTGUN);
    if keys[pygame.K_o] and not plr.smg: plr.smg = True; plr.laser = False; plr.shotgun = False; plr.smgAmmo = 30;
    if keys[pygame.K_g] and not plr.grenade: plr.grenade = True;
        # set player gre3ndesa to 3, removing other weapons \deosn't need to happen
    if keys[pygame.K_d]: #go right
        if plr.xv < mxspd:
            plr.xv += spd;

    if keys[pygame.K_a]: #go left
       if plr.xv > -mxspd:
        plr.xv -= spd;
    
    if keys[pygame.K_w] and plr.y > 0: # go up
        if plr.yv > -mxspd:
            plr.yv -= spd;
            
    if keys[pygame.K_s] and plr.y < sH - plr.h: # go down
        if plr.yv < mxspd:
            plr.yv += spd;


    if (not keys[pygame.K_d] and not keys[pygame.K_a]) or (keys[pygame.K_d] and keys[pygame.K_a]) or abs(plr.xv) > mxspd:
        plr.xv -= plr.xv / 5;
    if (not keys[pygame.K_w] and not keys[pygame.K_s]) or (keys[pygame.K_w] and keys[pygame.K_s]) or abs(plr.yv) > mxspd:
        plr.yv -= plr.yv / 5;

    if plr.x < -50: # loop player to right edge of screen when hitting left edge
        plr.x = sW;
        
    if plr.x > sW + 50: # loop player to left edge of screen when hitting right edge
        plr.x = -plr.w;
        
        
    if plr.y > sH - plr.h: # push player outta the bottom edge of the screen
        plr.y = sH - plr.h;
        plr.yv = 0.0;
    
    if plr.y < 0: # push player outta the top limit of ur movement
        plr.y = sH - 50;
        plr.yv = 0.0;
        # fire attack
    if keys[pygame.K_g] and plr.grenades > 0 and plr.grenadeCD == 0: 
        createProj(x = plr.x+plr.w/2, y = plr.y+plr.h/2, img = TESTIMG, yv = -10, color = YELLOW);
        plr.grenades -= 1;
        plr.grenadeCD = 100;
    if plr.laserShoot: plr.laserShoot = False;
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
        
        if plr.laser and plr.laserAmmo > 0: 
            plr.laserShoot = True;
            plr.shootDel = 60;
            c.shakeStr = 30;
            plr.laserAmmo -= 1;
            pygame.mixer.Sound.play(SNIPER);
            if plr.laserAmmo == 0: pygame.mixer.Sound.play(AMMOOUT); plr.laser = False;
        elif plr.shotgun and plr.shotgunAmmo > 0:
            tempColor = YELLOW;
            tempVel = -15;
            createProj(x = plr.x + plr.w/2 - 3, y = plr.y - 16, img = TESTIMG, dmgT = "plr", xv = -2, yv = tempVel + 1, color = tempColor);
            createProj(x = plr.x + plr.w/2 - 3, y = plr.y - 16, img = TESTIMG, dmgT = "plr", xv = -1, yv = tempVel + 1, color = tempColor);
            #middle
            createProj(x = plr.x + plr.w/2 - 3, y = plr.y - 16, img = TESTIMG, dmgT = "plr", yv = tempVel, color = tempColor);

            createProj(x = plr.x + plr.w/2 - 3, y = plr.y - 16, img = TESTIMG, dmgT = "plr", xv = 1, yv = tempVel + 1, color = tempColor);
            createProj(x = plr.x + plr.w/2 - 3, y = plr.y - 16, img = TESTIMG, dmgT = "plr", xv = 2, yv = tempVel + 1, color = tempColor);
            plr.shootDel = 65;
            c.shakeStr = 10;
            c.shakeTime = 5;
            plr.shotgunAmmo -= 1;
            pygame.mixer.Sound.play(SHOTGUN);
            if plr.shotgunAmmo == 0: pygame.mixer.Sound.play(AMMOOUT); plr.shotgun = False;
        elif plr.smg and plr.smgAmmo > 0:
            tempColor = PURPLE;
            tempVel = -15;
            createProj(x = plr.x + plr.w/2 - 3, y = plr.y - 16, img = TESTIMG, dmgT = "plr", xv = 1, yv = tempVel + 1, color = tempColor);
            c.shakeStr = 10;
            c.shakeTime = 3;
            plr.shootDel = 10;
            plr.smgAmmo -= 1
            pygame.mixer.Sound.play(SMG);
            if plr.smgAmmo == 0: pygame.mixer.Sound.play(AMMOOUT); plr.smg = False;
        elif plr.grenade and plr.grenades > 0:
            tempColor = ORANGE;
            
            tempVel = -15;
            
            createProj(x = plr.x + plr.w/2 - 3, y = plr.y - 16, img = TESTIMG, dmgT = "grenade", xv = 1, yv = tempVel + 1, color = tempColor)
                
            plr.shootDel = 65;
            c.shakeStr = 10;
            c.shakeTime = 5;
            plr.grenadeAmmo -= 1;
            if plr.grenadeAmmo == 0: pygame.mixer.Sound.play(AMMOOUT); plr.grenade = False;
            
        else:
            createProj(x = plr.x + plr.w/2 - 2.5, y = plr.y, img = TESTIMG, dmgT = "plr", yv = tempVel, color = tempColor);
            plr.shootDel = 50 - randnum(0, 10)
            c.shakeStr = 5;
            pygame.mixer.Sound.play(BASICSHOT);
            
        c.shakeTime = 3;
        plr.shootCount += 1;
        randVal1 = 5;
        randVal2 = 5;
        if opmode:
            plr.shootDel = 5;
            createProj(x = plr.x + plr.w/2 - 2.5, y = plr.y, img = TESTIMG, dmgT = "plr", yv = randnum(-randVal1,randVal2), color = tempColor, xv = randnum(-randVal1,randVal2));
            createProj(x = plr.x + plr.w/2 - 2.5, y = plr.y, img = TESTIMG, dmgT = "plr", yv = randnum(-randVal1,randVal2), color = tempColor, xv = randnum(-randVal1,randVal2));
            createProj(x = plr.x + plr.w/2 - 2.5, y = plr.y, img = TESTIMG, dmgT = "plr", yv = randnum(-randVal1,randVal2), color = tempColor, xv = randnum(-randVal1,randVal2));
            createProj(x = plr.x + plr.w/2 - 2.5, y = plr.y, img = TESTIMG, dmgT = "plr", yv = randnum(-randVal1,randVal2), color = tempColor, xv = randnum(-randVal1,randVal2));
            createProj(x = plr.x + plr.w/2 - 2.5, y = plr.y, img = TESTIMG, dmgT = "plr", yv = randnum(-randVal1,randVal2), color = tempColor, xv = randnum(-randVal1,randVal2));
            createProj(x = plr.x + plr.w/2 - 2.5, y = plr.y, img = TESTIMG, dmgT = "plr", yv = randnum(-randVal1,randVal2), color = tempColor, xv = randnum(-randVal1,randVal2));
        

    
   
   
 # check for collisions, anything can use this

def collide(r1, r2):
    return pygame.Rect.colliderect(r1, r2);
def collideP(r1, x, y):
    return pygame.Rect.collidepoint(r1, x, y);
def revivePlayer():
    plr.visible = False;
    plr.dead = False;
    plr.w = plr.tempW;
    plr.h = plr.tempH;
    plr.x = int(sW / 2);
    plr.y = sH - 100;
    plr.img = PLAYERSHIP[0];
    plr.img = pygame.transform.scale(plr.img, (plr.w, plr.h));

    plr.rect.x = 0;
    plr.rect.y = 0;
    plr.rect.width = plr.w;
    plr.rect.height = plr.h;
    plr.img.fill(plr.color, plr.rect, 1);
    plr.dieDelay = fps * -2;
    plr.visible = True;
    


def plrDie():
    if not plr.w == 0:
        if plr.lives > 0: plr.lives -= 1;
        if plr.lives >= 1: setTimeout(revivePlayer, 2);
        if plr.lives <= 0: gameOver();
    plr.w = 0;
    plr.h = 0;

def plrFrame():
    global score;
    
    plr.x += plr.xv;
    plr.y += plr.yv;
    
    plr.laserX1 = plr.x + plr.w/2;
    plr.laserY1 = plr.y + 3;
    if plr.laser:
        plr.laserX2 = mx;
        plr.laserY2 = my;
    else: plr.laserX2 = plr.laserX1; plr.laserY2 = 0;
    if plr.laserShoot: plr.laserColor = RED;
    else: plr.laserColor = GRAY;
    
    plr.rect.x = int(plr.x);
    plr.rect.y = int(plr.y);
    
    if score > plr.scoreNeed:
        plr.lives += 1;
        plr.scoreNeed += 2000;
    if not plr.dieDelay < 0:
        for i in projectiles:
            if collide(i.rect, plr.rect): # run things when projectile
                if i.dmgT == "enemy": plr.deathAnim();
                if i.powerUp:
                    if i.dmgT == "laser": plr.laser = True; plr.laserAmmo = 10; plr.shotgun = False; plr.smg = False;
                    if i.dmgT == "shotgun": plr.shotgun = True; plr.shotgunAmmo = 10; plr.laser = False; plr.smg = False; pygame.mixer.Sound.play(GETSHOTGUN);
                    if i.dmgT == "smg": plr.smg = True; plr.shotgun = False; plr.laser = False;
                    projectiles.remove(i);
        if plr.dead and plr.dieDelay == 0:
            plrDie();
    
    if not plr.dead: plrInput();
    else: plr.xv = 0; plr.yv = 0;
    
    if plr.shootDel > 0:
        plr.shootDel -= 1;
    if plr.grenadeCD > 0: plr.grenadeCD -= 1;
    if plr.dieDelay > 0: plr.dieDelay -= 1;
    if plr.dieDelay > 10: plr.dieDelay = 9;
    if plr.dieDelay < 0: plr.dieDelay += 1; print(plr.dieDelay)

def enemyFrame(this):
    
    global score;
    if (this.type == "mShip"): mShipFrame(this);
    
    this.x += this.xv;
    this.y += this.yv;
    
    this.rect.x = this.x;
    this.rect.y = this.y;
    
    if this.type == "norm":
        if randnum(1, 300 - lvl * 2) == 1:
            createProj(this.x + this.w / 2, this.y, img = TESTIMG, dmgT = "enemy", yv = 5);
    
    if this.type == "mShip":
        if this.x > sW or this.x < -this.w:
            enemies.remove(this)
            

    if not this.dead and this.type == "norm":
        if this.y > sH or this.y < 0: enemies.remove(this);
        if this.x >= sW - this.w or this.x <= 0:
            if this.x >= sW - this.w:
                this.xv = -espd - lvl;
            if this.x <= 0:
                this.xv = espd + lvl;
            this.y += randnum(6, lvl + 9)
            if randnum(1, 1) == 1 and enemies[0] == this:
                createMShip();
    
    if collide(this.rect, plr.rect):
        plr.deathAnim();
        plrDie();
        print("kill player");
        
            

    if this.dead:
        this.xv, this.yv = 0, 0;

    if this.dieDelay > 0:
        this.dieDelay -= 1;
        if this.dieDelay == 0:
            enemies.remove(this);
            
     # check for touching player projectile
    if plr.laserShoot:
        if this.rect.clipline((plr.laserX1, plr.laserY1), (plr.laserX2, plr.laserY2)):
            this.deathAnim();
            score += this.scoreVal;
            if randnum(1,5) == 1: powerUps(this);
    for i in projectiles:
        if collide(this.rect, i.rect) and this.dieDelay == 0 and i.dmgT == "plr":
            score += this.scoreVal;
            this.deathAnim();
            if randnum(1, 10) == 1: powerUps(this);
            if not opmode and not i.pierce: projectiles.remove(i);
    
    # other things gonna happen here

    #mothership things

def mShipFrame(this):
    if randnum(1, 150) == 1: 
        tV = randnum(1, 5);
        createEnemy(this.x, this.y, img = ALIEN1, xv = this.xv, yv = tV);
        
    
def cameraFrame():
    if (c.shakeTime > 0): 
        c.shakeTime -= 1;
        c.shakeX += randnum(-c.shakeStr,c.shakeStr);
        c.shakeY += randnum(-c.shakeStr,c.shakeStr);
    
    if (c.shakeTime == 0):
        c.shakeX -= round(c.shakeX / 5);
        c.shakeY -= round(c.shakeY / 5);
    


# collision is already handled by pygame, don't do anything about it for now

def projFrame(this):
    
    this.x += this.xv;
    this.y += this.yv;
    
    this.rect.x = this.x;
    this.rect.y = this.y;
    
    if this.dmgT == "grenade":
        if this.yv < 0:
            this.yv -= this.yv / 5;
        if collide(this.rect, plr.rect) and this.yv > -3:
            plr.deathAnim();
            plrDie();
            this.kaplooey();
        for i in enemies:
            if collide(this.rect, i.rect):
                this.kaplooey();
        for i in projectiles:
            if collide(this.rect, i.rect):
                this.kaplooey();

    if this.y + this.h < 0 or this.y > sH or this.x < 0 or this.x > sW:
        projectiles.remove(this);
    for i in projectiles:
        if not i == this and not this.powerUp and not i.powerUp:
            if not i.dmgT == this.dmgT:
                if collide(i.rect, this.rect):
                    if not this.pierce: projectiles.remove(this);
                    if not i.pierce: projectiles.remove(i);

def textFrame(this):
    
    if collideP(this.rect, mx, my) and this.text == "Start" and mouseD:
        setupGame();
        
def bgFrame():
    bg1.y += 1;
    bg2.y += 1;
    if bg1.y >= sH: bg1.y = -bg1.h;
    if bg2.y >= sH: bg2.y = -bg2.h;

# create the menu's text
def makeMenu():
    
    createText("Space Invaders", y = 100);
    createText("Start", y = 274);
    
def powerUps(this):
    # on enemy death, call this
    
    randomNum = randnum(1,5);
    if randomNum == 1:
        createProj(this.x, this.y, color = BLUE, img = TESTIMG, w = 50, h = 50, dmgT = "laser", yv = 2, powerUp = True);
    if randomNum == 2:
        createProj(this.x, this.y, color = GREEN, img = TESTIMG, w = 50, h = 50, dmgT = "life", yv = 2, powerUp = True);
    if randomNum == 3:
        createProj(this.x, this.y, color = RED, img = TESTIMG, w = 50, h = 50, dmgT = "shotgun", yv = 2, powerUp = True);
    if randomNum == 4:
        createProj(this.x, this.y, color = ORANGE, img = TESTIMG, w = 50, h = 50, dmgT = "grenade", yv = 2, powerUp = True);
    if randomNum == 5:
        createProj(this.x, this.y, color = PURPLE, img = TESTIMG, w = 50, h = 50, dmgT = "smg", yv = 2, powerUp = True);


    
def setupGame():
    global text, gameState, score, enemies, projectiles, lvl;
    text = [];
    enemies = [];
    projectiles = [];
    plr.lives = 3;
    plr.scoreNeed = 2000;
    lvl = 1;
    revivePlayer();
    
    createEnemyRow(img = ALIEN1, anim = True);
    i = 3;
    while i > 0:
        screen.fill(BGCOLOR);
        createText(str(i), y = sH / 2 - 20);
        screen.blit(text[0].img, (int(text[0].x + c.shakeX), int(text[0].y + c.shakeY)));
        pygame.display.update();
        time.sleep(0.5);
        text = [];
        
        i -= 1;
    screen.fill(BGCOLOR);
    createText("Start!", y = sH / 2 - 20)
    screen.blit(text[0].img, (int(text[0].x + c.shakeX), int(text[0].y + c.shakeY)), special_flags = 0);
    pygame.display.update();
    time.sleep(0.5);
    text = [];
    
    createText("Score: ", x = 10, y = 10, size = 0.5);
    createText("Lives: ", x = 10, y = 30, size = 0.5);
    
    gameState = "game";
    
def rmvLvlText():
    
    for i in text:
        if i.special == "lvl": text.remove(i); break;
    

def setTimeout(function = None, delay = 0.0, arg = ()):
    timer = threading.Timer(interval = float(delay), function = function, args = arg);
    timer.start();



    


def gameOver():
    global gameState, enemies, mouseD;
    enemies = [];
    if gameState == "game":
        gameState = "game over";
        createText("Game Over", y = 160)
        
        setTimeout(createText, 2, ("Try Again?", sW / 2, 220, True, GREEN, 1, "gameOver"));
        setTimeout(createText, 2, ("Yeh", sW / 2 - 150, 300, True, GREEN, 0.7, "restart"));
        setTimeout(createText, 2, ("Nah", sW / 2 + 75, 300, True, GREEN, 0.7, "give up"));
    if mouseD:
        for i in text:
            if gameState == "game over":
                if i.special == "restart" and collideP(i.rect, mx, my): setupGame(); break;
                if i.special == "give up" and collideP(i.rect, mx, my): pygame.quit(); break;
            else:
                break;

    
    
def newLvl():
    global lvl, text, fps;
    lvl += 1;
    
    createText("Level " + str(lvl) + "!", special = "lvl");
    setTimeout(rmvLvlText, 1.5);
    
    
    createEnemyRow(img = ALIEN1, anim = True);



def screenThings():
    screen.fill(BGCOLOR) # clears the stuff off the screen, disable this if you want to see something fun...
    # render things
    global enemies, projectiles, plr, mx, my;
    screen.blit(bg1.img, (0, bg1.y));
    screen.blit(bg2.img, (0, bg2.y));
    bgFrame();
    cameraFrame();
    
    for i in text:
        textFrame(i);
        screen.blit(i.img, (int(i.x + c.shakeX), int(i.y + c.shakeY)))
    if gameState == "game":
        if plr.visible: screen.blit(plr.img, (int(plr.x + c.shakeX), int(plr.y + c.shakeY)));
        if not plr.dead: pygame.draw.line(screen, plr.laserColor, (plr.laserX1, plr.laserY1), (plr.laserX2, plr.laserY2));
        spot = 0;
        for i in str(score):
            screen.blit(num[int(i)], (107 + spot + c.shakeX, 10 + c.shakeY));
            thingy = font.size(num[int(i) + 10]);
            spot += thingy[0] / 2;
        spot = 0;
        for i in str(plr.lives):
            screen.blit(num[int(i)], (107 + spot + c.shakeX, 30 + c.shakeY));
            thingy = font.size(num[int(i) + 10]);
            spot += thingy[0] / 2;
        
        for i in enemies:
            if i.visible:
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
                    screen.blit(i.img, (int(i.x + c.shakeX), int(i.y + c.shakeY)));
            
        for i in projectiles:
            if i.visible: screen.blit(i.img, (int(i.x + c.shakeX), int(i.y + c.shakeY)));
            
    # show mouse position
    mpos = font.render(str(mx) + " " + str(my), False, BLUE)
    mposW = int(mpos.get_size()[0] / 4);
    mposH = int(mpos.get_size()[1] / 4);
    mpos = pygame.transform.scale(mpos, (mposW, mposH))
    screen.blit(mpos, (int(mx) + 30, int(my)));
    
    

def game():
    global enemies, projectiles
    plrFrame();
    
    
    if (len(enemies) == 0 and not updatingLvl and not plr.dead): newLvl();
    
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
    
    mpos = pygame.mouse.get_pos();
    mx = mpos[0];
    my = mpos[1];
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False;
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos());
            mouseD = True;
            
        if event.type == pygame.MOUSEBUTTONUP:
            mouseD = False;
            

    if gameState == "game":
        game();
    if gameState == "game over":
        gameOver();
    pygame.display.update();
    pygame.display.flip();
pygame.quit();





