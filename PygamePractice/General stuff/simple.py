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

 # set up the window

DISPLAYSURF = pygame.display.set_mode((800, 800), 0, 32)

pygame.display.set_caption('Drawing')
# set up the colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)

BLUE = (0,0,255)
# draw on the surface object
DISPLAYSURF.fill(WHITE)

pygame.draw.polygon(DISPLAYSURF, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))
pygame.draw.line(DISPLAYSURF, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(DISPLAYSURF, BLUE, (120, 60), (60, 120))
pygame.draw.line(DISPLAYSURF, BLUE, (60, 120), (120, 120), 4)
pygame.draw.circle(DISPLAYSURF, BLUE, (300, 50), 20, 10)

pygame.draw.ellipse(DISPLAYSURF, RED, (300, 250, 40, 80), 1)

pygame.draw.rect(DISPLAYSURF, RED, (200, 150, 100, 50))
pixObj = pygame.PixelArray(DISPLAYSURF)
pixObj[480][380] = BLACK
pixObj[482][382] = BLACK
pixObj[484][384] = BLACK
pixObj[486][386] = BLACK
pixObj[488][388] = BLACK
del pixObj

# run the game loop

while True:

 for event in pygame.event.get():

  if event.type == QUIT:

   pygame.quit()

   sys.exit()

  pygame.display.update()
