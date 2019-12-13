import unittest

import pygame

from enums.direction import Direction
from test.vehicle.player.test_player_vehicle import PlayerVehicleTest
from vehicule.player.helicopter import Helicopter


class HelicopterTest(PlayerVehicleTest, unittest.TestCase):
    cls = Helicopter

    def test_get_main_sprite(self):
        self.assertIsNone(self.instance.get_main_sprite(None))

        for direction in Direction:
            super().compare_surface(pygame.image.load("data/sprites/helicopter/helicopter.png"), self.instance.get_main_sprite(direction))
