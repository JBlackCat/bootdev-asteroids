import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    SCREEN_CENTER_PT = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    print(f"Screen Center X: {SCREEN_CENTER_PT[0]}")
    print(f"Screen Center Y: {SCREEN_CENTER_PT[1]}")

    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    clock = pygame.time.Clock()
    dt = 0
    max_fps = 60
    millsec_per_sec = 1000
    player = Player(SCREEN_CENTER_PT[0], SCREEN_CENTER_PT[1], PLAYER_RADIUS)

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0, 0, 0))
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(max_fps) / millsec_per_sec
        # print(f"Delta Time(sec): {dt}")


if __name__ == "__main__":
    main()
