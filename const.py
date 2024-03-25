import pygame
import random
import os

pygame.init()
''' параметры окна'''
SCREEN_W = 1024
SCREEN_H = 768
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))

pygame.display.set_caption("Игра Тир v0.2a")
icon = pygame.image.load('img/icon.jpg')
pygame.display.set_icon(icon)
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

''' параметры цели '''
tgt_folder_path = 'tgt_img'
files = os.listdir(tgt_folder_path)
random_file = random.choice(files)
random_file_path = os.path.join(tgt_folder_path, random_file)

target_img = pygame.image.load(random_file_path)
target_w, target_h = target_img.get_size()

target_x = random.randint(0, SCREEN_W - target_w)
target_y = random.randint(0, SCREEN_H - target_h)

print(random_file_path)
print(target_w, target_h)
