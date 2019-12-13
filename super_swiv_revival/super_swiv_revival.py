import pygame

from enums.direction import Direction
from vehicule.player.car import Car
from vehicule.player.helicopter import Helicopter

FPS = 30
SCREEN_WIDTH = 512
SCREEN_HEIGHT = 448


def main():
    pygame.init()
    pygame.display.set_caption("Super Swiv Revival")
    pygame.mouse.set_visible(0)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    background = pygame.image.load("data/background/level1/background.png")

    clock = pygame.time.Clock()

    all_sprites_group = pygame.sprite.Group()

    car = Car(SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, Direction.NORTH, all_sprites_group)
    helicopter = Helicopter(SCREEN_WIDTH, SCREEN_HEIGHT, 100, 100, Direction.NORTH, all_sprites_group)

    while True:
        clock.tick(FPS)
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        car.move(Direction.from_keyboard(pygame.key.get_pressed()))
        helicopter.move(Direction.from_keyboard(pygame.key.get_pressed()))
        helicopter.next_blade()

        all_sprites_group.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
    pygame.quit()
