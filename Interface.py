# encoding: utf-8
import pygame
import Constants
import Values


width, height = 1080, 720


def render_hp(screen):
    hp = Values.InstantHP
    font = pygame.font.Font(None, 30)
    text = font.render("Кол-во жизней: " + str(hp), 1, (100, 255, 100))
    text_x = width - text.get_width() - 10
    text_y = text.get_height()
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, (0, 255, 0), (text_x - 10, 2 * text_y + 20,
                                           text_w + 20, text_h + 20), 1)
    pygame.draw.rect(screen, (255, 0, 0), (text_x - 10 + 5, 2 * text_y + 25,
                                           (text_w * hp) // Constants.MAX_HP + 10, text_h + 10))