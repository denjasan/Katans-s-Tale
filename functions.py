import os
import sys

import pygame

from groups import *
from Constants import *


def all_pics(path, n, size, colorkey=None):
    images = []
    for i in range(n):
        image = load_image(path[5:] + str(i) + '.gif', colorkey)
        image = pygame.transform.scale(image, size)
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


def shift_world(world_shift, shift_x):
    """ When the user moves left/right and we need to scroll everything: """

    # Keep track of the shift amount
    world_shift += shift_x

    # Go through all the sprite lists and shift
    for fon in fon_group:
        fon.rect.x += shift_x

