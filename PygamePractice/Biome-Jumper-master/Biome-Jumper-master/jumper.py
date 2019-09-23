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
Katie Chiu
Swimming Squid
Version .1
Last updated 6 May 2019
Jump and get as many coins as you can. Monsters sit on platforms and shoot lasers at you. Each coin 1 point. Killing a monster is 25 points You lose by falling, touching a monster, or getting hit by a laser. Use arrows to move left and right. Use spacebar to jump. Use up arrow to shoot.'''
import pygame, sys, random

pygame.init()
pygame.font.init()

global current, platformx, platformlist, coinlist, points, start, platformy, enemy, enemylist, begin, all_sprites_list, newscore,player,userlaser,pic,laslist #assigns all values
newscore = 0
begin = 0
enemy = 0
count = 0
window_width = 500
window_height = 700
platformx = 100
points = 0
start = 0
enemylist = []
pic=None
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Platform Jumper")


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.image = pygame.transform.scale(self.image, (1400, 700))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


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


class Player(Entity):
    """The player controlled Object"""

    def __init__(self, x, y, width, height,image):
        global pic
        super(Player, self).__init__(x, y, width, height)
        self.object = pygame.image.load(image)
        if pic=="sea":
            self.image = pygame.transform.scale(self.object, (70, 70))
        else:
            self.image=pygame.transform.scale(self.object,(45,45))
        # How many pixels the Player should move on a given frame.
        self.y_change = 0
        self.x_change = 0
        self.move = 0
        self.done = 0
        self.fall = 0
        # How many pixels the player should move each frame a key is pressed.

    def MoveKeyDown(self, key):
        global userlaser
        """Responds to a key-down event and moves accordingly"""
        if key == pygame.K_LEFT:
            self.x_change += -2
        elif key == pygame.K_RIGHT:
            self.x_change += 2
        elif key==pygame.K_UP:
            shoot=PlayerLaser(player.rect.x+35,player.rect.y-30,3,30)
            userlaser.append(shoot)
            all_sprites_list.add(shoot)

    def MoveKeyUp(self, key):
        """Responds to a key-up event and stops movement accordingly"""
        if key == pygame.K_LEFT:
            self.x_change += 2
        elif key == pygame.K_RIGHT:
            self.x_change += -2

    def Jump(self):
        self.y_change = 2
        self.move = 1

    def update(self):  # movement for jump
        global begin
        if self.move == 1:
            if self.done >= 33:
                if self.done >= 36:  # lets player stay in air a little longer
                    self.y_change += -.1  # playerfalls
                    collision()  # checks for collision with platform
                else:
                    self.done += 1
                    collision()
            else:
                self.y_change += .1  # player jumps
                self.done += 1
        for platform in platformlist:  # all platforms move for movement of screen
            platform.rect.move_ip(0, self.y_change)
        for enemy in enemylist:
            enemy.rect.move_ip(0, self.y_change)
        for coin in coinlist:  # coins move with platforms
            coin.rect.move_ip(0, self.y_change)
        self.rect.move_ip(self.x_change, self.fall)  # movement of player
        # If the player moves off the screen, put it back on.
        if self.rect.x < -5:
            self.rect.x = -5
        elif self.rect.x > 440:
            self.rect.x = 440
        if self.rect.y >= 710:
            diesound.play()
            begin=4
        # Moves it relative to its current location.


class Enemy(Entity):
    def __init__(self, x, y, width, height):
        global pic
        super(Enemy, self).__init__(x, y, width, height)
        if pic=="land":
            self.monster = pygame.image.load("landmonster.png")
        else:
            self.monster=pygame.image.load("monster.png")
        self.image = pygame.transform.scale(self.monster, (50, 60))

    def update(self):  # makes sure no changes are made
        self.rect.move_ip(0, 0)


class Platform(Entity):
    def __init__(self, x, y, width, height):  # assigns platform
        super(Platform, self).__init__(x, y, width, height)
        global start
        self.grass = pygame.image.load("platform.png")
        self.image = pygame.transform.scale(self.grass, (170, 34))
        self.y_direction = 0
        coinx = self.rect.x - 35
        coiny = self.rect.y - 15
        if start != 0:  # puts coins on platform
            for x in range(5):
                coinx = coinx + 35
                coin = Coin(coinx, coiny, 25, 25)
                all_sprites_list.add(coin)
                coinlist.append(coin)
        else:
            start = 1

class Coin(Entity):  # assigns coins
    def __init__(self, x, y, width, height):
        super(Coin, self).__init__(x, y, width, height)
        self.coin = pygame.image.load("coin.png")
        self.image = pygame.transform.scale(self.coin, (25, 25))


def coincollide():  # if player touches coin
    global coinlist, points
    for coin in coinlist:
        if player.rect.colliderect(coin.rect):
            coinlist.remove(coin)
            coin.remove(all_sprites_list)
            points = points + 1
            coinsound.play()


def enemycollide():  # if player touches coin
    global enemylist,begin,userlaser,monster,coinlist,points
    for x in enemylist:
        if player.rect.x >= x.rect.x - 50 and player.rect.x <= x.rect.x + 35 and player.rect.y <= x.rect.y and player.rect.y >= x.rect.y - 20: #collision with user
            diesound.play()
            begin=4
        if player.rect.y == x.rect.y + 60 and player.y_change == .1:
            player.y_change = -.1
        for coin in coinlist: #collision with coins, remove coins
            if x.rect.colliderect(coin.rect):
                coinlist.remove(coin)
                coin.remove(all_sprites_list)
        for shoot in userlaser: #collision with laser, remove both objects
            if shoot.rect.colliderect(x.rect):
                points=points+25
                enemydie.play()
                userlaser.remove(shoot)
                shoot.remove(all_sprites_list)
                enemylist.remove(x)
                x.remove(all_sprites_list) 


class Laser(Entity): #enemy's laser

    def __init__(self, x, y, width, height):
        super(Laser, self).__init__(x, y, width, height)

        self.image = pygame.Surface([width, height])
        self.image.fill(RED)

        self.x_direction = 0
        self.y_direction = 1
        self.speed = 4

    def update(self):
        if player.y_change!=0:
            self.speed=6
        else:
            self.speed=4
        self.rect.move_ip(self.speed * self.x_direction,
                          self.speed * self.y_direction)

class PlayerLaser(Entity): #user's laser

    def __init__(self, x, y, width, height):
        super(PlayerLaser, self).__init__(x, y, width, height)

        self.image = pygame.Surface([width, height])
        self.image.fill(GREEN)

        self.x_direction = 0
        self.y_direction = -1
        self.speed = 4

    def update(self):
        self.rect.move_ip(self.speed * self.x_direction,
                          self.speed * self.y_direction)

def lasercollide():
    global laslist, begin,userlaser
    for x in laslist: #collision with laser and player
        if player.rect.colliderect(x.rect):
            diesound.play()
            begin=4
        for shoot in userlaser: #collision with both lasers
            if shoot.rect.colliderect(x.rect):
                userlaser.remove(shoot)
                shoot.remove(all_sprites_list)
                laslist.remove(x)
                x.remove(all_sprites_list)

def collision():  # if player jumps onto platform
    global current, platformlist, platformx, platformy, coinlist, enemy, enemylist,laslist,userlaser
    for platform in platformlist:
        if platform != current:  # if new platform
            if player.rect.colliderect(platform.rect) and player.move == 1:  # checks if x coordinates of player are in platform
                if pic=="sea":
                    if player.rect.y >= platform.rect.y - 55 and player.rect.y <= platform.rect.y - 40:  # checks if player actually hit platform
                        if player.y_change <= -.1:
                            enemy = enemy + 1
                            platformlist.remove(current)  # removes last platform
                            current.remove(all_sprites_list)
                            current = platform  # reassigns current platform
                            player.y_change = 0  # stops all movement
                            player.move = 0
                            player.done = 0
                            platformy = platformy
                            new = random.randrange(10, 300)
                            if platformx - new <= 100: #makes new platform
                                new = new + 125
                            elif new - platformx >= -100:
                                new = new - 125
                            platform = Platform(new, platformy, 170, 34)
                            platformlist.append(platform)
                            all_sprites_list.add(platform)
                            for coin in coinlist: #adds coins to new platform
                                if coin.rect.y > 600:
                                    findy = coin.rect.y
                                    coin.remove(all_sprites_list)
                                    coinlist.remove(coin)
                                    for coin in coinlist:
                                        if coin.rect.y == findy:
                                            coin.remove(all_sprites_list)
                                            coinlist.remove(coin)
                            for x in enemylist: #if enemy is below screen
                                if x.rect.y > 600:
                                    x.remove(all_sprites_list)
                                    enemylist.remove(x)
                            last = platformlist[-1]
                            if enemy >= 7 and last.x <= 330: #adds enemy to platform
                                monster = Enemy(last.x + 50, last.y - 45, 60, 60)
                                enemylist.append(monster)
                                all_sprites_list.add(monster)
                                enemy = 0
                else:
                    if player.rect.y >= platform.rect.y - 30 and player.rect.y <= platform.rect.y - 20:  # checks if player actually hit platform
                        if player.y_change <= -.1:
                            enemy = enemy + 1
                            platformlist.remove(current)  # removes last platform
                            current.remove(all_sprites_list)
                            current = platform  # reassigns current platform
                            player.y_change = 0  # stops all movement
                            player.move = 0
                            player.done = 0
                            platformy = platformy
                            new = random.randrange(10, 300)
                            if platformx - new <= 100: #makes new platform
                                new = new + 125
                            elif new - platformx >= -100:
                                new = new - 125
                            platform = Platform(new, platformy, 170, 34)
                            platformlist.append(platform)
                            all_sprites_list.add(platform)
                            for coin in coinlist: #adds coins to new platform
                                if coin.rect.y > 600:
                                    findy = coin.rect.y
                                    coin.remove(all_sprites_list)
                                    coinlist.remove(coin)
                                    for coin in coinlist:
                                        if coin.rect.y == findy:
                                            coin.remove(all_sprites_list)
                                            coinlist.remove(coin)
                            for x in enemylist: #if enemy is below screen
                                if x.rect.y > 600:
                                    x.remove(all_sprites_list)
                                    enemylist.remove(x)
                            last = platformlist[-1]
                            if enemy >= 7 and last.x <= 330: #adds enemy to platform
                                monster = Enemy(last.x + 50, last.y - 45, 60, 60)
                                enemylist.append(monster)
                                all_sprites_list.add(monster)
                                enemy = 0

        else:
            if player.rect.colliderect(platform.rect):  # if falling back onto original platform
                if pic=="sea":
                    if player.rect.y >= platform.rect.y - 45:
                        player.y_change = 0  # resets everything
                        player.move = 0
                        player.done = 0
                    else:
                        player.y_change = -1
                else:
                    if player.rect.y >= platform.rect.y - 30:
                        player.y_change = 0  # resets everything
                        player.move = 0
                        player.done = 0
                    else:
                        player.y_change = -1


def restart(): #reassigns all values
    global all_sprites_list, platformy, coinlist, platformlist, laslist, begin, enemy, count, platformx, points, start, enemylist, current,player,newscore,userlaser,pic
    player.rect.y=545
    all_sprites_list=None
    all_sprites_list = pygame.sprite.Group()
    laslist=None
    laslist=[]
    coinlist=None
    coinlist=[]
    platformlist=None
    platformlist=[]
    enemylist=None
    enemylist=[]
    userlaser=None
    userlaser=[]
    platformy = 600
    begin = 0
    enemy = 0
    count = 0
    platformx = 100
    points = 0
    newscore=0
    start = 0
    pic=0
    platform = Platform(100, 600, 170, 34)

    current = platform
    platformlist.append(platform)
    all_sprites_list.add(platform)

    for x in range(7):  # initial platforms
        new = random.randrange(10, 300)
        platformy = platformy - 175
        if platformx - new <= 100:
            new = new + 125
        elif new - platformx >= -100:
            new = new - 125
        if window_width - new <= 150:
            new = new - 150
        platformx = new
        platform = Platform(platformx, platformy, 170, 34)
        platformlist.append(platform)
        all_sprites_list.add(platform)

    last = platformlist[-1]
    monster = Enemy(last.x + 50, last.y - 45, 60, 60)
    enemylist.append(monster)
    all_sprites_list.add(monster)
    all_sprites_list.draw(screen)


platformy = 600
coinlist = []
platformlist = []
laslist = []
userlaser=[]
need=250

all_sprites_list = pygame.sprite.Group()
font = pygame.font.SysFont('arial', 18) #fonts
titlefont = pygame.font.SysFont('arial', 30)
BLACK = (0, 0, 0) #colors
WHITE = (255, 255, 255)
RED = (238, 59, 59)
GREEN=(118,238,0)
lasersound = pygame.mixer.Sound("lasersound2.wav") #sounds
diesound = pygame.mixer.Sound("fail.wav")
coinsound=pygame.mixer.Sound("ding.wav")
enemydie=pygame.mixer.Sound("crash.wav")

platform = Platform(100, 600, 170, 34)
current = platform
platformlist.append(platform)
all_sprites_list.add(platform)

for x in range(7):  # initial platforms
    new = random.randrange(10, 300)
    platformy = platformy - 175
    if platformx - new <= 100:
        new = new + 125
    elif new - platformx >= -100:
        new = new - 125
    if window_width - new <= 150:
        new = new - 150
    platformx = new
    platform = Platform(platformx, platformy, 170, 34)
    platformlist.append(platform)
    all_sprites_list.add(platform)

last = platformlist[-1]
monster = Enemy(last.x + 50, last.y - 45, 60, 60)
enemylist.append(monster)
all_sprites_list.add(monster)
all_sprites_list.draw(screen)

while True:
    if begin == 0: #menu
        screen.fill(BLACK)
        title = titlefont.render(str("BIOME JUMPER"), True, WHITE) #display for menu
        titlerect = title.get_rect()
        titlerect.center = (250, 50)
        starttext = font.render("Press Spacebar to Start", True, WHITE)
        startrect = starttext.get_rect()
        startrect.center = (250, 125)
        how = font.render("Press Enter for Instructions", True, WHITE)
        howrect = how.get_rect()
        howrect.center = (250, 175)
        highscores=font.render("Press H for Highscores",True,WHITE)
        scorerect=highscores.get_rect()
        scorerect.center=(250,225)

        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]: #if spacebar pressed, starts game
            begin = 1
        if key[pygame.K_h]:
            begin=5
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.stop()
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN: #if enter pressed, goes to instructions
                begin = 2
        screen.blit(title, titlerect)
        screen.blit(starttext, startrect)
        screen.blit(how, howrect)
        screen.blit(highscores,scorerect)
    elif begin==1:
        screen.fill(BLACK)
        seatheme=font.render(str("Press S for Sea Theme"),True,WHITE)
        landtheme=font.render(str("Press L for Land Theme"),True,WHITE)
        seathemebox=seatheme.get_rect()
        landthemebox=landtheme.get_rect()
        seathemebox.center=(250,200)
        landthemebox.center=(250,250)
        screen.blit(landtheme,landthemebox)
        screen.blit(seatheme,seathemebox)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.stop()
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN and event.key==pygame.K_s:
                background = Background('ocean.png', [0, 0])
                pic="sea"
                player = Player(120, 545, 70, 70,'squid.png')
                all_sprites_list.add(player)
                begin=3
            if event.type==pygame.KEYDOWN and event.key==pygame.K_l:
                background = Background('sky.png', [0, 0])
                pic="land"
                player = Player(120, 575, 55, 55,'squirrel.png')
                all_sprites_list.add(player)
                begin=3
    elif begin == 2: #instructions
        screen.fill(BLACK)
        textsurface = font.render(str("INSTRUCTIONS"), True, WHITE)
        textrect = textsurface.get_rect()
        textrect.center = (250, 50)
        screen.blit(textsurface, textrect)
        instruct1 = font.render(str("Jump and get as many coins as you can."), True, WHITE) #assigns all texts
        instruct2 = font.render(str("Monsters sit on platforms and shoot lasers at you."), True, WHITE)
        instruct3 = font.render(str("Each coin is 1 point. Killing a monster is 25 points."),True,WHITE)
        instruct4=font.render(str("You lose by falling, touching a monster, or getting hit by a laser."), True, WHITE)
        instruct5=font.render(str("Enemy lasers increase speed with each enemy."),True,WHITE)
        instruct6 = font.render(str("Use arrows to move left and right. Use spacebar to jump."), True, WHITE)
        instruct7=font.render(str("Use up arrow to shoot."),True,WHITE)
        instruct8 = font.render(str("PRESS ENTER TO RETURN TO HOME SCREEN"), True, WHITE)

        instructbox1 = instruct1.get_rect() #displays all texts
        instructbox2 = instruct2.get_rect()
        instructbox3 = instruct3.get_rect()
        instructbox4 = instruct4.get_rect()
        instructbox5 = instruct5.get_rect()
        instructbox6 = instruct6.get_rect()
        instructbox7=instruct7.get_rect()
        instructbox8=instruct8.get_rect()
        instructbox1.center = (250, 100)
        instructbox2.center = (250, 125)
        instructbox3.center = (250, 150)
        instructbox4.center = (250, 175)
        instructbox5.center = (250, 225)
        instructbox6.center = (250, 250)
        instructbox7.center=(250,275)
        instructbox8.center=(250,325)
        screen.blit(instruct1, instructbox1)
        screen.blit(instruct2, instructbox2)
        screen.blit(instruct3, instructbox3)
        screen.blit(instruct4, instructbox4)
        screen.blit(instruct5, instructbox5)
        screen.blit(instruct6, instructbox6)
        screen.blit(instruct7,instructbox7)
        screen.blit(instruct8,instructbox8)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.stop()
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN: #if enter is pressed, goes to menu
                begin = 0
    elif begin == 3: #starts game
        if pic==1:
            player.object = pygame.image.load('squid.png')
            pic=3
        elif pic==2:
            player.object = pygame.image.load('squirrel.png')
            pic=3
        count = count + 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # program closes
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: #user presses spacebar, player jumps
                if player.y_change==0:
                    player.Jump()
            elif event.type == pygame.KEYDOWN: #user presses arrows, moves and shoots lasers
                player.MoveKeyDown(event.key)
            elif event.type == pygame.KEYUP:
                player.MoveKeyUp(event.key)

        if count>=need: #shoots lasers periodically
            for monster in enemylist:
                lasersound.play()
                laser = Laser(monster.rect.x + 25, monster.rect.y + 70, 3, 30)
                laslist.append(laser)
                all_sprites_list.add(laser)
                need=need-1
                count=0
        for x in laslist:
            if x.rect.y >750:
                x.remove(all_sprites_list)
                laslist.remove(x)
        for x in userlaser:
            if x.rect.y < -50:
                x.remove(all_sprites_list)
                userlaser.remove(x)

        coincollide() #checks collision with all objects
        enemycollide()
        lasercollide()

        if player.rect.y >= current.rect.y: #checks if player falls below platform
            if player.rect.x + 50 <= current.rect.x or player.rect.x >= current.rect.x + 150:
                player.y_change = 0
                player.fall += .1
        if player.rect.colliderect(current):
            if player.rect.x + 50 <= current.rect.x or player.rect.x >= current.rect.x + 150:
                player.y_change = 0
                player.fall += .5

        for ent in all_sprites_list:
            ent.update()
        screen.blit(background.image, background.rect)
        all_sprites_list.draw(screen)
        textSurfaceObj = font.render(str("POINTS: " + str(points)), True, WHITE)  # text
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (60, 15)  # places text
        screen.blit(textSurfaceObj, textRectObj)
    elif begin==4: #end menu and highscores
        screen.fill(BLACK)
        total = points
        score = font.render(str("POINTS: " + str(points)), True, WHITE) #shows score
        scorerect = score.get_rect()
        scorerect.center = (250, 25)
        screen.blit(score, scorerect)
        textsurface = font.render(str("You died!"), True, WHITE)
        textrect = textsurface.get_rect()
        textrect.center = (250, 50)
        screen.blit(textsurface, textrect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.stop()
                pygame.quit()
                sys.exit()
        key = pygame.key.get_pressed() #if enter key is pressed, returns to menu
        if key[pygame.K_RETURN]:
            restart()

        file = open("jumperscore.txt", "r")
        y = file.readline()
        scores = []
        while y: #checks for high scores
            if int(points) > int(y) and newscore == 0:
                scores.append(points)
                scores.append("\n")
                newscore = 1
                y = file.readline()
            else:
                scores.append(y)
                y = file.readline()
        file.close()
        files = open("jumperscore.txt", "w") #rewrites scores to file
        for z in scores:
            files.write(str(z))
        files.close()

        if newscore == 1: #if user has high score then print
            new = font.render(str("NEW HIGHSCORE!"), True, WHITE)
            newbox = new.get_rect()
            newbox.center = (250, 75)
            screen.blit(new, newbox)
        file = open("jumperscore.txt", "r")
        label = "HIGHSCORES"
        line = file.readlines()
        leave = "PRESS ENTER TO RETURN TO HOME SCREEN"
        file.close()
        positions = [(250, 150), (250, 175), (250, 200), (250, 225), (250, 250), (250, 275),
                     (250, 300), (250, 325), (250, 350), (250, 375), (250, 425)]

        textsurface1 = font.render(label, True, WHITE)
        textrect1 = textsurface1.get_rect()
        textrect1.center = (250, 125)

        line = [SCORE.replace('\n', '') for SCORE in line]

        textsurface2 = font.render(str("1. " + line[0]), True, WHITE) #shows top 10 scores
        textrect2 = textsurface2.get_rect()
        textrect2.center = positions[0]

        textsurface3 = font.render(str("2. " + line[1]), True, WHITE)
        textrect3 = textsurface3.get_rect()
        textrect3.center = positions[1]

        textsurface4 = font.render(str("3. " + line[2]), True, WHITE)
        textrect4 = textsurface4.get_rect()
        textrect4.center = positions[2]

        textsurface5 = font.render(str("4. " + line[3]), True, WHITE)
        textrect5 = textsurface5.get_rect()
        textrect5.center = positions[3]

        textsurface6 = font.render(str("5. " + line[4]), True, WHITE)
        textrect6 = textsurface6.get_rect()
        textrect6.center = positions[4]

        textsurface7 = font.render(str("6. " + line[5]), True, WHITE)
        textrect7 = textsurface7.get_rect()
        textrect7.center = positions[5]

        textsurface8 = font.render(str("7. " + line[6]), True, WHITE)
        textrect8 = textsurface8.get_rect()
        textrect8.center = positions[6]

        textsurface9 = font.render(str("8. " + line[7]), True, WHITE)
        textrect9 = textsurface9.get_rect()
        textrect9.center = positions[7]

        textsurface10 = font.render(str("9. " + line[8]), True, WHITE)
        textrect10 = textsurface10.get_rect()
        textrect10.center = positions[8]

        textsurface11 = font.render(str("10. " + line[9]), True, WHITE)
        textrect11 = textsurface11.get_rect()
        textrect11.center = positions[9]

        textsurface12 = font.render(leave, True, WHITE)
        textrect12 = textsurface12.get_rect()
        textrect12.center = positions[10]

        screen.blit(textsurface1, textrect1)
        screen.blit(textsurface2, textrect2)
        screen.blit(textsurface3, textrect3)
        screen.blit(textsurface4, textrect4)
        screen.blit(textsurface5, textrect5)
        screen.blit(textsurface6, textrect6)
        screen.blit(textsurface7, textrect7)
        screen.blit(textsurface8, textrect8)
        screen.blit(textsurface9, textrect9)
        screen.blit(textsurface10, textrect10)
        screen.blit(textsurface11, textrect11)
        screen.blit(textsurface12, textrect12)
        pygame.display.flip()
    elif begin==5:
        screen.fill(BLACK)
        file = open("jumperscore.txt", "r")
        line = file.readlines()
        label = "HIGHSCORES"
        leave = "PRESS ENTER TO RETURN TO HOME SCREEN"
        file.close()
        positions = [(250, 150), (250, 175), (250, 200), (250, 225), (250, 250), (250, 275),
                     (250, 300), (250, 325), (250, 350), (250, 375), (250, 425)]

        textsurface1 = font.render(label, True, WHITE)
        textrect1 = textsurface1.get_rect()
        textrect1.center = (250, 125)

        line = [SCORE.replace('\n', '') for SCORE in line]

        textsurface2 = font.render(str("1. " + line[0]), True, WHITE)  # shows top 10 scores
        textrect2 = textsurface2.get_rect()
        textrect2.center = positions[0]

        textsurface3 = font.render(str("2. " + line[1]), True, WHITE)
        textrect3 = textsurface3.get_rect()
        textrect3.center = positions[1]

        textsurface4 = font.render(str("3. " + line[2]), True, WHITE)
        textrect4 = textsurface4.get_rect()
        textrect4.center = positions[2]

        textsurface5 = font.render(str("4. " + line[3]), True, WHITE)
        textrect5 = textsurface5.get_rect()
        textrect5.center = positions[3]

        textsurface6 = font.render(str("5. " + line[4]), True, WHITE)
        textrect6 = textsurface6.get_rect()
        textrect6.center = positions[4]

        textsurface7 = font.render(str("6. " + line[5]), True, WHITE)
        textrect7 = textsurface7.get_rect()
        textrect7.center = positions[5]

        textsurface8 = font.render(str("7. " + line[6]), True, WHITE)
        textrect8 = textsurface8.get_rect()
        textrect8.center = positions[6]

        textsurface9 = font.render(str("8. " + line[7]), True, WHITE)
        textrect9 = textsurface9.get_rect()
        textrect9.center = positions[7]

        textsurface10 = font.render(str("9. " + line[8]), True, WHITE)
        textrect10 = textsurface10.get_rect()
        textrect10.center = positions[8]

        textsurface11 = font.render(str("10. " + line[9]), True, WHITE)
        textrect11 = textsurface11.get_rect()
        textrect11.center = positions[9]

        textsurface12 = font.render(leave, True, WHITE)
        textrect12 = textsurface12.get_rect()
        textrect12.center = positions[10]

        screen.blit(textsurface1, textrect1)
        screen.blit(textsurface2, textrect2)
        screen.blit(textsurface3, textrect3)
        screen.blit(textsurface4, textrect4)
        screen.blit(textsurface5, textrect5)
        screen.blit(textsurface6, textrect6)
        screen.blit(textsurface7, textrect7)
        screen.blit(textsurface8, textrect8)
        screen.blit(textsurface9, textrect9)
        screen.blit(textsurface10, textrect10)
        screen.blit(textsurface11, textrect11)
        screen.blit(textsurface12, textrect12)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.stop()
                pygame.quit()
                sys.exit()
        key = pygame.key.get_pressed() #if enter key is pressed, returns to menu
        if key[pygame.K_RETURN]:
            begin=0
        pygame.display.flip()

    pygame.display.update()
