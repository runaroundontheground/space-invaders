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
font = pygame.font.Font("font/PressStart2P-Regular.ttf", 64)

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

    if keys[pygame.K_d] and plr["x"] > 0: #go right
        if plr["xv"] < mxspd:
            plr["xv"] += spd;

    if keys[pygame.K_a] and plr["x"] + plrW  < sW: #go left
       if plr["xv"] > -mxspd:
        plr["xv"] -= spd;
    
    if keys[pygame.K_w] and plr["y"] > sH - 200: # go up
        if plr["yv"] > -mxspd:
            pass

    if (not keys[pygame.K_d] and not keys[pygame.K_a]) or (keys[pygame.K_d] and keys[pygame.K_a]):
        plr["xv"] -= plr["xv"] / 5;

    if plr["x"] < 0:
        plr["x"] += 1
        plr["xv"] = 0.0;
        

    if plr["x"] > sW:
        plr["x"] -= 1
        plr["xv"] = 0.0;
    if keys[pygame.K_SPACE] and len(plrBul) < maxBullets: #shoot a bullet if there's not a playr bullet alread on screen
        #pBul = pygame.Rect(plrRect.x + plrW, plr.y + plrH/2 -2, 10, 5) 
        pBul.append(plrBul)
    
    
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



#menu things
def makeMenu():
    menuText = [
        "0": {
            "text": font.render("Space Invaders", True, BLACK),
            "pos": (100, 100)
            },
        "1": {
            "text": font.render("Start", False, BLACK),
            "pos": (296, 274)
        }
    ];
    
    text.append(menuText);
    
def menu():
    pass
    
    
    






    



def screenThings():
    screen.fill(GREEN) # reset window maybe
    # render things
    plr["x"] += plr["xv"];
    plr["y"] += plr["yv"];
    screen.blit(plrImg, (round(plr["x"]), round(plr["y"])));
    
    i = 0;
    while i < len(text):
        screen.blit(text[i][str(i)]["text"], text[i][str(i)]["pos"])
        i += 1;
    
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