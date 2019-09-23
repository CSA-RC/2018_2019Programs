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
import time
import random

pygame.init()
FPS = 100 # frames per second setting
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((1000, 900))
score = 0
you_lose = False
you_win = False
wrong_count = 0

#            R    G    B
GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (230,   0, 255)
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


    def redraw(self, x, y, height, width, color):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color
        self.rect = Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)


    def click(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos[0], mouse_pos[1])

exampleshape = Button(1, 1, 1, 1, BLACK)
choice1 = Button(1, 1, 1, 1, BLACK)
choice2 = Button(1, 1, 1, 1, BLACK)

def makeshapes():
    colors = [GREEN, RED, YELLOW, ORANGE]
    randcolor1 = random.choice(colors)
    colors.remove(randcolor1)
    s1width = random.randint(5, 200)
    s1height = random.randint(5, 200)
    exampleshape.redraw(10, 10, s1height, s1width, randcolor1)
    choice1.redraw(random.randint(220, 650), random.randint(10, 750), s1height, s1width, randcolor1)
    choice2.redraw(random.randint(220, 650), random.randint(10, 750), random.randint(5, 200), random.randint(5, 200), random.choice(colors))

    screen.fill(BLUE)

    exampleshape.draw()
    choice1.draw()
    choice2.draw()

makeshapes()

text = pygame.font.SysFont('arial', 32)
textSurfaceObj = text.render(str(score), True, (0, 255, 0), (0, 0, 255))
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (900, 150)

pygame.mixer.music.load('Hypnotic-Puzzle.mp3')
pygame.mixer.music.play(-1, 0.0)

hit = pygame.mixer.Sound('hit.wav')
miss = pygame.mixer.Sound('tumpunch.wav')
while True:
    screen.blit(textSurfaceObj, textRectObj)

    if you_lose == True:
        screen.fill(RED)
        text = pygame.font.SysFont('arial', 32)
        textSurfaceObj = text.render(('YOU LOSE'), True, (0, 0, 0))
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (500, 430)
        screen.blit(textSurfaceObj, textRectObj)
        text = pygame.font.SysFont('arial', 32)
        textSurfaceObj = text.render(('Your score was: %s' % score), True, (0, 0, 0))
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (500, 470)
        screen.blit(textSurfaceObj, textRectObj)
        pygame.display.update()

        pygame.mixer.music.stop()
        pygame.mixer.music.load('lose.mp3')
        pygame.mixer.music.play(-1, 0.0)
        time.sleep(5)
        pygame.quit()
        sys.exit()


    if you_win == True:
        screen = pygame.display.set_mode((1000, 900), pygame.FULLSCREEN)
        sans = pygame.image.load('bigsans.png')
        screen.fill(GREEN)
        text = pygame.font.SysFont('arial', 32, True)
        textSurfaceObj = text.render(('SANS UNDERTALE!!?!???!?!?!!?'), True, (0, 0, 0))
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (500, 650)
        screen.blit(textSurfaceObj, textRectObj)
        text = pygame.font.SysFont('Comic Sans MS', 32, True)
        textSurfaceObj = text.render("geeeeeeeeeeeeeet dunked on", True, (0, 0, 0))
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (500, 700)
        screen.blit(textSurfaceObj, textRectObj)
        screen.blit(sans, (300, 10))
        pygame.display.update()

        pygame.mixer.music.stop()
        pygame.mixer.music.load('megalovania.mp3')
        pygame.mixer.music.play(-1, 0.0)
        time.sleep(156)
        pygame.quit()
        sys.exit()

    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONUP:
            if choice1.click(pygame.mouse.get_pos()):
                score += 10
                textSurfaceObj = text.render(str(score), True, (0, 255, 0))
                hit.play()
                makeshapes()
                wrong_count = 0
                if score >= 100:
                    you_win = True

            if choice2.click(pygame.mouse.get_pos()):
                if not score < 0 and not wrong_count >= 2:
                    score -= 1
                    wrong_count += 1
                    textSurfaceObj = text.render(str(score), True, (0, 255, 0))
                    makeshapes()
                    miss.play()
                if wrong_count >= 2:
                    you_lose = True
                if score < 0:
                    you_lose = True
                    score = 0
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()


    pygame.display.update()
    fpsClock.tick(FPS)