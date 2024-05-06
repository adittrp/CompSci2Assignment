# Import pygame
import pygame


# Main class to define boxer
class Boxer:
    # Initialization that defines alot of variables, piece_taker checks if the boxer is taking the piece
    def __init__(self, window, x, y, attack_animation1, block_animation1, attack_amt, health_amt, index_to_change=None):
        self.window = window
        self.x = x
        self.y = y
        self.value = 0
        self.idle_anim = attack_animation1[0]
        self.attack_anim_1 = attack_animation1
        self.block_anim_1 = block_animation1

        self.index_to_change = index_to_change

        self.build_up_block = True

        self.blocking = False

        self.attack_damage = attack_amt
        self.health = health_amt

    # Definition to play the attack animation
    def attack(self, other_boxer):
        boxing = play_animation(self.attack_anim_1, self.value, self.window, self.x, self.y, 0.3)

        # As long as the attack animation has not finished, the attack variable returns true and keeps displaying
        self.value = boxing[2]
        if not boxing[1]:
            # Once the animation has ended, check if the opposition is blocking and do damage based on that
            if not other_boxer.blocking:
                other_boxer.health -= self.attack_damage
            else:
                other_boxer.health -= int(self.attack_damage/5)

            image = self.attack_anim_1[int(0)]
            attack = pygame.image.load(image)
            attack = pygame.transform.scale(attack, (500, 500))
            self.window.blit(attack, (self.x, self.y))

            return False
        else:
            return True

    # Definition to play block animation
    def defend(self):
        # Until the block animation has actually gone to its last image, this will stay true and go through animation
        if self.build_up_block:
            boxing = play_animation(self.block_anim_1, self.value, self.window, self.x, self.y, 0.35)

            self.value = boxing[2]
            if not boxing[1]:
                image = self.block_anim_1[int(-1)]
                block = pygame.image.load(image)
                block = pygame.transform.scale(block, (500, 500))
                self.window.blit(block, (self.x, self.y))
                self.build_up_block = False
        # Once the block animation has finished the player will stay in a block as long as they hold the button
        else:
            image = self.block_anim_1[int(-1)]
            block = pygame.image.load(image)
            block = pygame.transform.scale(block, (500, 500))
            self.window.blit(block, (self.x, self.y))

        self.blocking = True

        return True

    # If a player is not attacking or blocking, simply set their image as self.idle_anim
    def idle(self):
        self.blocking = False

        image = self.idle_anim
        idle = pygame.image.load(image)
        idle = pygame.transform.scale(idle, (500, 500))
        self.window.blit(idle, (self.x, self.y))

    # Reset the build_up_block variable for the next time a player blocks
    def reset_block_bool(self):
        self.build_up_block = True

    # Display health using text and a rectangle with a gold border
    def update_health(self, font, window, x_increment, rect_val_1):
        # The x value of the rectangle and border are based on each boxer
        pygame.draw.rect(window, 'light gray', [rect_val_1, 0, 380, 125], 100)
        pygame.draw.rect(window, 'gold', [rect_val_1, 0, 380, 125], 5)

        text = font.render("Health: " + str(self.health), True, 'black')
        text_rect = text.get_rect(center=(self.x + x_increment, self.y - 135))
        window.blit(text, text_rect)

    # Check if health is 0 or below
    def check_health(self):
        if self.health <= 0:
            return True
        else:
            return False


# Called to move through the images in order to make a smooth animation
def play_animation(attack_sheet, value, window, x, y, value_added):
    # As long as there are more images, keep displaying the next image
    if value >= len(attack_sheet):
        return 0, False, 0
    else:
        image = attack_sheet[int(value)]
        attack = pygame.image.load(image)
        attack = pygame.transform.scale(attack, (500, 500))
        window.blit(attack, (x, y))

    value += value_added

    return image, True, value
