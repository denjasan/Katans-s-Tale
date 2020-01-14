import os
import random
import pygame

pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.flip()
player_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()


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
        self.rect.x = width // 2
        self.rect.y = height // 2

    def update(self, x, y):
        self.rect.x += x
        if self.rect.x > width:
            self.rect.x -= width
        if self.rect.x < 0:
            self.rect.x += width

        self.rect.y += y

        if self.rect.y > height:
            self.rect.y -= height
        if self.rect.y < 0:
            self.rect.y += height


class Enemy(pygame.sprite.Sprite):
    def __init__(self, group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite. Это очень важно!!!
        super().__init__(group)
        self.image = pygame.Surface([20, 20])
        self.image.fill(pygame.Color("white"))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, width)
        self.vx = self.vy = 7
        self.rect.y = random.randint(0, height)

    def update(self):
        self.rect.x += self.vx
        if self.rect.x > width or self.rect.x < 0:
            self.rect.x = random.randint(0, width)

        self.rect.y += self.vy

        if self.rect.y > height or self.rect.y < 0:
            self.rect.y = random.randint(0, height)


heart = Player(player_group)
running = True
y = 0
v = 300  # пикселей в секунду
fps = 60
dx = dy = 0
clock = pygame.time.Clock()
for _ in range(10):
    Enemy(enemy_group)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if pygame.key.get_pressed()[275]:
        dx = v / fps + 1
    if pygame.key.get_pressed()[276]:
        dx = -v / fps

    if pygame.key.get_pressed()[274]:
        dy = v / fps + 1
    if pygame.key.get_pressed()[273]:
        dy = -v / fps
    screen.fill((0, 0, 0))
    heart.update(dx, dy)
    enemy_group.update()
    enemy_group.draw(screen)
    dx = dy = 0
    player_group.draw(screen)
    clock.tick(fps)
    pygame.display.flip()
