#Imported items
import math
import random
import time
import pygame
import os
#variables go here
    
pygame.font.init();
pygame.mixer.init();
pygame.init();



#debugRect = pygame.Rect(); this'll do something later

from pygame.locals import (
K_UP,
K_DOWN,
K_LEFT,
K_RIGHT,
K_ESCAPE,
K_SPACE,
KEYDOWN,
QUIT
)


if os.path.exists("D:/programming stuff/"):
    hP = "D:/programming stuff/space invaders/";
else:
    hP = "";

# get which path to use cuz programming at home is diff
clock = pygame.time.Clock();
font = pygame.font.Font(hP + "fonts/PressStart2P-Regular.ttf", 32)


#Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BGCOLOR = BLACK;
FPS = 60;

gameState = "menu"; # can be "menu", "game", or "gameover"

sW, sH = 600, 600;
screen = pygame.display.set_mode((sW, sH));
mouseD = False;
mx, my = 0, 0;

projectiles = [];
players = []; # multiplayer, if we have time
enemies = [];
text = [];

PLAYERSHIP = [pygame.image.load(hP + "images/player.png")];
PLRBULLET = [pygame.image.load(hP + "images/player bullet.png")];
ALIEN1 = [pygame.image.load(hP + "images/alien1-1.png"), pygame.image.load(hP + "images/alien1-2.png")];
#ALIEN2 = pygame.image.load(os.path.join("images", "alien2.png"))
ALIENDIE = pygame.image.load(hP + "images/alien death.png");

BLANK = [pygame.image.load(hP + "images/blank.png")];



class obj:
    
    def __init__(self, x = sW / 2, y = sH / 2, hp = 1.0, color = GREEN, img = BLANK, w = 32, h = 32, anim = False):
        
        self.x = x;
        self.y = y;
        self.xv = 0.0;
        self.yv = 0.0;
        self.hp = hp;
        self.color = color;
        self.w = w;
        self.h = h;
        self.dieDelay = 0;
        if anim:
            self.img = img;
            for i in img:
                self.img[i] = pygame.transform.scale(self.img[i], (self.w, self.h));
                self.img[i].fill(self.color, special_flags = pygame.BLENDMODE_BLEND);
        else:
            self.img = img[0];
            self.img = pygame.transform.scale(self.img, (self.w, self.h));
            self.img.fill(self.color, special_flags = pygame.BLENDMODE_BLEND);
        
        self.rect = pygame.rect.Rect(self.x, self.y, self.w, self.h);
        
    def deathAnim(self):
        self.img = ALIENDIE;
        self.img = pygame.transform.scale(self.img, (self.w + (self.w / 3), self.h));
        self.x -= 3;
        self.dieDelay = 20;
            
            

def createText(textVal = "none", x = sW / 2, y = sH / 2, centered = True, color = GREEN):
    
    global text;
    n = obj(x, y, color);
    n.img = font.render(textVal, False, n.color);
    n.text = textVal;
    n.w, n.h = font.size(textVal);
    
    if centered:
        n.x -= n.w / 2;
    
    n.rect.x = n.x;
    n.rect.w, n.rect.h = n.w, n.h;
    
    
    text.append(n);
    

def createEnemy(x = sW / 2, y = sH / 2, hp = 1.0, color = GREEN, img = BLANK, w = 32, h = 32):
    
    global enemies;
    n = obj(x, y, hp, color, img, w, h);
    
    
    enemies.append(n);

def createEnemyRow(x = 15, y = 15, count = 8, img = BLANK):
    
    i = 0;
    
    while i < count:
        createEnemy(x, y, img = img);
        x += 32;
        i += 1;
        



def createProj(x = sW / 2, y = sH / 2, hp = 1.0, color = GREEN, img = BLANK, w = 3, h = 16, dmgT = "plr", yv = -5):
    
    global projectiles;
    n = obj(x, y , hp, color, img, w, h);
    n.dmgT = dmgT;
    n.yv = yv;
    
    projectiles.append(n);






createEnemyRow(img = ALIEN1)

plr = obj(sW / 2 - 32, sH - 32, 1.0, GREEN, PLAYERSHIP, 32, 32);
plr.shootDel = 0;

spd = sW / 600; #speed for player
mxspd = sW / 200; #player max speed
bspd = 10; #projectile speed
espd = 3; #enemy speed
maxBullets = 1;




plrRect = pygame.Rect(200, 200, plr.w, plr.h);
pBul = pygame.Rect(round(plr.x), round(plr.y), 5, 5);



