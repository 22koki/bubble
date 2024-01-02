import pygame
from random import randint

class Ball(pygame.sprite.Sprite):
    def __init__(self, color, x, y, radius):
        super().__init__()
        self.image = pygame.Surface([radius * 2, radius * 2])
        self.image.fill(color)
        self.image.set_colorkey(color)
        pygame.draw.circle(self.image, color, [radius, radius], radius)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.radius = radius
        self.color = color

class Shooter(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([50, 25])
        self.image.fill(pygame.Color('black'))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 10

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill(pygame.Color('red'))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 10