import os
import sys
import pygame


def terminate():
    pygame.quit()
    sys.exit()


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


def handle_events():
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