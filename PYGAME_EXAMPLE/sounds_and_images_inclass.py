import pygame, sys, random
from pygame.locals import *

# Set up pygame
pygame.init()
mainClock = pygame.time.Clock()

WINDOWWIDTH = 600
WINDOWHEIGHT = 600
windowSurface = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT),0,32)
pygame.display.set_caption('Images and Sounds')


#Set up color
BLACK = (0,0,0)
GREEN = (0,255,0)
WHITE = (255,255,255)

# Here is where we set up the player and food structure
foodCounter = 0
FOODSIZE = 25
NEWFOOD = 40
player = pygame.Rect(250,200,50,50)
playerImage = pygame.image.load('player.png')
playerStrechedImage = pygame.transform.scale(playerImage,(40,40))
foodImage = pygame.image.load('cherry.png')
foods = []
for i in range(20):
    foods.append(pygame.Rect(random.randint(0,WINDOWWIDTH-FOODSIZE),random.randint(0,WINDOWHEIGHT-FOODSIZE),FOODSIZE,FOODSIZE))

# Set up the movement variables
moveLeft = False
moveRight = False
moveUp = False
moveDown = False

MOVESPEED = 10

# Set up the music
pickUpSound = pygame.mixer.Sound('pickup.wav')
pygame.mixer.music.load('background.mid')
pygame.mixer.music.play(-1,0.0)
musicPlaying = True

#Run the game loop
while True:
    #Checking for events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            #Change the movement variables
            if event.key == K_LEFT or event.key == K_a:
                moveLeft = True
                moveRight = False
            if event.key == K_RIGHT or event.key == K_d:
                moveLeft = False
                moveRight = True
            if event.key == K_UP or event.key == K_w:
                moveDown = False
                moveUp = True
            if event.key == K_DOWN or event.key == K_s:
                moveDown = True
                moveUp = False

        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == K_a:
                moveLeft = False
            if event.key == K_RIGHT or event.key == K_d:
                moveRight = False
            if event.key == K_UP or event.key == K_w:
                moveUp = False
            if event.key == K_DOWN or event.key == K_s:
                moveDown = False
            if event.key == K_x:
                player.top = random.randint(0,WINDOWHEIGHT-player.height)
                player.left = random.randint(0,WINDOWWIDTH-player.width)
            if event.key == K_m:
                if musicPlaying:
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play(-1,0.0)
                musicPlaying = not musicPlaying

        if event.type == MOUSEBUTTONUP:
            foods.append(pygame.Rect(random.randint(0,WINDOWWIDTH),random.randint(0,WINDOWHEIGHT),FOODSIZE,FOODSIZE))

    foodCounter += 1
    if foodCounter >= NEWFOOD:
        #ADD NEW FOOD
        foodCounter = 0
        foods.append(pygame.Rect(random.randint(0,WINDOWWIDTH-FOODSIZE),random.randint(0,WINDOWHEIGHT-FOODSIZE),FOODSIZE,FOODSIZE))

    # Draw the white background
    windowSurface.fill(WHITE)

    #Move the player
    if moveDown and player.bottom<WINDOWHEIGHT:
        player.top += MOVESPEED
    if moveUp and player.top > 0:
        player.top -= MOVESPEED
    if moveLeft and player.left >0:
        player.right -= MOVESPEED
    if moveRight and player.right < WINDOWWIDTH:
        player.right += MOVESPEED

    #Draw the player onto the surface
    #pygame.draw.rect(windowSurface,BLACK,player)
    windowSurface.blit(playerStrechedImage,player)

    #Checking wether our player is eating/touching any other food squares
    for food in foods[:]:
        if player.colliderect(food):
            foods.remove(food)
            #add effects to the player in here
            player = pygame.Rect(player.left,player.top,player.width+2,player.height+2)
            playerStrechedImage = pygame.transform.scale(playerImage,(player.width,player.height))
            if musicPlaying:
                pickUpSound.play()

    # Drawing the food
    for food in foods:
        windowSurface.blit(foodImage,food)

    #Draw the window onto the screen
    pygame.display.update()
    mainClock.tick(40)

