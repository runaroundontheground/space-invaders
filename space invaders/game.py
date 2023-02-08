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
Font = pygame.font.Font("font/PressStart2P-Regular.ttf", 64)

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
BLUE = (0, 255, 0)
GREEN = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60;
spd = 3; #speed for player
mxspd = 5; #player max speed
bspd = 10; #projectile speed
espd = 3; #enemy speed
maxBullets = 1;
plrBul = [];

#images
plrW, plrH = 32, 32;
plrImg = pygame.image.load(os.path.join("images", "player.png" ));
plrImg = pygame.transform.scale(plrImg, (plrW, plrH));
plrRect = pygame.Rect(200, 200, plrW, plrH);
plr = {
    "x": 0.0,
    "y": 0.0,
    "xv": 0.0,
    "yv": 0.0
    };
pBul = pygame.Rect(round(plr["x"]), round(plr["y"]), 5, 5);

plr["xv"] = 1;

def plrMove():
    #player movement
    global sW, sH, spd, pBul, bspd, mxspd;
    keys = pygame.key.get_pressed()

    if keys[pygame.K_d] and plr["x"] - spd  > 0: #go right
        if plr["xv"] < mxspd:
            plr["xv"] += spd;

    if keys[pygame.K_a] and plr["x"] + spd + plrW  < sW: #go left
       if plr["xv"] > -mxspd:
        plr["xv"] -= spd;

    if (not keys[pygame.K_d] and not keys[pygame.K_a]) or (keys[pygame.K_d] and keys[pygame.K_a]):
        plr["xv"] -= plr["xv"] / 5;

    if plr["x"] < 0:
        plr["xv"] = 1.0;

    if plr["x"] > sW:
        plr["xv"] = -1.0;

    if keys[pygame.K_SPACE] and len(pBul) < maxBullets: #shoot a bullet if there's not a playr bullet alread on screen
        #pBul = pygame.Rect(plrRect.x + plrW, plr.y + plrH/2 -2, 10, 5) 
        pBul.append(plrBul)

    if pBul.y > 0: #if bullet y is not off top of screen
        pBul.y += bspd


bigImg = pygame.image.load(os.path.join("images", "big.png"))   
bigW, bigH = 32, 32;
big = pygame.transform.scale(bigImg, (bigW, bigH))
bigRect = pygame.Rect(100, 100, bigW, bigH);



"""
def bCollision(pBul, eBul, plrRect, bigRect, smallRect): #still need to define eBul, and smallRect


"""

#collision is already handled by pygame, don't do anything about it for now



#menu things

def menu():
    menuText = Font.render("SPACE INVADERS", True, GREEN, BLUE)
    menuTextRect = menuText.get_rect();
    screen.blit(menuText, menuTextRect)

    



#input thingys


    



def screenThings():
    screen.fill(RED) # reset window maybe
    # render things
    plr["x"] += plr["xv"];
    plr["y"] += plr["yv"];
    screen.blit(plrImg, (round(plr["x"]), round(plr["y"])));
    #for length of enemies:
    #screen.blit(enemies[i], enemies[i]but get x)
    #screen.blit()
    # update positions?
    pygame.display.update();

#this is where we call things, don't assign values / functions below here

pygame.display.set_caption("AAAAA");
running = True;
while running:
    screenThings();
    plrMove();
    clock.tick(FPS);
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False;
    if gameState == "menu":
        menu();
    if gameState == "game":
        pass
    
pygame.quit();
#while gameState == "gameover":
#   pass




