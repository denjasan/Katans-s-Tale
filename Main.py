import os
import time

import pygame

from Constants import *
from Player import *
from functions import *
from game_area import *
from groups import *
from Camera import Camera
from Enemy import Enemy
from Levels import Levels
import MiniGame
import Interface


class Background(pygame.sprite.Sprite):
    def __init__(self, flag=False):
        super().__init__(all_sprites)
        self.image = load_image("ClubNeon.png")
        self.rect = self.image.get_rect()
        if not flag:
            self.rect.x = 0
        else:
            self.rect.x = -215
        self.rect.y = 117
        self.add(fon_group)


class Fon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        # self.image = load_image("ZEROposter.jpg")
        self.image = load_image("start_screen/fire/0.gif")
        self.rect = self.image.get_rect()
        self.rect = 0, 0  # -200, 0
        self.add(fon_group)


class Loading(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.image = load_image("Loading/0.gif")
        self.rect = self.image.get_rect()
        self.rect = -200, 0
        self.add(fon_group)


class Main(Levels):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.clock = pygame.time.Clock()

        pygame.mixer.init()
        pygame.mixer.music.load('data/music/start.ogg')
        pygame.mixer.music.play(-1)

        self.screen.fill((255, 255, 255))
        self.anim_count = 0
        self.images = []
        self.images.append(all_pics(path='data/start_screen/fire/', n=5))
        self.fon = Fon()
        self.start_screen()
        self.fon.kill()
        self.images = []

        pygame.mixer.music.load('data/music/club.ogg')
        pygame.mixer.music.play(-1)

        self.anim_count = 0
        self.images.append(all_pics(path='data/Loading/', n=3))
        self.pause = Loading()
        self.loading()
        self.pause.kill()
        self.screen.fill((0, 0, 0))
        self.images = None

        self.stairs_del = False  # Have we got stairs in that floor?
        self.running = True
        self.background = Background()
        self.player = Player('Sosiska', ZERO)
        self.area_y = AreaY1()
        self.area_x = AreaX1()
        self.camera = Camera()
        # self.MiniGame = MiniGame(self.player)

        self.main_person = MiniGame.MiniGame()

        self.main_loop()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    self.player.moving[RIGHT] = True
                if event.key == pygame.K_a:
                    self.player.moving[LEFT] = True
                if event.key == pygame.K_w:
                    self.player.moving[DANCE] = True
                if event.key == pygame.K_SPACE:
                    self.player.moving[SWORD] = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    self.player.moving[RIGHT] = False
                if event.key == pygame.K_a:
                    self.player.moving[LEFT] = False
                if event.key == pygame.K_w:
                    self.player.moving[DANCE] = False
                # if event.key == pygame.K_SPACE:
                #     self.player.moving[SWORD] = True

    def render(self):
        """ rendering everything """
        self.player.render()
        self.level.render()
        all_sprites.update(self.area_y, self.area_x, self.stairs_del)
        all_sprites.draw(self.screen)

        laser_group.update(self.player.fps)
        laser_group.draw(self.screen)

        enemy_group.update(self.player, self.player.situation)
        enemy_group.draw(self.screen)

        player_group.update(self.area_y, self.area_x, self.stairs_del)
        player_group.draw(screen)

        # player_group.update(self.x, self.area)
        # self.x = 0
        # player_group.draw(self.screen)

        if self.player.mini_game:  # если мини игра работает то мы рисуем одно иначе другое
            self.screen.fill((0, 0, 0))
            self.main_person.update()
            for i in self.main_person.AvailableGroup:
                i.draw(self.screen)
                i.update()
            # v = 50
            # #self.screen.fill((0, 0, 0))
            # self.mini_game.update(v / self.player.fps)
            # self.mini_game.AvailableGroup.draw(self.screen)
        Interface.render_hp(self.screen)  # вы выодим на экран self.screen кол-во жизней hp.
        self.clock.tick(self.player.fps)
        # self.screen.blit(pygame.image.load('data/laser.png'), (316, 409))
        pygame.display.flip()

    def start_screen(self):
        """ start screen loop """

        intro_text = "PRESS ANY KEY TO START"
        font = pygame.font.Font(None, 40)
        string_rendered = font.render(intro_text, 1, pygame.Color('pink'))
        intro_rect = string_rendered.get_rect()
        text_w = string_rendered.get_width()
        text_h = string_rendered.get_height()
        intro_rect.y = 630
        intro_rect.x = 655
        pygame.draw.rect(self.screen, (0, 0, 0), (intro_rect.x - 10, intro_rect.y - 10, text_w + 20, text_h + 20), 0)
        pygame.draw.rect(self.screen, pygame.Color('pink'),
                         (intro_rect.x - 10, intro_rect.y - 10, text_w + 20, text_h + 20), 1)
        pygame.draw.rect(self.screen, (0, 0, 0), (601, 0, 1, 720), 0)
        self.screen.blit(string_rendered, intro_rect)

        intro_text = "Тут могла бы быть ваша реклама"
        font = pygame.font.Font(None, 34)
        string_rendered = font.render(intro_text, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_w = string_rendered.get_width()
        text_h = string_rendered.get_height()
        intro_rect.y = 270
        intro_rect.x = 655
        # pygame.draw.rect(self.screen, (0, 0, 0), (intro_rect.x - 10, intro_rect.y - 10, text_w + 20, text_h + 20), 0)
        pygame.draw.rect(self.screen, pygame.Color('black'),
                         (intro_rect.x - 10, intro_rect.y - 10, text_w + 20, text_h + 20), 1)
        pygame.draw.rect(self.screen, (0, 0, 0), (601, 0, 1, 720), 0)
        self.screen.blit(string_rendered, intro_rect)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    return  # начинаем игру
            # print(self.images, self.anim_count)
            # print(pygame.mixer.music.set_endevent())
            if self.anim_count == 4:
                self.anim_count = 0
            self.fon.image = self.images[0][self.anim_count]
            self.anim_count += 1

            all_sprites.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(FPS // 4)

    def loading(self):
        # all_sprites.draw(self.screen)

        k = 0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
            if k == 0:  # 39
                time.sleep(0.8)
                return  # начинаем игру через 13.8 секунд

            if self.anim_count == 3:
                self.anim_count = 0
            self.pause.image = self.images[0][self.anim_count]
            self.anim_count += 1
            k += 1

            all_sprites.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(FPS // 10)

    def main_loop(self):
        """ main program cycle """

        first_time = True
        while self.running:
            self.render()
            self.handle_events()
            if not self.player.mini_game:
                if self.player.state != DEAD:
                    self.player.move()
                if self.player.rect.y < SECOND_FLOOR and first_time:
                    self.area_y.kill()
                    self.background.kill()
                    self.area_x.kill()
                    self.area_y = AreaY2()
                    self.background = Background(True)
                    self.area_x = AreaX1(True)
                    first_time = False
                    self.stairs_del = True
                self.camera.update(self.player)
                # for i in fon_group:
                self.camera.apply(laser_group, self.player)
                self.camera.apply(fon_group, self.player)
                self.level.applying(self.camera, self.player)
                # self.camera.apply(enemy_group, self.player, self.girl.start_pos)
                # all_sprites.remove(player_group, self.area_x, self.area_y)
        terminate()


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    # screen = pygame.display.set_mode((1920, 1080))
    game = Main(screen)
    # game.main_loop()
