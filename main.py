import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


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

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_CENTER_PT[0], SCREEN_CENTER_PT[1], PLAYER_RADIUS)
    asteroid_field = AsteroidField()

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for entity in updatable:
            entity.update(dt)

        for asteroid in asteroids:
            if asteroid.has_collided_with(player):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if shot.has_collided_with(asteroid):
                    asteroid.kill()
                    break

        screen.fill((0, 0, 0))

        for entity in drawable:
            entity.draw(screen)

        pygame.display.flip()
        dt = clock.tick(max_fps) / millsec_per_sec
        # print(f"Delta Time(sec): {dt}")


if __name__ == "__main__":
    main()
