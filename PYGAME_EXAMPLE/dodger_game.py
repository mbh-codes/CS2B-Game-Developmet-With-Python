
import pygame, sys, random
from pygame.locals import *

# Set up pygame
pygame.init()
mainClock = pygame.time.Clock()

# Set up the window
WINDOWWIDTH = 600
WINDOWHEIGHT = 600
#making window surface to fullscreen
windowSurface = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT),pygame.FULLSCREEN)
pygame.display.set_caption('Dodger')
pygame.mouse.set_visible(False)
#setting up frames per second
FPS = 60
#setting up variables for our badman
BADDIEMINSIZE = 10
BADDIEMAXSIZE = 40
BADDIEMINSPEED = 1
BADDIEMAXSPEED = 8
ADDNEWBADDIERATE = 6
baddieAddCounter = 0
#Establish how many pixels our player moves
PLAYERMOVERATE = 5

# Set up the colors
BACKGROUNDCOLOR = (255,255,255)
TEXTCOLOR = (0,0,0)
GREEN = (0,255,0)


# Set up the player and food data structures
foodCounter = 0
NEWFOOD = 40
FOODSIZE = 20
player = pygame.Rect(300,100,40,40)
playerImage = pygame.image.load('player.png')
playerStretchedImage = pygame.transform.scale(playerImage,(40,40))
foodImage = pygame.image.load('cherry.png')
baddieImage = pygame.image.load('baddie.png')
foods = []
for i in range(20):
    foods.append(pygame.Rect(random.randint(0,WINDOWWIDTH-FOODSIZE),random.randint(0,WINDOWHEIGHT-FOODSIZE),FOODSIZE,FOODSIZE))

# Set up movement variables
moveLeft = False
moveRight = False
moveUp = False
moveDown = False

MOVESPEED = 6

# Set up the music
pickUpSound = pygame.mixer.Sound('pickup.wav')
pygame.mixer.music.load('background.mid')
pygame.mixer.music.play(-1,0.0)
musicPlaying = True

#function for stopping the game
def terminate():
    pygame.quit()
    sys.exit()

#Keeping track of the player colliding with baddies
def playerHasHitBaddie(playerRect,baddies):
    for b in baddies:
        if playerRect.colliderect(b['rect']):
            return True
    return False




baddies = []
#Run the game loop
while True:
    #Check for events
    for event in pygame.event.get():
        if event.type == QUIT:
            terminate()

        if event.type == KEYDOWN:
            #Change the keyboard variabls
            if event.key == K_LEFT or event.key == K_a:
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT or event.key == K_d:
                moveLeft = False
                moveRight = True
            if event.key == K_UP or event.key == K_w:
                moveDown = False
                moveUp = True
            if event.key == K_DOWN or event.key == K_s:
                moveUp = False
                moveDown = True

        if event.type == KEYUP:
            if event.key == K_ESCAPE:
               terminate()
            if event.key == K_LEFT or event.key == K_a:
                moveLeft = False
            if event.key == K_RIGHT or event.key == K_d:
                moveRight = False
            if event.key == K_UP or event.key == K_w:
                moveUp = False
            if event.key == K_DOWN or event.type == K_s:
                moveDown = False
            if event.key == K_x:
                player.top = random.randint(0,WINDOWHEIGHT-player.height)
                player.left = random.randint(0,WINDOWWIDTH-player.width)
            #Handling when m button is pressed
            if event.key == K_m:
                if musicPlaying:
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play(-1,0.0)
                musicPlaying = not musicPlaying

        if event.type == MOUSEBUTTONUP:
            foods.append(pygame.Rect(event.pos[0],event.pos[1],FOODSIZE,FOODSIZE))
    foodCounter += 1
    if foodCounter >= NEWFOOD:
        #Add new food
        foodCounter = 0
        foods.append(pygame.Rect(random.randint(0,WINDOWWIDTH-FOODSIZE),random.randint(0,WINDOWHEIGHT-FOODSIZE),FOODSIZE,FOODSIZE))
    #add new baddies
    baddieAddCounter += 1
    if baddieAddCounter == ADDNEWBADDIERATE:
        baddieAddCounter = 0
        baddieSize = random.randint(BADDIEMINSIZE,BADDIEMAXSIZE)
        newBaddie = {'rect':pygame.Rect(random.randint(0,WINDOWWIDTH-baddieSize),0-baddieSize,baddieSize,baddieSize),'speed':random.randint(BADDIEMINSPEED,BADDIEMAXSPEED),'surface':pygame.transform.scale(baddieImage,(baddieSize,baddieSize)),}

    #Move the player
    if moveDown and player.bottom<WINDOWHEIGHT:
        player.top += MOVESPEED
    if moveUp and player.top > 0:
        player.top -= MOVESPEED
    if moveLeft and player.left > 0:
        player.right -= MOVESPEED
    if moveRight and player.right < WINDOWWIDTH:
        player.right += MOVESPEED

    #Move the baddies down
    for b in baddies:
        b['rect'].move_ip(0,b['speed'])

    #delete the baddies
    for b in baddies[:]:
        if b['rect'].top > WINDOWHEIGHT:
            baddies.remove(b)


    #Draw the white background onto the surface
    windowSurface.fill(BACKGROUNDCOLOR)


    #Draw the player onto the surface. #Changed
    windowSurface.blit(playerStretchedImage,player)

    #Draw each baddie
    for b in baddies:
        windowSurface.blit(b['surface'],b['rect'])


    # Check wether the player has his with any food squares
    for food in foods[:]:
        if player.colliderect(food):
            foods.remove(food)
            #adding effects to the player
            player = pygame.Rect(player.left,player.top,player.width + 2, player.height + 2)
            playerStretchedImage = pygame.transform.scale(playerImage,(player.width,player.height))
            if musicPlaying:
                pickUpSound.play()



    # Draw the food.
    for i in range(len(foods)):
        pygame.draw.rect(windowSurface,GREEN,foods[i])


    #Draw the window onto the screen
    pygame.display.update()
    mainClock.tick(40)
