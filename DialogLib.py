import pygame


class Dialog:
    def __init__(self, screen, clock, speed, fps):
        self.screen = screen
        self.clock = clock
        self.speed = speed
        self.fps = fps
        self.progress = 0

    def draw_dialog(self, text):
        my_value = self.clock.tick(self.fps)
        self.progress += my_value
        my_index = self.progress // 10

        if my_index < len(text):
            font = pygame.font.Font(None, 30)
            text1 = font.render(text[:my_index], 1, (255, 255, 255))
            self.screen.blit(text1, (0, 0))
