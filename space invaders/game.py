#Imported items
import math
import random
import time
import pygame
import os
#variables go here
def setup(): #make the game ready
    
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
    KEYDOWN,
    QUIT
    )

setup();

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
FPS = 60;

gameState = "menu"; # can be "menu", "game", or "gameover"
sW, sH = 800, 600;
screen = pygame.display.set_mode((sW, sH));

projectiles = [];
text = [];
enemies = [];


PLAYERSHIP = pygame.image.load(hP + "images/player.png");
ALIEN1 = pygame.image.load(hP + "images/alien1.png");
#ALIEN2 = pygame.image.load(os.path.join("images", "alien2.png"))
BLANK = pygame.image.load(hP + "images/blank.png");



class obj:
    
    def __init__(self, x = sW / 2, y = sH / 2, hp = 1.0, color = BLACK, img = BLANK, w = 32, h = 32):
        
            self.x = x;
            self.y = y;
            self.xv = 0.0;
            self.yv = 0.0;
            self.hp = hp;
            self.color = color;
            self.img = img;
            self.w = w;
            self.h = h;
            pygame.transform.scale(self.img, (self.w, self.h));
            def destroy():
                pass

def createEnemy(x = None, y = None, hp = None, color = None, img = BLANK, w = 32, h = 32):
    global enemies;
    n = obj(x, y, hp, color, img, w, h);
    n.img = pygame.transform.scale(n.img, (n.w, n.h));
    enemies.append(n);

def createProjectile(x = None, y = None, hp = None, color = None, img = BLANK, w = 32, h = 32):
    global projectiles;
    n = obj(x, y , hp, color, img, w, h);
    n.img = pygame.transform.scale(n.img, (n.w, n.h));
    projectiles.append(n);






createEnemy(img = ALIEN1)

plr = obj(sW / 2 - 32, sH - 32, 1.0, BLACK, PLAYERSHIP, 32, 32);
plr.img = pygame.transform.scale(plr.img, (plr.w, plr.h));

spd = 1; #speed for player
mxspd = 3; #player max speed
bspd = 10; #projectile speed
espd = 3; #enemy speed
maxBullets = 1;




plrRect = pygame.Rect(200, 200, plr.w, plr.h);
pBul = pygame.Rect(round(plr.x), round(plr.y), 5, 5);



def plrMove():
    #player movement
    global sW, sH, spd, pBul, bspd, mxspd;
    keys = pygame.key.get_pressed()

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
        plr.x += 1.0;
        # IDEA!!!!: player loops around the screen, go off edge and you come out the other side
        plr.xv = 12.0; # player go bounce
        
    if plr.x > sW - plr.w: # push player outta the right edge of the screen
        plr.x -= 1.0;
        plr.xv = -12.0;
        
    if plr.y > sH - plr.h: # push player outta the bottom edge of the screen
        plr.y -= 0.1;
        plr.yv = 0.0;
    
    if plr.y < sH - 50: # push player outta the top limit of ur movement
        plr.y += 0.1;
        plr.yv = 0.0;
        
    if keys[pygame.K_SPACE] and len(projectiles) < maxBullets: #shoot a bullet if there's not a playr bullet alread on screen
        #pBul = pygame.Rect(plrRect.x + plr.w, plr.y + plr.h/2 -2, 10, 5) 
        #pBul.append(plrBul)
        pass
    
    
    if pBul.y > 0: #if bullet y is not off top of screen
        pBul.y += bspd
    #else

Alien1Count = 0;
Alien1xpos =100;
Alien1ypos = 100;

def alien1():
    
    alien1Img = ALIEN1; 
    alien1W, alien1H = 32, 32;
    alien1 = pygame.transform.scale(alien1Img, (alien1W, alien1H))
    while Alien1Count < 8:
        #alien1Rect = pygame.Rect(Alien1xPos, Alien1yPos, alien1W, alien1H);
        #alien1xpos += 3
        #Alien1Count += 1
        if Alien1Count < 8:
            break
        
    
"""
plrAlive = True
while plrAlive:
    while alien1xpos < 790:
        clock.tick(FPS);
        alien1xpos += 6
    while alien1xPos > 10:
        clock.tick(FPS);
        alien1xpos -= 6

"""



#collision is already handled by pygame, don't do anything about it for now



# create the menu's text
def makeMenu():
    t1 = {
        "text": font.render("Space Invaders", False, BLACK),
        "pos": [100, 100] #middle of screen, 100 y down
    }
    t1["pos"][0] = sW / 2 - t1["text"].get_width() / 2;
    t2 = {
    "text": font.render("Start", False, BLACK),
    "pos": [296, 274]
    }
    t2["pos"][0] = sW / 2 - t2["text"].get_width() / 2;
    menuText = [t1, t2]
    text.append(menuText);
    
def menu():
    pass
    
    
    






    



def screenThings():
    screen.fill(GREEN) # clears the stuff off the screen, disable this if you want to see something fun...
    # render things
    plr.x += plr.xv;
    plr.y += plr.yv;
    screen.blit(plr.img, (round(plr.x), round(plr.y)));
    
    for i in text:
        for i in i:
            screen.blit(i["text"], i["pos"])
    
    # show mouse position
    mpos1 = font.render(str(pygame.mouse.get_pos()[0]) + " " + str(pygame.mouse.get_pos()[1]), False, BLUE)
    mpos1W = int(mpos1.get_size()[0] / 6);
    mpos1H = int(mpos1.get_size()[1] / 6);
    mpos1 = pygame.transform.scale(mpos1, (mpos1W, mpos1H))
    screen.blit(mpos1, (pygame.mouse.get_pos()[0] + 30, pygame.mouse.get_pos()[1]))
    #for length of enemies:
    #screen.blit(enemies[i], enemies[i]but get x)
    #screen.blit()
    # update positions?
    pygame.display.flip();

#this is where we call things, don't assign values / functions below here

makeMenu();
print(len(text));
pygame.display.set_caption("Frijoles Con Limon");
running = True;
while running:
    screenThings();
    plrMove();
    clock.tick(FPS);
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False;
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos());
    if gameState == "menu":
        menu();
    if gameState == "game":
        pass
    
pygame.quit();





