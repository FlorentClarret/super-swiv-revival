import pygame

from enums.direction import Direction
from vehicule.player.player_vehicle import PlayerVehicle

HELICOPTER_IMAGE = pygame.image.load("data/sprites/helicopter/helicopter.png")
HELICOPTER_SHADOW_IMAGE = pygame.image.load("data/sprites/helicopter/helicopter_shadow.png")
HELICOPTER_BLADES_IMAGES = [pygame.image.load("data/sprites/helicopter/helicopter_blade0.png"),
                            pygame.image.load("data/sprites/helicopter/helicopter_blade1.png"),
                            pygame.image.load("data/sprites/helicopter/helicopter_blade2.png"),
                            pygame.image.load("data/sprites/helicopter/helicopter_blade3.png"),
                            pygame.image.load("data/sprites/helicopter/helicopter_blade4.png"),
                            pygame.image.load("data/sprites/helicopter/helicopter_blade5.png"),
                            pygame.image.load("data/sprites/helicopter/helicopter_blade6.png"),
                            pygame.image.load("data/sprites/helicopter/helicopter_blade7.png")]

HELICOPTER_SHADOW_GAP = (16, 32)
HELICOPTER_BLADE_GAP = (0, -2)


class Helicopter(PlayerVehicle):
    def __init__(self, screen_width, screen_height, x=0, y=0, direction=Direction.NORTH, *groups):
        self.shadow = Shadow(x + HELICOPTER_SHADOW_GAP[0], y + HELICOPTER_SHADOW_GAP[1])
        self.blade = Blade(x + HELICOPTER_BLADE_GAP[0], y + HELICOPTER_BLADE_GAP[1])
        super().__init__(screen_width, screen_height, x, y, direction, groups)

        for group in groups:
            group.add(self.shadow)
            group.add(self.blade)

    def get_main_sprite(self, direction):
        if direction is None:
            return None

        return HELICOPTER_IMAGE

    def next_blade(self):
        self.blade.next_blade()

    def _render_vehicle(self, direction, x, y):
        super()._render_vehicle(direction, x, y)
        self.shadow.move(x + HELICOPTER_SHADOW_GAP[0], y + HELICOPTER_SHADOW_GAP[1])
        self.blade.move(x + HELICOPTER_BLADE_GAP[0], y + HELICOPTER_BLADE_GAP[1])


class Shadow(pygame.sprite.Sprite):
    def __init__(self, x, y, *groups):
        super().__init__(groups)
        self.image = HELICOPTER_SHADOW_IMAGE
        self.rect = self.image.get_rect()
        self.move(x, y)

    def move(self, x, y):
        self.rect.x = x
        self.rect.y = y


class Blade(pygame.sprite.Sprite):
    def __init__(self, x, y, *groups):
        super().__init__(groups)
        self.current_blade = 0
        self.image = HELICOPTER_BLADES_IMAGES[0]
        self.rect = self.image.get_rect()
        self.move(x, y)

    def move(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def next_blade(self):
        self.current_blade = (self.current_blade + 1) % len(HELICOPTER_BLADES_IMAGES)
        previous_x = self.rect.x
        previous_y = self.rect.y
        self.image = HELICOPTER_BLADES_IMAGES[self.current_blade]
        self.rect = self.image.get_rect()
        self.move(previous_x, previous_y)
