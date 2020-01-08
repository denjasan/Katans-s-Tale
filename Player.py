import pygame
from Constants import *


class Player:
    def __init__(self, name):

        self.name = name
        self.state = ALIVE
        self.x = START_X
        self.y = START_Y
        self.hp = MAX_HP

    def move(self):
        """ the movement of the player """
        pass

    def render(self):
        """ rendering player """
        pass



