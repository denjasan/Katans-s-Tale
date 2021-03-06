# encoding: utf-8
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
import Values
from random import randrange
import groups


class Background(pygame.sprite.Sprite):
    def __init__(self, flag=False):
        super().__init__(groups.all_sprites)
        self.image = load_image("ClubNeon.png")
        self.rect = self.image.get_rect()
        if not flag:
            self.rect.x = 0
        else:
            self.rect.x = -215
        self.rect.y = 117
        self.add(fon_group)


class FirstGround(pygame.sprite.Sprite):
    def __init__(self, flag=False):
        super().__init__(first_plan_group)
        if not flag:
            self.image = load_image("fon/first_plan1.png")
            self.rect = self.image.get_rect()
            self.rect.x = 0
        else:
            self.image = load_image("fon/first_plan.png")
            self.rect = self.image.get_rect()
            self.rect.x = -215
        self.rect.y = 117


class Fon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(groups.all_sprites)
        self.image = load_image("start_screen/fire/0.gif")
        self.rect = self.image.get_rect()
        self.rect = 0, 0  # -200, 0
        self.add(fon_group)


class Loading(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(groups.all_sprites)
        self.image = load_image("Loading/0.gif")
        self.rect = self.image.get_rect()
        self.rect = -200, 0
        self.add(fon_group)


class Ending(pygame.sprite.Sprite):
    def __init__(self, win, screen):
        super().__init__(groups.all_sprites)
        self.screen = screen
        if win:
            self.image = pygame.transform.scale(load_image("endgame.png"), (WIDTH, HEIGHT))
        else:
            self.image = pygame.transform.scale(load_image("endgame.png"), (WIDTH, HEIGHT))
        self.rect = self.image.get_rect()
        self.rect = 0, 0


class Button(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(groups.all_sprites)
        self.image = pygame.Surface([400, 50])
        self.image.fill((100, 0, 100))
        self.rect = self.image.get_rect()
        self.x, self.y = x, y
        self.rect = [x, y]

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
                if event.pos[0] - self.x <= 400 and event.pos[1] - self.y <= 50:
                    terminate()


class ButtonText(pygame.sprite.Sprite):
    def __init__(self, x, y, text):
        super().__init__(groups.all_sprites)
        self.font = pygame.font.Font(None, 50)
        self.image = self.font.render(text, 1, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect = [x, y]


class Main(Levels):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.clock = pygame.time.Clock()

        self.end_image = pygame.transform.scale(load_image("endgame.png"), (WIDTH, HEIGHT))
        self.designations = load_image("key_designation.png")

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
        self.first_ground = FirstGround()  # it will have something when player on 2nd floor
        self.background = Background()
        self.player = Player('Sosiska', ZERO)
        self.area_y = AreaY1()
        self.area_x = AreaX1()
        self.camera = Camera()
        # self.MiniGame = MiniGame(self.player)

        self.main_person = MiniGame.MiniGame(self.screen, self.player, self)

        self.main_loop()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    self.player.moving[RIGHT] = True
                if event.key == pygame.K_a:
                    self.player.moving[LEFT] = True
                if event.key == pygame.K_w:
                    self.player.moving[DANCE] = True
                if event.key == pygame.K_SPACE:
                    self.player.moving[SWORD] = True
                if event.key == pygame.K_e:
                    self.player.interaction = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    self.player.moving[RIGHT] = False
                if event.key == pygame.K_a:
                    self.player.moving[LEFT] = False
                if event.key == pygame.K_w:
                    self.player.moving[DANCE] = False
                if event.key == pygame.K_e:
                    self.player.interaction = False

    def render(self):
        """ rendering everything """
        self.player.render()
        self.level.render()
        groups.all_sprites.update(self.area_y, self.area_x, self.stairs_del)
        groups.all_sprites.draw(self.screen)

        laser_group.update(self.player.fps)
        laser_group.draw(self.screen)

        enemy_group.update(self.player, self.player.situation)
        enemy_group.draw(self.screen)

        player_group.update(self.area_y, self.area_x, self.stairs_del)
        player_group.draw(screen)

        first_plan_group.draw(self.screen)

        if Values.MINIGAME:  # если мини игра работает то мы рисуем одно иначе другое
            self.screen.fill((0, 0, 0))
            self.main_person.update()
            for i in self.main_person.AvailableGroup:
                i.draw(self.screen)
                i.update()
        Interface.render_hp(self.screen)  # вы выодим на экран self.screen кол-во жизней hp.
        self.clock.tick(self.player.fps)

        if Values.END:
            # self.end_image.blit(self.screen, (0, 0))
            self.running = False
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

        self.text('black', pos=(655, 270))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    return  # начинаем игру

            if self.anim_count == 4:
                self.anim_count = 0
            self.fon.image = self.images[0][self.anim_count]
            self.anim_count += 1

            groups.all_sprites.draw(self.screen)
            self.screen.blit(self.designations, (695, 312))
            pygame.display.flip()
            self.clock.tick(FPS // 4)

    def loading(self):

        k = 0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
            if k == 39:  # 39
                time.sleep(0.8)
                return  # начинаем игру через 13.8 секунд

            if self.anim_count == 3:
                self.anim_count = 0
            self.pause.image = self.images[0][self.anim_count]
            self.anim_count += 1
            k += 1

            groups.all_sprites.draw(self.screen)
            self.text('white', 'Цель: добраться до лифта', (700, 400))
            pygame.display.flip()
            self.clock.tick(FPS // 10)

    def main_loop(self):
        """ main program cycle """

        dead_frames = 0
        dead = False
        first_time = True
        # win = False
        while self.running:
            # if self.level.girl
            self.screen.fill((0, 0, 0))
            self.render()
            self.handle_events()
            if not Values.MINIGAME:
                self.player.move()
                if self.player.state == DEAD:
                    self.player.moving[DIE] = True
                    if dead_frames >= 6:
                        dead = True
                        break
                    dead_frames += 1
                if self.player.rect.y < SECOND_FLOOR and first_time:
                    self.area_y.kill()
                    self.background.kill()
                    self.area_x.kill()
                    self.first_ground.kill()
                    self.area_y = AreaY2()
                    self.first_ground = FirstGround(True)
                    self.background = Background(True)
                    self.area_x = AreaX1(True)
                    first_time = False
                    self.stairs_del = True
                self.camera.update(self.player)
                self.camera.apply(fon_group, self.player)
                self.camera.apply(first_plan_group, self.player)
                self.level.applying(self.camera, self.player)

        pygame.mixer.music.load('data/music/start.ogg')
        pygame.mixer.music.play(-1)
        pygame.mouse.set_visible(True)
        if dead:
            self.death()

        else:
            self.win()

        terminate()

    def death(self):
        groups.all_sprites = pygame.sprite.Group()
        end = Ending(win=False, screen=self.screen)
        self.buttons = [Button(300, 200), Button(300, 350), Button(300, 500)]
        self.buttonstext = [ButtonText(300, 200, "Выход из игры"),
                            ButtonText(300, 350, "Все уровни"),
                            ButtonText(300, 500, "Настройки")]
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                self.buttons[0].update()
            self.screen.fill((0, 0, 0))
            for i in range(10000):
                self.screen.fill((255, 255, 255), ((randrange(120, 920), randrange(80, 620)), (5, 5)))
            groups.all_sprites.draw(self.screen)
            groups.all_sprites.update()
            self.text('purple', 'Колебаться - значит проиграть', (325, 435), 0)
            pygame.display.flip()
            self.clock.tick(FPS // 4)

    def win(self):
        groups.all_sprites = pygame.sprite.Group()
        end = Ending(win=True, screen=self.screen)
        self.buttons = [Button(300, 200), Button(300, 350), Button(300, 500)]
        self.buttonstext = [ButtonText(300, 200, "Выход из игры"),
                            ButtonText(300, 350, "Все уровни"),
                            ButtonText(300, 500, "Настройки")]
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                self.buttons[0].update()
            self.screen.fill((0, 0, 0))
            for i in range(10000):
                self.screen.fill((255, 255, 255), ((randrange(120, 920), randrange(80, 620)), (5, 5)))
            groups.all_sprites.draw(self.screen)
            groups.all_sprites.update()
            self.text('purple', 'Надо поднять бокалы за прекрасную победу', (230, 435), 0)
            pygame.display.flip()
            self.clock.tick(FPS // 4)

    def text(self, color='white', text="Тут могла бы быть ваша реклама", pos=(0, 0), zal=1):
        intro_text = text
        font = pygame.font.Font(None, 34)
        if zal == 0:
            string_rendered = font.render(intro_text, 1, pygame.Color('white'))
        else:
            string_rendered = font.render(intro_text, 1, pygame.Color(color))
        intro_rect = string_rendered.get_rect()
        text_w = string_rendered.get_width()
        text_h = string_rendered.get_height()
        intro_rect.y = pos[1]
        intro_rect.x = pos[0]
        pygame.draw.rect(self.screen, pygame.Color(color),
                         (intro_rect.x - 10, intro_rect.y - 10, text_w + 20, text_h + 20), zal)
        self.screen.blit(string_rendered, intro_rect)


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    # screen = pygame.display.set_mode((1920, 1080))
    game = Main(screen)
    # game.main_loop()
