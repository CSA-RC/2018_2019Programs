import pygame
import sys
import time
import random

background = (0, 0, 0)
entity_color = (255, 255, 255)

tick = 60

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


class Paddle(Entity):
    """
    Player controlled or AI controlled, main interaction with
    the game
    """

    def __init__(self, x, y, width, height):
        super(Paddle, self).__init__(x, y, width, height)

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(entity_color)


class Player(Paddle):
    """The player controlled Paddle"""

    def __init__(self, x, y, width, height):
        super(Player, self).__init__(x, y, width, height)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        # How many pixels the Player Paddle should move on a given frame.
        self.y_change = 0
        # How many pixels the paddle should move each frame a key is pressed.
        self.y_dist = 5

    def MoveKeyDown(self, key):
        """Responds to a key-down event and moves accordingly"""
        if (key == pygame.K_UP):
            self.y_change += -self.y_dist
        elif (key == pygame.K_DOWN):
            self.y_change += self.y_dist

    def MoveKeyUp(self, key):
        """Responds to a key-up event and stops movement accordingly"""
        if (key == pygame.K_UP):
            self.y_change += self.y_dist
        elif (key == pygame.K_DOWN):
            self.y_change += -self.y_dist

    def getRects(self):
        ptop = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, (self.rect.height/2))
        pmid = pygame.Rect(self.rect.x, (self.rect.y + (self.rect.height/3)), self.rect.width, (self.rect.height/3))
        pbottom = pygame.Rect(self.rect.x, (self.rect.y + (self.rect.height/2)), self.rect.width, (self.rect.height/2))
        return(ptop,pmid,pbottom)

    def update(self):
        """
        Moves the paddle while ensuring it stays in bounds
        """
        # Moves it relative to its current location.
        self.rect.move_ip(0, self.y_change)

        # If the paddle moves off the screen, put it back on.
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > window_height - self.height:
            self.rect.y = window_height - self.height


class Enemy(Paddle):
    """
    AI controlled paddle, simply moves towards the ball
    and nothing else.
    """

    def __init__(self, x, y, width, height):
        super(Enemy, self).__init__(x, y, width, height)

        self.y_change = 3

    def get_enemy_speed(self, speed):
        self.y_change = speed

    def update(self):
        """
        Moves the Paddle while ensuring it stays in bounds
        """
        # Moves the Paddle up if the ball is above,
        # and down if below.
        if ball.rect.y < (self.rect.y + 20):
            self.rect.y -= self.y_change
        elif ball.rect.y > (self.rect.y + 20):
            self.rect.y += self.y_change

        # The paddle can never go above the window since it follows
        # the ball, but this keeps it from going under.
        if self.rect.y + self.height > window_height:
            self.rect.y = window_height - self.height


class Ball(Entity):
    """
    The ball!  Moves around the screen.
    """

    def __init__(self, x, y, width, height):
        super(Ball, self).__init__(x, y, width, height)
        self.tick = 60

        self.image = pygame.Surface([width, height])
        self.image.fill(entity_color)

        self.x_direction = 1
        # Positive = down, negative = up
        self.y_direction = 1
        # Current speed.
        self.speed = 3

        self.enemyspeed = 3

        self.score1 = 0
        self.score2 = 0

    def get_score(self):
        return (self.score1, self.score2)

    def set_score(self, score1, score2):
        self.score1 = score1
        self.score2 = score2


    def update(self):
        # Move the ball!
        self.rect.move_ip(self.speed * self.x_direction,
                          self.speed * self.y_direction)

        # Keep the ball in bounds, and make it bounce off the sides.
        if self.rect.y < 0:
            self.y_direction *= -1
        elif self.rect.y > window_height - 20:
            self.y_direction *= -1
        if self.rect.x < 0:
            self.score2 += 1
            self.speed = 3
            self.enemyspeed = 3
            enemy.get_enemy_speed(self.enemyspeed)
            time.sleep(1)
            self.rect.x = window_width / 2
            self.rect.y = window_height / 2
        elif self.rect.x > window_width - 20:
            self.score1 += 1
            self.speed = 3
            self.enemyspeed = 3
            enemy.get_enemy_speed(self.enemyspeed)
            time.sleep(1)
            self.rect.x = window_width / 2
            self.rect.y = window_height / 2

        ptop, pmid, pbottom = player.getRects()
        if self.rect.colliderect(ptop):
            self.x_direction *= -1
            self.y_direction = -1
            #print('top')
            self.speed += 1
            self.enemyspeed+=.7
            enemy.get_enemy_speed(self.enemyspeed)

        #elif self.rect.colliderect(pmid):
         #   self.x_direction *= -1
          #  self.y_direction = 0
           # print('mid')

        elif self.rect.colliderect(pbottom):
            self.x_direction *= -1
            self.y_direction = 1
            self.speed += 1
            self.enemyspeed += .7
            enemy.get_enemy_speed(self.enemyspeed)

            #print('bottom')
        if self.rect.colliderect(enemy):
            self.x_direction *= -1
            self.y_direction = random.choice([-1, 1])
            self.speed += 1
            self.enemyspeed += .7
            enemy.get_enemy_speed(self.enemyspeed)

class Button:

    def __init__(self, x, y, height, width, color):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)


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


pygame.init()

window_width = 700
window_height = 400
screen = pygame.display.set_mode((window_width, window_height))

pygame.display.set_caption("Pong")

clock = pygame.time.Clock()

scoreboard = Button(0,0,400,700, (0,0,0))
ball = Ball(window_width / 2, window_height / 2, 20, 20)
player = Player(20, window_height / 2, 20, 50)
enemy = Enemy(window_width - 40, window_height / 2, 20, 50)

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(ball)
all_sprites_list.add(player)
all_sprites_list.add(enemy)



while True:
    score1, score2 = ball.get_score()
    if score2 == 1:
        try:
            with open("scores.txt", "r") as high_scores:
                current_scores = high_scores.read().split("\n")
        except FileNotFoundError:
            with open("scores.txt", "w") as high_scores:
                high_scores.write("0\n0\n0\n0\n0\n0\n0\n0\n0\n0")
            with open("scores.txt", "r") as high_scores:
                current_scores = high_scores.read().split("\n")
        for score in range(len(current_scores)):
            if int(score1) >= int(current_scores[score]):
                score1, current_scores[score] = str(current_scores[score]), str(score1)
                break
        with open("scores.txt", "w") as high_scores:
            high_scores.write("\n".join([str(score) for score in current_scores]))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    ball.set_score(0,0)


        string = ("High Scores " + " ".join(current_scores) +" press Space to continue")

        scoreboard.draw()
        scoreboard.write((255,255,255), string, 'Arial', 15)


    if score2 != 1:
        left_score = pygame.font.SysFont('arial', 40)
        score1SurfaceObj = left_score.render(str(score1), True, (200, 200, 200))
        score1RectObj = score1SurfaceObj.get_rect()
        score1RectObj.center = (100, 50)

        right_score = pygame.font.SysFont('arial', 40)
        score2SurfaceObj = left_score.render(str(score2), True, (200, 200, 200))
        score2RectObj = score2SurfaceObj.get_rect()
        score2RectObj.center = (window_width - 100, 50)
        # Event processing here
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                player.MoveKeyDown(event.key)
            elif event.type == pygame.KEYUP:
                player.MoveKeyUp(event.key)

        for ent in all_sprites_list:
            ent.update()

        screen.fill(background)

        all_sprites_list.draw(screen)

        screen.blit(score1SurfaceObj, score1RectObj)
        screen.blit(score2SurfaceObj, score2RectObj)

    pygame.display.flip()

    clock.tick(tick)