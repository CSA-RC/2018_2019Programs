##                 END OF TERMS AND CONDITIONS
##
##        How to Apply These Terms to Your New Programs
##If you develop a new program, and you want it to be of the greatest possible use to the public, the best way to achieve this is to make it free software which everyone can redistribute and change under these terms.
##
##To do so, attach the following notices to the program. It is safest to attach them to the start of each source file to most effectively state the exclusion of warranty; and each file should have at least the "copyright" line and a pointer to where the full notice is found.
##
##{one line to give the program's name and a brief idea of what it does.}
##Copyright (C) 2018  {name of author}
##
##This program is free software: you can redistribute it and/or modify
##it under the terms of the GNU General Public License as published by
##the Free Software Foundation, either version 3 of the License, or
##(at your option) any later version.
##
##This program is distributed in the hope that it will be useful,
##but WITHOUT ANY WARRANTY; without even the implied warranty of
##MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##GNU General Public License for more details.
##
##You should have received a copy of the GNU General Public License
##along with this program.  If not, see <http://www.gnu.org/licenses/>.
##Also add information on how to contact you by electronic and paper mail.
##
##If the program does terminal interaction, make it output a short notice like this when it starts in an interactive mode:
##
##MC-Originals  Copyright (C) 2018  CSA-RJU
##This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
##This is free software, and you are welcome to redistribute it
##under certain conditions; type `show c' for details.
##The hypothetical commands show w' and show c' should show the appropriate parts of the General Public License. Of course, your program's commands might be different; for a GUI interface, you would use an "about box".
##
##You should also get your employer (if you work as a programmer) or school, if any, to sign a "copyright disclaimer" for the program, if necessary. For more information on this, and how to apply and follow the GNU GPL, see http://www.gnu.org/licenses/.
##
##The GNU General Public License does not permit incorporating your program into proprietary programs. If your program is a subroutine library, you may consider it more useful to permit linking proprietary applications with the library. If this is what you want to do, use the GNU Lesser General Public License instead of this License. But first, please read http://www.gnu.org/philosophy/why-not-lgpl.html.

import pygame, random, os
from sprite_maker import Ship, Asteroid, Star, Beam, Big_Beam, Gold_Beam, Big_Gold_Beam, Dist_Beam, Big_Dist_Beam, Torpidorito, LilFlame, Flame

global carryOn, titleOn, Ptext, Ttext, HTPtext, Ctext, timeout, FUEL, ship_type, accesory_type, FUEL_GAIN, SHIELD, RF_FUEL, MLG_SHOTS, PU_COUNT, SCORE, HEALTH, HEALTH_GAIN, rect_beams, traffic_speedy, speed_points, all_scoreslist1, all_scoreslist2, Power_up_y, Game_finish, WIN, START_UP, Galaxy, SoundMute, MusicMute, SONG_END

SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)

pygame.mixer.pre_init(44100, 16, 20, 0) #frequency, size, channels, buffersize

pygame.init()

#Colors  ( R )( G )( B )
BLACK  = (  0,   0,   0)
GREEN  = ( 50, 200, 100)
GREY   = (100, 100, 100)
WHITE  = (255, 255, 255)
RED    = (255,   0,   0)
PURPLE = (255,   0, 255)
YELLOW = (255, 255,   0)
CYAN   = (130, 170, 230)
BLUE   = (  0,   0, 255)
colorList = (RED, GREEN, PURPLE, YELLOW, CYAN, BLUE)

# Mis. definitions
traffic_speedy = 1
decor_speedy = 10 
LRspeed = 0
speed_points = 0
color = 1
touchingwall = 0 
BEAMSIZEx = 3
BEAMSIZEy = 12
B_BEAM_CHARGE = 0
M_BEAM_CHARGE = 0
FUEL = 3600
COIN_FRAME = 1
PU_COUNT = 0
SHIELD = 0
MLG_SHOTS = 0
RF_FUEL = 0
SCORE = 0
HEALTH = 100
HEALTH_GAIN = 0
ship_type = 1
accesory_type = 0
A1_Hit_Time = 0
A2_Hit_Time = 0
A3_Hit_Time = 0
A4_Hit_Time = 0
PU_type = random.randrange(1,4)
background_picker = random.randrange(1,52)
mousexy = (0, 0)
beams = []
asteroids = []
Game_finish = True
Score_Reset = True
WIN = False
START_UP = True
timeout = False
RemP_image = False
Rem1_rect = False
Rem2_rect = False
Rem3_rect = False
Rem4_rect = False
Rem1_image = False
Rem2_image = False
Rem3_image = False
Rem4_image = False
Rem1_coin = False
Rem2_coin = False
Rem3_coin = False
Rem4_coin = False
RemPU_rect = False
Crash1 = False
Crash2 = False
Crash3 = False
Crash4 = False
Ptext = "off"
HTPtext = "off"
Ctext = "off"
AdminBlocktext = "off"
SoundMute = "on"
MusicMute = "on"

# Screen definition
SCREENWIDTH = 700
SCREENHEIGHT = 600
size = (SCREENWIDTH, SCREENHEIGHT) 
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Last Defence") 

# Images
## Background
Title_Galaxy = pygame.image.load('nebula.jpg').convert()
Title_Galaxy = pygame.transform.scale(Title_Galaxy, (700, 500))
if background_picker >= 1 and background_picker <= 10:
    Galaxy = pygame.image.load('galaxy.jpg').convert() 
    Galaxy = pygame.transform.scale(Galaxy, (700, 500))
elif background_picker >= 2 and background_picker <= 20:
    Galaxy = pygame.image.load('galaxy 2.jpg').convert()
    Galaxy = pygame.transform.scale(Galaxy, (700, 500))
elif background_picker >= 3 and background_picker <= 30:
    Galaxy = pygame.image.load('galaxy 3.jpg').convert()
    Galaxy = pygame.transform.scale(Galaxy, (700, 500))
elif background_picker >= 4 and background_picker <= 40:
    Galaxy = pygame.image.load('galaxy 4.jpg').convert()
    Galaxy = pygame.transform.scale(Galaxy, (700, 500))
elif background_picker >= 5 and background_picker <= 50:
    Galaxy = pygame.image.load('galaxy 5.jpg').convert()
    Galaxy = pygame.transform.scale(Galaxy, (700, 500))
else:
    Galaxy = pygame.image.load('galaxy 6.jpg').convert()
    Galaxy = pygame.transform.scale(Galaxy, (700, 500))
Solar_System = pygame.image.load('solar system.jpg')

## Ships
Ship1 = pygame.image.load('Spaceship-1.png').convert_alpha()
BigShip1 = pygame.transform.scale(Ship1, (160, 232))
Ship2 = pygame.image.load('Spaceship-2.png').convert_alpha()
BigShip2 = pygame.transform.scale(Ship2, (160, 232))
Ship3 = pygame.image.load('Spaceship-3.png').convert_alpha()
BigShip3 = pygame.transform.scale(Ship3, (160, 232))
ShipS = pygame.image.load('Spaceship-S.png').convert_alpha()
BigShipS = pygame.transform.scale(ShipS, (160, 232))
ShipS_L  = pygame.image.load('Spaceship-S (Locked).png').convert_alpha()
BigShipS_L  = pygame.transform.scale(ShipS_L, (160, 232))

Ship_Desc_1  = pygame.image.load('ship description (1).png')
Ship_Desc_1B  = pygame.image.load('ship description (1B).png')
Ship_Desc_2  = pygame.image.load('ship description (2).png')
Ship_Desc_2B  = pygame.image.load('ship description (2B).png')
Ship_Desc_3  = pygame.image.load('ship description (3).png')
Ship_Desc_3B  = pygame.image.load('ship description (3B).png')
Ship_Desc_S  = pygame.image.load('ship description (S).png')
Ship_Desc_SB  = pygame.image.load('ship description (SB).png')

## Accessories
MLGlasses = pygame.image.load('MLGlasses.png').convert_alpha()
BigMLGlasses = pygame.transform.scale(MLGlasses, (230, 112))
Angry_Eyes = pygame.image.load('angry eyes.png').convert_alpha()
BigAngry_Eyes = pygame.transform.scale(Angry_Eyes, (190, 112))

Accesory_Desc_0  = pygame.image.load('accesory description (0).png')
Accesory_Desc_1  = pygame.image.load('accesory description (1).png')
Accesory_Desc_2  = pygame.image.load('accesory description (2).png')

How_to_Play = pygame.image.load('How to Play.png')

## Power ups
Time_Up = pygame.image.load('Time +.png')
Shield = pygame.image.load('Shield.png')
Rapid_Fire = pygame.image.load('Rapid Fire.png')
MLG = pygame.image.load('MLG.png')
Bubble = pygame.image.load('Bubble.png')

## Duplicates
Health = pygame.image.load('health.jpg')
Health_Bar = pygame.image.load('health bar.png')
Fuel = pygame.image.load('fuel.jpg')
Coin_F1 = pygame.image.load('Coin (1).png')
Coin_F2 = pygame.image.load('Coin (2).png')
Coin_F3 = pygame.image.load('Coin (3).png')
Coin_F4 = pygame.image.load('Coin (4).png')
Hitmarker = pygame.image.load('HITMARKER.png')
Broken_Asteroid = pygame.image.load('asteroid (broken).png')
Broken_Asteroid_2 = pygame.image.load('asteroid (broken)2.png')
Broken_Asteroid_3 = pygame.image.load('asteroid (broken)3.png')

