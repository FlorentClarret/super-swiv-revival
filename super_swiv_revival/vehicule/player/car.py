import pygame

from enums.direction import Direction
from vehicule.vehicle import Vehicle

CAR_IMAGES = [pygame.image.load("data/sprites/car/car_front.png"),
              pygame.image.load("data/sprites/car/car_back.png"),
              pygame.image.load("data/sprites/car/car_right.png"),
              pygame.image.load("data/sprites/car/car_left.png"),
              pygame.image.load("data/sprites/car/car_front_right.png"),
              pygame.image.load("data/sprites/car/car_back_right.png"),
              pygame.image.load("data/sprites/car/car_front_left.png"),
              pygame.image.load("data/sprites/car/car_back_left.png")]


class Car(Vehicle):
    def __init__(self, screen_width, screen_height, x=0, y=0, direction=Direction.NORTH):
        super().__init__(screen_width, screen_height, x, y, direction)

    def get_sprite(self, direction):
        if direction is None:
            return None

        if not isinstance(direction, Direction):
            raise TypeError('direction must be an instance of Direction Enum')

        return CAR_IMAGES[direction.value]

