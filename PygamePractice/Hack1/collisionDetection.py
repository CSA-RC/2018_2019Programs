import pygame, sys, random
from pygame.locals import *

def doRectsOverlap(rect1, rect2):
    for a, b in [(rect1, rect2), (rect2, rect1)]:
        # Check if a's corners are inside b
        if ((isPointInsideRect(a.left, a.top, b)) or
            (isPointInsideRect(a.left, a.bottom, b)) or
            (isPointInsideRect(a.right, a.top, b)) or
            (isPointInsideRect(a.right, a.bottom, b))):
            return True

    return False

def isPointInsideRect(x, y, rect):
    if (x > rect.left) and (x < rect.right) and (y > rect.top) and (y < rect.bottom):
        return True
    else:
        return False


# set up pygame
pygame.init()
mainClock = pygame.time.Clock()

# set up the window
WINDOWWIDTH = 700
WINDOWHEIGHT = 700
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Collision Detection')

# set up direction variables
DOWNLEFT = 1
DOWNRIGHT = 3
UPLEFT = 7
UPRIGHT = 9

MOVESPEED = 4

# set up the colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
color_list = (GREEN, BLUE, WHITE)

# set up the bouncer and food data structures
foodCounter = 0
NEWFOOD = 40
FOODSIZE = 10
bouncer = {'rect':pygame.Rect(300, 100, 50, 50), 'dir':UPLEFT, 'color':BLUE}
bouncer2 = {'rect':pygame.Rect(50, 100, 50, 50), 'dir':UPRIGHT, 'color':WHITE}
bouncer_list = (bouncer, bouncer2)
foods = []
for i in range(200):
    foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))

# run the game loop
while True:
    # check for the QUIT event
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    foodCounter += 1
    if foodCounter >= NEWFOOD:
        # add new food
        foodCounter = 0
        foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))

    # draw the black background onto the surface
    windowSurface.fill(BLACK)

    for x in bouncer_list:
        # move the bouncer data structure
        if x['dir'] == DOWNLEFT:
            x['rect'].left -= MOVESPEED
            x['rect'].top += MOVESPEED*1.5
        if x['dir'] == DOWNRIGHT:
            x['rect'].left += MOVESPEED
            x['rect'].top += MOVESPEED*1.5
        if x['dir'] == UPLEFT:
            x['rect'].left -= MOVESPEED
            x['rect'].top -= MOVESPEED*1.5
        if x['dir'] == UPRIGHT:
            x['rect'].left += MOVESPEED
            x['rect'].top -= MOVESPEED*1.5



        # check if the bouncer has move out of the window
        if x['rect'].top < 0:
            x['color'] = random.choice(color_list)
            # bouncer has moved past the top
            if x['dir'] == UPLEFT:
                x['dir'] = DOWNLEFT
            if x['dir'] == UPRIGHT:
                x['dir'] = DOWNRIGHT
        if x['rect'].bottom > WINDOWHEIGHT:
            x['color'] = random.choice(color_list)
            # bouncer has moved past the bottom
            if x['dir'] == DOWNLEFT:
                x['dir'] = UPLEFT
            if x['dir'] == DOWNRIGHT:
                x['dir'] = UPRIGHT
        if x['rect'].left < 0:
            x['color'] = random.choice(color_list)
            # bouncer has moved past the left side
            if x['dir'] == DOWNLEFT:
                x['dir'] = DOWNRIGHT
            if x['dir'] == UPLEFT:
                x['dir'] = UPRIGHT
        if x['rect'].right > WINDOWWIDTH:
            x['color'] = random.choice(color_list)
            # bouncer has moved past the right side
            if x['dir'] == DOWNRIGHT:
                x['dir'] = DOWNLEFT
            if x['dir'] == UPRIGHT:
                x['dir'] = UPLEFT

    # draw the bouncer onto the surface
    pygame.draw.rect(windowSurface, bouncer['color'], bouncer['rect'])
    pygame.draw.rect(windowSurface, bouncer2['color'], bouncer2['rect'])

    # check if the bouncer has intersected with any food squares.
    for food in foods[:]:
        if doRectsOverlap(bouncer2['rect'], food):
            bouncer2['rect'].width += 5
            bouncer2['rect'].height += 5
            if bouncer2['rect'].width == 100:
                bouncer2['rect'].width = 50
                bouncer2['rect'].height = 50
            foods.remove(food)
        if doRectsOverlap(bouncer['rect'], food):
            bouncer['rect'].width += 5
            bouncer['rect'].height += 5
            if bouncer['rect'].width == 100:
                bouncer['rect'].width = 50
                bouncer['rect'].height = 50
            foods.remove(food)

    # draw the food
    for i in range(len(foods)):
        pygame.draw.rect(windowSurface, RED, foods[i])

    # draw the window onto the screen
    pygame.display.flip()

    mainClock.tick(200)