## GUIs
Title_Gui = pygame.image.load('TITLE GUI.png')
Mixer_Gui = pygame.image.load('MIXER GUI.png')
Sound_Check = pygame.image.load('SOUND CHECK.png')
Music_Check = pygame.image.load('MUSIC CHECK.png')
Block_Gui = pygame.image.load('BLOCK (admin1111).png')
Pu_Gui = pygame.image.load('PU GUI.png')
Pause_Gui = pygame.image.load('PAUSED.png')
Customize_Gui = pygame.image.load('CUSTOMIZE GUI.png')
Customize_Arrows = pygame.image.load('CUSTOMIZE ARROWS.png')
Customize_Na = pygame.image.load('CUSTOMIZE NA.png')
Customize_Back = pygame.image.load('CUSTOMIZE BACK.png')

# Music
Titlesong = pygame.mixer.music.load('Dance Energetic.wav')

# Sounds
Crunch = pygame.mixer.Sound('Crunch.wav')
Crunch_D = pygame.mixer.Sound('Crunch-D.wav')
Pew = pygame.mixer.Sound('Pew.wav')
Pew_D = pygame.mixer.Sound('Pew-D.wav')
Win = pygame.mixer.Sound('Win (WAV).wav')
Lose = pygame.mixer.Sound('Oops.wav')
Evil_Laugh = pygame.mixer.Sound('Evil Laugh.wav')
Collect = pygame.mixer.Sound('Coin.wav')
Coin = pygame.mixer.Sound('Collect.wav')
Ship_Hit = pygame.mixer.Sound('Clang.wav')
Reflect = pygame.mixer.Sound('Squeaky Toy.wav')
Error = pygame.mixer.Sound('XP ERROR.wav')
Hit_marker = pygame.mixer.Sound('HITMARKER.wav')
Snipe = pygame.mixer.Sound('snipe.wav')

# Text 
## Variables
pu_countfont = pygame.font.Font('orbitron-black.ttf', 20)
pu_counttextSurface = pu_countfont.render("x", True, WHITE)
pu_counttextRect = pu_counttextSurface.get_rect()
pu_counttextRect.center = (95, 580)

shieldfont = pygame.font.Font('orbitron-black.ttf', 20)
shieldtextSurface = shieldfont.render("Shield: ", True, WHITE)
shieldtextRect = shieldtextSurface.get_rect()
shieldtextRect.center = (SCREENWIDTH - 100, 480) 

scorefont = pygame.font.Font('orbitron-black.ttf', 20)
scoretextSurface = scorefont.render("0", True, WHITE) 
scoretextRect = scoretextSurface.get_rect()
scoretextRect.center = (100, 520)

timefont = pygame.font.Font('orbitron-black.ttf', 12)
timetextSurface = timefont.render("0", True, GREEN)
timetextRect = timetextSurface.get_rect()
timetextRect.center = (416, 531)

livesfont = pygame.font.Font('orbitron-black.ttf', 20)
livestextSurface = livesfont.render("0", True, WHITE)
livestextRect = livestextSurface.get_rect()
livestextRect.center = (560, 520)

pu_counttextSurface = pu_countfont.render("x0", True, WHITE)
timetextSurface = timefont.render((str(int(FUEL / 60))), True, GREEN)
scoretextSurface = scorefont.render(("Score: " +(str(SCORE))), True, WHITE )
livestextSurface = livesfont.render(("Lives: " +(str(HEALTH))), True, BLACK)

## Title screen
titlefont = pygame.font.Font('orbitron-black.ttf', 120)
titletextSurface = titlefont.render("Last", True, WHITE)
titletextRect = titletextSurface.get_rect()
titletextRect.center = (160, 80)

titleHfont = pygame.font.Font('orbitron-black.ttf', 100)
titleHtextSurface = titleHfont.render("Defence", True, WHITE)
titleHtextRect = titleHtextSurface.get_rect()
titleHtextRect.center = (450, 180)

title2font = pygame.font.Font('orbitron-black.ttf', 50)
title2textSurface = title2font.render("Press P to start", True, WHITE)
title2textRect = title2textSurface.get_rect()
title2textRect.center = (450, 300)

HTPfont = pygame.font.Font('orbitron-black.ttf', 50)
HTPtextSurface = HTPfont.render("How to play", True, WHITE)
HTPtextRect = HTPtextSurface.get_rect()
HTPtextRect.center = (450, 415)

topfont = pygame.font.Font('orbitron-black.ttf', 10)
toptextSurface = topfont.render("Top Scores:", True, BLACK)
toptextRect = toptextSurface.get_rect()
toptextRect.center = (100, 190)

resetfont = pygame.font.Font('orbitron-black.ttf', 45)
resettextSurface = resetfont.render("Reset", True, WHITE)
resettextRect = resettextSurface.get_rect()
resettextRect = (33, 436)

S1font = pygame.font.Font('orbitron-black.ttf', 15)
S1textSurface = S1font.render("0", True, BLACK)
S1textRect = S1textSurface.get_rect()
S1textRect.center = (50, 210)

S2font = pygame.font.Font('orbitron-black.ttf', 15) 
S2textSurface = S2font.render("0", True, BLACK)
S2textRect = S2textSurface.get_rect()
S2textRect.center = (50, 230)

S3font = pygame.font.Font('orbitron-black.ttf', 15)
S3textSurface = S3font.render("0", True, BLACK)
S3textRect = S3textSurface.get_rect()
S3textRect.center = (50, 250)

S4font = pygame.font.Font('orbitron-black.ttf', 15)
S4textSurface = S4font.render("0", True, BLACK)
S4textRect = S4textSurface.get_rect()
S4textRect.center = (50, 270)

S5font = pygame.font.Font('orbitron-black.ttf', 15)
S5textSurface = S5font.render("0", True, BLACK) 
S5textRect = S5textSurface.get_rect()
S5textRect.center = (50, 290)

S6font = pygame.font.Font('orbitron-black.ttf', 15)
S6textSurface = S6font.render("0", True, BLACK)
S6textRect = S6textSurface.get_rect()
S6textRect.center = (50, 310)

S7font = pygame.font.Font('orbitron-black.ttf', 15)
S7textSurface = S7font.render("0", True, BLACK)
S7textRect = S7textSurface.get_rect()
S7textRect.center = (50, 330)

S8font = pygame.font.Font('orbitron-black.ttf', 15)
S8textSurface = S8font.render("0", True, BLACK)
S8textRect = S8textSurface.get_rect()
S8textRect.center = (50, 350)

S9font = pygame.font.Font('orbitron-black.ttf', 15)
S9textSurface = S9font.render("0", True, BLACK)
S9textRect = S9textSurface.get_rect()
S9textRect.center = (50, 370)

S10font = pygame.font.Font('orbitron-black.ttf', 15)
S10textSurface = S10font.render("0", True, BLACK)
S10textRect = S10textSurface.get_rect()
S10textRect.center = (50, 390)

#Sprites
playerCar = Ship(60, 80, 70)
playerCar.rect.x = 310
playerCar.rect.y = SCREENHEIGHT - 200
playerCar_list = pygame.sprite.Group()
playerCar_list.add(playerCar)

## Specifically the asteroid sprites
car1 = Asteroid(60, 0, random.randint(50, 100))
car1.rect.x = 50
car1.rect.y = -200
car1_list = pygame.sprite.Group()
car1_list.add(car1)

car2 = Asteroid(60, 0, random.randint(50, 100))
car2.rect.x = 200
car2.rect.y = -700
car2_list = pygame.sprite.Group()
car2_list.add(car2)

car3 = Asteroid(60, 0, random.randint(50, 100))
car3.rect.x = 350
car3.rect.y = -400
car3_list = pygame.sprite.Group()
car3_list.add(car3)

car4 = Asteroid(60, 0, random.randint(50, 100))
car4.rect.x = 500
car4.rect.y = -1000
car4_list = pygame.sprite.Group()
car4_list.add(car4)

## Specifically the star sprites
tree1 = Star(60, 0, random.randint(50, 100))
tree1.rect.x = -300
tree1.rect.y = -100
tree2 = Star(60, 0, random.randint(50, 100))
tree2.rect.x = 0
tree2.rect.y = -400
tree3 = Star(60, 0, random.randint(50, 100))
tree3.rect.x = 300
tree3.rect.y = -200
tree4 = Star(60, 0, random.randint(50, 100))
tree4.rect.x = 600
tree4.rect.y = -600

# This will be a list that will contain all the sprites we intend to use in our game.
## Add the car to the list of objects
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(playerCar)
all_sprites_list.add(car1)
all_sprites_list.add(car2)
all_sprites_list.add(car3)
all_sprites_list.add(car4)
all_sprites_list.add(tree1)
all_sprites_list.add(tree2)
all_sprites_list.add(tree3)
all_sprites_list.add(tree4)

