import pygame

from enums.direction import Direction
from vehicule.player.player_vehicle import PlayerVehicle

HELICOPTER_IMAGE = pygame.image.load("data/sprites/helicopter/helicopter.png")


class Helicopter(PlayerVehicle):
    def __init__(self, screen_width, screen_height, x=0, y=0, direction=Direction.NORTH):
        super().__init__(screen_width, screen_height, x, y, direction)

    def get_sprite(self, direction):
        if direction is None:
            return None

        return HELICOPTER_IMAGE
