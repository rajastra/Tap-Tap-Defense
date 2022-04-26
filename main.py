import pygame
from pygame import mixer
import time
import os
import random
import math

#initialize the pygame
pygame.init()

#create screen
width = 700
height = 300
screen = pygame.display.set_mode((width, height))
bgImage = pygame.image.load(os.path.join("game_assets", "background.jpg"))
rescaledBackground = pygame.transform.scale(bgImage, (width, height))

#cursor edit
crosshair = pygame.image.load(os.path.join("game_assets", "crosshair.png")).convert_alpha()
pygame.mouse.set_visible(False)

#bg music
mixer.music.load(os.path.join("game_assets", "grasswalk.mp3"))
mixer.music.play(-1)

#glock music
start = mixer.Sound(os.path.join("game_assets", "glock_start.mp3"))
reload = mixer.Sound(os.path.join("game_assets", "glock_reload.mp3"))
shoot = mixer.Sound(os.path.join("game_assets", "glock_shoot.mp3"))

#our data
damage = 0
score_value = 0

font = pygame.font.Font("freesansbold.ttf", 32)
textx = 10
texty = 10

#normal bombo
nbomboImage = pygame.image.load(os.path.join("game_assets", "Normal Bombo.png"))
nbomboSpd = 0.03

#giant bombo
gbomboImage = pygame.image.load(os.path.join("game_assets", "Giant Bombo.png"))
gbomboSpd = 0.015

#explode
explodeImage = pygame.image.load(os.path.join("game_assets", "explosion.png"))
explodeImage = pygame.transform.scale(explodeImage, (80, 80))
explodeSound = mixer.Sound(os.path.join("game_assets", "explosion.mp3"))

#enemy data
spawn_rate = 1000
add_mob = 0
mob_pos = [15, 75, 135, 195, 255]

mob_counter = 0
mob = []
mobImg = [nbomboImage, gbomboImage, explodeImage]
mobSpd = [nbomboSpd, gbomboSpd, 0]

#skill1
s1Sound = mixer.Sound(os.path.join("game_assets", "skill1.mp3"))

#game over
gvSound = mixer.Sound(os.path.join("game_assets", "gameover.mp3"))

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def show_defense(x, y):
    lives = font.render("Lives : " + str(10 - damage), True, (255, 255, 255))
    screen.blit(lives, (x, y + 32))

def nbombo(x, y, i):
    screen.blit(i, (x, y))

def isCollision(mobx, moby, curx, cury):
    distance = math.sqrt((math.pow(mobx - curx, 2)) + (math.pow(moby - cury, 2)))
    if distance < 15:
        return True
    else:
        return False

def generate():
    x = random.randint(0, 1)
    temp_mob = [mobImg[x], mobSpd[x], 700, random.choice(mob_pos), False, 0]
    return temp_mob

def remove(list, i):
    list.remove(i)
    return list

#title and icon
pygame.display.set_caption("Tap Tap Defense | MC-KRIW")
icon = pygame.image.load(os.path.join("game_assets", "icon.png"))
pygame.display.set_icon(icon)

#game loop
run = True
start.play()
while run:
    screen.blit(rescaledBackground, (0, 0))  # draw bg
    curx, cury = pygame.mouse.get_pos()
    screen.blit(crosshair, (curx, cury))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        #controls
        if event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_r]:
                reload.play()
        if event.type == pygame.MOUSEBUTTONDOWN:
            key = pygame.mouse.get_pressed()
            if key[0]:
                if start.play():
                    start.stop()
                if reload.play():
                    reload.stop()
                shoot.play()
                #collision
                for i in mob:
                    collision = isCollision(i[2], i[3], curx, cury)
                    if collision:
                        explodeSound.play()
                        score_value += 1
                        i[0] = mobImg[2]
                        i[1] = mobSpd[2]
                        i[4] = True
            if key[2]:
                s1Sound.play()
                for i in mob:
                    if i[0] == mobImg[0]:
                        i[2] += 100
                    elif i[0] == mobImg[1]:
                        i[2] += i[1] + 2

    mob_counter += 1
    if mob_counter == spawn_rate:
        mob_counter = 0
        temp_mob = generate()
        mob.append(temp_mob)

    for j in mob:
        if j[4]:
            j[5] += 1
        if j[5] == 500:
            mob = remove(mob, j)
        if j[2] <= 280 and j[4] == False:
            explodeSound.play()
            damage += 1
            j[0] = mobImg[2]
            j[1] = 0
            j[4] = True
        j[2] -= j[1]
        nbombo(j[2], j[3], j[0])

    if damage == 10:
        mixer.music.stop()
        explodeSound.stop()
        gvSound.play()
        time.sleep(3)
        break

    show_score(textx, texty)
    show_defense(textx, texty)
    pygame.display.update()