## Just the oncoming asteroids
all_coming_cars = pygame.sprite.Group()
all_coming_cars.add(car1)
all_coming_cars.add(car2)
all_coming_cars.add(car3)
all_coming_cars.add(car4)

## Just decorations to make the game look better
all_coming_decor = pygame.sprite.Group()
all_coming_decor.add(tree1)
all_coming_decor.add(tree2)
all_coming_decor.add(tree3)
all_coming_decor.add(tree4)

rect_beams = pygame.sprite.Group()

rect_flames = pygame.sprite.Group()


Ship_sensor = {'rect': pygame.Rect(playerCar.rect.x + 16, playerCar.rect.y + 5, 50, 73)}

A1 = {'rect': pygame.Rect(car1.rect.x + 58, car1.rect.y + 100, 46, 33)}
A2 = {'rect': pygame.Rect(car2.rect.x + 58, car2.rect.y + 100, 46, 33)}
A3 = {'rect': pygame.Rect(car3.rect.x + 58, car3.rect.y + 100, 46, 33)}
A4 = {'rect': pygame.Rect(car4.rect.x + 58 , car4.rect.y + 100, 46, 33)}
asteroids.append(A1)
asteroids.append(A2)
asteroids.append(A3)
asteroids.append(A4)

Power_up_x = random.randrange(0, 630)
Power_up_y = -2000
Power_up = {'rect': pygame.Rect(Power_up_x, Power_up_y, 50, 60)}

everyOn = True
carryOn = False
titleOn = False
clock = pygame.time.Clock()

# Opens the file of top scores
def Check_scores1():
    global all_scoreslist1, SCORE
    if Game_finish == True or Score_Reset == True:
        all_scoreslist1 = [] 
        open_scores = open("Star_Battles_HScores.txt", "r")
        line = open_scores.readline() #Reads the first line once to get it started.
        while line:  # Assures the program runs through the whole script.
            all_scoreslist1.append(line)
            line = open_scores.readline()  # Assures that the program checks more than one line.
    ##    all_scorestext = (("1: " + str(all_scoresstring[0])) + "\n 2: " + (str(all_scoresstring[1])) + "\n 3: " + (str(all_scoresstring[2])) + "\n 4: " + (str(all_scoresstring[3])) + "\n 5: " + (str(all_scoresstring[4])) + "\n 6: " + (str(all_scoresstring[5])) + "\n 7: " + (str(all_scoresstring[6])) + "\n 8: " + (str(all_scoresstring[7])) + "\n 9: " + (str(all_scoresstring[8])) + "\n 10: " + (str(all_scoresstring[9])))
        open_scores.close()
        Check_scores2()

def Check_scores2():
    global all_scoreslist1, all_scoreslist2, SCORE, WIN
    done = False
    previous_score = 0
    all_scoreslist2 = []
    for x in all_scoreslist1:  # Checks every line separated into a list.
        linesplit = x.split(":")
        if linesplit[0] == '1'and done != True:
            if SCORE > int(linesplit[1]):
                adder = int(SCORE)
                done = True
                WIN = True
            else:
                adder = linesplit[1]
                done = False
            all_scoreslist2.append(adder)
            
        if linesplit[0] == '2'and done != True:
            if SCORE > int(linesplit[1]):
                adder = int(SCORE)
                previous_score = int(SCORE)
                done = True
                WIN = True
            else:
                adder = linesplit[1]
                done = False
            all_scoreslist2.append(adder)
        elif linesplit[0] == '2'and done != False:
            all_scoreslist2.append(previous_score[1])
            
        if linesplit[0] == '3'and done != True:
            if SCORE > int(linesplit[1]):
                adder = int(SCORE)
                previous_score = int(SCORE)
                done = True
                WIN = True
            else:
                adder = linesplit[1]
                done = False
            all_scoreslist2.append(adder)
        elif linesplit[0] == '3'and done != False:
            all_scoreslist2.append(previous_score[1])
            
        if linesplit[0] == '4'and done != True:
            if SCORE > int(linesplit[1]):
                adder = int(SCORE)
                previous_score = int(SCORE)
                done = True
                WIN = True
            else:
                adder = linesplit[1]
                done = False
            all_scoreslist2.append(adder)
        elif linesplit[0] == '4'and done != False:
            all_scoreslist2.append(previous_score[1])
            
        if linesplit[0] == '5'and done != True:
            if SCORE > int(linesplit[1]):
                adder = int(SCORE)
                previous_score = int(SCORE)
                done = True
                WIN = True
            else:
                adder = linesplit[1]
                done = False
            all_scoreslist2.append(adder)
        elif linesplit[0] == '5'and done != False:
            all_scoreslist2.append(previous_score[1])
            
        if linesplit[0] == '6'and done != True:
            if SCORE > int(linesplit[1]):
                adder = int(SCORE)
                previous_score = int(SCORE)
                done = True
                WIN = True
            else:
                adder = linesplit[1]
                done = False
            all_scoreslist2.append(adder)
        elif linesplit[0] == '6'and done != False:
            all_scoreslist2.append(previous_score[1])
            
        if linesplit[0] == '7'and done != True:
            if SCORE > int(linesplit[1]):
                adder = int(SCORE)
                previous_score = int(SCORE)
                done = True
                WIN = True
            else:
                adder = linesplit[1]
                done = False
            all_scoreslist2.append(adder)
        elif linesplit[0] == '7'and done != False:
            all_scoreslist2.append(previous_score[1])
            
        if linesplit[0] == '8'and done != True:
            if SCORE > int(linesplit[1]):
                adder = int(SCORE)
                previous_score = int(SCORE)
                done = True
                WIN = True
            else:
                adder = linesplit[1]
                done = False
            all_scoreslist2.append(adder)
        elif linesplit[0] == '8'and done != False:
            all_scoreslist2.append(previous_score[1])
            
        if linesplit[0] == '9'and done != True:
            if SCORE > int(linesplit[1]):
                adder = int(SCORE)
                previous_score = int(SCORE)
                done = True
                WIN = True
            else:
                adder = linesplit[1]
                done = False
            all_scoreslist2.append(adder)
        elif linesplit[0] == '9'and done != False:
            all_scoreslist2.append(previous_score[1])
            
        if linesplit[0] == '10'and done != True:
            if SCORE > int(linesplit[1]):
                adder = int(SCORE)
                previous_score = int(SCORE)
                done = True
                WIN = True
            else:
                adder = linesplit[1]
                done = False
            all_scoreslist2.append(adder)
        elif linesplit[0] == '10'and done != False: 
            all_scoreslist2.append(previous_score[1])
        previous_score = linesplit
    all_scoreslist1 = [("1:" + (str(all_scoreslist2[0]))), ("2:" + (str(all_scoreslist2[1]))), ("3:" + (str(all_scoreslist2[2]))), ("4:" + (str(all_scoreslist2[3]))), ("5:" + (str(all_scoreslist2[4]))), ("6:" + (str(all_scoreslist2[5]))), ("7:" + (str(all_scoreslist2[6]))), ("8:" + (str(all_scoreslist2[7]))), ("9:" + (str(all_scoreslist2[8]))), ("10:" + (str(all_scoreslist2[9])))]
    Write_scores()
    
def Write_scores():
    global all_scoreslist1
    scorecheck = open("Star_Battles_HScores.txt", "w")
    for x in all_scoreslist1:
        scorecheck.write(str(x)) #Shows what was tryed, when, and if it was successful, with spacing inbetween.
        scorecheck.write("\n") #This is so that the .txt file does not just have one big line of entrys.
    scorecheck.close()
    Score_Reset = False

def Reset_scores():
    global ship_type
    if ship_type == 4:
        ship_type = 1

    if SoundMute == "off":
        Evil_Laugh.play()

    Score_Reset = True

    all_scoreslist1 = [("1:0:"), ("2:0:"), ("3:0:"), ("4:0:"), ("5:0:"), ("6:0:"), ("7:0:"), ("8:0:"), ("9:0:"), ("10:0:")]
    scorecheck = open("Star_Battles_HScores.txt", "w")
    for x in all_scoreslist1:
        scorecheck.write(str(x)) #Shows what was tryed, when, and if it was successful, with spacing inbetween.
        scorecheck.write("\n") #This is so that the .txt file does not just have one big line of entrys.
    scorecheck.close()
    Check_scores1()

def doRectsOverlap(rect1, rect2):
    for a, b in [(rect1, rect2), (rect2, rect1)]:
        # Check if a's corners are inside b
        if ((isPointInsideRect(a.left, a.top, b)) or
            (isPointInsideRect(a.left, a.bottom, b)) or
            (isPointInsideRect(a.right, a.top, b)) or
            (isPointInsideRect(a.right, a.bottom, b))):
            return True

def isPointInsideRect(x, y, rect):
    if (x > rect.left) and (x < rect.right) and (y > rect.top) and (y < rect.bottom):
        return True
    else:
        return False 

