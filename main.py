import pygame
from pygame import mixer
import time, os, random, math
from abc import ABC, abstractmethod

# initialize the pygame
pygame.init()

# settings
FPS = 60
fpsClock = pygame.time.Clock()

width = 700
height = 300
screen = pygame.display.set_mode((width, height))
bgImage = pygame.image.load(os.path.join("game_assets", "background.jpg"))
rescaledBackground = pygame.transform.scale(bgImage, (width, height))

pygame.display.set_caption("Tap Tap Defense | MC-KRIW")
icon = pygame.image.load(os.path.join("game_assets", "icon.png"))
pygame.display.set_icon(icon)

mixer.music.load(os.path.join("game_assets", "music.ogg"))
gvSound = mixer.Sound(os.path.join("game_assets", "gameover.mp3"))

font_size = 20
font = pygame.font.Font("freesansbold.ttf", font_size)
white = (255, 255, 255)
black = (0, 0, 0)


class Player():
    textX = 10
    textY = 10
    base = 200

    def __init__(self):
        self.score = 0
        self.damage = 0
        self.mana = 0

    def get_kill(self):
        self.score += 1
        if self.mana != 300:
            self.mana += 10

    def take_damage(self):
        self.damage += 1

    def game_over(self):
        mixer.music.stop()
        gvSound.play()
        end_menu.set_game_active(False)

    def use_skill(self, cost):
        self.mana -= cost

    def update(self):
        self.x, self.y = pygame.mouse.get_pos()
        crosshair = pygame.image.load(os.path.join("game_assets", "crosshair.png")).convert_alpha()
        score = font.render("Score : " + str(self.score), True, white)
        lives = font.render("Lives : " + str(5 - self.damage), True, white)
        mana = font.render("Mana : " + str(self.mana) + "/300", True, white)
        screen.blit(crosshair, (self.x, self.y))
        screen.blit(score, (Player.textX, Player.textY))
        screen.blit(lives, (Player.textX, Player.textY + 35))
        screen.blit(mana, (Player.textX, Player.textY + 260))

class BomboSapiens(ABC):
    spawn_rate = 90
    add_mob = 0
    mob_pos = [5, 65, 125, 185, 245]
    explodeImage = []
    for i in range(9):
        tempImage = pygame.image.load(os.path.join("game_assets", "explosion0" + str(i) + ".png"))
        tempImage = pygame.transform.scale(tempImage, (80, 80))
        explodeImage.append(tempImage)
    explodeSound = mixer.Sound(os.path.join("game_assets", "explosion.mp3"))
    explodeDuration = 8
    spot = pygame.image.load(os.path.join("game_assets", "spot.png"))

    def __init__(self, name, hp, spd, image):
        self.name = name
        self.animation = 0
        self.walk = image
        self.hp = hp
        self.__spd = spd
        self.move = self.__spd
        self.ISexplode = False
        self.ISstun = False
        self.time = 0
        self.x = 700
        self.y = random.choice(BomboSapiens.mob_pos)

    @abstractmethod
    def maju(self):
        if self.animation < len(self.walk) - 1:
            self.animation += 1
        else:
            self.animation = 0
        self.image = self.walk[self.animation]
        self.x -= self.move

    @abstractmethod
    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp <= 0:
            self.explode()
            Player.get_kill(player)

    @abstractmethod
    def explode(self):
        self.move = 0
        self.time = 0
        BomboSapiens.explodeSound.play()
        self.ISexplode = True

    @abstractmethod
    def stun(self, time):
        self.time = 0
        self.move = 0
        self.stun_duration = time
        self.ISstun = True

    @abstractmethod
    def update(self):
        if not self.ISexplode:
            self.maju()
        if self.x < Player.base and not self.ISexplode:
            self.explode()
            Player.take_damage(player)
        if self.ISexplode:
            self.time += 1
            self.image = BomboSapiens.explodeImage[self.time]
            if self.time == BomboSapiens.explodeDuration:
                remove(mob, i)
                self.time = 0
        if self.ISstun and not self.ISexplode:
            self.time += 1
            if self.time == self.stun_duration:
                self.ISstun = False
                self.move = self.__spd
                self.time = 0
        screen.blit(self.image, (self.x, self.y))
        screen.blit(BomboSapiens.spot, (self.x, self.y))


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

    def take_damage(self, dmg):
        super().take_damage(dmg)

    def explode(self):
        super().explode()

    def stun(self, time):
        super().stun(time)

    def update(self):
        super().update()


class GiantBombo(BomboSapiens):
    angryimage = []
    for i in range(4, 8):
        tempimage = pygame.image.load(os.path.join("game_assets", "giant" + str(i) + ".png"))
        tempimage = pygame.transform.scale(tempimage, (80, 80))
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

    def take_damage(self, dmg):
        self.angry_sound.play()
        self.walk = GiantBombo.angryimage
        self.move += 1
        super().take_damage(dmg)

    def explode(self):
        self.angry_sound.stop()
        super().explode()

    def stun(self, time):
        super().stun(time)

    def update(self):
        super().update()


