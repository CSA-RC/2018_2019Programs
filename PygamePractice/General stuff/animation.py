import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 100 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)
catImg = pygame.image.load('sanic.png')
catx = 10
caty = 10
direction = 'right'
text = pygame.font.SysFont('Comic Sans MS', 32)
textSurfaceObj = text.render('Hello world!', True, (0,255,0), (0,0,255))
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200, 150)
while True: # the main game loop
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)


    if direction == 'right':
        catx += 7
        if catx == 290:
            direction = 'down'
    elif direction == 'down':
        caty += 7
        if caty == 220:
            direction = 'left'
    elif direction == 'left':
        catx -= 7
        if catx == 24:
            direction = 'up'
    elif direction == 'up':
        caty -= 7
        if caty == 24:
            direction = 'right'

    DISPLAYSURF.blit(catImg, (catx, caty))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)