def plrInput():
    
    #player movement
    global sW, sH, spd, pBul, bspd, mxspd;
    keys = pygame.key.get_pressed();

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

    if plr.x < 0: # push player outta the left edge of the screen
        plr.x = 0;
        # IDEA!!!!: player loops around the screen, go off edge and you come out the other side
        plr.xv = 0.0; # player go bounce
        
    if plr.x > sW - plr.w: # push player outta the right edge of the screen
        plr.x = sW - plr.w;
        plr.xv = 0.0;
        
    if plr.y > sH - plr.h: # push player outta the bottom edge of the screen
        plr.y = sH - plr.h;
        plr.yv = 0.0;
    
    if plr.y < sH - 50: # push player outta the top limit of ur movement
        plr.y = sH - 50;
        plr.yv = 0.0;
        
    if (keys[pygame.K_SPACE] or mouseD) and plr.shootDel == 0: #shoot a bullet if there's not a playr bullet alread on screen
        
        createProj(plr.x + plr.w/2 - 2.5, plr.y, img = PLRBULLET, dmgT = "plr", yv = -10, color = WHITE);
        
        plr.shootDel = 50;


    
   
   
   
    
    


        
    
def plrFrame():
    
    plr.x += plr.xv;
    plr.y += plr.yv;
    
    plr.rect.x = plr.x;
    plr.rect.y = plr.y;
    
    #pygame.draw.line(screen, RED, (plr.x, plr.y), (0, 0), 30); trying to make a laser for aim assistance
    
    plrInput();
    if plr.shootDel > 0:
        plr.shootDel -= 1;



def enemyFrame(self):
    
    self.x += self.xv;
    self.y += self.yv;
    
    self.rect.x = self.x;
    self.rect.y = self.y;
    if self.dieDelay > 1:
        self.dieDelay -= 1;
        if self.dieDelay == 1:
            enemies.remove(self);
    for i in projectiles:
        if pygame.Rect.collidepoint(self.rect, (i.x, i.y)) and self.dieDelay == 0:
            self.deathAnim();
            projectiles.remove(i);
    
    # other things gonna happen here

# collision is already handled by pygame, don't do anything about it for now

def projFrame(self):
    
    self.x += self.xv;
    self.y += self.yv;
    
    self.rect.x = self.x;
    self.rect.y = self.y;
    if self.y < 0:
        projectiles.remove(self);
    
def textFrame(self):
    
    if pygame.Rect.collidepoint(self.rect, (mx, my)) and self.text == "Start" and mouseD:
        setupGame();
        
        

# create the menu's text
def makeMenu():
    
    createText("Space Invaders", y = 100);
    createText("Start", y = 274);
    
    
def menu():
    if mouseD:
        pass#if mx >
    
def setupGame():
    global text, gameState;
    text = [];
    
    
    i = 3;
    while i > 0:
        screen.fill(BGCOLOR);
        createText(str(i), y = sH / 2 - 20);
        screen.blit(text[0].img, (text[0].x, text[0].y));
        pygame.display.update();
        time.sleep(0.5);
        text = [];
        
        i -= 1;
    screen.fill(BGCOLOR);
    createText("Start!", y = sH / 2 - 20)
    screen.blit(text[0].img, (text[0].x, text[0].y))
    pygame.display.update();
    time.sleep(0.5);
    text = [];
    
    
    
    gameState = "game";
    
    






    



def screenThings():
    screen.fill(BGCOLOR) # clears the stuff off the screen, disable this if you want to see something fun...
    # render things
    
    
    
    for i in text:
        textFrame(i);
        screen.blit(i.img, (i.x, i.y))
    if gameState == "game":
        screen.blit(plr.img, (plr.x, plr.y));
        for i in enemies:
            screen.blit(i.img, (i.x, i.y));
        for i in projectiles:
            screen.blit(i.img, (i.x, i.y));
    # show mouse position
    mpos1 = font.render(str(pygame.mouse.get_pos()[0]) + " " + str(pygame.mouse.get_pos()[1]), False, BLUE)
    mpos1W = int(mpos1.get_size()[0] / 4);
    mpos1H = int(mpos1.get_size()[1] / 4);
    mpos1 = pygame.transform.scale(mpos1, (mpos1W, mpos1H))
    screen.blit(mpos1, (mx + 30, my))
    pygame.display.flip();
    

def game():
        
    plrFrame();
    screen.blit(plr.img, (round(plr.x), round(plr.y)));
    
    for i in enemies:
        enemyFrame(i);
        screen.blit(i.img, (round(i.x), round(i.y)));
        
    for i in projectiles:
        projFrame(i);
        screen.blit(i.img, (round(i.x), round(i.y)));
    
    
#this is where we call things, don't assign values / functions below here

makeMenu();

pygame.display.set_caption("space invaders go weeee");









running = True;

while running:
    
    screenThings();
    clock.tick(FPS);
    
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
        menu();
        
    if gameState == "game":
        game();
pygame.quit();





