import pygame


class Boxer:
    def __init__(self, window, x, y, attack_animation):
        print("as")
        self.window = window
        self.x = x
        self.y = y
        self.value = 0
        self.attack_anim = attack_animation

    def attack(self, attack_available):
        if attack_available:
            boxing = play_animation(self.attack_anim, self.value, self.window, self.x, self.y)

            self.value = boxing[2]
            if not boxing[1]:
                return False
            else:
                return True
        else:
            image = self.attack_anim[int(0)]
            attack_Example = pygame.image.load(image)
            attack_Example = pygame.transform.scale(attack_Example, (500, 500))
            self.window.blit(attack_Example, (self.x, self.y))

        return False


def play_animation(attack_sheet, value, window, x, y):
    if value >= len(attack_sheet):
        return 0, False, 0
    else:
        if value == int(value):
            image = attack_sheet[int(value)]
        else:
            image = attack_sheet[int(value)]
        attack_example = pygame.image.load(image)
        attack_example = pygame.transform.scale(attack_example, (500, 500))
        window.blit(attack_example, (x, y))

    value += 0.1

    return image, True, value
