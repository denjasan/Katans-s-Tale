import os
import random
import pygame
from Constants import *
from functions import *


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


class MiniGame:
    def __init__(self):
        self.status = ATTACK
        self.button_pressed = {"W": 0, "A": 0, "S": 0, "D": 0, "Sp": 0}
        self.groups_dict = {ATTACK: pygame.sprite.Group(), DEFENSE: pygame.sprite.Group()}

        self.main_person = Heart(self.groups_dict[ATTACK])

        self.AvailableGroup = self.groups_dict[self.status]

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
