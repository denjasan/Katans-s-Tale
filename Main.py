import os

import pygame

from Constants import *
from Player import *
from functions import *
from game_area import *
from groups import *
from Camera import Camera


class Main:
    def __init__(self, screen):

        self.clock = pygame.time.Clock()

        self.screen = screen
        self.running = True

        self.background = pygame.image.load('data/ClubNeon.png')

        self.player = Player('Sosiska', ZERO)

        self.area = Area()

        self.main_loop()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    self.player.mooving = [0, 1]
                if event.key == pygame.K_a:
                    self.player.mooving = [1, 0]

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    self.player.mooving = [0, 0]
                if event.key == pygame.K_a:
                    self.player.mooving = [0, 0]

    def render(self):
        """ rendering everything """
        self.screen.blit(self.background, (0, 0))
        self.player.render()

        all_sprites.draw(self.screen)
        all_sprites.update(self.area)

        # player_group.update(self.x, self.area)
        # self.x = 0
        # player_group.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.flip()

    def main_loop(self):
        """ main program cycle """

        while self.running:
            if self.player.state != DEAD:
                self.player.moove()
            self.render()
            self.handle_events()


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    game = Main(screen)
    game.main_loop()


