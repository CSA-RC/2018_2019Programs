import pygame, sys
from pygame.locals import *
import random

pygame.init()
windowwidth = 500
windowheight = 400

screen = pygame.display.set_mode((windowwidth, windowheight))

#            R    G    B
GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)
BLACK    = (  0,   0,   0)

class Button:

    def __init__(self, x, y, height, width, color):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color
        self.rect = Rect(self.x, self.y, self.width, self.height)


    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)


    def write(self, textcolor, script, fonttype, size):
        text = pygame.font.SysFont(fonttype, size)
        textSurfaceObj = text.render(script, True, textcolor)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (((self.width / 2) + self.x), ((self.height / 2) + self.y))
        screen.blit(textSurfaceObj, textRectObj)

    def click(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos[0], mouse_pos[1])
px = 50
py = 100
sonic = pygame.image.load('fastsmith.png')
rx, ry = sonic.get_size()
player = pygame.Rect(px, py, rx, ry)

quitButton = Button(10, 10, 50, 100, CYAN)
saveButton = Button(200, 10, 50, 100, CYAN)
loadButton = Button(390, 10, 50, 100, CYAN)

moveLeft = False
moveRight = False
moveUp = False
moveDown = False

MOVESPEED = 6

while True:
    screen.fill(BLACK)
    screen.blit(sonic, (px, py))
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            # change the keyboard variables
            if event.key == K_LEFT or event.key == ord('a'):
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT or event.key == ord('d'):
                moveLeft = False
                moveRight = True
            if event.key == K_UP or event.key == ord('w'):
                moveDown = False
                moveUp = True
            if event.key == K_DOWN or event.key == ord('s'):
                moveUp = False
                moveDown = True
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == ord('a'):
                moveLeft = False
            if event.key == K_RIGHT or event.key == ord('d'):
                moveRight = False
            if event.key == K_UP or event.key == ord('w'):
                moveUp = False
            if event.key == K_DOWN or event.key == ord('s'):
                moveDown = False
            if event.key == K_SPACE:
                py = random.randint(0, windowheight - ry)
                px = random.randint(0, windowwidth - rx)
        if event.type == MOUSEBUTTONUP:
            if quitButton.click(pygame.mouse.get_pos()):
                pygame.quit()
                sys.exit()
            if saveButton.click(pygame.mouse.get_pos()):
                sx = px
                sy = py
            if loadButton.click(pygame.mouse.get_pos()):
                px = sx
                py = sy
            else:
                px, py = pygame.mouse.get_pos()
                px -= rx/2
                py -= ry/2




    if moveDown and (py + ry) < windowheight:
        py += MOVESPEED
    if moveUp and py > 0:
        py -= MOVESPEED
    if moveLeft and px > 0:
        px -= MOVESPEED
    if moveRight and (px + rx) < windowwidth:
        px += MOVESPEED


    quitButton.draw()
    quitButton.write(WHITE, "Quit", "arial", 28)

    saveButton.draw()
    saveButton.write(WHITE, "Save", "arial", 28)

    loadButton.draw()
    loadButton.write(WHITE, "Load", "arial", 28)

    pygame.display.update()