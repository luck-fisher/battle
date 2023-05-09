import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, num, attack, defense, attack_range):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/enemy"+num+".jpg")
        self.attack = attack
        self.defense = defense
        self.attack_range = attack_range
