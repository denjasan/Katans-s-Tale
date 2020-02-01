import pygame
from Constants import *


class Dialog:
    def __init__(self, screen, speed, fps):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.speed = speed
        self.fps = fps
        self.progress = 0
        self.d = True
        self.font = pygame.font.Font(None, 30)

    def draw_dialog(self, text):
        my_value = self.clock.tick(self.fps)
        if self.d:
            self.progress -= my_value
            self.d = False
        self.progress += my_value
        my_index = self.progress // 200

        if my_index >= len(text):
            return True
        text01 = text[:my_index]
        if "\n" in text01:
            for i in range(len(text01.split("֍"))):
                print(text01.split("֍")[i])
                text1 = self.font.render(text01.split("֍")[i], 1, (255, 255, 255))
                self.screen.blit(text1, (0, i * 30))
        else:
            text1 = self.font.render(text[:my_index], 1, (255, 255, 255))
            self.screen.blit(text1, (0, 0))