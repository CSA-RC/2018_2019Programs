"""
    #advanced_final.py (program v.1.0.0)
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
import pygame
import sys
import random
from pygame.locals import *

window_height = 480
window_width = 640

play = False

tick = 80
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Advanced Final")
clock = pygame.time.Clock()


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

class Entity(pygame.sprite.Sprite):
    """Inherited by any object in the game."""

    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y
        self.width = width
        self.height = height

        # This makes a rectangle around the entity, used for anything
        # from collision to moving around.
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

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

class Line:

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.speed = 5
        self.Rect = pygame.Rect(self.x, self.y-2, 200, 4)

    def update(self):
        pygame.draw.line(screen, self.color, (self.x, self.y), (self.x+200, self.y), 4)
        self.Rect.x = self.x
        self.x += self.speed
        if self.x+200 == 640:
            self.speed *= -1
        if self.x == 0:
            self.speed *= -1

class Circle:

    def __init__(self, x, y, diameter,color):
        self.x = x
        self.y = y
        self.radius = int(diameter/2)
        self.color = color
        self.colorlist = [RED, GREEN, WHITE, PURPLE, BLACK, ORANGE, YELLOW, GRAY, NAVYBLUE, CYAN]
        self.xspeed = 5
        self.yspeed = 5
        self.Rect = pygame.Rect(self.x-self.radius, self.y-self.radius, 50, 50)
    def changespeed(self, xspeed, yspeed):
        if self.xspeed in range(-1, -7):
            self.xspeed = -xspeed
        if self.yspeed in range(-1, -7):
            self.yspeed = -yspeed
        if self.xspeed in range(1, 7):
            self.xspeed = xspeed
        if self.yspeed in range(1, 7):
            self.yspeed = yspeed

    def update(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        self.x += self.xspeed
        self.y += self.yspeed
        self.Rect.x = self.x-self.radius
        self.Rect.y = self.y-self.radius

        if self.x + self.radius >= 640:
            self.xspeed *= -1
            self.color = random.choice(self.colorlist)
            if self.xspeed in range(-1,-7):
                self.xspeed = random.randint(-1, -6)
            if self.yspeed in range(-1, -7):
                self.yspeed = random.randint(-1, -6)
            if self.xspeed in range(1,7):
                self.xspeed = random.randint(1, 6)
            if self.yspeed in range(1,7):
                self.yspeed = random.randint(1, 6)

        if self.x - self.radius <= 0:
            self.xspeed *= -1
            self.color = random.choice(self.colorlist)
            if self.xspeed in range(-1,-7):
                self.xspeed = random.randint(-1, -6)
            if self.yspeed in range(-1, -7):
                self.yspeed = random.randint(-1, -6)
            if self.xspeed in range(1,7):
                self.xspeed = random.randint(1, 6)
            if self.yspeed in range(1,7):
                self.yspeed = random.randint(1, 6)

        if self.y + self.radius >= 480:
            self.yspeed *= -1
            self.color = random.choice(self.colorlist)
            if self.xspeed in range(-1,-7):
                self.xspeed = random.randint(-1, -6)
            if self.yspeed in range(-1, -7):
                self.yspeed = random.randint(-1, -6)
            if self.xspeed in range(1,7):
                self.xspeed = random.randint(1, 6)
            if self.yspeed in range(1,7):
                self.yspeed = random.randint(1, 6)
        if self.y - self.radius <= 0:
            self.yspeed *= -1
            self.color = random.choice(self.colorlist)
            if self.xspeed in range(-1,-7):
                self.xspeed = random.randint(-1, -6)
            if self.yspeed in range(-1, -7):
                self.yspeed = random.randint(-1, -6)
            if self.xspeed in range(1,7):
                self.xspeed = random.randint(1, 6)
            if self.yspeed in range(1,7):
                self.yspeed = random.randint(1, 6)

        if self.Rect.colliderect(line.Rect):
            self.yspeed *= -1
            self.color = random.choice(self.colorlist)
            if self.xspeed in range(-1,-7):
                self.xspeed = random.randint(-1, -6)
            if self.yspeed in range(-1, -7):
                self.yspeed = random.randint(-1, -6)
            if self.xspeed in range(1,7):
                self.xspeed = random.randint(1, 6)
            if self.yspeed in range(1,7):
                self.yspeed = random.randint(1, 6)

        if self.Rect.colliderect(rectangle.top):
            self.yspeed *= -1
            self.color = random.choice(self.colorlist)
            if self.xspeed in range(-1,-7):
                self.xspeed = random.randint(-1, -6)
            if self.yspeed in range(-1, -7):
                self.yspeed = random.randint(-1, -6)
            if self.xspeed in range(1,7):
                self.xspeed = random.randint(1, 6)
            if self.yspeed in range(1,7):
                self.yspeed = random.randint(1, 6)

        if self.Rect.colliderect(rectangle.left):
            self.xspeed *= -1
            self.color = random.choice(self.colorlist)
            if self.xspeed in range(-1,-7):
                self.xspeed = random.randint(-1, -6)
            if self.yspeed in range(-1, -7):
                self.yspeed = random.randint(-1, -6)
            if self.xspeed in range(1,7):
                self.xspeed = random.randint(1, 6)
            if self.yspeed in range(1,7):
                self.yspeed = random.randint(1, 6)




class Rectangle:

    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = (self.x, self.y, self.width, self.height)
        self.color = color
        self.Rect = pygame.Rect(self.rect)
        self.top = pygame.Rect(self.x+1, self.y, self.width-1, 1)
        self.left = pygame.Rect(self.x, self.y+1, 1, self.height-1)

    def update(self):
        pygame.draw.rect(screen, self.color, self.rect)
        self.Rect.x = self.x
        self.Rect.y = self.y

pygame.init()

line = Line(200, 40, WHITE)
circle = Circle(200, 100, 50, GREEN)
rectangle = Rectangle(window_width-100, window_height-100, 100, 100, RED)
changebutton = Button(window_width-75, 0, 25, 75, ORANGE)
quitbutton = Button(0, 0, 25, 75, RED)
playbutton = Button(0, 0, window_height, window_width, WHITE)
screen.fill(BLUE)
line.update()
circle.update()
rectangle.update()
changebutton.draw()
changebutton.write(WHITE, "CHANGE", "Arial", 12)
quitbutton.draw()
quitbutton.write(WHITE, "QUIT", "Arial", 12)

while True:
    if play == True:
        screen.fill(BLUE)
        line.update()
        circle.update()
        rectangle.update()
        changebutton.draw()
        changebutton.write(WHITE, "CHANGE", "Arial", 12)
        quitbutton.draw()
        quitbutton.write(WHITE, "QUIT", "Arial", 12)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONUP:
                if changebutton.click(pygame.mouse.get_pos()):
                    circle.changespeed(random.randint(1,6), random.randint(1,6))
                if quitbutton.click(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
    else:
        playbutton.write(BLACK, "PRESS SPACE TO START", "Arial", 32)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    play = True
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()


    pygame.display.flip()
    clock.tick(tick)