import os
import random
import pygame


pygame.init()
size = width, height = 600, 95
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


class Car(pygame.sprite.Sprite):
    image = load_image("car.png")

    def __init__(self, group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite. Это очень важно!!!
        super().__init__(group)
        self.image = Car.image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.v = 100  # пикселей в секунду
        self.fps = 60
        self.clock = pygame.time.Clock()
        self.k = 1
        self.image = pygame.transform.flip(self.image, True, False)

    def update(self):
        if self.rect.x + self.image.get_width() >= 600:
            self.k = -1
            self.image = pygame.transform.flip(self.image, True, False)
        elif self.rect.x <= 0:
            self.k = 1
            self.image = pygame.transform.flip(self.image, True, False)

        self.rect.x += self.k * self.v / self.fps
        self.clock.tick(self.fps)


all_sprites = pygame.sprite.Group()
Car(all_sprites)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if event.type == pygame.MOUSEBUTTONDOWN:
        for bomb in all_sprites:
            bomb.update(event)
    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()

