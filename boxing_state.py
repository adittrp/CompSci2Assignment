import pygame


class Boxer:
    def __init__(self):
        print("as")


def play_animation(attack_sheet, value, window):
    if value >= len(attack_sheet):
        value = 0
        return 0, False
    else:
        if value == int(value):
            image = attack_sheet[int(value)]
        else:
            image = attack_sheet[int(value)]
        attack_example = pygame.image.load(image)
        attack_example = pygame.transform.scale(attack_example, (500, 500))
        window.blit(attack_example, (300, 200))

    value += 0.1

    return image, True
