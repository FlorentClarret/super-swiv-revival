from abc import ABC, abstractmethod

import pygame

from enums.direction import Direction


class SwivSprite(pygame.sprite.Sprite, ABC):
    def __init__(self, screen_width, screen_height, x=0, y=0, direction=Direction.NORTH, *groups):
        super().__init__(groups or [])
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.image = self.get_main_sprite(direction)
        self.rect = self.image.get_rect()
        self._render_vehicle(direction, x, y)

    @abstractmethod
    def get_main_sprite(self, direction):
        pass

    def move(self, direction):
        if direction is None:
            return None

        if not isinstance(direction, Direction):
            raise TypeError('direction must be an instance of Direction Enum')

        self._render_vehicle(direction, self.rect.x + direction.vector[0], self.rect.y + direction.vector[1])

    def _render_vehicle(self, direction, x, y):
        if not isinstance(direction, Direction):
            raise TypeError('direction must be an instance of Direction Enum')

        new_sprite = self.get_main_sprite(direction)

        if self.image != new_sprite:
            self.image = new_sprite
            self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
