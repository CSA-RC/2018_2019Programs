import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 100 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')


pygame.mixer.music.load('megalovania.wav')
pygame.mixer.music.play(-1, 0.0)

sound = pygame.mixer.Sound('tumpunch.wav')
color = (255, 255, 255)
catImg = pygame.image.load('smallsans.png')
catx = 1
caty = 100
direction = 'right'
DISPLAYSURF.fill(color)
while True: # the main game loop
    DISPLAYSURF.fill(color)


    if direction == 'right':
        catx += 7
        if catx == 309:
            direction = 'left'
            sound.play()
            color = (255,255,255)

    elif direction == 'left':
        catx -= 7
        if catx == 15:
            direction = 'right'
            sound.play()
            color = (0,0,0)


    DISPLAYSURF.blit(catImg, (catx, caty))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)