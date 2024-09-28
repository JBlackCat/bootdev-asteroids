import pygame
from constants import *


def main():
    pygame.init()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_WIDTH])
    clock = pygame.time.Clock()
    dt = 0
    max_fps = 60
    millsec_per_sec = 1000

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0, 0, 0))
        pygame.display.flip()
        dt = clock.tick(max_fps) / millsec_per_sec
        # print(f"Delta Time(sec): {dt}")


if __name__ == "__main__":
    main()
