from enum import Enum, unique

import pygame


@unique
class Direction(Enum):
    NORTH = 0, (0, -1)
    SUD = 1, (0, 1)
    EAST = 2, (1, 0)
    WEST = 3, (-1, 0)
    NORTH_EAST = 4, (1, -1)
    SOUTH_EAST = 5, (1, 1)
    NORTH_WEST = 6, (-1, -1)
    SOUTH_WEST = 7, (-1, 1)

    def __new__(cls, value, vector):
        result = object.__new__(cls)
        result._value_ = value
        result.vector = vector
        return result

    @staticmethod
    def from_keyboard(pressed):
        if pressed[pygame.K_UP] and pressed[pygame.K_LEFT]:
            return Direction.NORTH_WEST
        elif pressed[pygame.K_UP] and pressed[pygame.K_RIGHT]:
            return Direction.NORTH_EAST
        elif pressed[pygame.K_DOWN] and pressed[pygame.K_LEFT]:
            return Direction.SOUTH_WEST
        elif pressed[pygame.K_DOWN] and pressed[pygame.K_RIGHT]:
            return Direction.SOUTH_EAST
        elif pressed[pygame.K_LEFT]:
            return Direction.WEST
        elif pressed[pygame.K_RIGHT]:
            return Direction.EAST
        elif pressed[pygame.K_UP]:
            return Direction.NORTH
        elif pressed[pygame.K_DOWN]:
            return Direction.SUD

        return None
