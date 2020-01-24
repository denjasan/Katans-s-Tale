import os
import random
import pygame
import Constants

pygame.init()
size = width, height = 1080, 720
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


def death():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    text = font.render("Вы, умерли.", 1, (100, 255, 100))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, (0, 255, 0), (text_x - 10, text_y - 10,
                                           text_w + 20, text_h + 20), 1)
    pygame.display.flip()


class Heart(pygame.sprite.Sprite):
    def __init__(self, group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite. Это очень важно!!!
        super().__init__(group)
        self.image = pygame.transform.scale(load_image("heart.png"), (2000, 2000))
        self.rect = self.image.get_rect()
        self.rect.x = width // 2
        self.rect.y = height // 2
        self.Zahler = 1

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
            self.rect.x += random.randint(-100, 100)
            self.rect.y += random.randint(-100, 100)

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


def defense():
    global dx, dy, heart, running, enemy_group
    if heart.Zahler <= 500:
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
        Constants.E_HP - int(width * 0.8 - abs(width // 2 - x - 100))
        if Constants.E_HP <= 0:
            win()
        else:
            heart.Zahler = 0

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


def win():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), (width // 2, 0, 5, 1000), 0)
    pygame.display.flip()


heart.image = pygame.transform.scale(heart.image, (30, 30))

for _ in range(10):
    Enemy(enemy_group)


def mini_game():
    heart.Zahler += 1
    if heart.Zahler <= 500 and Constants.MAX_HP > 0:
        defense()
    elif Constants.MAX_HP <= 0:
        death()
    elif Constants.E_HP <= 0:
        win()
    else:
        attack()