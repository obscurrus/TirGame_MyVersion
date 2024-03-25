import pygame
import random

pygame.init()

SCREEN_W = 800
SCREEN_H = 600
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))

pygame.display.set_caption("Игра Тир v0.2a")
icon = pygame.image.load('img/icon.jpg')
pygame.display.set_icon(icon)

target_img = pygame.image.load('img/tgt1_80.png')
target_w = 80
target_h = 80

target_x = random.randint(0, SCREEN_W - target_w)
target_y = random.randint(0, SCREEN_H - target_h)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
