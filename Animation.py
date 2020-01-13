import pygame

from Main import *


class AnimatedSprite(pygame.sprite.Sprite):
    pass
    # def __init__(self, frames, x, y):
    #     super().__init__()
    #     self.frames = frames
    #     self.frame_number = 0
    #     self.image = self.frames[self.frame_number]
    #     self.rect = self.rect.move(x, y)
    #     self.add(all_sprites)

    # def __init__(self, path, x, y):
    #     super().__init__(self, player_group, all_sprites)
    #     self.image = load_image(path + '0.gif')
    #     self.images = []
    #     self.rect = self.image.get_rect()
    #     self.rect.x = x
    #     self.rect.y = y
    #
    # def sprites(self, n):
    #     for i in range(n):
    #         self.images.append()

