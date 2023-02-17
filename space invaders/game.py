
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

# this checks for the path to use with stuff cuz it was wierd at my house
if os.path.exists("D:/programming stuff/space invaders"):
    hP = "D:/programming stuff/space invaders/";
else:
    hP = "";

# get which path to use cuz programming at home is diff
clock = pygame.time.Clock();
font = pygame.font.Font(hP + "fonts/PressStart2P-Regular.ttf", 32)
print(font)
def randnum(s = 1, e = 15):
    return random.randint(s, e);

#Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (1, 50, 32)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SPACE_BLUE = (31, 66, 119)
BGCOLOR = BLACK
STARCOLOR = WHITE
FPS = 60;
gameState = "menu"; # can be "menu", "game", or "gameover"

sW, sH = 800, 600;
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
MOTHERSHIP = [pygame.image.load(hP + "images/mothership.png")];
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
    
star()


class obj:
    
    def __init__(self, x = sW / 2, y = sH / 2, hp = 1.0, color = GREEN, img = BLANK, w = 32, h = 32, anim = False, deathImg = ALIENDIE, animDelay = 5):
        
        self.x = x;
        self.y = y;
        self.xv = 0.0;
        self.yv = 0.0;
        self.hp = hp;
        self.color = color;
        self.w = w;
        self.h = h;
        self.img = img;
        self.dieDelay = 0;
        self.deathImg = deathImg;
        self.rect = pygame.rect.Rect(int(self.x), int(self.y), int(self.w), int(self.h));
        self.anim = anim;
        
        if anim:
            self.animDelay = animDelay;
            self.currentAnim = 0;
            for i in img:
                
                self.img[i] = pygame.transform.scale(self.img[i], (self.w, self.h));
                self.img[i].fill(GREEN, self.rect, 1);
                
                
        else:
            
            self.img = self.img[0];
            self.img = pygame.transform.scale(self.img, (self.w, self.h))
            self.rect.width = self.w + 50;
            self.rect.height = self.h;
            
            self.rect.x = -50;
            self.rect.y = 0;

            self.img.fill(self.color, self.rect, 1);
            
            
        
        
        self.rect = pygame.rect.Rect(int(self.x), int(self.y), int(self.w), int(self.h));
        
    def deathAnim(self):
        self.img = self.deathImg;
        self.img = pygame.transform.scale(self.img, (int(self.w + (self.w / 3)), int(self.h)));
        
        self.rect.w = self.w + 50;
        self.rect.x = -50;
        self.rect.y = 0;
        
        
        self.img.fill(WHITE, self.rect, 1);
        
        
        self.dieDelay = 20;
            
            

def createText(textVal = "none", x = sW / 2, y = sH / 2, centered = True, color = GREEN, size = 1):
    
    global text;
    n = obj(x, y, color);
    n.w = 20;
    n.img = font.render(textVal, False, n.color);
    n.text = textVal;
    n.w, n.h = 3, 3;
    #n.w, n.h = font.size(textVal);
    
    if centered:
        n.x -= n.w / 2;
    
    n.rect.x = int(n.x);
    n.w = 20;
    n.h = 20;
    n.rect.w, n.rect.h = n.w, n.h;
    
    
    text.append(n);
    

def createEnemy(x = sW / 2, y = sH / 2, hp = 1.0, color = GREEN, img = BLANK, w = 32, h = 32, xv = 0, yv = 0, type = "norm", anim = False):
    
    global enemies;
    n = obj(x, y, hp, color, img, w, h);
    n.type = type;
    n.xv = xv;
    n.yv = yv;
    
    
    enemies.append(n);

def createEnemyRow(x = 15, y = 15, count = 8, img = BLANK, color = GREEN, anim = False):
    
    global espd
    i = 0;
    xv = espd;
    while i < count:
        createEnemy(x, y, img = img, color = color, xv = xv, type = "norm", anim = anim);
        x += 64;
        i += 1;
        



def createProj(x = sW / 2, y = sH / 2, hp = 1.0, color = GREEN, img = BLANK, w = 3, h = 16, dmgT = "plr", yv = -5):
    
    global projectiles;
    n = obj(x, y , hp, color, img, w, h);
    n.dmgT = dmgT;
    n.yv = yv;
    
    
    projectiles.append(n);

def createMShip(x = sW / 2, y = sH / 2, hp = 1.0, color = (0, 150, 0), img = MOTHERSHIP, w = 64, h = 64, deathImg = MOTHERSHIPDIE):

    global enemies
    n = obj(x, y, hp, color, img, w, h, deathImg = deathImg);
    n.y = randnum(0, 100);

    if randnum(0,1) == 1:
        n.x = -n.w;
        n.xv = 5;
    else: 
        n.x = sW;
        n.xv = -5
    
    n.type = "mShip";


    enemies.append(n);
        




 

createEnemyRow(img = ALIEN1, color = GREEN, anim = True)


plr = obj(sW / 2 - 32, sH - 32, 1.0, GREEN, PLAYERSHIP, 32, 32, deathImg = PLAYERDIE);
plr.shootDel = 0;
plr.lives =  3;