# Title Screen
def Title_screen():
    global carryOn, titleOn, Ptext, Ctext, Ttext, asteroids, timeout, FUEL, accesory_type, FUEL_GAIN, SCORE, HEALTH, HEALTH_GAIN, SHIELD, RF_FUEL, MLG_SHOTS, PU_COUNT, rect_beams, traffic_speedy, speed_points, Power_up_y, Galaxy, SoundMute, MusicMute, SONG_END, Game_finish
    carryOn = False
    titleOn = True
    asteroids = []
    SCORE = 0
    HEALTH = 100
    HEALTH_GAIN = 0
    FUEL = 3601
    FUEL_GAIN = 0
    SHIELD = 0
    RF_FUEL = 0
    MLG_SHOTS = 0
    PU_COUNT = 0
    Power_up_y = -2000
    Ptext = "off"
    Ctext = "off"
    Ttext = "on"

    for beam in rect_beams:
        rect_beams.remove(beam)
    beams.clear()

    for flame in rect_flames:
        rect_flames.remove(flame)
    
    pygame.mixer.music.stop()
    if Game_finish == True:
        if WIN == True:
            if SoundMute == "off":
                Win.play()
            if MusicMute == "off":
                Titlesong = pygame.mixer.music.load('Video Game 1.wav')
                pygame.mixer.music.play(-1)
        elif WIN == False:
            if START_UP == False:
                if SoundMute == "off": 
                    Lose.play()
                if MusicMute == "off":
                    Titlesong = pygame.mixer.music.load('Dance Energetic.wav')
                    pygame.mixer.music.play(-1)
            else:
                if MusicMute =="off":
                    Titlesong = pygame.mixer.music.load('Dance Energetic.wav')
                    pygame.mixer.music.play(-1)
    else:
        if MusicMute == "off":
            Titlesong = pygame.mixer.music.load('Dance Energetic.wav')
            pygame.mixer.music.play(-1)

    
    screen.blit(Title_Galaxy, (0, 0))
    traffic_speedy = 1
    speed_points = 0
    
    playerCar.rect.x = 310
    car1.rect.y = -200
    car2.rect.y = -700
    car3.rect.y = -400
    car4.rect.y = -1000

    background_picker = random.randrange(1,52)
    if background_picker >= 1 and background_picker <= 10:
        Galaxy = pygame.image.load('galaxy.jpg').convert()
        Galaxy = pygame.transform.scale(Galaxy, (700, 500))
    elif background_picker >= 2 and background_picker <= 20:
        Galaxy = pygame.image.load('galaxy 2.jpg').convert()
        Galaxy = pygame.transform.scale(Galaxy, (700, 500))
    elif background_picker >= 3 and background_picker <= 30:
        Galaxy = pygame.image.load('galaxy 3.jpg').convert()
        Galaxy = pygame.transform.scale(Galaxy, (700, 500))
    elif background_picker >= 4 and background_picker <= 40:
        Galaxy = pygame.image.load('galaxy 4.jpg').convert()
        Galaxy = pygame.transform.scale(Galaxy, (700, 500))
    elif background_picker >= 5 and background_picker <= 50:
        Galaxy = pygame.image.load('galaxy 5.jpg').convert()
        Galaxy = pygame.transform.scale(Galaxy, (700, 500))
    else:
        Galaxy = pygame.image.load('galaxy 6.jpg').convert()
        Galaxy = pygame.transform.scale(Galaxy, (700, 500))

    Game_finish = False 

def Weaponry_screen():
    global Ptext, Ttext, Ctext
    Ptext = "off"
    Ttext = "off"
    Ctext = "on"

def Pause():
    global carryOn, Ptext, Ttext, Ctext
    carryOn = False
    Ctext = "off"
    Ptext = "on"

def Unpause():
    global carryOn, Ptext, Ttext, Ctext, HTPtext, titleOn, START_UP, SoundMute, MusicMute
    carryOn = True
    titleOn = False
    START_UP = False
    if Ptext == "on" or Ttext == "on" or Ctext == "on":
        Playsong = pygame.mixer.music.load('Video Game 2.wav')
        if MusicMute == "off":
            pygame.mixer.music.play(-1)
    Ptext = "off"
    Ctext = "off"
    Ttext = "off"
    HTPtext = "off"

Check_scores1()
Title_screen()

# Anything that updates ever
while everyOn:
    # To pause/quit the game
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            everyOn = False
        if event.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed()
            
            #When "P" is pressed
            if event.key == pygame.K_p:
                if carryOn == True and Ctext == "off":
                    if timeout == True:
                        timeout = False
                    if ship_type != 4 or ship_type == 4 and int(all_scoreslist2[0]) >= 7500:
                        Pause()
                elif carryOn == False and titleOn == False or carryOn == False and titleOn == True and Ctext == "off":
                    if timeout == True:
                        timeout = False
                    if ship_type != 4 or ship_type == 4 and int(all_scoreslist2[0]) >= 7500:
                        Unpause()

            #When "U" is pressed
            if Ttext == "on" and HTPtext == "off" and AdminBlocktext == "on" and carryOn == False and key[pygame.K_a] and key[pygame.K_d] and key[pygame.K_m] and key[pygame.K_i] and key[pygame.K_n]:
                Reset_scores()
                AdminBlocktext = "off"
                Score_Reset = True
            NEWBEAMx1 = playerCar.rect.x + 40
            if event.key == pygame.K_u:
                if carryOn == True:
                    beams.append(pygame.Rect(NEWBEAMx1, playerCar.rect.y +  0, BEAMSIZEx, BEAMSIZEy))
                    if accesory_type == 2:
                        Newbiem = (rect_beams.add(Dist_Beam((NEWBEAMx1 - 10), (playerCar.rect.y + 10), BEAMSIZEx, BEAMSIZEy, 20)))
                        if SoundMute == "off":
                            Pew_D.play()
                    elif ship_type >= 1 and ship_type <= 3:
                        Newbiem = (rect_beams.add(Beam((NEWBEAMx1 - 10), (playerCar.rect.y + 10), BEAMSIZEx, BEAMSIZEy, 20)))
                        if SoundMute == "off":
                            Pew.play()
                    elif ship_type == 4:
                        Newbiem = (rect_beams.add(Gold_Beam((NEWBEAMx1 - 10), (playerCar.rect.y + 10), BEAMSIZEx, BEAMSIZEy, 20)))
                        if SoundMute == "off":
                            Pew.play()
                if Ptext == "on":
                    Title_screen()

            # When "I" is pressed
            if event.key == pygame.K_i:
                if carryOn == True and B_BEAM_CHARGE <= 0:
                    beams.append(pygame.Rect(NEWBEAMx1 - 5, playerCar.rect.y + 10, BEAMSIZEx + 10, BEAMSIZEy + 40))
                    if accesory_type == 1:
                        Newbiem = (rect_beams.add(Torpidorito((NEWBEAMx1 - 23), (playerCar.rect.y + 5), BEAMSIZEx, BEAMSIZEy, 20)))
