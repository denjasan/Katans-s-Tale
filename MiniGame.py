# encoding: utf-8
import os
import random

import pygame
import DialogLib
from Constants import *
from functions import *
from groups import *
import groups
import Values
from Dialogs import *


width, height = WIDTH, HEIGHT


class Heart(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.button_pressed = {"W": False, "A": False, "S": False, "D": False, "Sp": False}
        self.image = pygame.transform.scale(load_image("heartv2.0.png"), (30, 30))
        self.size = 3000
        self.rect = self.image.get_rect()
        self.rect.x = width // 2
        self.rect.y = height // 2

    def handle_events(self):
        self.button_pressed = {"W": False, "A": False, "S": False, "D": False}
        if pygame.key.get_pressed()[100]:
            self.button_pressed["D"] = True
        if pygame.key.get_pressed()[97]:
            self.button_pressed["A"] = True
        if pygame.key.get_pressed()[119]:
            self.button_pressed["W"] = True
        if pygame.key.get_pressed()[115]:
            self.button_pressed["S"] = True

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                self.rect.x, self.rect.y = event.pos

        if pygame.sprite.spritecollideany(self, enemy_group):
            pass


class Enemy(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.image = load_image("shuriken.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, width)
        self.vx, self.vy = random.randint(5, 15), random.randint(5, 15)
        self.rect.y = random.randint(0, height)

    def update(self):
        if pygame.sprite.spritecollideany(self, MG_mp):
            self.kill()
            Values.InstantHP -= 5

        self.rect.x += self.vx
        if self.rect.x > width:
            self.rect.x -= width
        if self.rect.x < 0:
            self.rect.x += width

        self.rect.y += self.vy

        if self.rect.y > height:
            self.rect.y -= height
        if self.rect.y < 0:
            self.rect.y += height


class Katana(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.image = load_image("katana.png")
        self.image = pygame.transform.flip(self.image, 1, 0)
        self.rect = self.image.get_rect()
        self.rect.x = width * 0.1
        self.sizeX = self.rect[0]
        self.vx = 30
        self.stop = False
        self.rect.y = HEIGHT * 0.1

    def update(self):
        if not self.stop:
            print("self.rect.x:\t", self.rect.x)
            if self.rect.x >= 800:
                self.vx = -30
                self.image = pygame.transform.flip(self.image, 1, 0)
            elif self.rect.x <= -10:
                self.vx = 30
                self.image = pygame.transform.flip(self.image, 1, 0)
            self.rect.x += self.vx


class Girl(pygame.sprite.Sprite):
    def __init__(self, group, path):
        super().__init__(group)
        self.image = load_image(path)
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH // 2 - 100
        self.rect.y = HEIGHT // 2 - 200
        self.hp = E_HP


class Fon(pygame.sprite.Sprite):
    def __init__(self, group, path):
        super().__init__(group)
        self.image = load_image(path)
        self.image = pygame.transform.scale(self.image, (WIDTH, HEIGHT))
        self.rect = self.image.get_rect()


class MiniGame:
    def __init__(self, screen, player, main):
        self.main = main
        self.first_time = True
        self.katana = False
        self.player = player
        self.screen = screen
        self.status = ATTACK
        self.dialog = DialogLib.Dialog(self.screen, 10, FPS)
        self.girl = Girl(MG_d, "Girl/GirlSkeleton.png")
        self.Fon_A = Fon(MG_fon, "cityfon.png")
        self.zahler = 0
        self.x = self.y = 0
        self.fon = load_image("demon_fon.png")
        self.button_pressed = {"W": False, "A": False, "S": False, "D": False, "Sp": False}
        self.groups_dict = {ATTACK: [MG_mp, MG_fon, MG_e], DEFENSE: [MG_d], INTRO: [MG_intro]}
        for i in range(30):
            Enemy(self.groups_dict[ATTACK][2])
        self.main_person = Heart(self.groups_dict[ATTACK])

        self.AvailableGroup = [self.groups_dict[self.status]]
        self.first_attack = True

    def handle_events(self):
        if pygame.key.get_pressed()[32]:
            self.button_pressed["Sp"] = True

    def introA(self):
        s = self.main_person.size
        self.screen.blit(pygame.transform.scale(self.main_person.image, (s, s)), ((width - s) // 2, (height - s) // 2))
        self.main_person.size -= 10

    def update(self):
        if self.first_time:
            self.music()
            self.first_time = False
        x = y = 0
        print("self.girl.hp:\t", self.girl.hp, "Values.InstantHP\t", Values.InstantHP)
        if Values.InstantHP <= 0:
            self.status = DEAD

        elif self.zahler >= 100:
            #self.first_attack = False
            self.status = DEFENSE

        if self.girl.hp <= 0:
            self.main.level.girl.kill()
            self.status = WIN

        if self.status == ATTACK:
            self.attack()

        elif self.status == DEFENSE:
            self.button_pressed["Sp"] = False
            self.defense()

        elif self.status == WIN:
            self.player.state = WIN
            self.end()

        elif self.status == DEAD:
            self.player.state = DEAD
            self.end()

        self.AvailableGroup = self.groups_dict[self.status]

    def attack(self):
        pygame.mouse.set_visible(False)
        self.zahler += 1
        self.main_person.update()

    def end(self):
        pygame.mouse.set_visible(True)
        self.status = ATTACK
        self.player.moving = [False] * MOVING_LEN
        self.screen.fill((0, 0, 0))
        Values.MINIGAME = False
        Values.GIRL = False
        self.first_time = True
        pygame.mixer.music.load('data/music/club.ogg')
        pygame.mixer.music.play(-1)

    def defense(self):
        pygame.mouse.set_visible(True)
        self.handle_events()
        if self.button_pressed["Sp"] and self.katana:
            self.katana.stop = True
            self.katana.image = pygame.transform.scale(self.katana.image, (2, 4000))
            self.katana.rect[1] = 0
            self.girl.hp -= int((WIDTH // 2 - abs(WIDTH // 2 - self.katana.rect.x)) / (WIDTH // 2) * E_HP) + 2
            print("self.girl.hp in defense\t", self.girl.hp)
            self.zahler = 0
            self.groups_dict[ATTACK][2] = pygame.sprite.Group()
            for i in range(20):
                Enemy(self.groups_dict[ATTACK][2])
            self.status = ATTACK
        if self.dialog.draw_dialog(DEFENSE_DIALOG):
            self.katana = Katana(groups.MG_d)
            self.katana.update()
            pygame.draw.rect(self.screen, (255, 255, 255), (int(width * 0.1),
                                                            int(height * 0.7), int(width * 0.8), 50), 0)
            groups.MG_d = pygame.sprite.Group()

    def music(self):
        pygame.mixer.music.load('data/music/mus_boss1.ogg')
        pygame.mixer.music.play(-1)

