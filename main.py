from tir_func import *

running = True
shoot_img = pygame.image.load('img/bang_s.png')  # загрузить изображение выстрела
mouse_x = -100
mouse_y = -100

while running:
    screen.fill(color)
    crnt_time = time.time()

    if target_img is None or crnt_time >= nxt_tgt_time:
        target_x, target_y, target_w, target_h, target_img, file_path = newtgt()
        nxt_tgt_time = crnt_time + random.uniform(1, 2)
        mouse_x = -100
        mouse_y = -100

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_w and target_y < mouse_y < target_y + target_h:
                if 's' in file_path:
                    score += 5
                else:
                    score += 1
                target_x, target_y, target_w, target_h, target_img, file_path = newtgt()
            else:
                mouse_x = -100
                mouse_y = -100

    screen.blit(shoot_img, (mouse_x - 64, mouse_y - 64))  # отобразить Surface в месте клика мыши

    screen.blit(target_img, (target_x, target_y))
    scr_text = font.render('Score: ' + str(score), True, (255, 255, 255))
    screen.blit(scr_text, (10, 10))
    pygame.display.update()

pygame.quit()
