from abc import ABC, abstractmethod

import pygame

from enums.direction import Direction


class Vehicle(pygame.sprite.Sprite, ABC):
    def __init__(self, screen_width, screen_height, x=0, y=0, direction=Direction.NORTH):
        super().__init__()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.image = self.get_sprite(direction)
        self.rect = self.image.get_rect()
        self.__load_image(direction, x, y)

    @abstractmethod
    def get_sprite(self, direction):
        pass

    def move(self, direction):
        if direction is None:
            return None

        if not isinstance(direction, Direction):
            raise TypeError('direction must be an instance of Direction Enum')

        new_x = Vehicle.__compute_new_position(self.rect.x, direction.vector[0], self.screen_width, self.image.get_size()[0])
        new_y = Vehicle.__compute_new_position(self.rect.y, direction.vector[1], self.screen_height, self.image.get_size()[1])

        self.__load_image(direction, new_x, new_y)

    def __load_image(self, direction, x, y):
        if not isinstance(direction, Direction):
            raise TypeError('direction must be an instance of Direction Enum')

        new_sprite = self.get_sprite(direction)

        if self.image != new_sprite:
            self.image = new_sprite
            self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

    @staticmethod
    def __compute_new_position(current_value, difference, max_value, sprite_size):
        result = current_value + 2 * difference

        if result < 0:
            return 0

        if result + sprite_size >= max_value:
            return max_value - sprite_size

        return result
