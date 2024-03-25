from const import *


def newtgt():
    random_file = random.choice(files)
    random_file_path = os.path.join(tgt_folder_path, random_file)

    target_img = pygame.image.load(random_file_path)
    target_w, target_h = target_img.get_size()

    target_x = random.randint(0, SCREEN_W - target_w)
    target_y = random.randint(0, SCREEN_H - target_h)
    return target_x, target_y, target_w, target_h, target_img, random_file_path
