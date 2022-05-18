import pygame
from pygame import mixer
import os, math, time
from settings import *
from classes import *

pygame.init()
pygame.mixer.init()

class Game:
    def __init__(self):
        #loop setup
        self.running = True
        self.section = 0

        #screen setup
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        pygame.display.set_icon(pygame.image.load(os.path.join("game_assets", "icon.png")))

        #FPS
        self.FPS = FPS
        self.clock = pygame.time.Clock()

        #background music
        mixer.music.load(os.path.join("game_assets", "music.ogg"))

        #font
        self.font = pygame.font.Font(font_name, font_size)

        #gameplay setup
        self.background_image = pygame.image.load(os.path.join("game_assets", "background.png"))
        self.rescaled_background_image = pygame.transform.scale(self.background_image, (width, height - 100))
        self.gameover_sound = mixer.Sound(os.path.join("game_assets", "gameover.mp3"))

    def iscollision(self, mob, curx, cury, shoot):
        distance = math.sqrt((math.pow(mob[0] - curx, 2)) + (math.pow(mob[1] - cury, 2)))
        if distance < 15 and shoot:
            return True
        else:
            return False

    def events(self, section):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.waiting = False
                self.running = False
            if section == 1:
                if event.type == pygame.KEYDOWN:
                    if pygame.key.get_pressed()[pygame.K_r]:
                        self.weapon.reload()
                    if pygame.key.get_pressed()[pygame.K_p]:
                        if self.FPS == 30:
                            self.FPS = 240
                        else:
                            self.FPS = 30
                    if pygame.key.get_pressed()[pygame.K_o]:
                        self.player.mana += (300 - self.player.mana)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    key = pygame.mouse.get_pressed()
                    if key[0]:
                        self.weapon.shoot()
                        for i in self.mob:
                            for j in i.spot:
                                if self.iscollision(j, self.player.x, self.player.y, self.weapon.isshoot):
                                    i.take_damage(self.player, self.weapon.dmg)
                                    if self.weapon.name == 'R' and self.weapon.boost <= 5:
                                        self.weapon.boost += 1
                                    break
                    if key[2]:
                        self.skill.active(self.player, self.mob, self.player.mana)
            elif section == 0:
                pygame.mouse.set_visible(True)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    key = pygame.mouse.get_pressed()
                    mouse = pygame.mouse.get_pos()
                    if key[0]:
                        if 305 <= mouse[0] <= 395:
                            if 180 <= mouse[1] <= 220:
                                if self.weapon_selection == 0:
                                    self.sm.weapon_select = self.font.render("Revolver", True, white)
                                    self.sm.weapon_select_rect = self.sm.weapon_select.get_rect(center=(350, 200))
                                    self.weapon_selection = 1
                                elif self.weapon_selection == 1:
                                    self.sm.weapon_select = self.font.render("Glock", True, white)
                                    self.sm.weapon_select_rect = self.sm.weapon_select.get_rect(center=(350, 200))
                                    self.weapon_selection = 0
                            elif 230 <= mouse[1] <= 270:
                                if self.skill_selection == 2:
                                    self.sm.skill_select = self.font.render("Skill1", True, white)
                                    self.sm.skill_select_rect = self.sm.skill_select.get_rect(center=(350, 250))
                                    self.skill_selection = 0
                                elif self.skill_selection == 0:
                                    self.sm.skill_select = self.font.render("Skill2", True, white)
                                    self.sm.skill_select_rect = self.sm.skill_select.get_rect(center=(350, 250))
                                    self.skill_selection = 1
                                elif self.skill_selection == 1:
                                    self.sm.skill_select = self.font.render("Skill3", True, white)
                                    self.sm.skill_select_rect = self.sm.skill_select.get_rect(center=(350, 250))
                                    self.skill_selection = 2
                if event.type == pygame.KEYDOWN:
                    self.waiting = False
                    self.section = 1
            elif section == 2:
                if event.type == pygame.KEYDOWN:
                    if pygame.key.get_pressed()[pygame.K_CAPSLOCK]:
                        self.section = 0
                        self.waiting = False
                    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                        self.section = 4
                        self.waiting = False

    def start_screen(self):
        self.sm = StartMenu(self.font)
        mixer.music.set_volume(1)
        mixer.music.play(-1)
        self.weapon_selection = 0
        self.skill_selection = 0
        self.waiting = True
        while self.waiting:
            self.sm.draw(self.screen)
            self.events(0)
            pygame.display.update()
            self.clock.tick(self.FPS)

    def gameplay(self):
        self.player = Player()
        if self.weapon_selection == 0:
            self.weapon = Glock()
        elif self.weapon_selection == 1:
            self.weapon = Revolver()
        if self.skill_selection == 0:
            self.skill = Skill1()
        elif self.skill_selection == 1:
            self.skill = Skill2()
        elif self.skill_selection == 2:
            self.skill = Skill3()
        self.mob = []
        self.add_mob = 0
        self.weapon.start()
        mixer.music.set_volume(0.25)
        pygame.mouse.set_visible(False)
        self.waiting = True
        while self.waiting:
            self.screen.blit(self.rescaled_background_image, (0, 0))
            for i in self.mob:
                i.update(self.screen, self.player, self.mob, i)
            if self.player.damage == 3:
                mixer.music.stop()
                self.gameover_sound.play()
                time.sleep(3)
                self.section = 2
                self.waiting = False
            self.skill.update(self.screen)
            pygame.draw.rect(self.screen, black, [0, 300, 700, 131])
            self.player.update(self.screen, self.font)
            self.weapon.update(self.screen, self.font)

            self.events(1)

            self.add_mob += 1
            if self.add_mob == spawn_rate:
                x = random.randint(0, 1)
                if x == 0:
                    self.mob.append(NormalBombo())
                elif x == 1:
                    self.mob.append(GiantBombo())
                self.add_mob = 0

            pygame.display.update()
            self.clock.tick(self.FPS)

    def end_screen(self):
        self.em = EndMenu(self.font)
        self.waiting = True
        while self.waiting:
            self.em.draw(self.screen)
            self.events(2)
            pygame.display.update()
            self.clock.tick(self.FPS)

g = Game()
while g.running:
    if g.section == 0:
        g.start_screen()
    elif g.section == 1:
        g.gameplay()
    elif g.section == 2:
        g.end_screen()
    else:
        g.running = False
pygame.quit()