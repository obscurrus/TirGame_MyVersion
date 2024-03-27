import pygame
import random
import os
import time

pygame.init()

''' параметры окна'''
SCREEN_W = 1024
SCREEN_H = 768
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))

pygame.display.set_caption("Игра Тир v0.2a")
icon = pygame.image.load('img/icon.jpg')
pygame.display.set_icon(icon)
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
font = pygame.font.Font(None, 36)

''' параметры цели '''
tgt_folder_path = 'tgt_img'
files = os.listdir(tgt_folder_path)

''' стартовые значения игровых переменных'''
target_img = None
nxt_tgt_time = time.time()
score = 0

# загрузить звуковой эффект
click_sound = pygame.mixer.Sound('shoot.wav')
# загрузить звук промазал
click_mimo_sound = pygame.mixer.Sound('mimo.wav')
# загрузить музыкальный файл
pygame.mixer.music.load('musik.mp3')


running = True
shoot_img = pygame.image.load('img/bang_s.png')  # загрузить изображение выстрела
mouse_x = -100
mouse_y = -100



# воспроизвести музыку в бесконечном цикле
pygame.mixer.music.play(-1)
