from const import *

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
