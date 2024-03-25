import pygame
import random

pygame.init()

SCREEN_W = 800
SCREEN_H = 600
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load('img/icon.jpg')
pygame.display.set_icon(icon)

target_img = pygame.image.load('img/tgt1_80.png')
target_w = 80
target_h = 80

target_x = random.randint(0, SCREEN_W - target_w)
target_y = random.randint(0, SCREEN_H - target_h)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


running = True
while running:
    screen.fill(color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_w and target_y < mouse_y < target_y + target_h:
                target_x = random.randint(0, SCREEN_W - target_w)
                target_y = random.randint(0, SCREEN_H - target_h)
    screen.blit(target_img, (target_x, target_y))
    pygame.display.update()


pygame.quit()
