import os
import sys

import pygame


def all_pics(path, n):
    images = []
    for i in range(n):
        image = load_image(path[5:] + str(i) + '.gif')
        image = pygame.transform.scale(image, (60, 50))
        images.append(image)
    return images


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


def terminate():
    pygame.quit()
    sys.exit()
