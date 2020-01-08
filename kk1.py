import os
import random
import sys
from Enemy import *
import pygame


pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.flip()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert_alpha()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


clock = pygame.time.Clock()
FPS = 50


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = ["Р—РђРЎРўРђР’РљРђ", "",
                  "РџСЂР°РІРёР»Р° РёРіСЂС‹",
                  "Р•СЃР»Рё РІ РїСЂР°РІРёР»Р°С… РЅРµСЃРєРѕР»СЊРєРѕ СЃС‚СЂРѕРє,",
                  "РїСЂРёС…РѕРґРёС‚СЃСЏ РІС‹РІРѕРґРёС‚СЊ РёС… РїРѕСЃС‚СЂРѕС‡РЅРѕ"]

    fon = pygame.transform.scale(load_image('fon.jpg'), (800, 600))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return  # РЅР°С‡РёРЅР°РµРј РёРіСЂСѓ
        pygame.display.flip()
        clock.tick(FPS)


start_screen()


def load_level(filename):
    filename = "data/" + filename
    # С‡РёС‚Р°РµРј СѓСЂРѕРІРµРЅСЊ, СѓР±РёСЂР°СЏ СЃРёРјРІРѕР»С‹ РїРµСЂРµРІРѕРґР° СЃС‚СЂРѕРєРё
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    # Рё РїРѕРґСЃС‡РёС‚С‹РІР°РµРј РјР°РєСЃРёРјР°Р»СЊРЅСѓСЋ РґР»РёРЅСѓ
    max_width = max(map(len, level_map))

    # РґРѕРїРѕР»РЅСЏРµРј РєР°Р¶РґСѓСЋ СЃС‚СЂРѕРєСѓ РїСѓСЃС‚С‹РјРё РєР»РµС‚РєР°РјРё ('.')
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


tile_images = {'wall': load_image('box.png'), 'empty': load_image('grass.png')}
player_image = load_image('mar.png')

tile_width = tile_height = 50
tiles_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
player_group = pygame.sprite.Group()


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = player_image
        self.rect = self.image.get_rect().move(tile_width * pos_x + 15, tile_height * pos_y + 5)


player_coord = []


def generate_level(level):
    global player_coord
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
            elif level[y][x] == 'E':
                Tile('empty', x, y)
                new_enemy = Enemy(x, y, load_image('orc_regular_bald.png'))
            elif level[y][x] == '@':
                Tile('empty', x, y)
                new_player = Player(x, y)
                player_coord = [x, y]
    return new_player, x, y


player, level_x, level_y = generate_level(load_level('level'))


class Camera:
    def __init__(self):
        self.dx = 0
        self.dy = 0

    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - width // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - height // 2)


def continue_screen():
    x, y = 0, 0
    screen.fill((0, 0, 0))
    camera = Camera()
    while True:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            keys = list(pygame.key.get_pressed())
            if 1 in keys:
                if keys[119] == 1:
                    y = 10
                if keys[97] == 1:
                    x = -10
                if keys[115] == 1:
                    y = -10
                if keys[100] == 1:
                    x = 10
        all_sprites.draw(screen)
        player.rect.x += x
        player.rect.y -= y
        player_coord[0] += x
        player_coord[1] -= y
        all_enemies.draw(screen)
        all_enemies.update(player.rect.x, player.rect.y)
        x, y = 0, 0
        camera.update(player)
        for sprite in all_sprites:
            camera.apply(sprite)
        for enemy in all_enemies:
            camera.apply(enemy)
        player_group.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)


continue_screen()