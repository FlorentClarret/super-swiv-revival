import pygame

from enums.direction import Direction
from vehicule.player.player_vehicle import PlayerVehicle
from vehicule.player.sub_sprites.gun import Gun

CAR_IMAGES = [pygame.image.load("data/sprites/car/car_front.png"),
              pygame.image.load("data/sprites/car/car_back.png"),
              pygame.image.load("data/sprites/car/car_right.png"),
              pygame.image.load("data/sprites/car/car_left.png"),
              pygame.image.load("data/sprites/car/car_front_right.png"),
              pygame.image.load("data/sprites/car/car_back_right.png"),
              pygame.image.load("data/sprites/car/car_front_left.png"),
              pygame.image.load("data/sprites/car/car_back_left.png")]

CAR_GUN_GAP = (8, 7)


class Car(PlayerVehicle):
    def __init__(self, screen_width, screen_height, x=0, y=0, direction=Direction.NORTH, *groups):
        self.gun = Gun(x, y)
        super().__init__(screen_width, screen_height, x, y, direction, groups)

        for group in groups:
            group.add(self.gun or [])

    def _render_vehicle(self, direction, x, y):
        super()._render_vehicle(direction, x, y)
        self.gun.move(self.rect.x + CAR_GUN_GAP[0], self.rect.y + CAR_GUN_GAP[1], direction)

    def get_main_sprite(self, direction):
        if direction is None:
            return None

        if not isinstance(direction, Direction):
            raise TypeError('direction must be an instance of Direction Enum')

        return CAR_IMAGES[direction.value]
