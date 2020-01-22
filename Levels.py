import pygame

from Enemy import *


class Levels:
    def __init__(self):
        self.level = L01()


class L01:
    def __init__(self):
        self.girl = Enemy(GIRL, x=334, y=330, hp=100)

    def render(self):
        self.girl.render()

    def applying(self, camera, player):
        camera.apply(enemy_group, player, self.girl.start_pos)

