import os
import random
import pygame


pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.flip()
all_sprites = pygame.sprite.Group()


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


class Player(pygame.sprite.Sprite):
    def __init__(self, group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite. Это очень важно!!!
        super().__init__(group)
        self.image = pygame.Surface([20, 20])
        self.image.fill(pygame.Color("blue"))
        self.rect = self.image.get_rect()
        self.sleep = False

    def update(self, n):
        if not self.sleep:
            self.rect.y = n
        if pygame.sprite.spritecollideany(self, all_obstacles):
            self.sleep = True
        else:
            self.sleep = False


class Platform(pygame.sprite.Sprite):
    def __init__(self, group, x, y):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite. Это очень важно!!!
        super().__init__(group)
        self.image = pygame.Surface([50, 10])
        self.image.fill(pygame.Color("grey"))
        self.rect = pygame.Rect(x, y, 50, 10)


all_obstacles = pygame.sprite.Group()
running = True
y = 0
v = 50  # пикселей в секунду
fps = 60
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                Platform(all_obstacles, event.pos[0], event.pos[1])
            if event.button == 3 and not all_sprites:
                Player(all_sprites)
                for i in all_sprites:
                    i.rect.x = event.pos[0]
                    i.rect.y = event.pos[1]
                y = event.pos[1]
            elif event.button == 3 and all_sprites:
                for i in all_sprites:
                    i.rect.x, i.rect.y = event.pos
                    y = event.pos[1]
    if pygame.key.get_pressed()[275]:
        for i in all_sprites:
            i.rect.x += 10
    if pygame.key.get_pressed()[276]:
        for i in all_sprites:
            i.rect.x -= 10
    screen.fill((0, 0, 0))
    if all_sprites:
        y += v / fps
    all_sprites.draw(screen)
    all_obstacles.draw(screen)
    all_sprites.update(y)
    clock.tick(fps)
    pygame.display.flip()