##                        MLG_SHOTS -= 1
                        if SoundMute == "off":
                            Snipe.play()
                    elif accesory_type == 2:
                        Newbiem = (rect_beams.add(Big_Dist_Beam((NEWBEAMx1 - 48), (playerCar.rect.y - 85), BEAMSIZEx, BEAMSIZEy, 20)))
                        if SoundMute == "off":
                            Pew_D.play()
                    elif ship_type == 4:
                        Newbiem = (rect_beams.add(Big_Gold_Beam((NEWBEAMx1 - 48), (playerCar.rect.y + 85), BEAMSIZEx, BEAMSIZEy, 20)))
                        if SoundMute == "off":
                            Pew.play()
                    else:
                        Newbiem = (rect_beams.add(Big_Beam((NEWBEAMx1 - 48), (playerCar.rect.y - 85), BEAMSIZEx, BEAMSIZEy, 20)))
                        if SoundMute == "off":
                            Pew.play()
                    B_BEAM_CHARGE = 30
                        
                if Ptext == "on" and Ctext == "off":
                    Weaponry_screen()
                elif Ctext == "on" and Ptext == "off" and titleOn == False:
                    if ship_type != 4 or ship_type == 4 and int(all_scoreslist2[0]) >= 7500:
                        Pause()

            # When "O" is pressed
            if carryOn == True and M_BEAM_CHARGE <= 0 and event.key == pygame.K_o:
                for i in range(4):
                    beams.append(pygame.Rect(0 + (150 * i), SCREENHEIGHT - 70, 150, BEAMSIZEy))
                for i in range(40):
                    NEWBEAMx2 = random.randint(0, SCREENWIDTH - BEAMSIZEx)
                    if accesory_type == 2:
                        Newbiem = (rect_beams.add(Dist_Beam((NEWBEAMx2), (SCREENHEIGHT - 60), BEAMSIZEx, BEAMSIZEy, 20)))
                        if SoundMute == "off":
                            Pew_D.play()
                    elif ship_type >= 1 and ship_type <= 3:
                        Newbiem = (rect_beams.add(Beam((NEWBEAMx2), (SCREENHEIGHT - 60), BEAMSIZEx, BEAMSIZEy, 20)))
                        if SoundMute == "off":
                            Pew.play()
                    elif ship_type == 4:
                        Newbiem = (rect_beams.add(Gold_Beam((NEWBEAMx2), (SCREENHEIGHT - 60), BEAMSIZEx, BEAMSIZEy, 20)))
                        if SoundMute == "off":
                            Pew.play()
                M_BEAM_CHARGE = 350
                
            # When "W" is pressed
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                if Ttext == "off" and Ptext == "off" and Ctext == "on":
                    if accesory_type < 2:
                        accesory_type += 1
                    elif accesory_type == 2:
                        accesory_type = 0
                        
            # When "S" is pressed
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                if Ttext == "off" and Ptext == "off" and Ctext == "on":
                    if accesory_type > 0:
                        accesory_type -= 1
                    elif accesory_type == 0:
                        accesory_type = 2

            # When "A" is pressed
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                if Ttext == "off" and Ptext == "off" and Ctext == "on":
                    if ship_type > 1:
                        ship_type -= 1
                    elif ship_type == 1:
                        ship_type = 4

            # When "D" is pressed
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                if Ttext == "off" and Ptext == "off" and Ctext == "on":
                    if ship_type < 4:
                        ship_type += 1
                    elif ship_type == 4:
                        ship_type = 1

        #Moving the mouse
        if event.type == pygame.MOUSEMOTION:
            mousexy = event.pos
        if event.type == 5:
            #How to play button
            if Ttext == "on" and HTPtext == "off":
                if mousexy[0] >= 270 and mousexy[0] <= (270 + 360) and mousexy[1] >= 360 and mousexy[1] <= (360 + 100):
                    HTPtext = "on"
            elif Ttext == "on" and HTPtext == "on":
                if mousexy[0] >= 540 and mousexy[0] <= (540 + 120) and mousexy[1] >= 439 and mousexy[1] <= (439 + 50):
                    HTPtext = "off"

            #Highscore reset button
            if Ttext == "on" and HTPtext == "off" and AdminBlocktext == "off":
                if mousexy[0] >= 20 and mousexy[0] <= (20 + 175) and mousexy[1] >= 425 and mousexy[1] <= (425 + 60):
                    AdminBlocktext = "on"
                    if SoundMute == "off":
                        Error.play()
            elif Ttext == "on" and HTPtext == "off" and AdminBlocktext == "on":
                if mousexy[0] >= 20 and mousexy[0] <= (20 + 175) and mousexy[1] >= 425 and mousexy[1] <= (425 + 60):
                    AdminBlocktext = "off"
                if mousexy[0] >= 481 and mousexy[0] <= (481 + 28) and mousexy[1] >= 67 and mousexy[1] <= (67 + 28):
                    AdminBlocktext = "off"

            #Music toggle button 
            if titleOn == True and Ptext == "off" and HTPtext == "off" and MusicMute == "off":
                if mousexy[0] >= 8 and mousexy[0] <= (8 + 148) and mousexy[1] > 550 and mousexy[1] < (550 + 50):
                    MusicMute = "on"
                    pygame.mixer.music.stop()
            elif titleOn == True and Ptext == "off" and HTPtext == "off" and MusicMute == "on":
                if mousexy[0] >= 8 and mousexy[0] <= (8 + 148) and mousexy[1] > 550 and mousexy[1] < (550 + 50):
                    MusicMute = "off"
                    pygame.mixer.music.play(-1)
                    
            #Sound toggle button
            if titleOn == True and Ptext == "off" and HTPtext == "off" and SoundMute == "off":
                if mousexy[0] >= 8 and mousexy[0] <= (8 + 148) and mousexy[1] > 508 and mousexy[1] < (508 + 42):
                    SoundMute = "on"
            elif titleOn == True and Ptext == "off" and HTPtext == "off" and SoundMute == "on":
                if mousexy[0] >= 8 and mousexy[0] <= (8 + 148) and mousexy[1] > 508 and mousexy[1] < (508 + 42):
                    SoundMute = "off"

            #Main menu button
            if Ttext == "off" and Ptext == "on" and carryOn == False:
                if mousexy[0] >= 16 and mousexy[0] <= (16 + 322) and mousexy[1] >= 328 and mousexy[1] <= (328 + 72):
                    Title_screen()
            
            #Weaponry button (Paused)
            if Ttext == "off" and Ptext == "on" and carryOn == False:
                if mousexy[0] >= 363 and mousexy[0] <= (363 + 322) and mousexy[1] >= 328 and mousexy[1] <= (328 + 72):
                    Weaponry_screen()
            #Weaponry button (Menu)
            if mousexy[0] >= 363 and mousexy[0] <= (363 + 322) and mousexy[1] >= 519 and mousexy[1] <= (519 + 72):
                if titleOn == True and Ptext == "off" and Ctext == "off" and carryOn == False:
                    Weaponry_screen()
                elif titleOn == True and Ptext == "off" and Ctext == "on" and carryOn == False:
                    if ship_type != 4 or ship_type == 4 and int(all_scoreslist2[0]) >= 7500:
                        Title_screen()
            #Back button (Weaponry)
            if mousexy[0] >= 574 and mousexy[0] <= (574 + 94) and mousexy[1] >= 436 and mousexy[1] <= (436 + 38):
                if titleOn == True and Ptext == "off" and Ctext == "on" and carryOn == False:
                    if ship_type != 4 or ship_type == 4 and int(all_scoreslist2[0]) >= 7500:
                        Title_screen()
                if Ttext == "off" and Ptext == "off" and Ctext == "on":
                    if ship_type != 4 or ship_type == 4 and int(all_scoreslist2[0]) >= 7500:
                        Pause()

            #Left side arrows
            if Ttext == "off" and Ptext == "off" and Ctext == "on":
                ##Left
                if mousexy[0] >= 81 and mousexy[0] <= (81 + 56) and mousexy[1] >= 130 and mousexy[1] <= (130 + 94):
                    if ship_type > 1:
                        ship_type -= 1
                    elif ship_type == 1:
                        ship_type = 4
                ##Right
                if mousexy[0] >= 242 and mousexy[0] <= (242 + 56) and mousexy[1] >= 130 and mousexy[1] <= (130 + 94):
                    if ship_type < 4:
                        ship_type += 1
                    elif ship_type == 4:
                        ship_type = 1
            #Right side arrows
            if Ttext == "off" and Ptext == "off" and Ctext == "on":
                ##Up
                if mousexy[0] >= 468 and mousexy[0] <= (468 + 94) and mousexy[1] >= 72 and mousexy[1] <= (72 + 56):
                    if accesory_type < 2:
                        accesory_type += 1
                    elif accesory_type == 2:
                        accesory_type = 0
                ##Down
                if mousexy[0] >= 468 and mousexy[0] <= (468 + 94) and mousexy[1] >= 233 and mousexy[1] <= (233 + 56):
                    if accesory_type > 0:
                        accesory_type -= 1
                    elif accesory_type == 0:
                        accesory_type = 2


    # Only for title screen:
    if Ttext == "on":
        screen.blit(Title_Galaxy, (0, 0))
        screen.blit(Title_Gui, (0, 0))
        screen.blit(titletextSurface, titletextRect)
        screen.blit(titleHtextSurface, titleHtextRect)
        screen.blit(title2textSurface, title2textRect)
        pygame.draw.rect(screen, CYAN, (270, 360, 360, 100), 0)
        
        screen.blit(HTPtextSurface, HTPtextRect)

        # Each individual score (tedious but working version)
        pygame.draw.rect(screen, CYAN, (20, 170 , 175, 240), 0)
        toptextSurface = topfont.render("Top Scores:", True, WHITE)
        screen.blit(toptextSurface, toptextRect)
        S1textSurface = S1font.render(("1:        " +(str(all_scoreslist2[0]))), True, WHITE)
        screen.blit(S1textSurface, S1textRect)
        S2textSurface = S2font.render(("2:       " +(str(all_scoreslist2[1]))), True, WHITE)
        screen.blit(S2textSurface, S2textRect)
        S3textSurface = S3font.render(("3:       " +(str(all_scoreslist2[2]))), True, WHITE)
        screen.blit(S3textSurface, S3textRect)
        S4textSurface = S4font.render(("4:       " +(str(all_scoreslist2[3]))), True, WHITE)
        screen.blit(S4textSurface, S4textRect)
        S5textSurface = S5font.render(("5:       " +(str(all_scoreslist2[4]))), True, WHITE)
        screen.blit(S5textSurface, S5textRect)
        S6textSurface = S6font.render(("6:       " +(str(all_scoreslist2[5]))), True, WHITE)
        screen.blit(S6textSurface, S6textRect)
        S7textSurface = S7font.render(("7:       " +(str(all_scoreslist2[6]))), True, WHITE)
        screen.blit(S7textSurface, S7textRect)
        S8textSurface = S8font.render(("8:       " +(str(all_scoreslist2[7]))), True, WHITE)
        screen.blit(S8textSurface, S8textRect)
        S9textSurface = S9font.render(("9:       " +(str(all_scoreslist2[8]))), True, WHITE)
        screen.blit(S9textSurface, S9textRect)
        S10textSurface = S10font.render(("10:      " +(str(all_scoreslist2[9]))), True, WHITE)
        screen.blit(S10textSurface, S10textRect)

        pygame.draw.rect(screen, CYAN, (20, 425 , 175, 60), 0)
        resettextSurface = resetfont.render("Reset", True, WHITE)
        screen.blit(resettextSurface, resettextRect)

        if Ttext == "on" and HTPtext == "off" and AdminBlocktext == "on":
            screen.blit(Block_Gui, (0, 0))
        
        if HTPtext == "on":
            screen.blit(How_to_Play, (0, 0))
            pygame.draw.rect(screen, BLACK, (540, 439, 120, 50), 5)

    else:
        screen.blit(Galaxy, (0, 0))

    # Coin Animation
    ## Shows the second digit of the variable resosnible for counting frames
    if Ptext == "off":
        if COIN_FRAME >= 11:
            COIN_FRAME -= 1
        else:
            COIN_FRAME = 89

        ## Setting a framerate for the coin animation
        stopper = 0
        for i in str(COIN_FRAME):
            stopper += 1
            if stopper == 1:
                first_digit = int(i)
    
    if Rem1_image == True and Rem1_coin == False and titleOn == False and ship_type == 4:
        if first_digit == 1 or first_digit == 5:
            screen.blit(Coin_F1, ((A1['rect'][0] - 58), (A1['rect'][1] - 100)))
        elif first_digit == 2 or first_digit == 6:
            screen.blit(Coin_F2, ((A1['rect'][0] - 58), (A1['rect'][1] - 100)))
        elif first_digit == 3 or first_digit == 7:
            screen.blit(Coin_F3, ((A1['rect'][0] - 58), (A1['rect'][1] - 100)))
        elif first_digit == 4 or first_digit == 8:
            screen.blit(Coin_F4, ((A1['rect'][0] - 58), (A1['rect'][1] - 100)))
            
    if Rem2_image == True and Rem2_coin == False and titleOn == False and ship_type == 4:
        if first_digit == 1 or first_digit == 5:
            screen.blit(Coin_F1, ((A2['rect'][0] - 58), (A2['rect'][1] - 100)))
        elif first_digit == 2 or first_digit == 6:
            screen.blit(Coin_F2, ((A2['rect'][0] - 58), (A2['rect'][1] - 100)))
        elif first_digit == 3 or first_digit == 7:
            screen.blit(Coin_F3, ((A2['rect'][0] - 58), (A2['rect'][1] - 100)))
        elif first_digit == 4 or first_digit == 8:
            screen.blit(Coin_F4, ((A2['rect'][0] - 58), (A2['rect'][1] - 100)))
            
    if Rem3_image == True and Rem3_coin == False and titleOn == False and ship_type == 4:
        if first_digit == 1 or first_digit == 5:
            screen.blit(Coin_F1, ((A3['rect'][0] - 58), (A3['rect'][1] - 100)))
        elif first_digit == 2 or first_digit == 6:
            screen.blit(Coin_F2, ((A3['rect'][0] - 58), (A3['rect'][1] - 100)))
        elif first_digit == 3 or first_digit == 7:
            screen.blit(Coin_F3, ((A3['rect'][0] - 58), (A3['rect'][1] - 100)))
        elif first_digit == 4 or first_digit == 8:
            screen.blit(Coin_F4, ((A3['rect'][0] - 58), (A3['rect'][1] - 100)))

    if Rem4_image == True and Rem4_coin == False and titleOn == False and ship_type == 4:
        if first_digit == 1 or first_digit == 5:
            screen.blit(Coin_F1, ((A4['rect'][0] - 58), (A4['rect'][1] - 100)))
        elif first_digit == 2 or first_digit == 6:
            screen.blit(Coin_F2, ((A4['rect'][0] - 58), (A4['rect'][1] - 100)))
        elif first_digit == 3 or first_digit == 7:
            screen.blit(Coin_F3, ((A4['rect'][0] - 58), (A4['rect'][1] - 100)))
        elif first_digit == 4 or first_digit == 8:
            screen.blit(Coin_F4, ((A4['rect'][0] - 58), (A4['rect'][1] - 100)))

    # While not on title screen:
    if titleOn == False:
        all_coming_decor.update()
        all_coming_decor.draw(screen)
        rect_beams.update() 
        rect_beams.draw(screen)
        rect_flames.update() 
        rect_flames.draw(screen)

    #Drawing ships
    if RemP_image == False and titleOn == False:
        if ship_type == 1:
            playerCar_list.draw(screen)
            if carryOn:
                playerCar_list.update()
        if ship_type == 2:
            screen.blit(Ship2, (playerCar.rect.x, playerCar.rect.y))
        if ship_type == 3:
            screen.blit(Ship3, (playerCar.rect.x, playerCar.rect.y))
        if ship_type == 4:
            screen.blit(ShipS, (playerCar.rect.x, playerCar.rect.y))
        NEWFLAMEx = playerCar.rect.x
        if carryOn == True:
            Newflaim = (rect_flames.add(Flame((NEWFLAMEx + 1 + random.randrange(-4,5)), (playerCar.rect.y + 10), BEAMSIZEx, BEAMSIZEy, 5)))
            for i in range(5):
                Newflaim = (rect_flames.add(LilFlame((NEWFLAMEx + 1 + random.randrange(-4,5)), (playerCar.rect.y + 15), BEAMSIZEx, BEAMSIZEy, 5)))
            #if SoundMute == "off":
                #Pew.play()

    # Drawing asteroids
    if Rem1_image == False and titleOn == False:
        car1_list.draw(screen)
        if carryOn:
            car1_list.update()
    if Rem2_image == False and titleOn == False:
        car2_list.draw(screen)
        if carryOn:
            car2_list.update()
    if Rem3_image == False and titleOn == False:
        car3_list.draw(screen)
        if carryOn:
            car3_list.update()
    if Rem4_image == False and titleOn == False:
        car4_list.draw(screen)
        if carryOn:
            car4_list.update()


    ## In- game bar
    if PU_type == 1:
        screen.blit(Time_Up, (Power_up_x - 5, Power_up_y - 5))
    elif PU_type == 2:
        screen.blit(Shield, (Power_up_x - 5, Power_up_y - 5))
    elif PU_type == 3:
        screen.blit(Rapid_Fire, (Power_up_x - 5, Power_up_y - 5))
    #If I ever want the MLG glasses to be a power up again, I can undo this
        
    #elif PU_type == 4:
        #screen.blit(MLG, (Power_up_x - 5, Power_up_y - 5))

        
    screen.blit(Solar_System, (0, 500))
    pygame.draw.rect(screen, WHITE, (0, 500, SCREENWIDTH, 100), 5)
    screen.blit(Pu_Gui, (0, 0))
    #pygame.draw.rect(screen, WHITE, (10, SCREENHEIGHT - 90, 70, 80), 5)
    if SHIELD > 0:
        pu_counttextSurface = pu_countfont.render(("x" +(str(int(SHIELD / 60)))), True, WHITE) #If power up is shield
    elif RF_FUEL > 0:
        pu_counttextSurface = pu_countfont.render(("x" +(str(int(RF_FUEL)))), True, WHITE) #If power up is rapid fire
    elif MLG_SHOTS > 0:
        pu_counttextSurface = pu_countfont.render(("x" +(str(int(MLG_SHOTS)))), True, WHITE) #If power up is MLG
    else:
        pu_counttextSurface = pu_countfont.render("x0", True, GREY) #If power up is shield
    screen.blit(pu_counttextSurface, pu_counttextRect)

    # Draqawing accessories
    if accesory_type == 1 and Ttext == "off":
        screen.blit(MLGlasses, (playerCar.rect.x - 25, playerCar.rect.y + 10))
    if accesory_type == 2 and Ttext == "off":
        screen.blit(Angry_Eyes, (playerCar.rect.x - 8, playerCar.rect.y + 10))
    
    if SHIELD >= 1 and titleOn == False:
        if SHIELD >= 1 and SHIELD <= 20 or SHIELD >= 31 and SHIELD <= 50 or SHIELD >= 61 and SHIELD <= 80 or SHIELD >= 91 and SHIELD <= 110 or SHIELD >= 121 and SHIELD <= 140 or SHIELD >= 160:
            screen.blit(Bubble, (playerCar.rect.x - 25, playerCar.rect.y - 20))
            screen.blit(Shield, (15, SCREENHEIGHT - 85))
    if RF_FUEL >= 1 and titleOn == False:
        if RF_FUEL >= 1 and RF_FUEL <= 20 or RF_FUEL >= 31 and RF_FUEL <= 50 or RF_FUEL >= 61 and RF_FUEL <= 80 or RF_FUEL >= 91 and RF_FUEL <= 110 or RF_FUEL >= 121 and RF_FUEL <= 140 or RF_FUEL >= 160:
            screen.blit(Rapid_Fire, (15, SCREENHEIGHT - 85))
            
    ### Health Bar:
    HB_Spacing = 0 
    if HEALTH >= 1:
        if HEALTH_GAIN <= -1: 
            HEALTH -= 1
            HEALTH_GAIN += 1
    for i in range(HEALTH):
        HB_Spacing -= 3
        screen.blit(Health, ((681 + HB_Spacing), 545))

    ### Fuel Bar:
    FB_Spacing = 0
    if FUEL >= 1:
        if FUEL_GAIN <= -1:
            FUEL -= 1
            FUEL_GAIN += 1
    for i in range(int(FUEL / 15)):
        FB_Spacing -= 1
        screen.blit(Fuel, ((681 + FB_Spacing), 518))

    #When paused:
    if Ptext == "on" and Ctext == "off":
        screen.blit(Pause_Gui, (0, 0))
        pygame.mixer.music.stop()

    #When Customizing ship:
    if Ctext == "on" and Ptext == "off":
        screen.blit(Customize_Gui, (0, 0))
        if ship_type == 1:
            screen.blit(Ship1, (310, 350))
            screen.blit(BigShip1, (110, 90))
            screen.blit(Ship_Desc_1, (0, 0))
        elif ship_type == 2:
            screen.blit(Ship2, (310, 350))
            screen.blit(BigShip2, (110, 90))
            screen.blit(Ship_Desc_2, (0, 0))
        elif ship_type == 3:
            screen.blit(Ship3, (310, 350))
            screen.blit(BigShip3, (110, 90))
            screen.blit(Ship_Desc_3, (0, 0))
        elif ship_type == 4:
            if int(all_scoreslist2[0]) >= 7500:
                screen.blit(ShipS, (310, 350))
                screen.blit(BigShipS, (110, 90))
                screen.blit(Ship_Desc_S, (0, 0))
            else:
                screen.blit(ShipS_L, (310, 350))
                screen.blit(BigShipS_L, (110, 90))
                screen.blit(Ship_Desc_SB, (0, 0))
                
        if accesory_type == 0:
            screen.blit(Customize_Na, (0, 0))
            screen.blit(Accesory_Desc_0, (0, 0))
        elif accesory_type == 1:
            screen.blit(MLGlasses, (285, 360))
            screen.blit(BigMLGlasses, (405, 120))
            screen.blit(Accesory_Desc_1, (0, 0))
        elif accesory_type == 2:
            screen.blit(Angry_Eyes, (302, 360))
            screen.blit(BigAngry_Eyes, (420, 120))
            screen.blit(Accesory_Desc_2, (0, 0))
        screen.blit(Customize_Arrows, (0, 0))
        screen.blit(Customize_Back, (0, 0))
    
    if HTPtext == "off" and Ttext == "off":
        screen.blit(timetextSurface, timetextRect)
        screen.blit(scoretextSurface, scoretextRect)

    if titleOn == True:
        pygame.draw.rect(screen, BLACK, (0, 500, SCREENWIDTH, 100), 0)
        screen.blit(Mixer_Gui, (0, 0))
        if MusicMute == "off":
            screen.blit(Music_Check, (0, 0))
        if SoundMute == "off":
            screen.blit(Sound_Check, (0, 0))


    # If game is not paused
    if carryOn:
        Ship_sensor = {'rect': pygame.Rect(playerCar.rect.x + 16, playerCar.rect.y + 5, 50, 73)}

        A1 = {'rect': pygame.Rect(car1.rect.x + 58, car1.rect.y + 100, 36, 33)}
        A2 = {'rect': pygame.Rect(car2.rect.x + 58, car2.rect.y + 100, 36, 33)}
        A3 = {'rect': pygame.Rect(car3.rect.x + 58, car3.rect.y + 100, 36, 33)} 
        A4 = {'rect': pygame.Rect(car4.rect.x + 58, car4.rect.y + 100, 36, 33)} 

        Power_up_y += 5
        Power_up = {'rect': pygame.Rect(Power_up_x, Power_up_y, 50, 60)}

        asteroids.clear()
        if Rem1_rect == False:
            asteroids.append(A1)
        if Rem2_rect == False:
            asteroids.append(A2) 
        if Rem3_rect == False:
            asteroids.append(A3)
        if Rem4_rect == False:
            asteroids.append(A4)

        # Beam collision
        for beam in beams[:]:
            if doRectsOverlap(A1['rect'], beam):
                beams.remove(beam)
                if A1['rect'][1] >= -50 and Rem1_rect == False and Rem1_image == False:
                    Rem1_rect = True
                    Rem1_image = True
                    if ship_type == 1:
                        SCORE += 100
                    elif ship_type == 2:
                        SCORE += 150
                    elif ship_type == 3 or ship_type == 4:
                        SCORE += 200
                    if SoundMute == "off":
                        if accesory_type == 1:
                            Hit_marker.play()
                        else:
                            if accesory_type == 2:
                                Crunch_D.play()
                            else:
                                Crunch.play()
                    A1_Hit_Time = 6
            elif doRectsOverlap(A2['rect'], beam):
                beams.remove(beam)
                if A2['rect'][1] >= -50 and Rem2_rect == False and Rem2_image == False:
                    Rem2_rect = True
                    Rem2_image = True
                    if ship_type == 1:
                        SCORE += 100
                    elif ship_type == 2:
                        SCORE += 150
                    elif ship_type == 3 or ship_type == 4:
                        SCORE += 200
                    if SoundMute == "off":
                        if accesory_type == 1:
                            Hit_marker.play()
                        else:
                            if accesory_type == 2:
                                Crunch_D.play()
                            else:
                                Crunch.play()
                    A2_Hit_Time = 6
            elif doRectsOverlap(A3['rect'], beam):
                beams.remove(beam)
                if A3['rect'][1] >= -50 and Rem3_rect == False and Rem3_image == False:
                    Rem3_rect = True
                    Rem3_image = True
                    if ship_type == 1:
                        SCORE += 100
                    elif ship_type == 2:
                        SCORE += 150
                    elif ship_type == 3 or ship_type == 4:
                        SCORE += 200
                    if SoundMute == "off":
                        if accesory_type == 1:
                            Hit_marker.play()
                        else:
                            if accesory_type == 2:
                                Crunch_D.play()
                            else:
                                Crunch.play()
                    A3_Hit_Time = 6
            elif doRectsOverlap(A4['rect'], beam):
                beams.remove(beam)
                if A4['rect'][1] >= -50 and Rem4_rect == False and Rem4_image == False:
                    Rem4_rect = True
                    Rem4_image = True
                    if ship_type == 1:
                        SCORE += 100
                    elif ship_type == 2:
                        SCORE += 150
                    elif ship_type == 3 or ship_type == 4:
                        SCORE += 200
                    if SoundMute == "off":
                        if accesory_type == 1:
                            Hit_marker.play()
                        else:
                            if accesory_type == 2:
                                Crunch_D.play()
                            else:
                                Crunch.play()
                    A4_Hit_Time = 6
        
        # Animations after an asteroid is hit
        if A1_Hit_Time >= 1:
            if accesory_type == 1:
                A1_Hit_Time -= 2
                screen.blit(Hitmarker, ((A1['rect'][0] - 6), (A1['rect'][1] - 4)))
            else:
                A1_Hit_Time -= .6
                if A1_Hit_Time > 4: 
                    screen.blit(Broken_Asteroid, ((A1['rect'][0] - 58), (A1['rect'][1] - 100)))
                elif A1_Hit_Time > 2: 
                    screen.blit(Broken_Asteroid_2, ((A1['rect'][0] - 58), (A1['rect'][1] - 100)))
                else:
                    screen.blit(Broken_Asteroid_3, ((A1['rect'][0] - 58), (A1['rect'][1] - 100)))
                
        if A2_Hit_Time >= 1:
            if accesory_type == 1:
                A2_Hit_Time -= 2
                screen.blit(Hitmarker, ((A2['rect'][0] - 6), (A2['rect'][1] - 4)))
            else:
                A2_Hit_Time -= .6
                if A2_Hit_Time > 4:
                    screen.blit(Broken_Asteroid, ((A2['rect'][0] - 58), (A2['rect'][1] - 100)))
                elif A2_Hit_Time > 2:
                    screen.blit(Broken_Asteroid_2, ((A2['rect'][0] - 58), (A2['rect'][1] - 100)))
                else:
                    screen.blit(Broken_Asteroid_3, ((A2['rect'][0] - 58), (A2['rect'][1] - 100)))

        if A3_Hit_Time >= 1:
            if accesory_type == 1:
                A3_Hit_Time -= 2
                screen.blit(Hitmarker, ((A3['rect'][0] - 6), (A3['rect'][1] - 4)))
            else:
                A3_Hit_Time -= .6
                if A3_Hit_Time > 4:
                    screen.blit(Broken_Asteroid, ((A3['rect'][0] - 58), (A3['rect'][1] - 100)))
                elif A3_Hit_Time > 2:
                    screen.blit(Broken_Asteroid_2, ((A3['rect'][0] - 58), (A3['rect'][1] - 100)))
                else:
                    screen.blit(Broken_Asteroid_3, ((A3['rect'][0] - 58), (A3['rect'][1] - 100)))

        if A4_Hit_Time >= 1:
            if accesory_type == 1:
                A4_Hit_Time -= 2
                screen.blit(Hitmarker, ((A4['rect'][0] - 6), (A4['rect'][1] - 4)))
            else:
                A4_Hit_Time -= .6
                if A4_Hit_Time > 4:
                    screen.blit(Broken_Asteroid, ((A4['rect'][0] - 58), (A4['rect'][1] - 100)))
                elif A4_Hit_Time > 2:
                    screen.blit(Broken_Asteroid_2, ((A4['rect'][0] - 58), (A4['rect'][1] - 100)))
                else:
                    screen.blit(Broken_Asteroid_3, ((A4['rect'][0] - 58), (A4['rect'][1] - 100)))

        # Asteroid collision
        if doRectsOverlap(A1["rect"], Ship_sensor["rect"]):
            if Rem1_rect == False and Rem1_image == False:
                if SHIELD <= 0:
                    if HEALTH >= 0:
                        HEALTH_GAIN -= 34
                    else:
                        HEALTH = 100
                        HEALTH_GAIN = 100
                if SHIELD > 0:
                    if SoundMute == "off":
                        Reflect.play()
                else:
                    if SoundMute == "off":
                        Ship_Hit.play()
            elif Rem1_image == True and Rem1_coin == False and ship_type == 4:
                SCORE += 200
                Rem1_coin = True
                if SoundMute == "off":
                    Coin.play()
            Rem1_rect = True
            Rem1_image = True
        if doRectsOverlap(A2["rect"], Ship_sensor["rect"]):
            if Rem2_rect == False and Rem2_image == False:
                if SHIELD <= 0:
                    if HEALTH >= 0:
                        HEALTH_GAIN -= 34
                    else:
                        HEALTH = 100
                        HEALTH_GAIN = 100
                if SHIELD > 0:
                    if SoundMute == "off":
                        Reflect.play()
                else:
                    if SoundMute == "off":
                        Ship_Hit.play()
            elif Rem2_image == True and Rem2_coin == False and ship_type == 4:
                SCORE += 200
                Rem2_coin = True
                if SoundMute == "off":
                    Coin.play()
            Rem2_rect = True
            Rem2_image = True
        if doRectsOverlap(A3["rect"], Ship_sensor["rect"]):
            if Rem3_rect == False and Rem3_image == False:
                if SHIELD <= 0:
                    if HEALTH >= 0:
                        HEALTH_GAIN -= 34
                    else:
                        HEALTH = 100
                        HEALTH_GAIN = 100
                if SHIELD > 0:
                    if SoundMute == "off":
                        Reflect.play()
                else:
                    if SoundMute == "off":
                        Ship_Hit.play()
            elif Rem3_image == True and Rem3_coin == False and ship_type == 4:
                SCORE += 200
                Rem3_coin = True
                if SoundMute == "off":
                    Coin.play()
            Rem3_rect = True
            Rem3_image = True
        if doRectsOverlap(A4["rect"], Ship_sensor["rect"]):
            if Rem4_rect == False and Rem4_image == False:
                if SHIELD <= 0:
                    if HEALTH >= 0:
                        HEALTH_GAIN -= 34
                    else:
                        HEALTH = 100
                        HEALTH_GAIN = 100
                if SHIELD > 0:
                    if SoundMute == "off":
                        Reflect.play()
                else:
                    if SoundMute == "off":
                        Ship_Hit.play()
            elif Rem4_image == True and Rem4_coin == False and ship_type == 4:
                SCORE += 200
                Rem4_coin = True
                if SoundMute == "off":
                    Coin.play()
            Rem4_rect = True
            Rem4_image = True
        if doRectsOverlap(Ship_sensor["rect"], Power_up["rect"]):
            if SoundMute == "off":
                Collect.play()
            if RemPU_rect == False:
                Power_up_x = random.randrange(5, 631)
                Power_up_y = -2000
                if PU_type == 1:
                    FUEL += 500
                elif PU_type == 2:
                    RF_FUEL = 0
                    MLG_SHOTS = 0
                    SHIELD = 600
                elif PU_type == 3:
                    SHIELD = 0
                    MLG_SHOTS = 0
                    RF_FUEL = 240
                elif PU_type == 4:
                    SHIELD = 0
                    RF_FUEL = 0
                    MLG_SHOTS = 6
                PU_type = random.randrange(1,4)
            RemPU_rect = False

        if HEALTH <= 0:
            Game_finish = True
            WIN = False
            HEALTH = 100
            Check_scores2()
            Title_screen()

        # Showing the hitboxes.
        for i in range(len(beams)):
            beams[i][1] -= 20
