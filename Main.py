import os

import pygame

from Constants import *
from Player import *
from functions import *
from game_area import *
from groups import *
from Camera import Camera


class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.image = load_image("ClubNeon.png")
        self.rect = self.image.get_rect().move(0, 0)
class Main:
    def __init__(self, screen):

        self.clock = pygame.time.Clock()

        self.screen = screen
        self.running = True

        self.background = Background()

        self.player = Player('Sosiska', ZERO)

        self.area = Area()

        self.main_loop()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    self.player.moving = [0, 1]
                if event.key == pygame.K_a:
                    self.player.moving = [1, 0]

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    self.player.moving = [0, 0]
                if event.key == pygame.K_a:
                    self.player.moving = [0, 0]

    def render(self):
        """ rendering everything """
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

        terminate()


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    game = Main(screen)
    game.main_loop()


