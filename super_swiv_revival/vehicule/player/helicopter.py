import pygame

from enums.direction import Direction
from vehicule.player.player_vehicle import PlayerVehicle
from vehicule.player.sub_sprites.blade import Blade
from vehicule.player.sub_sprites.shadow import Shadow

HELICOPTER_IMAGE = pygame.image.load("data/sprites/helicopter/helicopter.png")

HELICOPTER_SHADOW_GAP = (16, 32)
HELICOPTER_BLADE_GAP = (-2, 0)


class Helicopter(PlayerVehicle):
    def __init__(self, screen_width, screen_height, x=0, y=0, direction=Direction.NORTH, *groups):
        self.shadow = Shadow(x + HELICOPTER_SHADOW_GAP[0], y + HELICOPTER_SHADOW_GAP[1])
        self.blade = Blade(x + HELICOPTER_BLADE_GAP[0], y + HELICOPTER_BLADE_GAP[1])
        super().__init__(screen_width, screen_height, x, y, direction, groups)

        for group in groups:
            group.add(self.shadow or [])
            group.add(self.blade or [])

    def get_main_sprite(self, direction):
        if direction is None:
            return None

        return HELICOPTER_IMAGE

    def _render_vehicle(self, direction, x, y):
        super()._render_vehicle(direction, x, y)
        self.shadow.move(self.rect.x + HELICOPTER_SHADOW_GAP[0], self.rect.y + HELICOPTER_SHADOW_GAP[1])
        self.blade.move(self.rect.x + HELICOPTER_BLADE_GAP[1], self.rect.y + HELICOPTER_BLADE_GAP[1])

    def update_sprite(self):
        self.blade.update_sprite()
