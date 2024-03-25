from tir_func import *

target_img = None
running = True
nxt_tgt_time = time.time()

while running:
    screen.fill(color)

    crnt_time = time.time()

    if target_img is None or crnt_time >= nxt_tgt_time:
        target_x, target_y, target_w, target_h, target_img = newtgt()
        nxt_tgt_time = crnt_time + random.uniform(1, 2)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_w and target_y < mouse_y < target_y + target_h:
                target_x, target_y, target_w, target_h, target_img = newtgt()

    screen.blit(target_img, (target_x, target_y))
    pygame.display.update()

pygame.quit()
