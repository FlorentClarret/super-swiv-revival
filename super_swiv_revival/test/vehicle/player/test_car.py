import unittest

import pygame

from enums.direction import Direction
from test.vehicle.player.test_player_vehicle import PlayerVehicleTest
from vehicule.player.car import Car


class CarTest(PlayerVehicleTest, unittest.TestCase):
    cls = Car

    def test_get_sprite(self):
        self.assertIsNone(self.instance.get_sprite(None))

        super().compare_surface(pygame.image.load("data/sprites/car/car_front.png"),
                                self.instance.get_sprite(Direction.NORTH))
        super().compare_surface(pygame.image.load("data/sprites/car/car_back.png"),
                                self.instance.get_sprite(Direction.SOUTH))
        super().compare_surface(pygame.image.load("data/sprites/car/car_right.png"),
                                self.instance.get_sprite(Direction.EAST))
        super().compare_surface(pygame.image.load("data/sprites/car/car_left.png"),
                                self.instance.get_sprite(Direction.WEST))
        super().compare_surface(pygame.image.load("data/sprites/car/car_front_right.png"),
                                self.instance.get_sprite(Direction.NORTH_EAST))
        super().compare_surface(pygame.image.load("data/sprites/car/car_back_right.png"),
                                self.instance.get_sprite(Direction.SOUTH_EAST))
        super().compare_surface(pygame.image.load("data/sprites/car/car_front_left.png"),
                                self.instance.get_sprite(Direction.NORTH_WEST))
        super().compare_surface(pygame.image.load("data/sprites/car/car_back_left.png"),
                                self.instance.get_sprite(Direction.SOUTH_WEST))
