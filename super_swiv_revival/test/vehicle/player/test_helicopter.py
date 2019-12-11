import unittest

import pygame

from enums.direction import Direction
from test.vehicle.test_vehicle import VehicleTest
from vehicule.player.helicopter import Helicopter


class HelicopterTest(VehicleTest, unittest.TestCase):
    cls = Helicopter

    def test_get_sprite(self):
        self.assertIsNone(self.instance.get_sprite(None))

        for direction in Direction:
            super().compare_surface(pygame.image.load("data/sprites/car/car_front.png"), self.instance.get_sprite(direction))
