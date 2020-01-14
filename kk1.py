import os
import random
import pygame
import Constants

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


class Heart(pygame.sprite.Sprite):
    def __init__(self, group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite. Это очень важно!!!
        super().__init__(group)
        self.image = pygame.transform.scale(load_image("heart.png"), (2000, 2000))
        self.rect = self.image.get_rect()
        self.rect.x = width // 2
        self.rect.y = height // 2
        self.Zähler = 1

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

        if pygame.sprite.spritecollideany(self, enemy_group):
            Constants.MAX_HP -= 2
        if Constants.MAX_HP == 0:
            print(123)


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
        if pygame.sprite.spritecollideany(self, player_group):
            self.rect.x += -self.vx * 4
            self.rect.y += -self.vy * 4

        self.rect.x += self.vx
        if self.rect.x > width:
            self.rect.x -= width
        if self.rect.x < 0:
            self.rect.x += width

        self.rect.y += self.vy

        if self.rect.y > height:
            self.rect.y -= height
        if self.rect.y < 0:
            self.rect.y += height


heart = Heart(player_group)
running = True
s_h = 2000
x = y = 0
v = 500  # пикселей в секунду
fps = 60
dx = dy = 0
clock = pygame.time.Clock()
f = 10
vector = v / fps
flag = False
while s_h > 25:
    screen.fill((0, 0, 0))
    player_group.draw(screen)
    if s_h - f < 25:
        f = s_h - 25
    s_h = s_h - f
    heart.image = pygame.transform.scale(heart.image, (s_h, s_h))
    heart.rect.x, heart.rect.y = width // 2 - s_h // 2, height // 2 - s_h // 2
    clock.tick(fps)
    pygame.display.flip()

heart.rect = heart.image.get_rect()
heart.rect.x, heart.rect.y = width // 2, height // 2


def defense():
    global dx, dy, heart, running, enemy_group
    if heart.Zähler <= 900:
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


def attack():
    global running, x, y, vector, flag
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if pygame.key.get_pressed()[Constants.SPACE] == 1:
        flag = True
    if flag:
        return
    if x >= int(width * 0.8) or x < 0:
        vector *= -1
    x += vector
    pygame.draw.rect(screen, (255, 255, 255), (int(width * 0.1), int(height * 0.7), int(width * 0.8), 50), 0)
    pygame.draw.rect(screen, (100, 100, 100), (int(width * 0.1) + x, int(height * 0.7) - 15, 10, 80), 0)
    pygame.draw.rect(screen, (255, 0, 0), (width // 2, 0, 5, 1000), 0)
    clock.tick(fps)
    pygame.display.flip()


heart.image = pygame.transform.scale(heart.image, (30, 30))

for _ in range(10):
    Enemy(enemy_group)

while running:
    heart.Zähler += 1
    if heart.Zähler <= 100:
        defense()
    else:
        attack()


