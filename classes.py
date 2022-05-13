import pygame
from pygame import mixer
import os, random
from abc import ABC, abstractmethod
from settings import *


class StartMenu:
    def __init__(self, font):
        self.animation = 0
        self.__game_active = False
        self.img = []
        self.rect = []
        for i in range(4):
            tempimage = pygame.image.load(os.path.join("game_assets", "giant" + str(i) + ".png"))
            tempimage = pygame.transform.scale(tempimage, (150, 150))
            tempimage_rect = tempimage.get_rect(center=(350, 100))
            self.img.append(tempimage)
            self.rect.append(tempimage_rect)
        self.text = font.render('Press any key to start', False, darker_cyan)
        self.text_rect = self.text.get_rect(center=(350, 150))
        self.weapon_select = font.render("Glock", True, white)
        self.weapon_select_rect = self.weapon_select.get_rect(center=(350, 200))
        self.skill_select = font.render("Skill1", True, white)
        self.skill_select_rect = self.skill_select.get_rect(center=(350, 250))

    def draw(self, screen):
        if self.animation < 3:
            self.animation += 1
        else:
            self.animation = 0
        screen.fill(cyan)
        screen.blit(self.img[self.animation], self.rect[self.animation])
        screen.blit(self.text, self.text_rect)
        pygame.draw.rect(screen, black, [305, 180, 90, 40])
        pygame.draw.rect(screen, black, [305, 230, 90, 40])
        screen.blit(self.weapon_select, self.weapon_select_rect)
        screen.blit(self.skill_select, self.skill_select_rect)

class EndMenu:
    def __init__(self, font):
        self.animation = 0
        self.img = []
        self.rect = []
        for i in range (4):
            tempimage = pygame.image.load(os.path.join("game_assets", "giant" + str(i + 4) + ".png"))
            tempimage = pygame.transform.scale(tempimage, (150, 150))
            tempimage_rect = tempimage.get_rect(center=(350, 100))
            self.img.append(tempimage)
            self.rect.append(tempimage_rect)
        self.text = font.render('GAME OVER', False, darker_cyan)
        self.text2 = font.render('Press CAPSLOCK to replay the game', False, white)
        self.text3 = font.render('Press ESC to exit', False, white)
        self.text_rect = self.text.get_rect(center=(350, 150))
        self.text2_rect = self.text2.get_rect(center=(350, 200))
        self.text3_rect = self.text3.get_rect(center=(350, 230))

    def draw(self, screen):
        if self.animation < 3:
            self.animation += 1
        else:
            self.animation = 0
        screen.fill(cyan)
        screen.blit(self.img[self.animation], self.rect[self.animation])
        screen.blit(self.text, self.text_rect)
        screen.blit(self.text2, self.text2_rect)
        screen.blit(self.text3, self.text3_rect)

class Player():
    def __init__(self):
        self.score = 0
        self.damage = 0
        self.mana = 0
        self.crosshair = pygame.image.load(os.path.join("game_assets", "crosshair.png")).convert_alpha()
        self.img = []
        for i in range(4):
            tempImage = pygame.image.load(os.path.join("game_assets", "castle_" + str(i) + ".png"))
            tempImage = pygame.transform.scale(tempImage, (250, 250))
            self.img.append(tempImage)

    def get_kill(self):
        self.score += 1
        if self.mana != 300:
            self.mana += 10

    def take_damage(self):
        self.damage += 1

    def use_skill(self, cost):
        self.mana -= cost

    def update(self, screen, font):
        self.x, self.y = pygame.mouse.get_pos()
        score = font.render("Score : " + str(self.score), True, white)
        mana = font.render("Mana : " + str(self.mana) + "/300", True, white)
        screen.blit(self.img[self.damage], (0, 25))
        screen.blit(self.crosshair, (self.x, self.y))
        screen.blit(score, (textX, textY))
        screen.blit(mana, (textX, textY + 260))

