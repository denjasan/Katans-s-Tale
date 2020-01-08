import pygame

from Main import


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, frames, x, y):
        super().__init__()
        self.frames = frames
        self.frame_number = 0
        self.image = self.frames[self.frame_number]
        self.rect = self.rect.move(x, y)
        self.add(all_sprites)

