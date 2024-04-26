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

        self.build_up_block = True

    def attack(self):
        boxing = play_attack_animation(self.attack_anim_1, self.value, self.window, self.x, self.y, 0.2)

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
        if self.build_up_block:
            boxing = play_attack_animation(self.block_anim_1, self.value, self.window, self.x, self.y, 0.25)

            self.value = boxing[2]
            if not boxing[1]:
                image = self.block_anim_1[int(-1)]
                block = pygame.image.load(image)
                block = pygame.transform.scale(block, (500, 500))
                self.window.blit(block, (self.x, self.y))
                self.build_up_block = False
        else:
            image = self.block_anim_1[int(-1)]
            block = pygame.image.load(image)
            block = pygame.transform.scale(block, (500, 500))
            self.window.blit(block, (self.x, self.y))

        return True

    def idle(self):
        image = self.idle_anim
        idle = pygame.image.load(image)
        idle = pygame.transform.scale(idle, (500, 500))
        self.window.blit(idle, (self.x, self.y))

    def reset_block_bool(self):
        self.build_up_block = True


def play_attack_animation(attack_sheet, value, window, x, y, value_added):
    if value >= len(attack_sheet):
        return 0, False, 0
    else:
        image = attack_sheet[int(value)]
        attack = pygame.image.load(image)
        attack = pygame.transform.scale(attack, (500, 500))
        window.blit(attack, (x, y))

    value += value_added

    return image, True, value
