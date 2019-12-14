from abc import ABC, abstractmethod

import pygame

from enums.direction import Direction

DEFAULT_SPEED = 2


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

        return self._render_vehicle(direction, self.rect.x + DEFAULT_SPEED * direction.vector[0],
                                    self.rect.y + DEFAULT_SPEED * direction.vector[1])

    def _render_vehicle(self, direction, x, y):
        if not isinstance(direction, Direction):
            raise TypeError('direction must be an instance of Direction Enum')

        new_sprite = self.get_main_sprite(direction)

        if self.image != new_sprite:
            self.image = new_sprite
            self.rect = self.image.get_rect()

        if x + self.image.get_size()[0] < self.screen_width and x > 0 and x != self.rect.x:
            self.rect.x = x
        if y + self.image.get_size()[1] < self.screen_height and y > 0 and y != self.rect.y:
            self.rect.y = y
