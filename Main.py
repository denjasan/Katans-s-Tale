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
        self.rect = self.image.get_rect().move(100, 0)
        self.rect.x = self.rect.y = 0
        self.add(fon_group)


class Main:
    def __init__(self, screen):

        self.clock = pygame.time.Clock()
        self.screen = screen
        self.running = True
        self.background = Background()
        self.player = Player('Sosiska', ZERO)
        self.area = Area()
        self.area_x = AreaX()
        self.camera = Camera()

        self.main_loop()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    self.player.moving[RIGHT] = 1
                if event.key == pygame.K_a:
                    self.player.moving[LEFT] = 1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    self.player.moving[RIGHT] = 0
                if event.key == pygame.K_a:
                    self.player.moving[LEFT] = 0

    def render(self):
        """ rendering everything """
        self.player.render()
        all_sprites.update(self.area, self.area_x)
        all_sprites.draw(self.screen)

        player_group.update(self.area, self.area_x)
        player_group.draw(screen)

        # player_group.update(self.x, self.area)
        # self.x = 0
        # player_group.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.flip()

    def main_loop(self):
        """ main program cycle """
        while self.running:
            if self.player.state != DEAD:
                self.player.move()
            self.render()
            self.handle_events()
            self.camera.update(self.player)
            for i in fon_group:
                self.camera.apply(i)
        terminate()


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    #screen = pygame.display.set_mode((1920, 1080))
    game = Main(screen)
    game.main_loop()


