import os
import pygame
from Constants import *
from Player import *
from functions import *
from game_area import *


class Main():
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.background = pygame.image.load('data/ClubNeon.png')
        self.player = Player
        self.image = pygame.image.load('data/Zero/Run/0.gif')
        self.image = pygame.transform.scale(self.image, (60, 50))
        self.area = Area()
        self.x = self.y = 0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        keys = list(pygame.key.get_pressed())
        if 1 in keys:
            if keys[97] == 1:
                self.x = -1
            if keys[100] == 1:
                self.x = 1

    def render(self):
        """ rendering everything """
        self.screen.blit(self.background, (0, 0))

        player_group.update(self.x, self.area)
        self.x = 0
        player_group.draw(self.screen)
        pygame.display.flip()

    def main_loop(self):
        """ main program cycle """
        new_player = Player("Main player", self.image)
        while self.running:
            self.handle_events()
            self.render()


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    game = Main(screen)
    game.main_loop()


