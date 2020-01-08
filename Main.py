import pygame
from Constants import *


class Main:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.main_loop()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def render(self):
        """ rendering everything """
        pygame.display.flip()

    def main_loop(self):
        """ main program cycle """
        while self.running:
            self.render()


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    game = Main(screen)


