import pygame

from enums.direction import Direction

CAR_IMAGES = [pygame.image.load("data/sprites/car/car_front.png"),
              pygame.image.load("data/sprites/car/car_back.png"),
              pygame.image.load("data/sprites/car/car_right.png"),
              pygame.image.load("data/sprites/car/car_left.png"),
              pygame.image.load("data/sprites/car/car_front_right.png"),
              pygame.image.load("data/sprites/car/car_back_right.png"),
              pygame.image.load("data/sprites/car/car_front_left.png"),
              pygame.image.load("data/sprites/car/car_back_left.png")]


class Car(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height, x=0, y=0):
        super().__init__()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.height = 25
        self.width = 24
        self.image = CAR_IMAGES[Direction.NORTH.value]
        self.rect = self.image.get_rect()
        self.__load_image(Direction.NORTH, x, y)

    def move(self, direction):
        if direction is None:
            return

        if not isinstance(direction, Direction):
            raise TypeError('direction must be an instance of Direction Enum')

        self.__load_image(direction,
                          Car._compute_coordinate(self.rect.x, direction.vector[0], self.screen_width, self.width),
                          Car._compute_coordinate(self.rect.y, direction.vector[1], self.screen_height, self.height))

    def __load_image(self, direction, x, y):
        if not isinstance(direction, Direction):
            raise TypeError('direction must be an instance of Direction Enum')

        if self.image != CAR_IMAGES[direction.value]:
            self.image = CAR_IMAGES[direction.value]
            self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

    @staticmethod
    def _compute_coordinate(current_value, difference, max_value, sprite_size):
        result = current_value + 2 * difference

        if result < 0:
            return 0

        if result + sprite_size > max_value:
            return max_value - sprite_size

        return result