class Senjata(ABC):
    def __init__(self, name, mag, dmg, time, start, reload, shoot):
        self.name = name
        self.mag = mag
        self.ammo = self.mag
        self.dmg = dmg
        self.reload_time = time
        self.time = 0
        self.ISshoot = True
        self.ISreload = False
        self.Sstart = start
        self.Sreload = reload
        self.Sshoot = shoot

    @abstractmethod
    def start(self):
        self.Sstart.play()

    @abstractmethod
    def shoot(self):
        if self.ISshoot:
            self.ammo -= 1
            self.Sshoot.play()

    @abstractmethod
    def reload(self):
        if not self.ISreload:
            self.Sreload.play()
            self.ISreload = True
            self.ISshoot = False

    @abstractmethod
    def update(self):
        ammo = font.render("Ammo : " + str(self.ammo) + "/" + str(self.mag), True, white)
        screen.blit(ammo, (Player.textX, Player.textY + 225))
        if self.ammo == 0 and not self.ISreload:
            self.reload()
        if self.ISreload:
            self.time += 1
        if self.time == self.reload_time:
            self.ammo = self.mag
            self.ISshoot = True
            self.ISreload = False
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

    def update(self):
        super().update()


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
        if not self.ISreload:
            self.time += (30 * self.boost)
            self.Sreload[self.boost].play()
            self.boost = 0
            self.ISreload = True
            self.ISshoot = False

    def update(self):
        super().update()


class Skill1:
    def __init__(self):
        self.cost = 100
        self.knockback = 100
        self.effect = 15
        self.sound = mixer.Sound(os.path.join("game_assets", "skill1.mp3"))

    def active(self, list, mana):
        if mana >= self.cost:
            Player.use_skill(player, self.cost)
            self.sound.play()
            for i in list:
                if i.name == "NB":
                    i.x += self.knockback
                elif i.name == 'GB':
                    i.stun(self.effect)


class Skill2:
    def __init__(self):
        self.cost = 150
        self.dmg = 5
        self.effect = 30
        self.sound = mixer.Sound(os.path.join("game_assets", "electric_zap_001-6374.mp3"))

    def active(self, list, mana):
        if mana >= self.cost:
            player.use_skill(self.cost)
            self.sound.play()
            for i in list:
                i.take_damage(self.dmg)
                i.stun(self.effect)


class Skill3:
    def __init__(self):
        self.cost = 300
        self.sound = mixer.Sound(os.path.join("game_assets", "skill_chant.ogg"))

    def active(self, list, mana):
        if mana >= self.cost:
            player.use_skill(self.cost)
            self.sound.play()
            for i in list:
                Player.get_kill(player)
            list.clear()


class StartMenu:
    def __init__(self):
        self.animation = 0
        self.__game_active = False
        self.img = []
        self.rect = []
        for i in range (4):
            tempimage = pygame.image.load(os.path.join("game_assets", "giant" + str(i) + ".png"))
            tempimage = pygame.transform.scale(tempimage, (150, 150))
            tempimage_rect = tempimage.get_rect(center=(350, 100))
            self.img.append(tempimage)
            self.rect.append(tempimage_rect)
        self.text = font.render('Press any key to start', False, (111, 196, 169))
        self.text_rect = self.text.get_rect(center=(350, 150))
        self.weapon_select = font.render("Glock", True, white)
        self.weapon_select_rect = self.weapon_select.get_rect(center=(350, 200))
        self.skill_select = font.render("Skill1", True, white)
        self.skill_select_rect = self.skill_select.get_rect(center=(350, 250))

    def draw(self):
        if self.animation < 3:
            self.animation += 1
        else:
            self.animation = 0
        screen.fill((94, 129, 162))
        screen.blit(self.img[self.animation], self.rect[self.animation])
        screen.blit(self.text, self.text_rect)
        pygame.draw.rect(screen, black, [305, 180, 90, 40])
        pygame.draw.rect(screen, black, [305, 230, 90, 40])
        screen.blit(self.weapon_select, self.weapon_select_rect)
        screen.blit(self.skill_select, self.skill_select_rect)


    def set_game_active(self, value):
        self.__game_active = value
        mixer.music.play(-1)
        weapon.start()
        mixer.music.set_volume(0.25)

    def get_game_active(self):
        return self.__game_active

