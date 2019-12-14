import pygame

HELICOPTER_BLADES_IMAGES = [pygame.image.load("data/sprites/helicopter/blade/helicopter_blade0.png"),
                            pygame.image.load("data/sprites/helicopter/blade/helicopter_blade1.png"),
                            pygame.image.load("data/sprites/helicopter/blade/helicopter_blade2.png"),
                            pygame.image.load("data/sprites/helicopter/blade/helicopter_blade3.png"),
                            pygame.image.load("data/sprites/helicopter/blade/helicopter_blade4.png"),
                            pygame.image.load("data/sprites/helicopter/blade/helicopter_blade5.png"),
                            pygame.image.load("data/sprites/helicopter/blade/helicopter_blade6.png"),
                            pygame.image.load("data/sprites/helicopter/blade/helicopter_blade7.png")]


class Blade(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, *groups):
        super().__init__(groups)
        self.current_blade = 0
        self.blade_count = len(HELICOPTER_BLADES_IMAGES)
        self.image = HELICOPTER_BLADES_IMAGES[self.current_blade]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def update_sprite(self):
        previous_x = self.rect.x
        previous_y = self.rect.y
        self.current_blade = (self.current_blade + 1) % self.blade_count
        self.image = HELICOPTER_BLADES_IMAGES[self.current_blade]
        self.rect = self.image.get_rect()
        self.rect.x = previous_x
        self.rect.y = previous_y