class BomboSapiens(ABC):
    def __init__(self, name, hp, spd, image):
        self.name = name
        self.animation = 0
        self.walk = image
        self.hp = hp
        self.__spd = spd
        self.move = self.__spd
        self.explodeImage = []
        for i in range(9):
            tempImage = pygame.image.load(os.path.join("game_assets", "explosion0" + str(i) + ".png"))
            tempImage = pygame.transform.scale(tempImage, (80, 80))
            self.explodeImage.append(tempImage)
        self.explode_sound = mixer.Sound(os.path.join("game_assets", "explosion.mp3"))
        self.explode_duration = 8
        self.spot = pygame.image.load(os.path.join("game_assets", "spot.png"))
        self.isexplode = False
        self.isstun = False
        self.time = 0
        self.x = 700
        self.y = random.choice(mob_position)

    @abstractmethod
    def maju(self):
        if self.animation < len(self.walk) - 1:
            self.animation += 1
        else:
            self.animation = 0
        self.image = self.walk[self.animation]
        self.x -= self.move

    @abstractmethod
    def take_damage(self, player, dmg):
        self.hp -= dmg
        if self.hp <= 0:
            self.explode()
            player.get_kill()

    @abstractmethod
    def explode(self):
        self.move = 0
        self.time = 0
        self.explode_sound.play()
        self.isexplode = True

    @abstractmethod
    def stun(self, time):
        self.time = 0
        self.move = 0
        self.stun_duration = time
        self.isstun = True

    @abstractmethod
    def remove(self, list, i):
        list.remove(i)
        return list

    @abstractmethod
    def update(self, screen, player, list, i):
        if not self.isexplode:
            self.maju()
        if self.x < base and not self.isexplode:
            self.explode()
            player.take_damage()
        if self.isexplode:
            self.time += 1
            self.image = self.explodeImage[self.time]
            if self.time == self.explode_duration:
                self.remove(list, i)
                self.time = 0
        if self.isstun and not self.isexplode:
            self.time += 1
            if self.time == self.stun_duration:
                self.isstun = False
                self.move = self.__spd
                self.time = 0
        screen.blit(self.image, (self.x, self.y))
        screen.blit(self.spot, (self.x, self.y))

class NormalBombo(BomboSapiens):
    def __init__(self):
        name = "NB"
        image = []
        for i in range(11):
            tempimage = pygame.image.load(os.path.join("game_assets", "bombo" + str(i + 1) + ".png"))
            tempimage = pygame.transform.scale(tempimage, (50, 50))
            image.append(tempimage)
        hp = 10
        spd = 1
        super().__init__(name, hp, spd, image)

    def maju(self):
        super().maju()

    def take_damage(self, player, dmg):
        super().take_damage(player, dmg)

    def explode(self):
        super().explode()

    def stun(self, time):
        super().stun(time)

    def remove(self, list, i):
        super().remove(list, i)

    def update(self, screen, player, list, i):
        super().update(screen, player, list, i)

class GiantBombo(BomboSapiens):
    angryimage = []
    for i in range(4, 8):
        tempimage = pygame.image.load(os.path.join("game_assets", "giant" + str(i) + ".png"))
        tempimage = pygame.transform.scale(tempimage, (50, 50))
        angryimage.append(tempimage)

    def __init__(self):
        name = "GB"
        image = []
        for i in range(4):
            tempimage = pygame.image.load(os.path.join("game_assets", "giant" + str(i) + ".png"))
            tempimage = pygame.transform.scale(tempimage, (80, 80))
            image.append(tempimage)
        self.angry_sound = mixer.Sound(os.path.join("game_assets", "Giant Bombo Angry.mp3"))
        hp = 30
        spd = 0.5
        super().__init__(name, hp, spd, image)

    def maju(self):
        super().maju()

    def take_damage(self, player, dmg):
        self.angry_sound.play()
        self.walk = GiantBombo.angryimage
        self.move += 1
        super().take_damage(player, dmg)

    def explode(self):
        self.angry_sound.stop()
        super().explode()

    def stun(self, time):
        super().stun(time)

    def remove(self, list, i):
        super().remove(list, i)

    def update(self, screen, player, list, i):
        super().update(screen, player, list, i)

class Senjata(ABC):
    def __init__(self, name, mag, dmg, time, start, reload, shoot):
        self.name = name
        self.mag = mag
        self.ammo = self.mag
        self.dmg = dmg
        self.reload_time = time
        self.time = 0
        self.isshoot = True
        self.isreload = False
        self.start_sound = start
        self.reload_sound = reload
        self.shoot_sound = shoot

    @abstractmethod
    def start(self):
        self.start_sound.play()

    @abstractmethod
    def shoot(self):
        if self.isshoot:
            self.ammo -= 1
            self.shoot_sound.play()

    @abstractmethod
    def reload(self):
        if not self.isreload:
            self.reload_sound.play()
            self.isreload = True
            self.isshoot = False

    @abstractmethod
    def update(self, screen, font):
        ammo = font.render("Ammo : " + str(self.ammo) + "/" + str(self.mag), True, white)
        screen.blit(ammo, (textX, textY + 225))
        if self.ammo == 0 and not self.isreload:
            self.reload()
        if self.isreload:
            self.time += 1
        if self.time == self.reload_time:
            self.ammo = self.mag
            self.isshoot = True
            self.isreload = False
            self.time = 0

