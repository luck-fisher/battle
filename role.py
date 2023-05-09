import pygame
from tkinter import messagebox


# 敌人单位
class Enemy(pygame.sprite.Sprite):
    def __init__(self, num, attack, defense, life, attack_range):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/enemy" + num + ".jpg")
        self.attack = attack
        self.defense = defense
        self.life = life
        self.attack_range = attack_range


# 玩家单位
class Player(pygame.sprite.Sprite):
    def __init__(self, attack, defense, life, attack_range):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("image/spare_protagonist2.jpg")
        self.attack = attack
        self.defense = defense
        self.life = life
        self.attack_range = attack_range
        self.talents = []
        self.place = (0, 0)

    # 获得技能
    def get_talent(self, talent_name, talent_cooldown):
        if self.talents.count((talent_name, talent_cooldown)) == 0:
            self.talents.append((talent_name, talent_cooldown))
        else:
            pass

    # TODO 受到伤害
