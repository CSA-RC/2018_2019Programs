"""
    #todo add text here (program v.0.0.0)
    Copyright (C) 2018  Ryan I Callahan

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import pygame, sys
from pygame.locals import *

pygame.init()
FPS = 100 # frames per second setting
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((400, 300))

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


quitButton = Button(150, 130, 50, 100, RED)
sansButton = Button(40, 70, 50, 100, CYAN)
yeeButton = Button(150, 70, 50, 100, YELLOW)
megaButton = Button(260, 70, 50, 100, YELLOW)

yee_sound = pygame.mixer.Sound('yee.wav')
sans_sound = pygame.mixer.Sound('voice_sans.wav')
pygame.mixer.music.load('megalovania.mp3')
while True:

    screen.fill(BLACK)

    quitButton.draw()
    quitButton.write(PURPLE, "quit", "arial", 32)

    sansButton.draw()
    sansButton.write(BLUE, "sans", "arial", 32)

    yeeButton.draw()
    yeeButton.write(ORANGE, "yee", "arial", 32)

    megaButton.draw()
    megaButton.write(RED, "MEGALOVANIA", "arial", 10)


    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONUP:
            if quitButton.click(pygame.mouse.get_pos()):
                pygame.quit()
                sys.exit()
            if sansButton.click(pygame.mouse.get_pos()):
                pygame.mixer.music.stop()
                sans_sound.play(5)
            if yeeButton.click(pygame.mouse.get_pos()):
                pygame.mixer.music.stop()
                yee_sound.play()
            if megaButton.click(pygame.mouse.get_pos()):
                pygame.mixer.music.play(-1, 0.0)



    pygame.display.update()
    fpsClock.tick(FPS)