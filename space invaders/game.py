#Imported items
import random
import time
import turtle

s = turtle.getscreen();
t = turtle.Turtle();
big1 = "images/big1.gif";
big2 = "images/big2.gif";
turtle.addshape(big1);
turtle.addshape(big2);
while True:
    t.shape(big1)
    time.sleep(0.1);
    t.shape(big2);
    time.sleep(0.1);