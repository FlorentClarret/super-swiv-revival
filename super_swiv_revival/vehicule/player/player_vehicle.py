from abc import ABC

from enums.direction import Direction
from vehicule.SwivSprite import SwivSprite, DEFAULT_SPEED


class PlayerVehicle(SwivSprite, ABC):
    def move(self, direction):
        if direction is None:
            return None

        if not isinstance(direction, Direction):
            raise TypeError('direction must be an instance of Direction Enum')

        new_x = PlayerVehicle.__compute_new_position(self.rect.x, direction.vector[0], self.screen_width, self.image.get_size()[0])
        new_y = PlayerVehicle.__compute_new_position(self.rect.y, direction.vector[1], self.screen_height, self.image.get_size()[1])

        self._render_vehicle(direction, new_x, new_y)

    @staticmethod
    def __compute_new_position(current_value, difference, max_value, sprite_size):
        result = current_value + DEFAULT_SPEED * difference

        if result < 0:
            return 0

        if result + sprite_size >= max_value:
            return max_value - sprite_size

        return result
