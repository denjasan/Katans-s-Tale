import os
import random
import pygame
from Constants import *
from functions import *
from groups import *
import Values


width, height = 1080, 720


class Heart(pygame.sprite.Sprite):
    def __init__(self, group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite. Это очень важно!!!
        super().__init__(group)
        self.button_pressed = {"W": 0, "A": 0, "S": 0, "D": 0, "Sp": 0}
        self.image = pygame.transform.scale(load_image("heart.png"), (25, 25))
        self.rect = self.image.get_rect()
        self.rect.x = width // 2
        self.rect.y = height // 2

    def handle_events(self):
        self.button_pressed = {"W": 0, "A": 0, "S": 0, "D": 0}
        if pygame.key.get_pressed()[100]:
            self.button_pressed["D"] = 1
        if pygame.key.get_pressed()[97]:
            self.button_pressed["A"] = 1
        if pygame.key.get_pressed()[119]:
            self.button_pressed["W"] = 1
        if pygame.key.get_pressed()[115]:
            self.button_pressed["S"] = 1

    def update(self):
        self.handle_events()

        if self.button_pressed["W"] == 1:
            self.rect.y -= 20
        if self.button_pressed["A"] == 1:
            self.rect.x -= 20
        if self.button_pressed["S"] == 1:
            self.rect.y += 20
        if self.button_pressed["D"] == 1:
            self.rect.x += 20

        if self.rect.x > width:
            self.rect.x -= width
        if self.rect.x < 0:
            self.rect.x += width

        if self.rect.y > height:
            self.rect.y -= height
        if self.rect.y < 0:
            self.rect.y += height

        if pygame.sprite.spritecollideany(self, enemy_group):
            pass


class Enemy(pygame.sprite.Sprite):
    def __init__(self, group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite. Это очень важно!!!
        super().__init__(group)
        self.image = pygame.Surface([20, 20])
        self.image.fill(pygame.Color("white"))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, width)
        self.vx = self.vy = 7
        self.rect.y = random.randint(0, height)

    def update(self):
        if pygame.sprite.spritecollideany(self, MG_mp):
            self.rect.x += random.randint(-100, 100)
            self.rect.y += random.randint(-100, 100)
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


class MiniGame:
    def __init__(self):
        self.status = ATTACK
        self.button_pressed = {"W": 0, "A": 0, "S": 0, "D": 0, "Sp": 0}
        self.groups_dict = {ATTACK: [MG_mp, MG_e], DEFENSE: MG_d}
        for i in range(10):
            Enemy(self.groups_dict[ATTACK][1])
        self.main_person = Heart(self.groups_dict[ATTACK])

        self.AvailableGroup = [self.groups_dict[self.status]]

    def handle_events(self):
        if pygame.key.get_pressed()[32]:
            self.button_pressed["Sp"] = 1

    def update(self):
        x = y = 0
        if self.status == ATTACK:
            if self.button_pressed["W"] == 1:
                self.main_person.rect.y -= 10

            if self.button_pressed["A"] == 1:
                self.main_person.rect.x -= 10

            if self.button_pressed["S"] == 1:
                self.main_person.rect.y += 10

            if self.button_pressed["D"] == 1:
                self.main_person.rect.x += 10

            self.main_person.update()

        elif self.status == DEFENSE:
            pass

        elif self.status == DEAD:
            pass

        self.AvailableGroup = self.groups_dict[self.status]

    def attack(self):
        pass

    def attack(self):
        pass

    def attack(self):
        pass
