from enums.direction import Direction


class PlayerVehicleTest:
    cls = None

    def setUp(self):
        self.instance = self.cls(500, 500, 5, 5)

    def test_move_north(self):
        self.instance.move(Direction.NORTH)
        self.assertEqual(self.instance.rect.x, 5)
        self.assertEqual(self.instance.rect.y, 3)
        self.assertEqual(self.instance.get_sprite(Direction.NORTH), self.instance.image)

    def test_move_south(self):
        self.instance.move(Direction.SOUTH)
        self.assertEqual(self.instance.rect.x, 5)
        self.assertEqual(self.instance.rect.y, 7)
        self.assertEqual(self.instance.get_sprite(Direction.SOUTH), self.instance.image)

    def test_move_east(self):
        self.instance.move(Direction.EAST)
        self.assertEqual(self.instance.rect.x, 7)
        self.assertEqual(self.instance.rect.y, 5)
        self.assertEqual(self.instance.get_sprite(Direction.EAST), self.instance.image)

    def test_move_west(self):
        self.instance.move(Direction.WEST)
        self.assertEqual(self.instance.rect.x, 3)
        self.assertEqual(self.instance.rect.y, 5)
        self.assertEqual(self.instance.get_sprite(Direction.WEST), self.instance.image)

    def test_move_north_east(self):
        self.instance.move(Direction.NORTH_EAST)
        self.assertEqual(self.instance.rect.x, 7)
        self.assertEqual(self.instance.rect.y, 3)
        self.assertEqual(self.instance.get_sprite(Direction.NORTH_EAST), self.instance.image)

    def test_move_south_west(self):
        self.instance.move(Direction.SOUTH_WEST)
        self.assertEqual(self.instance.rect.x, 3)
        self.assertEqual(self.instance.rect.y, 7)
        self.assertEqual(self.instance.get_sprite(Direction.SOUTH_WEST), self.instance.image)

    def test_move_north_west(self):
        self.instance.move(Direction.NORTH_WEST)
        self.assertEqual(self.instance.rect.x, 3)
        self.assertEqual(self.instance.rect.y, 3)
        self.assertEqual(self.instance.get_sprite(Direction.NORTH_WEST), self.instance.image)

    def test_move_south_west(self):
        self.instance.move(Direction.SOUTH_EAST)
        self.assertEqual(self.instance.rect.x, 7)
        self.assertEqual(self.instance.rect.y, 7)
        self.assertEqual(self.instance.get_sprite(Direction.SOUTH_EAST), self.instance.image)

    def test_move_north_out_of_screen(self):
        instance = self.cls(500, 500, 50, 0, Direction.NORTH)
        instance.move(Direction.NORTH)
        self.assertEqual(instance.rect.x, 50)
        self.assertEqual(instance.rect.y, 0)
        self.assertEqual(instance.get_sprite(Direction.NORTH), instance.image)

    def test_move_south_out_of_screen(self):
        instance = self.cls(500, 500, 50, 0, Direction.SOUTH)
        instance.rect.y = 500 - instance.image.get_size()[0]
        instance.move(Direction.SOUTH)
        self.assertEqual(instance.rect.x, 50)
        self.assertEqual(instance.rect.y, 500 - instance.image.get_size()[1])
        self.assertEqual(instance.get_sprite(Direction.SOUTH), instance.image)

    def test_move_east_out_of_screen(self):
        instance = self.cls(500, 500, 0, 0, Direction.EAST)
        instance.rect.x = 500 - instance.image.get_size()[0]
        instance.move(Direction.EAST)
        self.assertEqual(instance.rect.x, 500 - instance.image.get_size()[0])
        self.assertEqual(instance.rect.y, 0)
        self.assertEqual(instance.get_sprite(Direction.EAST), instance.image)

    def test_move_west_out_of_screen(self):
        instance = self.cls(500, 500, 0, 0, Direction.WEST)
        instance.rect.y = 500 - instance.image.get_size()[1]
        instance.move(Direction.WEST)
        self.assertEqual(instance.rect.x, 0)
        self.assertEqual(instance.rect.y, 500 - instance.image.get_size()[1])
        self.assertEqual(instance.get_sprite(Direction.WEST), instance.image)

    def test_move_north_west_out_of_screen(self):
        instance = self.cls(500, 500, 0, 0, Direction.NORTH_WEST)
        instance.move(Direction.NORTH_WEST)
        self.assertEqual(instance.rect.x, 0)
        self.assertEqual(instance.rect.y, 0)
        self.assertEqual(instance.get_sprite(Direction.NORTH_WEST), instance.image)

    def test_move_north_east_out_of_screen(self):
        instance = self.cls(500, 500, 0, 0, Direction.NORTH_EAST)
        instance.rect.x = 500 - instance.image.get_size()[0]
        instance.move(Direction.NORTH_EAST)
        self.assertEqual(instance.rect.x, 500 - instance.image.get_size()[0])
        self.assertEqual(instance.rect.y, 0)
        self.assertEqual(instance.get_sprite(Direction.NORTH_EAST), instance.image)

    def test_move_south_west_out_of_screen(self):
        instance = self.cls(500, 500, 0, 0, Direction.SOUTH_WEST)
        instance.rect.y = 500 - instance.image.get_size()[1]
        instance.move(Direction.SOUTH_WEST)
        self.assertEqual(instance.rect.x, 0)
        self.assertEqual(instance.rect.y, 500 - instance.image.get_size()[1])
        self.assertEqual(instance.get_sprite(Direction.SOUTH_WEST), instance.image)

    def test_move_south_east_out_of_screen(self):
        instance = self.cls(500, 500, 0, 0, Direction.SOUTH_EAST)
        instance.rect.x = 500 - instance.image.get_size()[0]
        instance.rect.y = 500 - instance.image.get_size()[1]
        instance.move(Direction.SOUTH_EAST)
        self.assertEqual(instance.rect.x, 500 - instance.image.get_size()[0])
        self.assertEqual(instance.rect.y, 500 - instance.image.get_size()[1])
        self.assertEqual(instance.get_sprite(Direction.SOUTH_EAST), instance.image)

    def compare_surface(self, expected, actual):
        self.assertEqual(expected.get_width(), actual.get_width())
        self.assertEqual(expected.get_height(), actual.get_height())

        for x in range(expected.get_width()):
            for y in range(expected.get_height()):
                self.assertEqual(expected.get_at((x, y)), actual.get_at((x, y)))
