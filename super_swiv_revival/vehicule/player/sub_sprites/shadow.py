import pygame

HELICOPTER_SHADOW_IMAGE = pygame.image.load("data/sprites/helicopter/helicopter_shadow.png")


class Shadow(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, *groups):
        super().__init__(groups)
        self.image = HELICOPTER_SHADOW_IMAGE
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move(self, x, y):
        self.rect.x = x
        self.rect.y = y
