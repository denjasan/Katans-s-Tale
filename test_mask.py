# -.- coding: utf8 -.-
import pygame
pygame.init()
size = [800, 600]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

image1 = pygame.image.load('data/car.png').convert_alpha()
image1 = pygame.transform.scale(image1, (100, 100))
image1_mask = pygame.mask.from_surface(image1)
image1_pos = [100, 100]

image2 = pygame.image.load('data/grass.png').convert_alpha()
image2 = pygame.transform.scale(image2, (100, 100))
image2_mask = pygame.mask.from_surface(image2)
image2_pos = [300, 100]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # двигаем image1
    image1_pos[0] += 1

    # offset, сдвиг - переменная зависящая от взаимного положения картинок
    # поскольку картинки двигаются, вычислять ее нужно каждый кадр заново
    offset = (int(image2_pos[0] - image1_pos[0]), int(image2_pos[1] - image1_pos[1]))

    # если картинки соприкоснулись, то перемещаем первую картинку назад
    # обратите внимание на использование переменной offset
    if image1_mask.overlap_area(image2_mask, offset) > 0:
        image1_pos[0] = 100

    # рисуем
    screen.fill((200, 100, 0))
    screen.blit(image1, image1_pos)
    screen.blit(image2, image2_pos)

    pygame.display.flip()
    clock.tick(30)
pygame.quit()
