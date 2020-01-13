import os
import pygame
from Constants import *
from Player import *
from functions import *
from game_area import *


def all_pics(path, n):
    images = []
    for i in range(n):
        image = load_image(path + str(i) + '.gif')
        images.append(load_image(image))
    return images


class Main():
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.background = pygame.image.load('data/ClubNeon.png')
        self.player = Player('Sosiska')
        self.image = pygame.image.load('data/Zero/Stand/0.gif')
        self.image = pygame.transform.scale(self.image, (60, 50))
        self.area = Area()
        self.x = self.y = 0
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
        # keys = list(pygame.key.get_pressed())
        # if 1 in keys:
        #     if keys[97] == 1:
        #         self.x = -1
        #     if keys[100] == 1:
        #         self.x = 1

    def render(self):
        """ rendering everything """

        self.player.render(self.screen, self.area)
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()

    def main_loop(self):
        """ main program cycle """
        # new_player = Player("Main player", self.image)
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