class EndMenu:
    def __init__(self):
        self.animation = 0
        self.__game_active = True
        self.img = []
        self.rect = []
        for i in range (4):
            tempimage = pygame.image.load(os.path.join("game_assets", "giant" + str(i) + ".png"))
            tempimage = pygame.transform.scale(tempimage, (150, 150))
            tempimage = pygame.transform.rotate(tempimage, -180)
            tempimage_rect = tempimage.get_rect(center=(350, 100))
            self.img.append(tempimage)
            self.rect.append(tempimage_rect)
        self.text = font.render('GAME OVER', False, "white")
        self.text2 = font.render('Press CAPSLOCK for Back to GAME', False, "white")
        self.text3 = font.render('Press ESCAPE for EXIT', False, "white")
        self.text_rect = self.text.get_rect(center=(350, 150))
        self.text2_rect = self.text2.get_rect(center=(350, 200))
        self.text3_rect = self.text3.get_rect(center=(350, 230))

    def draw(self):
        if self.animation < 3:
            self.animation += 1
        else:
            self.animation = 0
        screen.blit(self.img[self.animation], self.rect[self.animation])
        screen.blit(self.text, self.text_rect)
        screen.blit(self.text2, self.text2_rect)
        screen.blit(self.text3, self.text3_rect)

    def set_game_active(self, value):
        self.__game_active = value

    def get_game_active(self):
        return self.__game_active



def IScollision(mobx, moby, curx, cury, shoot):
    distance = math.sqrt((math.pow(mobx - curx, 2)) + (math.pow(moby - cury, 2)))
    if distance < 15 and shoot:
        return True
    else:
        return False


def remove(list, i):
    list.remove(i)
    return list


# initiation
start_menu = StartMenu()
end_menu = EndMenu()
player = Player()
game = False
mixer.music.play(-1)
weapon = 0
skill = 0
mob = []
# game loop
run = True
while run:
    # control
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if game == True:
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_r]:
                    weapon.reload()
                if pygame.key.get_pressed()[pygame.K_p]:
                    if not fast:
                        fast = True
                        FPS = 480
                    elif fast:
                        fast = False
                        FPS = 60
                if pygame.key.get_pressed()[pygame.K_o]:
                    player.mana += (300 - player.mana)
            if event.type == pygame.MOUSEBUTTONDOWN:
                key = pygame.mouse.get_pressed()
                if key[0]:
                    weapon.shoot()
                    for i in mob:
                        if IScollision(i.x, i.y, player.x, player.y, weapon.ISshoot):
                            i.take_damage(weapon.dmg)
                            if weapon.name == 'R' and weapon.boost <= 5:
                                weapon.boost += 1
                if key[2]:
                    skill.active(mob, player.mana)
        else:
            fast = False
            FPS = 60
            if event.type == pygame.MOUSEBUTTONDOWN:
                key = pygame.mouse.get_pressed()
                mouse = pygame.mouse.get_pos()
                if key[0]:
                    if 305 <= mouse[0] <= 395:
                        if 180 <= mouse[1] <= 220:
                            if weapon == 0:
                                start_menu.weapon_select = font.render("Revolver", True, white)
                                start_menu.weapon_select_rect = start_menu.weapon_select.get_rect(center=(350, 200))
                                weapon = 1
                            elif weapon == 1:
                                start_menu.weapon_select = font.render("Glock", True, white)
                                start_menu.weapon_select_rect = start_menu.weapon_select.get_rect(center=(350, 200))
                                weapon = 0
                        elif 230 <= mouse[1] <= 270:
                            if skill == 2:
                                start_menu.skill_select = font.render("Skill1", True, white)
                                start_menu.skill_select_rect = start_menu.skill_select.get_rect(center=(350, 250))
                                skill = 0
                            elif skill == 0:
                                start_menu.skill_select = font.render("Skill2", True, white)
                                start_menu.skill_select_rect = start_menu.skill_select.get_rect(center=(350, 250))
                                skill = 1
                            elif skill == 1:
                                start_menu.skill_select = font.render("Skill3", True, white)
                                start_menu.skill_select_rect = start_menu.skill_select.get_rect(center=(350, 250))
                                skill = 2
            if event.type == pygame.KEYDOWN:
                game = True
                if weapon == 0:
                    weapon = Glock()
                elif weapon == 1:
                    weapon = Revolver()
                if skill == 0:
                    skill = Skill1()
                elif skill == 1:
                    skill = Skill2()
                elif skill == 2:
                    skill = Skill3()
                pygame.mouse.set_visible(False)
                start_menu.set_game_active(True)
                end_menu.set_game_active(True)
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_CAPSLOCK]:
                    game = True
                    start_menu.set_game_active(True)
                if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    run = False

    # gameplay
    if game == True:
        screen.blit(rescaledBackground, (0, 0))
        weapon.update()
        for i in mob:
            i.update()

        if player.damage  == 5:
            game = False
            player.game_over()
        player.update()
        BomboSapiens.add_mob += 1
        if BomboSapiens.add_mob == BomboSapiens.spawn_rate:
            x = random.randint(0, 1)
            if x == 0:
                mob.append(NormalBombo())
            elif x == 1:
                mob.append(GiantBombo())
            BomboSapiens.add_mob = 0 

    if(not start_menu.get_game_active()):
        start_menu.draw()
    if(not end_menu.get_game_active()):
        player.damage = 0
        player.score = 0
        player.mana = 0
        weapon.ammo = weapon.mag
        mob.clear()
        end_menu.draw()

    pygame.display.update()
    fpsClock.tick(FPS)