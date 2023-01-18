#importing things and setting up screen
#from os import stat_result
import random
import time
#import os.path







# menuScreen() does menu stuff and does the screen 
	# Menu text in  Press Start 2p ← this is the font
# start button
	# When you press start button the game begins
	#other things: padding, text size, font style (already above), color
# Settings button
# Settings have a “Classic Mode” and a “Fun Mode” (If classic mode not finished say not finished)
#  exit button
# When you press exit button stops the code/exits game if it’s an exe
#def toLoc() - to location
	#changes what the UI is doing, so for example it’ll go to settings, back to the main menu, ect.
#Background
	# Background always shown with stars moving down because you fly past them maybe
	#planets in background for more variety
	#possibly different background element colors
#define game(mode, level)
	#sequencing things, these will go after defining stuff
		#while mode is “play”, run the main loop
			#updatePlayer()
			#updateEnemies()
			#updateProjectiles()
			#updateObjects() (destructables, but objects is faster to type)
	#import Random
		# chooses a num from 0 to 15 everytime enemies bump into the side  they’ll move down by the random amount and a mothership could spawn in





#defines enemies(level)
	#summon 24 enemies in a 8 long 3 tall grid pattern or summon enemy at  (x, y) then (x + 3 through 24, and y + 3 through 6)
#depending on the level, there will be different layouts locked until the level is higher and once its higher there is access to them
	#enemies will shoot and move faster/ down further based on the level/difficulty setting
	# enemies have a chance to move down each time they hit the wall and that chance increases every level
#enemies shoot after a randomized delay (lowered the higher the level/diff is)
	 	#enemies move faster based on level
		#if enemies are hit by player bullet, they get destroyed
		#If all enemies are gone, it will add 1 to level and reset

	#defines motherShip
		#spawns motherShip and it flies by
		#if it gets hit it pops displays a 100, and gives 100 points

#defines bullets (t) <- type
	#If t = “p”
		#do player bullet stuff
	#elif t = “e” (should we use elif?)
		#do enemy bullet stuff
		#bullet uses enemy types, fired by player, type = p, if it’s fired by an enemy the type will be e
		#if the bullet is fired by an enemy they go straight through other enemies but destroy the player 
#if the bullet is fired by a player the bullet destroys enemies 
		#all bullets will destroy blocks, as well as other bullets, provided they aren’t the same type
		#if the bullet touches a certain bar or color then destroy bullet
		#important: use colors for making bullets and other stuff interact, it’ll probably be easier 
		# (Isaac) i figured out how to do collisions in javascript, it cycles through a list containing the specified object you want to check                                                                                                        .                                    for, and it gets the x and y and width n stuff of the two objects to get whether it’s collided or not
		#basically: for (i = 0, i < objects.length, i++)
			#objects[i].tick()

#defines player
		#Spawn player
#def player move(r, l) (r is right, uses key d or right arrow, and l is left, uses a or left arrow)
		#note: make sure to use True and False so that it’s easier.. wait hm..
		#change player x (px) by xv
		#change player y (py) by yv (yv is normally 0)
			#get the keys, if it’s a/left arrow go left, d/right arrow go right
				#more info on movement
					#if r  then set player xv to max xv (mxv)
					#if l then set player xv to -mxv
					#if (not r AND not l) OR( r AND l) then set xv to 0, which stops player see below\
					#stop the player when they hit walls
					#friction: do we want a slightly slippery/smoother player? It’ll do xv /= 2 if not l or r until it’s abs value is less than 0.1 or something, and then it’ll set it to 0
			#firing stuff()
				#If firing delay is 0 (timer ran out)  & player bullet count is < max p bullet count
					#createBullet(p)
			#if fun mode
				#if up: go up a bit, depending on our max y height limit
				#if down: same as before but its do
				#tilt the player ship based on their x velocity (maybe)
				#use mouse to aim to a certain point (maybe)
				#any other ideas? (only the extra mode)
#If player hit by a bullet
				#check player lives and health (if it’s fun mode)
					#change player health by projectile damage
					#if player health <= 0, lose a life
#if lives becomes <= 0 after losing a life, gameOver() or reset()
			# if player has or req’d points (reqPoints is the req for getting another life, and starts at 2000 by default)
				# +1 life and  add 2000 to reqPoints, or maybe multiply it / have it be exponential
	#when game starts, choose a layout based on what level it is + the random layout type (it’d normally be 1 here)
	#set player lives to 3
	#spawn blocks
	#bullets(t)
	#player
	#enemies(level)
	#if num = 6  spawn a motherShip (num is the random number used to determine how far the enemies go down after hitting the side)
	#if fun mode true
		#Def powerUp(type)
#Have a chance of spawning a Power Up (pU) that falls from the enemies side to the player 
				#powerUp types
					#enemy freeze?
					#faster (player) bullets?
					#+health?
					#shield
					#regeneration?
					#shotgun temporarily? / multi-fire. Getting a second multifire powerup increases bullet count
#call game(mode,level)

#gameOver() or reset()
	#once it shows up have a short delay before anything can happen so you can’t accidentally click something
	#Text will say      Game Over (and your score below it)
	# Restart
		#When the player clicks on the restart button, it will send them to the game, but have a short delay so it doesn’t instantly start
	#Menu
		#When the player clicks on the menu button, It will send them to the menu ( use a fancy transition? Screen wipe?) [Maybe we could have the pixels slowly disappear and then reappear as the menu

