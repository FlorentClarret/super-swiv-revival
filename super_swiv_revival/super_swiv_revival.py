import pygame

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

    while True:
        clock.tick(FPS)
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.display.flip()


if __name__ == "__main__":
    main()
    pygame.quit()