class Glock(Senjata):
    def __init__(self):
        name = 'G'
        mag = 15
        dmg = 10
        time = 90
        start = mixer.Sound(os.path.join("game_assets", "glock_start.mp3"))
        reload = mixer.Sound(os.path.join("game_assets", "glock_reload.mp3"))
        shoot = mixer.Sound(os.path.join("game_assets", "glock_shoot.mp3"))
        super().__init__(name, mag, dmg, time, start, reload, shoot)

    def start(self):
        super().start()

    def shoot(self):
        super().shoot()

    def reload(self):
        super().reload()

    def update(self, screen, font):
        super().update(screen, font)

class Revolver(Senjata):
    def __init__(self):
        name = 'R'
        mag = 6
        dmg = 30
        time = 300
        start = mixer.Sound(os.path.join("game_assets", "revolver_start.mp3"))
        reload = []
        for i in range(7):
            temp = mixer.Sound(os.path.join("game_assets", "revolver_reload" + str(i) + ".mp3"))
            reload.append(temp)
        shoot = mixer.Sound(os.path.join("game_assets", "revolver_shoot.mp3"))
        super().__init__(name, mag, dmg, time, start, reload, shoot)
        self.boost = 0

    def start(self):
        super().start()

    def shoot(self):
        super().shoot()

    def reload(self):
        if not self.isreload:
            self.time += (30 * self.boost)
            self.reload_sound[self.boost].play()
            self.boost = 0
            self.isreload = True
            self.isshoot = False

    def update(self, screen, font):
        super().update(screen, font)

class Skill1:
    def __init__(self):
        self.cost = 100
        self.knockback = 100
        self.effect = 15
        self.sound = mixer.Sound(os.path.join("game_assets", "skill1.mp3"))

    def active(self, player, list, mana):
        if mana >= self.cost:
            player.use_skill(self.cost)
            self.sound.play()
            for i in list:
                if i.name == "NB":
                    i.x += self.knockback
                elif i.name == 'GB':
                    i.stun(self.effect)

    def update(self, screen):
        pass

class Skill2:
    def __init__(self):
        self.isactive = False
        self.animate = 0
        self.location = []
        self.cost = 150
        self.dmg = 5
        self.effect = 30
        self.sound = mixer.Sound(os.path.join("game_assets", "electric_zap_001-6374.mp3"))
        self.image = []
        for i in range(27):
            tempimage = pygame.image.load(os.path.join("game_assets", "skill-2 (" + str(i + 1) + ").png"))
            tempimage = pygame.transform.scale(tempimage, (80, 80))
            self.image.append(tempimage)

    def active(self, player, list, mana):
        if mana >= self.cost:
            self.isactive = True
            player.use_skill(self.cost)
            self.sound.play()
            for i in list:
                self.location.append([i.x, i.y])
                i.take_damage(player, self.dmg)
                i.stun(self.effect)

    def update(self, screen):
        if self.isactive:
            for i in self.location:
                screen.blit(self.image[self.animate], (i[0], i[1]))
            self.animate += 1
        if self.animate == len(self.image):
            self.animate = 0
            self.location = []
            self.isactive = False

class Skill3:
    def __init__(self):
        self.isactive = False
        self.animate = 0
        self.location = []
        self.cost = 300
        self.sound = mixer.Sound(os.path.join("game_assets", "skill_chant.ogg"))
        self.image = []
        for i in range (7):
            tempimage = pygame.image.load(os.path.join("game_assets", "skill3" + str(i) + ".png"))
            tempimage = pygame.transform.scale(tempimage, (80, 80))
            self.image.append(tempimage)

    def active(self, player, list, mana):
        if mana >= self.cost:
            self.isactive = True
            player.use_skill(self.cost)
            self.sound.play()
            for i in list:
                self.location.append([i.x, i.y])
                player.get_kill()
            list.clear()

    def update(self, screen):
        if self.isactive:
            for i in self.location:
                screen.blit(self.image[self.animate], (i[0], i[1]))
            self.animate += 1
        if self.animate == len(self.image):
            self.animate = 0
            self.location = []
            self.isactive = False