##            pygame.draw.rect(screen, RED, beams[i])
##            if beams[i][1] >= -60:
##                beams.remove(beam)
##
##        for h in range(len(asteroids)):
##             pygame.draw.rect(screen, WHITE, asteroids[h]['rect'])
##
##        pygame.draw.rect(screen, BLUE, Ship_sensor['rect'])
##
##        pygame.draw.rect(screen, GREEN, Power_up['rect'])

        SCORE += speed_points
        if FUEL <= 0:
            carryOn = False
            timeout = True
            Game_finish = True
            WIN = False
            Check_scores2()
            Title_screen()
        else:
            FUEL_GAIN = -10
            
        if SHIELD >= 1:
            SHIELD -= 1

        if RF_FUEL >= 1:
            RF_FUEL -= 1 
            beams.append(pygame.Rect(playerCar.rect.x + 40, playerCar.rect.y + 0, BEAMSIZEx, BEAMSIZEy))
            if accesory_type == 2:
                Newbiem = (rect_beams.add(Dist_Beam((playerCar.rect.x + 30), (playerCar.rect.y + 10), BEAMSIZEx, BEAMSIZEy, 20)))
                if SoundMute == "off":
                    Pew_D.play()
            elif ship_type >= 1 and ship_type <= 3:
                Newbiem = (rect_beams.add(Beam((playerCar.rect.x + 30), (playerCar.rect.y + 10), BEAMSIZEx, BEAMSIZEy, 20)))
                if SoundMute == "off":
                    Pew.play()
            elif ship_type == 4:
                Newbiem = (rect_beams.add(Gold_Beam((playerCar.rect.x + 30), (playerCar.rect.y + 10), BEAMSIZEx, BEAMSIZEy, 20)))
                if SoundMute == "off":
                    Pew.play()

        if B_BEAM_CHARGE >= 1:
            B_BEAM_CHARGE -= 1

        if M_BEAM_CHARGE >= 1:
            M_BEAM_CHARGE -= 1

        # Controls
        if key[pygame.K_a]:
            playerCar.moveLeft(8)
        if key[pygame.K_d]:
            playerCar.moveRight(8)
        if key[pygame.K_w] and traffic_speedy <= 2.5:
            traffic_speedy += 0.02
            speed_points += 0.01
        if key[pygame.K_s] and traffic_speedy >= -1.5:
            traffic_speedy -= 0.02
            speed_points -= 0.01

        # Game Logic
        for entity in all_coming_cars:
            entity.moveForward(traffic_speedy)

        for beam in rect_beams:
            if beam.rect.y <= -200:
                rect_beams.remove(beam)
            beam.moveForward(20)

        for flame in rect_flames:
            if flame.rect.y >= 410 + (traffic_speedy * 20):
                rect_flames.remove(flame)
            flame.moveBackward(1)

        if car1.rect.y > SCREENHEIGHT:
            car1.changeSpeed(random.randint(50, 100))
            car1.rect.y = -200
            if Rem1_image == False:
                SCORE -= 100
            Rem1_rect = False
            Rem1_image = False
            Rem1_coin = False
        if car2.rect.y > SCREENHEIGHT:
            car2.changeSpeed(random.randint(50, 100))
            car2.rect.y = -200
            if Rem2_image == False:
                SCORE -= 100
            Rem2_rect = False
            Rem2_image = False
            Rem2_coin = False
        if car3.rect.y > SCREENHEIGHT:
            car3.changeSpeed(random.randint(50, 100))
            car3.rect.y = -200
            if Rem3_image == False:
                SCORE -= 100
            Rem3_rect = False
            Rem3_image = False
            Rem3_coin = False
        if car4.rect.y > SCREENHEIGHT:
            car4.changeSpeed(random.randint(50, 100))
            car4.rect.y = -200
            if Rem4_image == False:
                SCORE -= 100
            Rem4_rect = False
            Rem4_image = False
            Rem4_coin = False
        if Power_up_y > SCREENHEIGHT:
            PU_type = random.randrange(1,4)
            Power_up_x = random.randrange(5, 631)
            Power_up_y = -1500
            RemPU_rect = False
 
        for star in all_coming_decor:
            star.moveForward(decor_speedy)
            if star.rect.y > SCREENHEIGHT - 200:
                star.rect.y = -1000

        ## Collision
        if playerCar.rect.x >= 549 and touchingwall == 0:
            touchingwall = 1
        elif playerCar.rect.x <= 0 and touchingwall == 0:
            touchingwall = 1
        elif playerCar.rect.x > 0 and playerCar.rect.x < 519:
            touchingwall = 0

        timetextSurface = timefont.render((str(int(FUEL / 60))), True, GREEN)
        shieldtextSurface = shieldfont.render(("Shield: " +(str(SHIELD))), True, WHITE)
        scoretextSurface = scorefont.render(("Score: " +(str(int(SCORE)))), True, WHITE)
        livestextSurface = livesfont.render(("Lives: " +(str(HEALTH))), True, BLACK)
    
    # Refresh Screen
    pygame.display.flip()

    # FPS
    clock.tick(60)

pygame.quit()
