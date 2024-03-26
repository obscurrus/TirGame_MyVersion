from const import *


def newtgt():
    random_file = random.choice(files)
    random_file_path = os.path.join(tgt_folder_path, random_file)

    target_img = pygame.image.load(random_file_path)
    target_w, target_h = target_img.get_size()

    target_x = random.randint(0, SCREEN_W - target_w)
    target_y = random.randint(0, SCREEN_H - target_h)
    return target_x, target_y, target_w, target_h, target_img, random_file_path

def splash():
    # отобразить изображение заставки на экране
    splash_surface = pygame.Surface((800, 600))
    splash_surface.blit(splash_img, (0, 0))
    screen.blit(splash_surface, (0, 0))
    pygame.display.update()

    # ждать нажатия клавиши пробел
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False