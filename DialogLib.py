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
        self.font = pygame.font.Font(None, 20)
        self.image = None

    def draw_dialog(self, text):
        my_value = self.clock.tick(self.fps)
        if self.d:
            self.progress -= my_value
            self.d = False
        self.progress += my_value
        my_index = self.progress // (self.speed * 10)

        if my_index >= len(text):
            return True
        text01 = text[:my_index]
        # if "n" in text01:
        #     for i in range(len(text01.split("n"))):
        #         print(text01.split("n")[i])
        #         text1 = self.font.render(text01.split("n")[i], 1, (255, 255, 255))
        #         self.screen.blit(text1, ((WIDTH - len(text01.split("n")[i]) * 15) // 2, i * 10))
        # else:
        #     text1 = self.font.render(text[:my_index], 1, (255, 255, 255))
        #     self.screen.blit(text1, (0, 0))
        for i in range(len(text01.split("n"))):
            ti = text01.split("n")[i]
            text1 = self.font.render(ti, 1, (255, 255, 255))
            self.screen.blit(text1, ((WIDTH - (len(ti) * 15 // 2)) // 2, (HEIGHT + i * 30) // 2))

