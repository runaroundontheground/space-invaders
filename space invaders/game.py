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
clock = pygame.time.Clock();
font = pygame.font.Font("font/PressStart2P-Regular.ttf", 32)
#debugRect = pygame.Rect(); this'll do something later

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
) # import key input stuff

gameState = "menu"; # can be "menu", "game", or "gameover"
sW, sH = 800, 600;
screen = pygame.display.set_mode((sW, sH));

#Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60;

PLAYERSHIP = pygame.image.load(os.path.join("images", "player.png"));
ALIEN1 = pygame.image.load(os.path.join("images", "alien1.png"))
#ALIEN2 = pygame.image.load(os.path.join("images", "alien2.png"))
spd = 1; #speed for player
mxspd = 3; #player max speed
bspd = 10; #projectile speed
espd = 3; #enemy speed
maxBullets = 1;
plrBul = [];
text = [];
#images
plrW, plrH = 32, 32;
plrImg = PLAYERSHIP;
plrImg = pygame.transform.scale(plrImg, (plrW, plrH));
plrRect = pygame.Rect(200, 200, plrW, plrH);
plr = {
    "x": (sW / 2) - plrW,
    "y": sH - plrH,
    "xv": 0.0,
    "yv": 0.0
    };
pBul = pygame.Rect(round(plr["x"]), round(plr["y"]), 5, 5);

plr["xv"] = 1;

def plrMove():
    #player movement
    global sW, sH, spd, pBul, bspd, mxspd;
    keys = pygame.key.get_pressed()

    if keys[pygame.K_d] and plr["x"] < sW: #go right
        if plr["xv"] < mxspd:
            plr["xv"] += spd;

    if keys[pygame.K_a] and plr["x"] > -plrW: #go left
       if plr["xv"] > -mxspd:
        plr["xv"] -= spd;
    
    if keys[pygame.K_w] and plr["y"] > sH - 50: # go up
        if plr["yv"] > -mxspd:
            plr["yv"] -= spd;
            
    if keys[pygame.K_s] and plr["y"] < sH - plrH: # go down
        if plr["yv"] < mxspd:
            plr["yv"] += spd;


    if (not keys[pygame.K_d] and not keys[pygame.K_a]) or (keys[pygame.K_d] and keys[pygame.K_a]) or abs(plr["xv"]) > mxspd:
        plr["xv"] -= plr["xv"] / 5;
    if (not keys[pygame.K_w] and not keys[pygame.K_s]) or (keys[pygame.K_w] and keys[pygame.K_s]) or abs(plr["yv"]) > mxspd:
        plr["yv"] -= plr["yv"] / 5;

    if plr["x"] < 0: # push player outta the left edge of the screen
        plr["x"] += 1.0;
        # IDEA!!!!: player loops around the screen, go off edge and you come out the other side
        plr["xv"] = 12.0; # player go bounce
        
    if plr["x"] > sW - plrW: # push player outta the right edge of the screen
        plr["x"] -= 1.0;
        plr["xv"] = -12.0;
        
    if plr["y"] > sH - plrH: # push player outta the bottom edge of the screen
        plr["y"] -= 0.1;
        plr["yv"] = 0.0;
    
    if plr["y"] < sH - 50: # push player outta the top limit of ur movement
        plr["y"] += 0.1;
        plr["yv"] = 0.0;
        
    if keys[pygame.K_SPACE] and len(plrBul) < maxBullets: #shoot a bullet if there's not a playr bullet alread on screen
        #pBul = pygame.Rect(plrRect.x + plrW, plr.y + plrH/2 -2, 10, 5) 
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
    plr["x"] += plr["xv"];
    plr["y"] += plr["yv"];
    screen.blit(plrImg, (round(plr["x"]), round(plr["y"])));
    
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
#while gameState == "gameover":
#   pass




'''
def main_menu():
    title_font = Font
    run = True
    while run:
        screen.blit(BLACK, (0,0))
        title_text = title_font.render("Click to Begin", 1, GREEN)
        screen.blit(title_text, (sW/2 - title_text.get_width()/2, 350))
        pygame.display.update()
        for event in pygame.event.get():


'''