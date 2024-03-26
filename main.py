from tir_func import *

running = True
score_change = 0

while running:
    screen.fill(color)
    crnt_time = time.time()

    if target_img is None or crnt_time >= nxt_tgt_time:
        target_x, target_y, target_w, target_h, target_img, file_path = newtgt()
        nxt_tgt_time = crnt_time + random.uniform(1, 2)
        bonus_txt = None

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

            scr_change_txt = font.render('+' + str(score_change), True, (255, 255, 255))
            screen.blit(scr_change_txt, (mouse_x + 20, mouse_y + 20))

    screen.blit(target_img, (target_x, target_y))
    scr_text = font.render('Score: ' + str(score), True, (255, 255, 255))
    screen.blit(scr_text, (10, 10))
    pygame.display.update()

pygame.quit()