plrRect = pygame.Rect(200, 200, plr.w, plr.h);
pBul = pygame.Rect(int(plr.x), int(plr.y), 5, 5);



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
        
        createProj(x = plr.x + plr.w/2 - 2.5, y = plr.y, img = TESTIMG, dmgT = "plr", yv = -10, color = WHITE);
        
        plr.shootDel = 50;


    
   
   
#player getting murdered stuff   d
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
    
    pygame.draw.line(screen, RED, (plr.x, plr.y), (0, 0), 30); #trying to make a laser for aim assistance
    
    if collide(plr.rect, useList = True, list = projectiles):
        pass

    plrInput();
    if plr.shootDel > 0:
        plr.shootDel -= 1;


def enemyFrame(self):
    
    self.x += self.xv;
    self.y += self.yv;
    
    if self.type == "norm":
        if randnum(1, 300) == 1:
            createProj(self.x + self.w / 2, self.y, img = TESTIMG, dmgT = "enemy", yv = 5);
    
    if self.type == "mShip":
        if self.x > sW or self.x < -self.w:
            enemies.remove(self)

    if self.dieDelay == 0 and self.type == "norm":
        
        if self.x >= sW - self.w:
            self.xv = -espd;
            self.y += randnum(6, lvl + 9)
            if randnum(1, 1) == 1 and enemies[0] == self:
                createMShip();
        if self.x <= 0:
            self.xv = espd;
            self.y += randnum(6, lvl + 9);
            if randnum(1, 1) == 1 and enemies[0] == self:
                createMShip();
    
    if self.y > plr.y:
        plr.deathAnim();
            

    if self.dieDelay > 0:
        self.xv, self.yv = 0, 0;



    


    
    self.rect.x = int(self.x);
    self.rect.y = int(self.y);
    
    if self.dieDelay > 1:
        self.dieDelay -= 1;
        if self.dieDelay == 1:
            enemies.remove(self);
    for i in projectiles:
        if collide(self.rect, i.x, i.y) and self.dieDelay == 0 and i.dmgT == "plr":

            self.deathAnim();
            projectiles.remove(i);
    
    # other things gonna happen here

    #mothership things

def mShipFrame():
    pass

    if enemies.x <= sW or enemies.x >= 5:
        pass
        
    


    


# collision is already handled by pygame, don't do anything about it for now

def projFrame(self):
    
    self.x += self.xv;
    self.y += self.yv;
    
    
    self.rect.x = 0;
    self.rect.y = 0;
    if self.y < 0 or self.y > sH or self.x < 0 or self.x > sW:
        projectiles.remove(self);
    
def textFrame(self):
    
    if collide(self.rect, mx, my) and self.text == "Start" and mouseD:
        setupGame();
        
        

# create the menu's text
def makeMenu():
    
    createText("Space Invaders", y = 100);
    createText("Start", y = 274);
    
    
    

    
def setupGame():
    global text, gameState, score;
    text = [];
    
    
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
    
    createText("Score: " + str(score), y = sH -100, size = 0.3);
    
    gameState = "game";
    
    

def plrDieChecker(self = players):
    if collide(plr.rect, useList = True, list = enemies):
        plr.lives -= 1
        if plr.lives == 0:
            gameOver()
    if collide(plr.rect, useList= True, list = projectiles):
        plr.lives -= 1
        print("I've Been discombobulated and also beans")
        if plr.lives == 0:
            gameOver()
    if self.y > plr.y:
        plr.lives -=1
        if plr.lives == 0:
            gameOver()
            
                



def gameOver():
    createText("Game Over", y = 274)
    time.sleep(5.0)
    




def screenThings():
    screen.fill(BGCOLOR) # clears the stuff off the screen, disable this if you want to see something fun...
    # render things
    global enemies, projectiles
    
    
    for i in text:
        textFrame(i);
        screen.blit(i.img, (int(i.x), int(i.y)))
    if gameState == "game":
        screen.blit(plr.img, (int(plr.x), int(plr.y)));
        for i in enemies:
            if i.anim:
                screen.blit(i.img[i.currentAnim], (int(i.x), int(i.y)));
            else:
                screen.blit(i.img, (int(i.x), int(i.y)));
            
        for i in projectiles:
            screen.blit(i.img, (int(i.x), int(i.y)));
            
    # show mouse position
    mpos1 = font.render(str(pygame.mouse.get_pos()[0]) + " " + str(pygame.mouse.get_pos()[1]), False, BLUE)
    mpos1W = int(mpos1.get_size()[0] / 4);
    mpos1H = int(mpos1.get_size()[1] / 4);
    mpos1 = pygame.transform.scale(mpos1, (mpos1W, mpos1H))
    screen.blit(mpos1, (int(mx) + 30, int(my)));
    pygame.display.flip();
    

def game():
    global enemies, projectiles
    plrFrame();
    
    
    for i in enemies:
        enemyFrame(i);
        
        
    for i in projectiles:
        projFrame(i);
        
    
    
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
        pass
        
    if gameState == "game":
        game();
pygame.quit();





