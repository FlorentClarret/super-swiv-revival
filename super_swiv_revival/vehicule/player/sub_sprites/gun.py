import pygame

from enums.direction import Direction

CAR_GUN_IMAGES = [pygame.image.load("data/sprites/car/gun/car_gun_front.png"),
                  pygame.image.load("data/sprites/car/gun/car_gun_back.png"),
                  pygame.image.load("data/sprites/car/gun/car_gun_right.png"),
                  pygame.image.load("data/sprites/car/gun/car_gun_left.png"),
                  pygame.image.load("data/sprites/car/gun/car_gun_front_right.png"),
                  pygame.image.load("data/sprites/car/gun/car_gun_back_right.png"),
                  pygame.image.load("data/sprites/car/gun/car_gun_front_left.png"),
                  pygame.image.load("data/sprites/car/gun/car_gun_back_left.png")]


class Gun(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, *groups):
        super().__init__(groups)
        self.image = CAR_GUN_IMAGES[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move(self, x, y, direction):
        if direction is None:
            return None

        if not isinstance(direction, Direction):
            raise TypeError('direction must be an instance of Direction Enum')

        new_sprite = CAR_GUN_IMAGES[direction.value]

        if self.image != new_sprite:
            self.image = new_sprite
            self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
