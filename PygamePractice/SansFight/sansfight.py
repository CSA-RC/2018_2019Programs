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
    GNU General Public License for morze details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import pygame, sys
from pygame.locals import *

pygame.init()
pygame.key.set_repeat(1, 10)
DISPLAYSURF = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
pygame.display.set_caption('Hello World!')
surface_text = pygame.font.SysFont("Comic Sans MS", 60, True).render("* Do you wanna have a bad time?", True, pygame.Color("white"))
battlebox = pygame.Rect((50,50, 300, 300))
player = pygame.image.load('Human_SOUL_test.png')
sans = pygame.image.load('sansmove.gif')
px = 950
py = 585
pygame.mixer.music.load('megalovania.mp3')
pygame.mixer.music.play(-1, 0.0)

while True:
    keys = pygame.key.get_pressed()
    DISPLAYSURF.fill((0,0,0))
    battlebox.center=((DISPLAYSURF.get_width() / 2),600 )
    pygame.draw.rect(DISPLAYSURF, (255, 255, 255), battlebox, 5)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()


    if keys[pygame.K_RIGHT]:
        if battlebox.collidepoint(px + player.get_width() + 4, py + player.get_height() - 15):
            px+=3
    if keys[pygame.K_LEFT]:
        if battlebox.collidepoint(px - 5, py + 5):
            px-=3
    if keys[pygame.K_UP]:
        if battlebox.collidepoint(px + 5, py - 4):
            py-=3
    if keys[pygame.K_DOWN]:
        if battlebox.collidepoint(px + player.get_width() - 15, py + player.get_height() + 2.5):
            py+=3

    DISPLAYSURF.blit(player, (px, py))
    DISPLAYSURF.blit(sans, (850, 100))
    pygame.display.update()
