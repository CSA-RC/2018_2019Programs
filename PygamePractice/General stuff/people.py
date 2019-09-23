import pygame, sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.key.set_repeat(1, 10)

class Player:

    def __init__(self, x,y, color):
        self.x = x
        self.y = y
        self.color = color


    def stickboi(self, x, y):
        pygame.draw.line(screen, self.color, (x, y), (x,(y+60)), 4)
        pygame.draw.line(screen, self.color, (x, (y+60)), ((x+20),(y+100)), 4)
        pygame.draw.line(screen, self.color, (x, (y+60)), ((x-20),(y+100)), 4)
        pygame.draw.line(screen, self.color, (x, y), ((x+20),(y+40)), 4)
        pygame.draw.line(screen, self.color, (x, y), ((x-20),(y+40)), 4)
        pygame.draw.circle(screen, self.color, ((x+1),(y-18)), 20)


#people
#stickboi(120, 150, (255,255,255))
px = 60
py = 150
player = Player(px, py, (0,0,0))
while True:

    # sky
    screen.fill((135, 206, 250))

    # house
    pygame.draw.polygon(screen, (255, 200, 0), ((246, 10), (336, 106), (336, 250), (156, 250), (156, 106)))

    # door
    pygame.draw.rect(screen, (255, 0, 0), (220, 140, 50, 200))
    pygame.draw.circle(screen, (255, 150, 0), ((230, 180)), 5)

    # windows
    pygame.draw.rect(screen, (0, 100, 240), (170, 150, 40, 40))
    pygame.draw.rect(screen, (0, 100, 240), (280, 150, 40, 40))

    # ground
    pygame.draw.rect(screen, (0, 255, 0), (0, 220, 400, 200))

    player.stickboi(px, py)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_RIGHT:
                px+=3
                player.stickboi(px, py)
            if event.key == K_LEFT:
                px-=3
                player.stickboi(px, py)
            if event.key == K_UP:
                py-=3
                player.stickboi(px, py)
            if event.key == K_DOWN:
                py+=3
                player.stickboi(px, py)


    pygame.display.update()