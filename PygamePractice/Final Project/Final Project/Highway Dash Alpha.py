'''
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
#####
Tommy Ramsey IV
Highway Dash'''

import sys, pygame, pygame.mixer
from pygame.locals import *
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
gray = (50, 50, 50)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)


clock = pygame.time.Clock()
FPS = 30

ZEROINTENSITY = 0
MAXINTENSITY = 255

block_color = (random.randint(ZEROINTENSITY, MAXINTENSITY), random.randint(ZEROINTENSITY, MAXINTENSITY),
             random.randint(ZEROINTENSITY, MAXINTENSITY))

bullets = []

car_width = 75
bullet_width = 70

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Highway Dash')
clock = pygame.time.Clock()

carImg = pygame.image.load('car.png').convert_alpha()
carImg = pygame.transform.scale(carImg, (100, 100))
background = pygame.image.load("road.png").convert()
bulletpicture = pygame.image.load("bullet.png").convert_alpha()

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, white)
    gameDisplay.blit(text, (0, 0))


def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


def car(x, y):
    gameDisplay.blit(carImg, (x, y))

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()


def crash():
    message_display('Game Over.')

def text_format(message, textFont, textSize, textColor):
    newFont = pygame.font.Font(textFont, textSize)
    newText = newFont.render(message, 0, textColor)

    return newText


def main_menu():
    menu = True
    selected = "start"

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = "start"
                elif event.key == pygame.K_DOWN:
                    selected = "quit"
                if event.key == pygame.K_RETURN:
                    if selected == "start":
                        print("Start")
                        game_loop()
                    if selected == "quit":
                        pygame.quit()
                        quit()

        gameDisplay.fill(gray)
        title = text_format("Highway Dash", None, 90, yellow)
        if selected == "start":
            text_start = text_format("START", None, 75, yellow)
        else:
            text_start = text_format("START", None, 75, black)
        if selected == "quit":
            text_quit = text_format("QUIT", None, 75, yellow)
        else:
            text_quit = text_format("QUIT", None, 75, black)

        title_rect = title.get_rect()
        start_rect = text_start.get_rect()
        quit_rect = text_quit.get_rect()

        gameDisplay.blit(title, (display_width / 2 - (title_rect[2] / 2), 80))
        gameDisplay.blit(text_start, (display_width / 2 - (start_rect[2] / 2), 300))
        gameDisplay.blit(text_quit, (display_width / 2 - (quit_rect[2] / 2), 360))
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("")

def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 4
    thing_width = 100
    thing_height = 100

    thingCount = 1

    dodged = 0

    gameExit = False

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == MOUSEBUTTONDOWN:
                bullets.append([event.pos[0] - 32, 600])

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    x_change = -5
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
                    x_change = 0

        x += x_change
        gameDisplay.blit(background, (0, 0))

        things(thing_startx, thing_starty, thing_width, thing_height, block_color)

        thing_starty += thing_speed
        car(x, y)
        things_dodged(dodged)

        if x > display_width - car_width or x < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            thing_speed += .5
            thing_width += (dodged + .75)

        if y < thing_starty + thing_height:
            print('y crossover')

            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
                print('x crossover')
                crash()

        for b in range(len(bullets)):
            bullets[b][1] += -7

        for bullet in bullets[:]:
            if bullet[0] < 0:
                bullets.remove(bullet)


        for bullet in bullets:
            gameDisplay.blit(bulletpicture, pygame.Rect(bullet[0], bullet[1], 0, 0))

        pygame.display.update()
        clock.tick(60)

main_menu()
game_loop()
pygame.quit()
quit()