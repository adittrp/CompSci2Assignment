import pygame


class Boxer:
    def __init__(self, window, x, y, attack_animation1, block_animation1):
        print("as")
        self.window = window
        self.x = x
        self.y = y
        self.value = 0
        self.idle_anim = attack_animation1[0]
        self.attack_anim_1 = attack_animation1
        self.block_anim_1 = block_animation1

    def attack(self):
        boxing = play_attack_animation(self.attack_anim_1, self.value, self.window, self.x, self.y)

        self.value = boxing[2]
        if not boxing[1]:
            image = self.attack_anim_1[int(0)]
            attack = pygame.image.load(image)
            attack = pygame.transform.scale(attack, (500, 500))
            self.window.blit(attack, (self.x, self.y))

            return False
        else:
            return True

    def defend(self):
        image = self.block_anim_1[int(self.value)]
        attack = pygame.image.load(image)
        attack = pygame.transform.scale(attack, (500, 500))
        self.window.blit(attack, (self.x, self.y))

        if self.value < len(self.block_anim_1):
            self.value += 0.1

        return True

    def idle(self):
        image = self.idle_anim
        idle = pygame.image.load(image)
        idle = pygame.transform.scale(idle, (500, 500))
        self.window.blit(idle, (self.x, self.y))


def play_attack_animation(attack_sheet, value, window, x, y):
    if value >= len(attack_sheet):
        return 0, False, 0
    else:
        if value == int(value):
            image = attack_sheet[int(value)]
        else:
            image = attack_sheet[int(value)]
        attack = pygame.image.load(image)
        attack = pygame.transform.scale(attack, (500, 500))
        window.blit(attack, (x, y))

    value += 0.1

    return image, True, value
