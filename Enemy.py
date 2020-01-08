import pygame

tile_width = tile_height = 50
all_enemies = pygame.sprite.Group()


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, player_image):
        super().__init__(all_enemies)
        self.image = player_image
        self.rect = self.image.get_rect().move(tile_width * pos_x + 15, tile_height * pos_y + 5)
        cropped = pygame.Surface((180 // 9, 40 // 2))
        cropped.set_colorkey((0, 0, 0))
        cropped.blit(self.image, (0, 0), (0, 40 // 2, 180 // 9, 40))
        self.image = pygame.transform.scale(cropped, (50, 50))

    def update(self, xm, ym):
        if xm > self.rect.x:
            self.rect.x += 1
        elif xm < self.rect.x:
            self.rect.x -= 1

        if ym > self.rect.y:
            self.rect.y += 1
        elif ym < self.rect.y:
            self.rect.y -= 1